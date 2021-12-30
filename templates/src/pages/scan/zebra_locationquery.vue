<template>
  <q-page>
    <q-card v-show="!fab" class="shadow-24" :style="{ width: width,  height: height }">
      <q-card-section>
          <q-input dense v-model="bin_scan" type="text" :label="bin_name_label" readonly disabled/>
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
import { getauth } from 'boot/axios_request'
import { LocalStorage, Platform, Screen } from 'quasar'

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
  name: 'Pagezebra_locationquery',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'stock/bin/',
      separator: 'cell',
      loading: false,
      device: LocalStorage.getItem('device'),
      device_name: LocalStorage.getItem('device_name'),
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
      fab: false,
      touchheight: ((Screen.width - 50) / 5) + '' + 'px',
      touchwidth: ((Screen.width - 50) / 5) + '' + 'px',
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
      barscan: '',
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
    if (Platform.is.electron) {
      _this.height = String(Screen.height) + 'px'
    } else if (Platform.is.cordova) {
      _this.device_name = LocalStorage.getItem('device_name')
      if (LocalStorage.getItem('device') === 2) {
        window.plugins.insomnia.keepAwake()
        if (LocalStorage.getItem('device_name') === 'Urovo' || LocalStorage.getItem('device_name') === 'Zebra Technologies') {
          _this.fab1.top = '0px'
          _this.fab1.bottom = (0 - ((Screen.width - 50) / 5)) + '' + 'px'
          _this.fab1.left = (((Screen.width - 50) / 6) - (Screen.width / 12 * 10)) + '' + 'px'
          _this.fab1.right = '0px'
          _this.fab2.top = '0px'
          _this.fab2.bottom = (0 - ((Screen.width - 50) / 5)) + '' + 'px'
          _this.fab2.left = ((((Screen.width - 50) / 6) - (Screen.width / 12 * 10)) / 2) + '' + 'px'
          _this.fab2.right = '0px'
          _this.fab3.top = '0px'
          _this.fab3.bottom = '0px'
          _this.fab3.left = '-0px'
          _this.fab3.right = '0px'
          _this.fab4.top = ((Screen.width - 50) / 5) + '' + 'px'
          _this.fab4.bottom = (0 - ((Screen.width - 50) / 5)) + '' + 'px'
          _this.fab4.left = (((Screen.width - 50) / 6) - (Screen.width / 12 * 10)) + '' + 'px'
          _this.fab4.right = '0px'
          _this.fab5.top = '0px'
          _this.fab5.bottom = (0 - ((Screen.width - 50) / 5)) + '' + 'px'
          _this.fab5.left = ((((Screen.width - 50) / 6) - (Screen.width / 12 * 10)) / 2) + '' + 'px'
          _this.fab5.right = '0px'
          _this.fab6.top = '0px'
          _this.fab6.bottom = '0px'
          _this.fab6.left = '0px'
          _this.fab6.right = '0px'
          _this.fab7.top = ((Screen.width - 50) / 5) + '' + 'px'
          _this.fab7.bottom = (0 - ((Screen.width - 50) / 5)) + '' + 'px'
          _this.fab7.left = (((Screen.width - 50) / 6) - (Screen.width / 12 * 10)) + '' + 'px'
          _this.fab7.right = '0px'
          _this.fab8.top = '0px'
          _this.fab8.bottom = ((Screen.width - 50) / 8) + '' + 'px'
          _this.fab8.left = ((((Screen.width - 50) / 6) - (Screen.width / 12 * 10)) / 2) + '' + 'px'
          _this.fab8.right = '0px'
        }
      }
    } else {
      _this.height = Screen.height + '' + 'px'
    }
    _this.width = Screen.width * 1 + '' + 'px'
    _this.height = Screen.height - 50 + '' + 'px'
    _this.scroll_height = Screen.height - 175 + '' + 'px'
    _this.barscan = ''
    _this.bin_scan = ''
    _this.scanEvents()
  },
  beforeDestroy () {
    var _this = this
    window.removeEventListener('deviceready', _this.onDeviceReady, false)
  }
}
</script>
