<template>
  <q-page>
    <q-card v-show="!fab" class="shadow-24" :style="{ width: width,  height: height }">
      <q-card-section>
        <q-btn-group push>
          <q-btn :label="$t('refresh')" icon="refresh" @click="reFresh()" />
          <q-btn color='purple' :label="$t('stock.view_stocklist.cyclecountresult')" @click="ConfirmCount()" />
        </q-btn-group>
      </q-card-section>
      <q-scroll-area
        :thumb-style="thumbStyle"
        :bar-style="barStyle"
        :style="{ height: scroll_height, width: width }"
      >
        <q-markup-table>
          <thead>
          <tr>
            <th class="text-left">{{ goods_code_label }}</th>
            <th class="text-right">{{ goods_qty_label }}</th>
            <th class="text-right">{{ goods_actual_qty_label }}</th>
            <th class="text-right">{{ action_label }}</th>
          </tr>
          </thead>
          <tbody>
          <template>
            <tr v-for='(item, index) in sorted_list.goodsData' :key='index'>
              <td class="text-left">{{ item.goods_code }}</td>
              <td class="text-right">{{ item.goods_qty }}</td>
              <td class="text-right">{{ item.goods_actual_qty }}</td>
              <td class="text-right"><q-btn round flat push color="purple" icon="repeat" @click="repeatCount(index)" style="width: 50px"></q-btn></td>
            </tr>
          </template>
          </tbody>
        </q-markup-table>
      </q-scroll-area>
      <q-separator dark />
      <q-card-actions>
        <input id="scannedBarcodes" v-model="barscan" type="text" @input="datachange()" readonly disabled/>
      </q-card-actions>
    </q-card>
    <q-page-sticky v-show="device === 2" position="bottom-right" :offset="[18, 18]">
      <q-fab
        v-model="fab"
        icon="add"
        direction="up"
        color="accent"
        vertical-actions-align="left"
      >
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_locationquery')"
          label-style="background-color:transparent"
          v-show="device_name === 'Urovo'"
          to="urovo_locationquery"
          :style="{
                         'margin-top': fab8.top,
                         'margin-bottom': fab8.bottom,
                         'margin-left': fab8.left,
                         'margin-right': fab8.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/stock/stocklist.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_locationquery')"
          label-style="background-color:transparent"
          v-show="device_name === 'Zebra Technologies'"
          to="zebra_locationquery"
          :style="{
                         'margin-top': fab8.top,
                         'margin-bottom': fab8.bottom,
                         'margin-left': fab8.left,
                         'margin-right': fab8.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/stock/stocklist.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_goodsquery')"
          label-style="background-color:transparent"
          v-show="device_name === 'Urovo'"
          to="urovo_goodslist"
          :style="{
                         'margin-top': fab7.top,
                         'margin-bottom': fab7.bottom,
                         'margin-left': fab7.left,
                         'margin-right': fab7.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/goods/goodslist.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_goodsquery')"
          label-style="background-color:transparent"
          v-show="device_name === 'Zebra Technologies'"
          to="zebra_goodslist"
          :style="{
                         'margin-top': fab7.top,
                         'margin-bottom': fab7.bottom,
                         'margin-left': fab7.left,
                         'margin-right': fab7.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/goods/goodslist.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          icon="img:statics/stock/cyclecount.png"
          :label="$t('scan.scan_inventory')"
          label-style="background-color:transparent"
          v-show="device_name === 'Urovo'"
          to="urovo_cyclecount"
          :style="{
                         'margin-top': fab6.top,
                         'margin-bottom': fab6.bottom,
                         'margin-left': fab6.left,
                         'margin-right': fab6.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/stock/cyclecount.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          icon="img:statics/stock/cyclecount.png"
          :label="$t('scan.scan_inventory')"
          label-style="background-color:transparent"
          v-show="device_name === 'Zebra Technologies'"
          to="zebra_cyclecount"
          :style="{
                         'margin-top': fab6.top,
                         'margin-bottom': fab6.bottom,
                         'margin-left': fab6.left,
                         'margin-right': fab6.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/stock/cyclecount.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_movetobin')"
          label-style="background-color:transparent"
          v-show="device_name === 'Urovo'"
          to="urovo_movetobin"
          :style="{
                         'margin-top': fab5.top,
                         'margin-bottom': fab5.bottom,
                         'margin-left': fab5.left,
                         'margin-right': fab5.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/icons/movetobin.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_movetobin')"
          label-style="background-color:transparent"
          v-show="device_name === 'Zebra Technologies'"
          to="zebra_movetobin"
          :style="{
                         'margin-top': fab5.top,
                         'margin-bottom': fab5.bottom,
                         'margin-left': fab5.left,
                         'margin-right': fab5.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/icons/movetobin.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_shipping')"
          label-style="background-color:transparent"
          v-show="device_name === 'Urovo'"
          to="urovo_shipping"
          :style="{
                         'margin-top': fab4.top,
                         'margin-bottom': fab4.bottom,
                         'margin-left': fab4.left,
                         'margin-right': fab4.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/icons/car.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_shipping')"
          label-style="background-color:transparent"
          v-show="device_name === 'Zebra Technologies'"
          to="zebra_shipping"
          :style="{
                         'margin-top': fab4.top,
                         'margin-bottom': fab4.bottom,
                         'margin-left': fab4.left,
                         'margin-right': fab4.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/icons/car.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_picking')"
          label-style="background-color:transparent"
          v-show="device_name === 'Urovo'"
          to="urovo_picking"
          :style="{
                         'margin-top': fab3.top,
                         'margin-bottom': fab3.bottom,
                         'margin-left': fab3.left,
                         'margin-right': fab3.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/outbound/picked.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_picking')"
          label-style="background-color:transparent"
          v-show="device_name === 'Zebra Technologies'"
          to="zebra_picking"
          :style="{
                         'margin-top': fab3.top,
                         'margin-bottom': fab3.bottom,
                         'margin-left': fab3.left,
                         'margin-right': fab3.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/outbound/picked.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_uptobin')"
          label-style="background-color:transparent"
          v-show="device_name === 'Urovo'"
          to="urovo_uptobin"
          :style="{
                         'margin-top': fab2.top,
                         'margin-bottom': fab2.bottom,
                         'margin-left': fab2.left,
                         'margin-right': fab2.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/inbound/presortstock.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_uptobin')"
          label-style="background-color:transparent"
          v-show="device_name === 'Zebra Technologies'"
          to="zebra_uptobin"
          :style="{
                         'margin-top': fab2.top,
                         'margin-bottom': fab2.bottom,
                         'margin-left': fab2.left,
                         'margin-right': fab2.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/inbound/presortstock.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_sorting')"
          label-style="background-color:transparent"
          v-show="device_name === 'Urovo'"
          to="urovo_sorting"
          :style="{
                         'margin-top': fab1.top,
                         'margin-bottom': fab1.bottom,
                         'margin-left': fab1.left,
                         'margin-right': fab1.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/inbound/preloadstock.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_sorting')"
          label-style="background-color:transparent"
          v-show="device_name === 'Zebra Technologies'"
          to="zebra_sorting"
          :style="{
                         'margin-top': fab1.top,
                         'margin-bottom': fab1.bottom,
                         'margin-left': fab1.left,
                         'margin-right': fab1.right,
                         'height': touchheight,
                         'width': touchwidth
              }">
          <q-img src="statics/inbound/preloadstock.png" />
        </q-fab-action>
      </q-fab>
    </q-page-sticky>
  </q-page>
</template>
<router-view />

<script>
import { getauth, putauth } from 'boot/axios_request'
import { LocalStorage } from 'quasar'

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
  name: 'Pageurovo_sorting',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'asn/detail/?asn_status=3&ordering=-id',
      device: 0,
      device_name: '',
      width: '',
      height: '',
      scroll_height: '',
      table_list: [],
      sorted_list: {
        asn_code: '',
        supplier: '',
        goodsData: [],
        creater: ''
      },
      goods_code_label: this.$t('goods.view_goodslist.goods_code'),
      goods_qty_label: this.$t('inbound.view_asn.goods_qty'),
      goods_actual_qty_label: this.$t('inbound.view_asn.goods_actual_qty'),
      action_label: this.$t('action'),
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
      fab: false,
      touchheight: ((this.$q.screen.width - 50) / 5) + '' + 'px',
      touchwidth: ((this.$q.screen.width - 50) / 5) + '' + 'px',
      fab1: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      fab2: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      fab3: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      fab4: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      fab5: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      fab6: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      fab7: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      fab8: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      batteryStatus: 'determining...',
      barscan: '',
      asn_scan: '',
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
    repeatCount (e) {
      var _this = this
      _this.table_list[e].physical_inventory = 0
    },
    ConfirmCount () {
      var _this = this
      if (LocalStorage.has('auth')) {
        putauth(_this.pathname, _this.table_list).then(res => {
          _this.table_list = []
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
    if (window.device) {
      if (window.device.manufacturer === 'Urovo' || window.device.manufacturer === 'Zebra Technologies') {
        _this.device_name = window.device.manufacturer
        _this.device = 2
      } else {
        _this.device = 1
      }
    } else {
      if (_this.$q.platform.is.mobile) {
        _this.device = 1
      }
    }
    if (_this.$q.platform.is.electron) {
      _this.height = String(_this.$q.screen.height) + 'px'
    } else if (_this.$q.platform.is.cordova) {
      if (window.device) {
        window.plugins.insomnia.keepAwake()
        if (window.device.manufacturer === 'Urovo' || window.device.manufacturer === 'Zebra Technologies') {
          _this.fab1.top = '0px'
          _this.fab1.bottom = (0 - ((_this.$q.screen.width - 50) / 5)) + '' + 'px'
          _this.fab1.left = (((_this.$q.screen.width - 50) / 6) - (_this.$q.screen.width / 12 * 10)) + '' + 'px'
          _this.fab1.right = '0px'
          _this.fab2.top = '0px'
          _this.fab2.bottom = (0 - ((_this.$q.screen.width - 50) / 5)) + '' + 'px'
          _this.fab2.left = ((((_this.$q.screen.width - 50) / 6) - (_this.$q.screen.width / 12 * 10)) / 2) + '' + 'px'
          _this.fab2.right = '0px'
          _this.fab3.top = '0px'
          _this.fab3.bottom = '0px'
          _this.fab3.left = '-0px'
          _this.fab3.right = '0px'
          _this.fab4.top = ((_this.$q.screen.width - 50) / 5) + '' + 'px'
          _this.fab4.bottom = (0 - ((_this.$q.screen.width - 50) / 5)) + '' + 'px'
          _this.fab4.left = (((_this.$q.screen.width - 50) / 6) - (_this.$q.screen.width / 12 * 10)) + '' + 'px'
          _this.fab4.right = '0px'
          _this.fab5.top = '0px'
          _this.fab5.bottom = (0 - ((_this.$q.screen.width - 50) / 5)) + '' + 'px'
          _this.fab5.left = ((((_this.$q.screen.width - 50) / 6) - (_this.$q.screen.width / 12 * 10)) / 2) + '' + 'px'
          _this.fab5.right = '0px'
          _this.fab6.top = '0px'
          _this.fab6.bottom = '0px'
          _this.fab6.left = '0px'
          _this.fab6.right = '0px'
          _this.fab7.top = ((_this.$q.screen.width - 50) / 5) + '' + 'px'
          _this.fab7.bottom = (0 - ((_this.$q.screen.width - 50) / 5)) + '' + 'px'
          _this.fab7.left = (((_this.$q.screen.width - 50) / 6) - (_this.$q.screen.width / 12 * 10)) + '' + 'px'
          _this.fab7.right = '0px'
          _this.fab8.top = '0px'
          _this.fab8.bottom = ((_this.$q.screen.width - 50) / 8) + '' + 'px'
          _this.fab8.left = ((((_this.$q.screen.width - 50) / 6) - (_this.$q.screen.width / 12 * 10)) / 2) + '' + 'px'
          _this.fab8.right = '0px'
        }
      }
    } else {
      _this.height = _this.$q.screen.height + '' + 'px'
    }
    window.addEventListener('batterystatus', _this.updateBatteryStatus, false)
    _this.width = _this.$q.screen.width * 1 + '' + 'px'
    _this.height = _this.$q.screen.height - 50 + '' + 'px'
    _this.scroll_height = _this.$q.screen.height - 175 + '' + 'px'
    _this.barscan = ''
    _this.asn_scan = ''
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
