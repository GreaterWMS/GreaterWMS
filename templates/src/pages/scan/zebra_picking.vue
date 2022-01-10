<template>
  <div>
    <q-input v-model="scaneddata.request_time" style="display:none" />
    <q-card v-show="!fab" flat :style="{ width: width, height: height }">
      <q-card-section>
        <q-bar class="bg-white q-mb-sm shadow-1 ">
          <div style="font-size: 12px;width: 100%;">{{ $t('scan.scan_goods_label') }}: {{ dn_scan }}</div>
        </q-bar>
        <q-btn-group push>
          <q-btn color="purple" :label="$t('stock.view_stocklist.cyclecountresult')" @click="pickedSubmit()"/>
        </q-btn-group>
      </q-card-section>
      <q-scroll-area ref="scrollArea" :thumb-style="thumbStyle" :bar-style="barStyle" :style="{ height: scroll_height, width: width }">
        <q-markup-table>
          <thead>
            <tr>
              <th class="text-center">{{ scan_bin_name }}</th>
              <th class="text-center">{{ scan_goods_code }}</th>
              <th class="text-center">{{ order_qty }}</th>
              <th class="text-center">{{ picking_qty }}</th>
            </tr>
          </thead>
          <tbody>
            <template>
              <tr :id="'dom' + index" v-for="(item, index) in table_list" :key="index">
                <td :class="{'scan-background text-center': item.bin_name === bin_scan, 'text-center': item.bin_name !== bin_scan }">{{ item.bin_name }}</td>
                <td :class="{'scan-background text-center': item.bin_name === bin_scan && item.goods_code === goods_scan, 'text-center': item.bin_name !== bin_scan && item.goods_code !== goods_scan }">{{ item.goods_code }}</td>
                <td :class="{'scan-background text-center': item.bin_name === bin_scan && item.goods_code === goods_scan, 'text-center': item.bin_name !== bin_scan && item.goods_code !== goods_scan }">{{ item.pick_qty }}</td>
                <td class="text-center">{{ item.picked_qty }}</td>
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
  name: 'Pagezebra_picking',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'picking/',
      width: '',
      height: '',
      scroll_height: '',
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
      bar_scanned: '',
      dn_scan: '',
      bin_scan: '',
      goods_scan: '',
      currentIndex: '',
      id: '',
      error1: this.$t('scan.scan_goods_label_error'),
      error2: this.$t('scan.view_picking.picking_qty_error')
    }
  },
  methods: {
    getPickingList (e) {
      var _this = this
      getauth('dn/pickinglistfilter/?dn_code=' + e, {})
        .then(res => {
          if (res.results.length === 0) {
            _this.$q.notify({
              message: 'No DN Data',
              position: 'top',
              icon: 'close',
              color: 'negative'
            })
          } else {
            console.log(res)
            _this.dn_scan = res.results[0].dn_code
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
    getBinList (e) {
      var _this = this
      var bindata = ''
      _this.table_list.filter(item => {
        if (item.bin_name.includes(e)) {
          bindata = e
        }
      })
      if (bindata !== '') {
        _this.bin_scan = e
      } else {
        _this.$q.notify({
          message: 'No Bin Data',
          position: 'top',
          icon: 'close',
          color: 'negative'
        })
      }
    },
    getGoodsList (e) {
      var _this = this
      var ct = 0
      _this.table_list.filter(item => {
        ct += 1
        if (item.goods_code.includes(e)) {
          if (item.picked_qty < item.pick_qty) {
            _this.goods_scan = e
            item.picked_qty += 1
          } else {
            if (ct === _this.table_list.length) {
              _this.$q.notify({
                message: 'Scanned More Data',
                position: 'top',
                icon: 'close',
                color: 'negative'
              })
            }
          }
        } else {
          return true
        }
      })
    },
    pickedSubmit () {
      var _this = this
      var pickFormData = {
        dn_code: _this.dn_scan,
        goodsData: _this.table_list,
        creater: _this.login_name
      }
      _this.pickedDataSubmit(pickFormData)
    },
    pickedDataSubmit (e) {
      var _this = this
      putauth(_this.pathname + 'picked/', e)
        .then(res => {
          _this.table_list = []
          _this.bin_scan = ''
          _this.goods_scan = ''
          _this.dn_scan = ''
          if (!res.detail) {
            _this.$q.notify({
              message: 'Success Confirm Picking List',
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
        if (_this.scaneddata.mode === 'DN') {
          _this.bar_scanned = _this.scaneddata.request_time
          _this.bin_scan = ''
          _this.goods_scan = ''
          _this.dn_scan = ''
          _this.getPickingList(_this.scaneddata.code)
        } else if (_this.scaneddata.mode === 'BINSET') {
          _this.bar_scanned = _this.scaneddata.request_time
          _this.bin_scan = ''
          _this.goods_scan = ''
          _this.getBinList(_this.scaneddata.code)
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
