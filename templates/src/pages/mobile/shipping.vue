<template>
  <div>
    <q-input v-model="scaneddata.request_time" style="display:none" />
    <q-card v-show="!fab" flat :style="{ width: width, height: height }">
      <q-card-section>
        <q-bar class="bg-white q-mb-sm shadow-1 ">
          <q-input v-model="license_plate" borderless stack-label :label="$t('driver.view_driver.license_plate')" style="font-size: 12px;width: 100%;" @keyup.enter="driverConfirm()"  @blur="driverConfirm()"/>
        </q-bar>
        <q-bar class="bg-white q-mb-sm shadow-1 ">
          <div style="font-size: 12px;width: 100%;">{{ $t('driver.view_driver.driver_name') }}: {{ driver_list.driver_name }}</div>
        </q-bar>
        <q-bar class="bg-white q-mb-sm shadow-1 ">
          <div style="font-size: 12px;width: 100%;">{{ $t('driver.view_driver.contact') }}: {{ driver_list.contact }}</div>
        </q-bar>
        <q-btn-group push>
          <q-btn color="purple" :label="$t('stock.view_stocklist.cyclecountresult')" @click="dispatchDataCheck()"/>
        </q-btn-group>
      </q-card-section>
      <q-scroll-area ref="scrollArea" :thumb-style="thumbStyle" :bar-style="barStyle" :style="{ height: scroll_height, width: width }">
        <q-markup-table>
          <thead>
            <tr>
              <th class="text-center">{{ scan_dn_code }}</th>
              <th class="text-center">{{ scan_goods_code }}</th>
              <th class="text-center">{{ order_qty }}</th>
              <th class="text-center">{{ picking_qty }}</th>
            </tr>
          </thead>
          <tbody>
            <template>
              <tr :id="'dom' + index" v-for="(item, index) in table_list" :key="index">
                <td class="text-center">{{ item.dn_code }}</td>
                <td class="text-center">{{ item.goods_code }}</td>
                <td class="text-center">{{ item.goods_qty }}</td>
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
import { getauth, postauth } from 'boot/axios_request'
import { LocalStorage, Screen } from 'quasar'

export default {
  name: 'Page_shipping',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'dn/detail/?dn_status=4&picked_qty__gt=0&dn_code=',
      width: '',
      height: '',
      scroll_height: '',
      table_list: [],
      driver_list: '',
      dn_list: '',
      scan_dn_code: this.$t('outbound.view_dn.dn_code'),
      scan_goods_code: this.$t('scan.scan_goods_code'),
      order_qty: this.$t('outbound.view_dn.goods_qty'),
      picking_qty: this.$t('stock.view_stocklist.picked_stock'),
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
      submitdata: {
        dn_code: '',
        driver: ''
      },
      license_plate: ''
    }
  },
  methods: {
    getDNList (e) {
      var _this = this
      getauth('dn/list/?dn_code=' + e, {
      }).then(res => {
        if (res.results.length === 0) {
          navigator.vibrate(100)
          _this.$q.notify({
            message: 'No DN Data',
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        } else {
          _this.dn_list = res.results[0]
          _this.submitdata.dn_code = _this.dn_list.dn_code
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
    getDNDetailList (e) {
      var _this = this
      getauth(_this.pathname + e, {
      }).then(res => {
        if (res.results.length === 0) {
          navigator.vibrate(100)
          _this.$q.notify({
            message: 'No DN Data',
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        } else {
          _this.table_list = res.results
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
    driverConfirm () {
      var _this = this
      if (_this.license_plate !== '') {
        getauth('driver/?license_plate=' + _this.license_plate, {
        }).then(res => {
          if (res.results.length === 0) {
            _this.driver_list = ''
            navigator.vibrate(100)
            _this.$q.notify({
              message: 'No Driver Data',
              position: 'top',
              icon: 'close',
              color: 'negative'
            })
          } else if (res.results.length === 1) {
            _this.driver_list = res.results[0]
            _this.submitdata.driver = _this.driver_list.driver_name
          } else {
            _this.driver_list = ''
            navigator.vibrate(100)
            _this.$q.notify({
              message: 'Repeating Data',
              position: 'top',
              icon: 'close',
              color: 'negative'
            })
          }
        }).catch(err => {
          _this.driver_list = ''
          navigator.vibrate(100)
          _this.$q.notify({
            message: err.detail,
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        })
      }
    },
    dispatchDataCheck () {
      var _this = this
      if (_this.dn_list === '') {
        _this.$q.notify({
          message: 'Please Scan Your DN',
          position: 'top',
          icon: 'close',
          color: 'negative'
        })
      } else {
        if (_this.driver_list === '') {
          _this.$q.notify({
            message: 'Please Confirm Your Driver Info',
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        } else {
          _this.dispatchDataSubmit()
        }
      }
    },
    dispatchDataSubmit () {
      var _this = this
      postauth('dn/dispatch/' + _this.dn_list.id + '/', _this.submitdata)
        .then(res => {
          _this.$q.notify({
            message: 'Success Dispatch',
            position: 'top',
            icon: 'check',
            color: 'green'
          })
          setTimeout(function () { location.reload() }, 1000)
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
    _this.scroll_height = Screen.height - 240 + '' + 'px'
    _this.bar_scanned = ''
  },
  updated () {
    var _this = this
    if (_this.scaneddata !== '') {
      if (_this.bar_scanned !== _this.scaneddata.request_time) {
        if (_this.scaneddata.mode === 'DN') {
          _this.bar_scanned = _this.scaneddata.request_time
          _this.getDNList(_this.scaneddata.code)
          _this.getDNDetailList(_this.scaneddata.code)
        } else {
          _this.$q.notify({
            message: 'No DN Query Data',
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        }
      }
    }
  }
}
</script>
