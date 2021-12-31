<template>
  <q-page>
    <q-card v-show="!fab" flat :style="{ width: width,  height: height }">
      <q-card-section>
        <q-bar class="bg-white shadow-1 ">
          <div style="font-size: 12px;width: 100%;">{{ $t('scan.scan_goods_label') }}: {{ bin_scan }}</div>
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
            <th class="text-left">{{ bin_name_label }}</th>
            <th class="text-right">{{ goods_code_label }}</th>
            <th class="text-right">{{ goods_desc_label }}</th>
            <th class="text-right">{{ goods_qty_label }}</th>
            <th class="text-right">{{ pick_qty_label }}</th>
            <th class="text-right">{{ picked_qty_label }}</th>
            <th class="text-right">{{ bin_size_label }}</th>
            <th class="text-right">{{ bin_property_label }}</th>
            <th class="text-right">{{ create_time_label }}</th>
            <th class="text-right">{{ update_time_label }}</th>
          </tr>
          </thead>
          <tbody>
          <template>
            <tr v-for='(item, index) in table_list' :key='index'>
              <td class="text-left">{{ item.bin_name }}</td>
              <td class="text-right">{{ item.goods_code }}</td>
              <td class="text-right">{{ item.goods_desc }}</td>
              <td class="text-right">{{ item.goods_qty }}</td>
              <td class="text-right">{{ item.pick_qty }}</td>
              <td class="text-right">{{ item.picked_qty }}</td>
              <td class="text-right">{{ item.bin_size }}</td>
              <td class="text-right">{{ item.bin_property }}</td>
              <td class="text-right">{{ item.create_time }}</td>
              <td class="text-right">{{ item.update_time }}</td>
            </tr>
          </template>
          </tbody>
        </q-markup-table>
      </q-scroll-area>
      <q-separator dark />
    </q-card>
  </q-page>
</template>
<router-view />

<script>
import { getauth } from 'boot/axios_request'
import { LocalStorage, Screen, throttle } from 'quasar'

export default {
  name: 'Pagezebra_locationquery',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'stock/bin/',
      separator: 'cell',
      loading: false,
      width: '',
      height: '',
      scroll_height: '',
      table_list: [],
      bin_name_label: this.$t('warehouse.view_binset.bin_name'),
      goods_code_label: this.$t('stock.view_stocklist.goods_code'),
      goods_desc_label: this.$t('stock.view_stocklist.goods_desc'),
      goods_qty_label: this.$t('stock.view_stocklist.onhand_stock'),
      pick_qty_label: this.$t('stock.view_stocklist.pick_stock'),
      picked_qty_label: this.$t('stock.view_stocklist.picked_stock'),
      bin_size_label: this.$t('warehouse.view_binset.bin_size'),
      bin_property_label: this.$t('warehouse.view_binset.bin_property'),
      create_time_label: this.$t('createtime'),
      update_time_label: this.$t('updatetime'),
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
      bin_scan: ''
    }
  },
  methods: {
    datachange () {
      var _this = this
      console.log(_this.barscan)
      if (LocalStorage.has('auth')) {
        getauth('scanner/?bar_code=' + _this.barscan, {
        }).then(res => {
          if (res.results[0].mode === 'BINSET') {
            _this.bin_scan = res.results[0].code
            _this.getList(res.results[0].code)
          } else {
            _this.notify({
              message: 'Please Scan Right BarCode',
              icon: 'close',
              color: 'negative'
            })
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
    getList (e) {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname + '?bin_name=' + e, {
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
    }
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
    _this.scroll_height = Screen.height - 175 + '' + 'px'
    _this.barscan = ''
    _this.bin_scan = ''
  },
  beforeDestroy () {
  }
}
</script>
