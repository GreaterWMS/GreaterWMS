<template>
  <q-page>
    <q-card v-show="!fab" flat :style="{ width: width, height: height }">
      <q-card-section>
        <q-bar class="bg-white q-mb-sm shadow-1 ">
          <div style="font-size: 12px;width: 100%;">{{ $t('scan.scan_goods_label') }}: {{ goods_scan }}</div>
        </q-bar>
        <q-btn-group push>
          <q-btn :label="$t('refresh')" @click="reFresh()" />
          <q-btn color="purple" :label="$t('stock.view_stocklist.cyclecountresult')" />
        </q-btn-group>
      </q-card-section>
      <q-scroll-area ref="scrollArea" :thumb-style="thumbStyle" :bar-style="barStyle" :style="{ height: scroll_height, width: width }">
        <q-markup-table>
          <thead>
            <tr>
              <th class="text-left">{{ scan_goods_code }}</th>
              <th class="text-right">{{ scan_bin_name }}</th>
              <th class="text-right">{{ order_qty }}</th>
              <th class="text-right">{{ picking_qty }}</th>
            </tr>
          </thead>
          <tbody>
            <template>
              <tr :id="'dom' + index" v-for="(item, index) in table_list" :key="index">
                <td class="text-center">{{ item.goods_code }}</td>
                <td class="text-center">{{ item.bin_name }}</td>
                <td class="text-center">{{ item.goods_qty }}</td>
                <td class="text-center">{{ item.picked_qty }}</td>
              </tr>
            </template>
          </tbody>
        </q-markup-table>
      </q-scroll-area>
    </q-card>
  </q-page>
</template>
<router-view />

<script>
import { getauth } from 'boot/axios_request'
import { LocalStorage, Screen, throttle } from 'quasar'

export default {
  name: 'Pagezebra_shipping',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'cyclecount/',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      scan_goods_code: this.$t('scan.scan_goods_code'),
      scan_bin_name: this.$t('scan.scan_bin_name'),
      order_qty: this.$t('scan.view_picking.order_qty'),
      picking_qty: this.$t('scan.view_picking.picking_qty'),
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
      barscan: '',
      bin_scan: '',
      goods_scan: ''
    }
  },
  methods: {
    datachange () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth('scanner/?bar_code=' + _this.barscan, {
        }).then(res => {
          _this.barscan = res.results[0].code
          if (res.results[0].mode === 'BINSET') {
            _this.bin_scan = res.results[0].code
            _this.goods_scan = ''
          } else if (res.results[0].mode === 'GOODS') {
            _this.goods_scan = res.results[0].code
            _this.countAdd(_this.goods_scan)
          }
        }).catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
      }
    },
    getList () {
      var _this = this
      if (LocalStorage.has('auth')) {
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
    reFresh () {
      var _this = this
      _this.barscan = ''
      _this.bin_scan = ''
      _this.goods_scan = ''
      _this.getList()
    },
  },
  computed: {
    fab: {
      get () {
        return this.$store.state.fabchange.fab
      }
    }
    // barscan: {
    //   get () {
    //     console.log('scaned_x', this.$store.state.datashare.barscan)
    //     return this.$store.state.datashare.barscan
    //   },
    //   set (val) {
    //     console.log('scaned_y', val)
    //     this.$store.commit('datashare/updateBarscan', val)
    //   }
    // }
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
    _this.datachange = throttle(_this.datachange, 200)
  },
  mounted () {
    var _this = this
    _this.width = Screen.width * 1 + '' + 'px'
    _this.height = Screen.height - 50 + '' + 'px'
    _this.scroll_height = Screen.height - 225 + '' + 'px'
    _this.barscan = ''
    _this.bin_scan = ''
    _this.goods_scan = ''
  },
  updated () {
  },
  beforeDestroy () {
  },
  destroyed () {
  }
}
</script>
