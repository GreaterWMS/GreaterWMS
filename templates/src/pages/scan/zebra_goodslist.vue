<template>
  <div>
    <transition appear enter-active-class="animated fadeIn">
      <q-table
        class="my-sticky-header-table shadow-24"
        :data="table_list"
        row-key="id"
        :separator="separator"
        :loading="loading"
        :columns="columns"
        hide-bottom
        :pagination.sync="pagination"
        no-data-label="No data"
        no-results-label="No data you want"
        :table-style="{ height: height }"
        flat
        bordered
      >
        <template v-slot:top>
          <q-btn-group push>
            <q-btn :label="$t('refresh')" icon="refresh" @click="reFresh()" />
          </q-btn-group>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td key="goods_code" :props="props">
              {{ props.row.goods_code }}
            </q-td>
            <q-td key="goods_desc" :props="props">
              {{ props.row.goods_desc }}
            </q-td>
            <q-td key="goods_supplier" :props="props">
              {{ props.row.goods_supplier }}
            </q-td>
            <q-td key="goods_weight" :props="props">
              {{ props.row.goods_weight }}
            </q-td>
            <q-td key="goods_w" :props="props">
              {{ props.row.goods_w }}
            </q-td>
            <q-td key="goods_d" :props="props">
              {{ props.row.goods_d }}
            </q-td>
            <q-td key="goods_h" :props="props">
              {{ props.row.goods_h }}
            </q-td>
            <q-td key="unit_volume" :props="props">
              {{ props.row.unit_volume }}
            </q-td>
            <q-td key="goods_unit" :props="props">
              {{ props.row.goods_unit }}
            </q-td>
            <q-td key="goods_class" :props="props">
              {{ props.row.goods_class }}
            </q-td>
            <q-td key="goods_brand" :props="props">
              {{ props.row.goods_brand }}
            </q-td>
            <q-td key="goods_color" :props="props">
              {{ props.row.goods_color }}
            </q-td>
            <q-td key="goods_shape" :props="props">
              {{ props.row.goods_shape }}
            </q-td>
            <q-td key="goods_specs" :props="props">
              {{ props.row.goods_specs }}
            </q-td>
            <q-td key="goods_origin" :props="props">
              {{ props.row.goods_origin }}
            </q-td>
            <q-td key="goods_cost" :props="props">
              {{ props.row.goods_cost }}
            </q-td>
            <q-td key="goods_price" :props="props">
              {{ props.row.goods_price }}
            </q-td>
            <q-td key="creater" :props="props">
              {{ props.row.creater }}
            </q-td>
            <q-td key="create_time" :props="props">
              {{ props.row.create_time }}
            </q-td>
            <q-td key="update_time" :props="props">
              {{ props.row.update_time }}
            </q-td>
          </q-tr>
        </template>
      </q-table>
    </transition>
    <template>
      <div class="q-pa-lg flex cordova-footer">
        <input id="scannedBarcodes" v-model="barscan" type="text" @input="datachange()" readonly disabled/>
      </div>
    </template>
  </div>
</template>
<router-view />

<script>
import { getauth, putauth } from 'boot/axios_request'
import Vconsole from 'vconsole'
import { LocalStorage } from 'quasar'
if (process.env.NODE_ENV !== 'production') {
  const vConsole = new Vconsole()
}
var sendCommandResults = 'false'

function sendCommand (extraName, extraValue) {
  var broadcastExtras = {}
  broadcastExtras[extraName] = extraValue
  broadcastExtras.SEND_RESULT = sendCommandResults
  window.plugins.intentShim.sendBroadcast({
    action: 'com.symbol.datawedge.api.ACTION',
    extras: broadcastExtras
  },
  function () { },
  function () { }
  )
}

function unregisterBroadcastReceiver () {
  window.plugins.intentShim.unregisterBroadcastReceiver()
}
function commandReceived (commandText) {
}
function enumerateScanners (enumeratedScanners) {
  // eslint-disable-next-line no-unused-vars
  var humanReadableScannerList = []
  for (var i = 0; i < enumeratedScanners.length; i++) {
    humanReadableScannerList += enumeratedScanners[i].SCANNER_NAME
    if (i < enumeratedScanners.length - 1) { humanReadableScannerList += ', ' }
  }
}
function activeProfile (theActiveProfile) {
}
function barcodeScanned (scanData, timeOfScan) {
  var scannedData = scanData.extras['com.symbol.datawedge.data_string']
  document.getElementById('scannedBarcodes').value = ''
  document.getElementById('scannedBarcodes').value = scannedData
  document.getElementById('scannedBarcodes').dispatchEvent(new Event('input'))
}

export default {
  name: 'Pageurovo_goodslist',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'goods/',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      columns: [
        { name: 'goods_code', required: true, label: this.$t('goods.view_goodslist.goods_code'), align: 'left', field: 'goods_code' },
        { name: 'goods_desc', label: this.$t('goods.view_goodslist.goods_desc'), field: 'goods_desc', align: 'center' },
        { name: 'goods_supplier', label: this.$t('goods.view_goodslist.goods_supplier'), field: 'goods_supplier', align: 'center' },
        { name: 'goods_weight', label: this.$t('goods.view_goodslist.goods_weight'), field: 'goods_weight', align: 'center' },
        { name: 'goods_w', label: this.$t('goods.view_goodslist.goods_w'), field: 'goods_w', align: 'center' },
        { name: 'goods_d', label: this.$t('goods.view_goodslist.goods_d'), field: 'goods_d', align: 'center' },
        { name: 'goods_h', label: this.$t('goods.view_goodslist.goods_h'), field: 'goods_h', align: 'center' },
        { name: 'unit_volume', label: this.$t('goods.view_goodslist.unit_volume'), field: 'unit_volume', align: 'center' },
        { name: 'goods_unit', label: this.$t('goods.view_goodslist.goods_unit'), field: 'goods_unit', align: 'center' },
        { name: 'goods_class', label: this.$t('goods.view_goodslist.goods_class'), field: 'goods_class', align: 'center' },
        { name: 'goods_brand', label: this.$t('goods.view_goodslist.goods_brand'), field: 'goods_brand', align: 'center' },
        { name: 'goods_color', label: this.$t('goods.view_goodslist.goods_color'), field: 'goods_color', align: 'center' },
        { name: 'goods_shape', label: this.$t('goods.view_goodslist.goods_shape'), field: 'goods_shape', align: 'center' },
        { name: 'goods_specs', label: this.$t('goods.view_goodslist.goods_specs'), field: 'goods_specs', align: 'center' },
        { name: 'goods_origin', label: this.$t('goods.view_goodslist.goods_origin'), field: 'goods_origin', align: 'center' },
        { name: 'goods_cost', label: this.$t('goods.view_goodslist.goods_cost'), field: 'goods_cost', align: 'center' },
        { name: 'goods_price', label: this.$t('goods.view_goodslist.goods_price'), field: 'goods_price', align: 'center' },
        { name: 'creater', label: this.$t('creater'), field: 'creater', align: 'center' },
        { name: 'create_time', label: this.$t('createtime'), field: 'create_time', align: 'center' },
        { name: 'update_time', label: this.$t('updatetime'), field: 'update_time', align: 'center' }
      ],
      filter: '',
      pagination: {
        page: 1,
        rowsPerPage: '10000'
      },
      screenq: this.$q.screen,
      IMEI: window.device,
      batteryStatus: 'determining...',
      barscan: '',
      goods_scan: ''
    }
  },
  methods: {
    datachange () {
      var _this = this
      if (_this.$q.localStorage.has('auth')) {
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
      } else {
      }
    },
    countAdd (e) {
      var _this = this
      _this.table_list.filter(function (value, index, array) {
        if (value.bin_name === _this.bin_scan && value.goods_code === e) {
          _this.table_list[index].physical_inventory += 1
        }
      })
    },
    getList () {
      var _this = this
      if (_this.$q.localStorage.has('auth')) {
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
      } else {
      }
    },
    reFresh () {
      var _this = this
      _this.barscan = ''
      _this.bin_scan = ''
      _this.goods_scan = ''
      _this.getList()
    },
    ConfirmCount () {
      var _this = this
      if (LocalStorage.has('auth')) {
        putauth(_this.pathname, _this.table_list).then(res => {
          _this.$q.notify({
            message: 'Success Confirm Cycle Count',
            icon: 'check',
            color: 'green'
          })
        }).catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
      } else {
      }
    },
    updateBatteryStatus (status) {
      var _this = this
      _this.batteryStatus = `Level: ${status.level}, plugged: ${status.isPlugged}`
    },
    scanEvents () {
      var _this = this
      document.addEventListener('deviceready', _this.onDeviceReady, false)
    },
    onDeviceReady () {
      var _this = this
      _this.receivedEvent('deviceready')
      _this.registerBroadcastReceiver()
      _this.determineVersion()
    },
    onPause: function () {
      unregisterBroadcastReceiver()
    },
    onResume () {
      var _this = this
      _this.registerBroadcastReceiver()
    },
    receivedEvent (id) {
    },
    startSoftTrigger () {
      sendCommand('com.symbol.datawedge.api.SOFT_SCAN_TRIGGER', 'START_SCANNING')
    },
    stopSoftTrigger () {
      sendCommand('com.symbol.datawedge.api.SOFT_SCAN_TRIGGER', 'STOP_SCANNING')
    },
    determineVersion () {
      sendCommand('com.symbol.datawedge.api.GET_VERSION_INFO', '')
    },
    setDecoders () {
      //  Set the new configuration
      var profileConfig = {
        PROFILE_NAME: 'wms',
        PROFILE_ENABLED: 'true',
        CONFIG_MODE: 'UPDATE',
        PLUGIN_CONFIG: {
          PLUGIN_NAME: 'BARCODE',
          PARAM_LIST: {
            // "current-device-id": this.selectedScannerId,
            scanner_selection: 'auto'
          }
        }
      }
      sendCommand('com.symbol.datawedge.api.SET_CONFIG', profileConfig)
    },
    registerBroadcastReceiver () {
      window.plugins.intentShim.registerBroadcastReceiver({
        filterActions: [
          'com.greaterwms.app.ACTION',
          'com.symbol.datawedge.api.RESULT_ACTION'
        ],
        filterCategories: [
          'android.intent.category.DEFAULT'
        ]
      },
      function (intent) {
        // eslint-disable-next-line no-prototype-builtins
        if (intent.extras.hasOwnProperty('RESULT_INFO')) {
          var commandResult = intent.extras.RESULT + ' (' +
              intent.extras.COMMAND.substring(intent.extras.COMMAND.lastIndexOf('.') + 1, intent.extras.COMMAND.length) + ')'// + JSON.stringify(intent.extras.RESULT_INFO);
          commandReceived(commandResult.toLowerCase())
        }
        // eslint-disable-next-line no-prototype-builtins
        if (intent.extras.hasOwnProperty('com.symbol.datawedge.api.RESULT_GET_VERSION_INFO')) {
          //  The version has been returned (DW 6.3 or higher).  Includes the DW version along with other subsystem versions e.g MX
          var versionInfo = intent.extras['com.symbol.datawedge.api.RESULT_GET_VERSION_INFO']
          var datawedgeVersion = versionInfo.DATAWEDGE
          //  Fire events sequentially so the application can gracefully degrade the functionality available on earlier DW versions
          if (datawedgeVersion >= '6.3') {
            sendCommand('com.symbol.datawedge.api.CREATE_PROFILE', 'wms')
            sendCommand('com.symbol.datawedge.api.GET_ACTIVE_PROFILE', '')
            sendCommand('com.symbol.datawedge.api.ENUMERATE_SCANNERS', '')
          }
          if (datawedgeVersion >= '6.4') {
            var profileConfig = {
              PROFILE_NAME: 'wms',
              PROFILE_ENABLED: 'true',
              CONFIG_MODE: 'UPDATE',
              PLUGIN_CONFIG: {
                PLUGIN_NAME: 'BARCODE',
                RESET_CONFIG: 'true',
                PARAM_LIST: {}
              },
              APP_LIST: [{
                PACKAGE_NAME: 'com.greaterwms.app',
                ACTIVITY_LIST: ['*']
              }]
            }
            sendCommand('com.symbol.datawedge.api.SET_CONFIG', profileConfig)
            //  Configure the created profile (intent plugin)
            var profileConfig2 = {
              PROFILE_NAME: 'wms',
              PROFILE_ENABLED: 'true',
              CONFIG_MODE: 'UPDATE',
              PLUGIN_CONFIG: {
                PLUGIN_NAME: 'INTENT',
                RESET_CONFIG: 'true',
                PARAM_LIST: {
                  intent_output_enabled: 'true',
                  intent_action: 'com.greaterwms.app.ACTION',
                  intent_delivery: '2'
                }
              }
            }
            sendCommand('com.symbol.datawedge.api.SET_CONFIG', profileConfig2)
            //  Give some time for the profile to settle then query its value
            setTimeout(function () {
              sendCommand('com.symbol.datawedge.api.GET_ACTIVE_PROFILE', '')
            }, 1000)
          }
          if (datawedgeVersion >= '6.5') {
            //  Instruct the API to send
            sendCommandResults = 'true'
          }
          // eslint-disable-next-line no-prototype-builtins
        } else if (intent.extras.hasOwnProperty('com.symbol.datawedge.api.RESULT_ENUMERATE_SCANNERS')) {
          //  Return from our request to enumerate the available scanners
          var enumeratedScannersObj = intent.extras['com.symbol.datawedge.api.RESULT_ENUMERATE_SCANNERS']
          enumerateScanners(enumeratedScannersObj)
          // eslint-disable-next-line no-prototype-builtins
        } else if (intent.extras.hasOwnProperty('com.symbol.datawedge.api.RESULT_GET_ACTIVE_PROFILE')) {
          //  Return from our request to obtain the active profile
          var activeProfileObj = intent.extras['com.symbol.datawedge.api.RESULT_GET_ACTIVE_PROFILE']
          activeProfile(activeProfileObj)
          // eslint-disable-next-line no-prototype-builtins
        } else if (!intent.extras.hasOwnProperty('RESULT_INFO')) {
          //  A barcode has been scanned
          barcodeScanned(intent, new Date().toLocaleString())
        }
      }
      )
    }
  },
  created () {
    var _this = this
    if (_this.$q.localStorage.has('openid')) {
      _this.openid = _this.$q.localStorage.getItem('openid')
    } else {
      _this.openid = ''
      _this.$q.localStorage.set('openid', '')
    }
    if (_this.$q.localStorage.has('login_name')) {
      _this.login_name = _this.$q.localStorage.getItem('login_name')
    } else {
      _this.login_name = ''
      _this.$q.localStorage.set('login_name', '')
    }
    if (_this.$q.localStorage.has('auth')) {
      _this.authin = '1'
    } else {
      _this.authin = '0'
    }
  },
  mounted () {
    var _this = this
    window.addEventListener('batterystatus', _this.updateBatteryStatus, false)
    _this.height = this.$q.screen.height - 175 + '' + 'px'
    _this.barscan = ''
    _this.goods_scan = ''
    _this.scanEvents()
  },
  updated () {
  },
  beforeDestroy () {
    var _this = this
    window.removeEventListener('batterystatus', _this.updateBatteryStatus, false)
    window.removeEventListener('deviceready', _this.onDeviceReady, false)
  },
  destroyed () {
  }
}
</script>
