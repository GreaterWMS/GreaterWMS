<template>
  <div>
    <q-input v-model="scaneddata.request_time" style="display:none" />
    <q-card v-show="!fab" flat :style="{ width: width,  height: height }">
      <q-card-section>
        <q-bar class="bg-white q-mb-sm shadow-1 ">
          <div style="font-size: 12px;width: 100%;">{{ $t('scan.scan_goods_label') }}: {{ frombin }}</div>
        </q-bar>
        <q-bar class="bg-white shadow-1 ">
          <div style="font-size: 12px;width: 100%;">{{ $t('scan.scan_goods_label') }}: {{ tobin }}</div>
        </q-bar>
      </q-card-section>
      <q-scroll-area
        :thumb-style="thumbStyle"
        :bar-style="barStyle"
        :style="{ height: scroll_height, width: width }"
      >
        <q-markup-table>
          <thead>
            <tr>
              <th class="text-right">{{ goods_code_label }}</th>
              <th class="text-right">{{ goods_qty_label }}</th>
              <th class="text-right">{{ move_qty_label }}</th>
            </tr>
          </thead>
          <tbody>
            <template>
              <tr v-for='(item, index) in table_list' :key='index'>
                <td class="text-left">{{ item.goods_code }}</td>
                <td class="text-right">{{ item.goods_qty }}</td>
                <td class="text-right">{{ item.move_qty }}</td>
              </tr>
            </template>
          </tbody>
        </q-markup-table>
      </q-scroll-area>
    </q-card>
    </div>
</template>
<router-view />

<script>
import { getauth } from 'boot/axios_request'
import { LocalStorage, Screen } from 'quasar'

export default {
  name: 'Pagezebra_movetobin',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'cyclecount/',
      width: '',
      height: '',
      scroll_height: '',
      table_list: [],
      goods_code_label: this.$t('stock.view_stocklist.goods_code'),
      goods_qty_label: this.$t('stock.view_stocklist.onhand_stock'),
      move_qty_label: 'Move Qty',
      thumbStyle: {
        right: '4px',
        borderRadius: '5px',
        backgroundColor: '#E0E0E0',
        width: '5px',
        opacity: 0.75
      },
      barStyle: {
        right: '2px',
        borderRadius: '9px',
        backgroundColor: '#EEEEEE',
        width: '9px',
        opacity: 0.2
      },
      frombin: '',
      tobin: '',
      barscan: '',
      bin_scan: '',
      goods_scan: ''
    }
  },
  methods: {
    getList () {
      var _this = this
      getauth(_this.pathname, {
      }).then(res => {
        _this.table_list = res.results
      }).catch(err => {
        _this.$q.notify({
          message: err.detail,
          icon: 'close',
          color: 'negative'
        })
      })
    }
  },
  computed: {
    fab: {
      get () {
        console.log('7', this.$store.state.fabchange.fab)
        return this.$store.state.fabchange.fab
      }
    },
    scaneddata: {
      get () {
        return this.$store.state.scanedsolve.scaneddata
      }
    }
  },
  created () {
    var _this = this
    if (LocalStorage.has('openid')) {
      _this.openid = LocalStorage.getItem('openid')
    } else {
      _this.openid = ''
      LocalStorage.set('openid', '')
    }
    if (LocalStorage.has('login_name')) {
      _this.login_name = LocalStorage.getItem('login_name')
    } else {
      _this.login_name = ''
      LocalStorage.set('login_name', '')
    }
    if (LocalStorage.has('auth')) {
      _this.authin = '1'
    } else {
      _this.authin = '0'
    }
  },
  mounted () {
    var _this = this
    _this.width = Screen.width * 1 + '' + 'px'
    _this.height = Screen.height - 50 + '' + 'px'
    _this.scroll_height = Screen.height - 200 + '' + 'px'
  },
  updated () {
  },
  beforeDestroy () {
  }
}
</script>
