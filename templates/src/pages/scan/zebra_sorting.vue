<template>
  <div>
    <q-input v-model="scaneddata.request_time" style="display:none" />
    <q-card v-show="!fab" flat :style="{ width: width, height: height }">
      <q-card-section>
        <q-bar class="bg-white q-mb-sm shadow-1 ">
          <div style="font-size: 12px;width: 100%;">{{ $t('scan.scan_goods_label') }}: {{ asn_scan }}</div>
        </q-bar>
        <q-btn-group push>
          <q-btn color="purple" :label="$t('stock.view_stocklist.cyclecountresult')" @click="sortedSubmit()"/>
        </q-btn-group>
      </q-card-section>
      <q-scroll-area ref="scrollArea" :thumb-style="thumbStyle" :bar-style="barStyle" :style="{ height: scroll_height, width: width }">
        <q-markup-table>
          <thead>
            <tr>
              <th class="text-center">{{ scan_goods_code }}</th>
              <th class="text-center">{{ goods_qty }}</th>
              <th class="text-center">{{ goods_actual_qty }}</th>
            </tr>
          </thead>
          <tbody>
            <template>
              <tr :id="'dom' + index" v-for="(item, index) in table_list" :key="index">
                <td :class="{'scan-background text-center': item.goods_code === goods_scan, 'text-center': item.goods_code !== goods_scan }">{{ item.goods_code }}</td>
                <td :class="{'scan-background text-center': item.goods_code === goods_scan, 'text-center': item.goods_code !== goods_scan }">{{ item.goods_qty }}</td>
                <td class="text-center">{{ item.goods_actual_qty }}</td>
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
import { getauth, putauth } from 'boot/axios_request'
import { LocalStorage, Screen } from 'quasar'

export default {
  name: 'Pagezebra_sorting',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'asn/detail/?asn_status=3&asn_code=',
      width: '',
      height: '',
      scroll_height: '',
      table_list: [],
      scan_goods_code: this.$t('scan.scan_goods_code'),
      goods_qty: this.$t('scan.view_picking.order_qty'),
      goods_actual_qty: this.$t('scan.view_picking.picking_qty'),
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
      bar_scanned: '',
      asn_scan: '',
      goods_scan: '',
      error1: this.$t('scan.scan_goods_label_error'),
      error2: this.$t('scan.view_picking.picking_qty_error')
    }
  },
  methods: {
    getASNDetailList (e) {
      var _this = this
      getauth(_this.pathname + e, {})
        .then(res => {
          if (res.results.length === 0) {
            _this.$q.notify({
              message: 'No ASN Data',
              position: 'top',
              icon: 'close',
              color: 'negative'
            })
          } else {
            console.log(res)
            _this.asn_scan = res.results[0].asn_code
            _this.table_list = res.results
          }
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        })
    },
    getGoodsList (e) {
      var _this = this
      _this.table_list.filter(item => {
        if (item.goods_code.includes(e)) {
          _this.goods_scan = e
          item.goods_actual_qty += 1
          return false
        } else {
          return true
        }
      })
    },
    sortedSubmit () {
      var _this = this
      var sortedFormData = {
        asn_code: _this.asn_scan,
        goodsData: _this.table_list,
        creater: _this.login_name
      }
      _this.sortedDataSubmit(sortedFormData)
    },
    sortedDataSubmit (e) {
      var _this = this
      putauth('asn/sorted/', e)
        .then(res => {
          _this.table_list = []
          _this.goods_scan = ''
          _this.dn_scan = ''
          if (!res.detail) {
            _this.$q.notify({
              message: 'Success Confirm ASN Sorted List',
              position: 'top',
              icon: 'check',
              color: 'green'
            })
          }
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        })
    }
  },
  computed: {
    fab: {
      get () {
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
    _this.scroll_height = Screen.height - 225 + '' + 'px'
  },
  updated () {
    var _this = this
    if (_this.scaneddata !== '') {
      if (_this.bar_scanned !== _this.scaneddata.request_time) {
        if (_this.scaneddata.mode === 'ASN') {
          _this.bar_scanned = _this.scaneddata.request_time
          _this.goods_scan = ''
          _this.asn_scan = ''
          _this.getASNDetailList(_this.scaneddata.code)
        } else if (_this.scaneddata.mode === 'GOODS') {
          _this.bar_scanned = _this.scaneddata.request_time
          _this.getGoodsList(_this.scaneddata.code)
        } else {
          _this.$q.notify({
            message: 'No Query Data',
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        }
      }
    }
  },
  beforeDestroy () {
  }
}
</script>
