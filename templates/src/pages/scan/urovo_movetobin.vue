<template>
  <div>
    <q-input v-model="scaneddata.request_time" style="display:none" />
    <q-card v-show="!fab" flat :style="{ width: width,  height: height }">
      <q-card-section>
        <q-bar class="bg-white q-mb-sm shadow-1 ">
          <div style="font-size: 12px;width: 100%;">From {{ $t('warehouse.view_binset.bin_name') }}: {{ frombin }}</div>
        </q-bar>
        <q-bar class="bg-white shadow-1 ">
          <div style="font-size: 12px;width: 100%;">To {{ $t('warehouse.view_binset.bin_name') }}: {{ tobin }}</div>
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
              <th class="text-center">{{ goods_code_label }}</th>
              <th class="text-center">{{ goods_qty_label }}</th>
              <th class="text-center">{{ move_qty_label }}</th>
            </tr>
          </thead>
          <tbody>
            <template>
              <tr v-for='(item, index) in table_list' :key='index'>
                <td class="text-center">{{ item.goods_code }}</td>
                <td class="text-center">{{ item.goods_qty }}</td>
                <td class="text-center">{{ item.move_qty }}</td>
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
      bar_scanned: '',
      frombin: '',
      tobin: '',
      moved: false,
      movecheck: []
    }
  },
  methods: {
    getGoodsList (e) {
      var _this = this
      getauth('goods/?goods_code=' + e, {
      }).then(res => {
        if (res.results.length === 0) {
          navigator.vibrate(100)
          _this.$q.notify({
            message: 'No Goods Data',
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        } else if (res.results.length === 1) {
          _this.table_list.filter(item => {
            if (item.bin_name.includes(_this.bin_scan) && item.goods_code.includes(res.results[0].goods_code)) {
              _this.movecheck.push(item)
            }
          })
          if (_this.movecheck.length > 0) {
            _this.movecheck.forEach(obj => {
              if (obj.qty === obj.goods_qty - obj.pick_qty - obj.picked_qty) {
                return true
              } else if (obj.qty < obj.goods_qty - obj.pick_qty - obj.picked_qty) {
                _this.table_list.filter(item => {
                  if (item.t_code.includes(obj.t_code)) {
                    item.qty += 1
                  }
                  _this.movecheck = []
                })
                return false
              } else {
                return false
              }
            })
          } else {
            navigator.vibrate(100)
            _this.$q.notify({
              message: 'No Goods Data',
              position: 'top',
              icon: 'close',
              color: 'negative'
            })
          }
        } else {
          navigator.vibrate(100)
          _this.$q.notify({
            message: 'Repeating Data',
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        }
      }).catch(err => {
        navigator.vibrate(100)
        _this.$q.notify({
          message: err.detail,
          position: 'top',
          icon: 'close',
          color: 'negative'
        })
      })
    },
    getFromBinList (e) {
      var _this = this
      getauth('stock/bin/?bin_name=' + e, {
      }).then(res => {
        if (res.results.length === 0) {
          navigator.vibrate(100)
          _this.$q.notify({
            message: 'No Bin Data',
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        } else {
          _this.table_list = res.results
          _this.frombin = _this.scaneddata
          _this.movecheck = true
        }
      }).catch(err => {
        navigator.vibrate(100)
        _this.$q.notify({
          message: err.detail,
          position: 'top',
          icon: 'close',
          color: 'negative'
        })
      })
    },
    getToBinList (e) {
      var _this = this
      getauth('binset/?bin_name=' + e, {
      }).then(res => {
        if (res.results.length === 0) {
          navigator.vibrate(100)
          _this.$q.notify({
            message: 'No Bin Data',
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        } else if (res.results.length === 1) {
          _this.moveSubmit()
        } else {
          navigator.vibrate(100)
          _this.$q.notify({
            message: 'Repeating Data',
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        }
      }).catch(err => {
        navigator.vibrate(100)
        _this.$q.notify({
          message: err.detail,
          position: 'top',
          icon: 'close',
          color: 'negative'
        })
      })
    },
    moveSubmit () {
      var _this = this
      putauth('staock/bin', _this.movedata).then(res => {
        _this.$q.notify({
          message: 'Success Move To Bin' + _this.tobin,
          position: 'top',
          icon: 'check',
          color: 'green'
        })
        _this.movecheck = false
        _this.table_list = []
        _this.frombin = ''
        _this.tobin = ''
      })
        .catch(err => {
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
    var _this = this
    if (_this.scaneddata !== '') {
      if (_this.bar_scanned !== _this.scaneddata.request_time) {
        if (_this.scaneddata.mode === 'BINSET') {
          if (!_this.moved) {
            _this.bar_scanned = _this.scaneddata.request_time
            _this.getFromBinList(_this.scaneddata.code)
          } else {
            _this.bar_scanned = _this.scaneddata.request_time
            _this.getToBinList(_this.scaneddata.code)
          }
        } else if (_this.scaneddata.mode === 'GOODS') {
          if (_this.bin_scan !== '') {
            _this.bar_scanned = _this.scaneddata.request_time
            _this.getGoodsList(_this.scaneddata.code)
          } else {
            _this.$q.notify({
              message: 'No Bin Query Data',
              position: 'top',
              icon: 'close',
              color: 'negative'
            })
          }
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
