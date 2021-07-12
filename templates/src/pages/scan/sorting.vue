<template>
    <div>
      <h1>Zebra Cordova DataWedge Demo</h1>
        <H3>Information / Configuration</H3>
        <div class="header">Datawedge version:</div>
        <div class="info attention" id="info_datawedgeVersion">Pre 6.3. Please create &amp; configure profile manually. See the ReadMe for more details</div>
        <P></P>
        <div class="header">Active Profile:</div>
        <div class="info" id="info_activeProfile">Requires Datawedge 6.3+</div>
        <P></P>
        <div class="header" id="header_lastApiMessage">Last API message:</div>
        <div class="info" id="info_lastApiMessage">Messages from Datawedge will go here</div>
        <P></P>
        <div class="header">Available scanners:</div>
        <div class="info" id="info_availableScanners">Requires Datawedge 6.3+</div>
        <P></P>
        <table width="100%">
            <tr>
                <td align="left">
                    <div>
                        <input id="chk_ean8" type="checkbox" @change='setDecoders(this);' checked>
                        <label for="chk_ean8">EAN 8</label>
                    </div>
                </td>
                <td align="left">
                    <div>
                        <input id="chk_ean13" type="checkbox" @change='setDecoders(this);' checked>
                        <label for="chk_ean13">EAN 13</label>
                    </div>
                </td>
            </tr>
            <tr>
                <td align="left">
                    <div>
                        <input id="chk_code39" type="checkbox" @change='setDecoders(this);' checked>
                        <label for="chk_code39">Code 39</label>
                    </div>
                </td>
                <td align="left">
                    <div>
                        <input id="chk_code128" type="checkbox" @change='setDecoders(this);' checked>
                        <label for="chk_code128">Code 128</label>
                    </div>
                </td>
            </tr>
        </table>
        <div class="event action" id="scanButton">Scan</div>
        <H3>Scanned Barcodes</H3>
        <div class="event display" id="scannedBarcodes">Scanned barcodes will be displayed here</div>
      <transition appear enter-active-class="animated fadeIn">
      <q-table
        class="my-sticky-header-table shadow-24"
        :data="table_list"
        row-key="id"
        :separator="separator"
        :loading="loading"
        :filter="filter"
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
             <q-btn :label="$t('refresh')" @click="reFresh()" />
           </q-btn-group>
           {{ IMEI }}
           {{ batteryStatus }}
           {{ barscan }}
           <q-space />
           <q-input class="cordova-search" outlined rounded dense debounce="300" color="primary" v-model="filter" :placeholder="$t('search')" @blur="getSearchList()" @keyup.enter="getSearchList()">
             <template v-slot:append>
               <q-icon name="search" @click="getSearchList()"/>
             </template>
           </q-input>
         </template>
         <template v-slot:body="props">
           <q-tr :props="props">
               <q-td key="goods_code" :props="props">
                 {{ props.row.goods_code }}
               </q-td>
               <q-td key="onhand_stock" :props="props">
                 {{ props.row.onhand_stock }}
               </q-td>
               <q-td key="qty" :props="props">
                 {{ props.row.qty }}
               </q-td>
           </q-tr>
         </template>
        </q-table>
      </transition>
      <template>
        <div class="q-pa-lg flex flex-center cordova-footer">
          <q-btn v-show="pathname_previous" flat push color="purple" :label="$t('previous')" icon="navigate_before" @click="getListPrevious()">
            <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
              {{ $t('previous') }}
            </q-tooltip>
          </q-btn>
          <q-btn v-show="pathname_next" flat push color="purple" :label="$t('next')" icon-right="navigate_next" @click="getListNext()">
            <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
              {{ $t('next') }}
            </q-tooltip>
          </q-btn>
          <q-btn v-show="!pathname_previous && !pathname_next" flat push color="dark" :label="$t('no_data')"></q-btn>
        </div>
      </template>
    </div>
</template>
    <router-view />
<style>
h1 {
    font-size:24px;
    font-weight:normal;
    margin:0px;
    overflow:visible;
    padding:0px;
    text-align:center;
}

.info {
    text-align:left;
    font-size:14px;
}

.header {
    text-align:left;
    font-size:12px;
    font-weight:bold;
}

.attention {
    background-color:#FFD200;
    color:#000000;
}

.event {
    border-radius:4px;
    -webkit-border-radius:4px;
    color:#FFFFFF;
    font-size:14px;
    margin:10px 10px 10px 10px;
    padding:2px 0px;
    word-break: break-word;
}

.event.listening {
    background-color:#333333;
    display:block;
}

.event.action {
    background-color:#ffd200;
    color:#000000;
    display:block;
    padding:10px 0px;
}

.event.display {
    background-color:#0077A0;
    color:#FFFFFF;
}

.event.received {
    background-color:#4B946A;
    display:none;
}

@keyframes fade {
    from { opacity: 1.0; }
    50% { opacity: 0.4; }
    to { opacity: 1.0; }
}

@-webkit-keyframes fade {
    from { opacity: 1.0; }
    50% { opacity: 0.4; }
    to { opacity: 1.0; }
}

.blink {
    animation:fade 3000ms infinite;
    -webkit-animation:fade 3000ms infinite;
}
</style>
<script>
import { getauth } from 'boot/axios_request'
var sendCommandResults = 'false'
var scans = []

function sendCommand (extraName, extraValue) {
  console.log('Sending Command: ' + extraName + ', ' + JSON.stringify(extraValue))
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
  document.getElementById('info_lastApiMessage').innerHTML = commandText
}
function enumerateScanners (enumeratedScanners) {
  var humanReadableScannerList = ''
  for (var i = 0; i < enumeratedScanners.length; i++) {
    console.log('Scanner found: name= ' + enumeratedScanners[i].SCANNER_NAME + ', id=' + enumeratedScanners[i].SCANNER_INDEX + ', connected=' + enumeratedScanners[i].SCANNER_CONNECTION_STATE)
    humanReadableScannerList += enumeratedScanners[i].SCANNER_NAME
    if (i < enumeratedScanners.length - 1) { humanReadableScannerList += ', ' }
  }
  document.getElementById('info_availableScanners').innerHTML = humanReadableScannerList
}
function activeProfile (theActiveProfile) {
  document.getElementById('info_activeProfile').innerHTML = theActiveProfile
}
function barcodeScanned (scanData, timeOfScan) {
  var scannedData = scanData.extras['com.symbol.datawedge.data_string']
  var scannedType = scanData.extras['com.symbol.datawedge.label_type']
  console.log('Scan: ' + scannedData)
  scans.unshift({ data: scannedData, decoder: scannedType, timeAtDecode: timeOfScan })
  console.log(scans)
  var scanDisplay = ''
  for (var i = 0; i < scans.length; i++) {
    scanDisplay += '<b><small>' + scans[i].decoder + ' (' + scans[i].timeAtDecode + ')</small></b><br>' + scans[i].data + '<br><br>'
  }
  document.getElementById('scannedBarcodes').innerHTML = scanDisplay
}

export default {
  name: 'Pagemovetobin_scan',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'stock/bin/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      columns: [
        { name: 'goods_code', required: true, label: this.$t('scan.view_binmove.goods_code'), align: 'left', field: 'goods_code' },
        { name: 'onhand_stock', label: this.$t('scan.view_binmove.onhand_stock'), field: 'onhand_stock', align: 'center' },
        { name: 'qty', label: this.$t('scan.view_binmove.qty'), field: 'qty', align: 'center' }
      ],
      filter: '',
      pagination: {
        page: 1,
        rowsPerPage: '30'
      },
      screenq: this.$q.screen,
      IMEI: window.device,
      batteryStatus: 'determining...',
      barscan: []
    }
  },
  methods: {
    getSearchList () {
      var _this = this
      if (_this.$q.localStorage.has('auth')) {
        getauth(_this.pathname + '?bin_name=' + _this.filter, {
        }).then(res => {
          _this.table_list = res.results
          if (res.previous) {
            var previous = res.previous.split(':')[0]
            var previouspage = res.previous.replace(previous, window.location.href.split(':')[0])
            _this.pathname_previous = previouspage
          } else {
            _this.pathname_previous = res.previous
          }
          if (res.next) {
            var next = res.next.split(':')[0]
            var nextpage = res.next.replace(next, window.location.href.split(':')[0])
            _this.pathname_next = nextpage
          } else {
            _this.pathname_next = res.next
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
    getListPrevious () {
      var _this = this
      if (_this.$q.localStorage.has('auth')) {
        getauth(_this.pathname_previous, {
        }).then(res => {
          _this.table_list = res.results
          if (res.previous) {
            var previous = res.previous.split(':')[0]
            var previouspage = res.previous.replace(previous, window.location.href.split(':')[0])
            _this.pathname_previous = previouspage
          } else {
            _this.pathname_previous = res.previous
          }
          if (res.next) {
            var next = res.next.split(':')[0]
            var nextpage = res.next.replace(next, window.location.href.split(':')[0])
            _this.pathname_next = nextpage
          } else {
            _this.pathname_next = res.next
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
    getListNext () {
      var _this = this
      if (_this.$q.localStorage.has('auth')) {
        getauth(_this.pathname_next, {
        }).then(res => {
          _this.table_list = res.results
          if (res.previous) {
            var previous = res.previous.split(':')[0]
            var previouspage = res.previous.replace(previous, window.location.href.split(':')[0])
            _this.pathname_previous = previouspage
          } else {
            _this.pathname_previous = res.previous
          }
          if (res.next) {
            var next = res.next.split(':')[0]
            var nextpage = res.next.replace(next, window.location.href.split(':')[0])
            _this.pathname_next = nextpage
          } else {
            _this.pathname_next = res.next
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
    reFresh () {
      var _this = this
      _this.getList()
    },
    updateBatteryStatus (status) {
      this.batteryStatus = `Level: ${status.level}, plugged: ${status.isPlugged}`
    },
    scanEvents () {
      var _this = this
      document.addEventListener('deviceready', _this.onDeviceReady, false)
    },
    onDeviceReady () {
      this.receivedEvent('deviceready')
      document.getElementById('scanButton').addEventListener('touchstart', this.startSoftTrigger)
      document.getElementById('scanButton').addEventListener('click', this.startSoftTrigger)
      // document.getElementById('disableScanningButton').addEventListener('click', this.disableEnableScanning)
      document.getElementById('scanButton').addEventListener('touchend', this.stopSoftTrigger)
      document.getElementById('scanButton').style.display = 'none'
      document.getElementById('header_lastApiMessage').style.display = 'none'
      document.getElementById('info_lastApiMessage').style.display = 'none'
      document.getElementById('chk_ean8').disabled = true
      document.getElementById('chk_ean13').disabled = true
      document.getElementById('chk_code39').disabled = true
      document.getElementById('chk_code128').disabled = true
      this.registerBroadcastReceiver()
      this.determineVersion()
    },
    onPause: function () {
      console.log('Paused')
      unregisterBroadcastReceiver()
    },
    onResume () {
      console.log('Resumed')
      this.registerBroadcastReceiver()
    },
    receivedEvent (id) {
      console.log('Received Event: ' + id)
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
      var ean8Decoder = '' + document.getElementById('chk_ean8').checked
      var ean13Decoder = '' + document.getElementById('chk_ean13').checked
      var code39Decoder = '' + document.getElementById('chk_code39').checked
      var code128Decoder = '' + document.getElementById('chk_code128').checked
      //  Set the new configuration
      var profileConfig = {
        PROFILE_NAME: 'wms',
        PROFILE_ENABLED: 'true',
        CONFIG_MODE: 'UPDATE',
        PLUGIN_CONFIG: {
          PLUGIN_NAME: 'BARCODE',
          PARAM_LIST: {
            // "current-device-id": this.selectedScannerId,
            scanner_selection: 'auto',
            decoder_ean8: '' + ean8Decoder,
            decoder_ean13: '' + ean13Decoder,
            decoder_code128: '' + code128Decoder,
            decoder_code39: '' + code39Decoder
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
        console.log('Received Intent: ' + JSON.stringify(intent))
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
          console.log('Version Info: ' + JSON.stringify(versionInfo))
          var datawedgeVersion = versionInfo.DATAWEDGE
          console.log('Datawedge version: ' + datawedgeVersion)
          //  Fire events sequentially so the application can gracefully degrade the functionality available on earlier DW versions
          if (datawedgeVersion >= '6.3') {
            console.log('Datawedge 6.3 APIs are available')
            //  Create a profile for our application
            sendCommand('com.symbol.datawedge.api.CREATE_PROFILE', 'wms')
            document.getElementById('info_datawedgeVersion').innerHTML = '6.3.  Please configure profile manually.  See ReadMe for more details.'
            //  Although we created the profile we can only configure it with DW 6.4.
            sendCommand('com.symbol.datawedge.api.GET_ACTIVE_PROFILE', '')
            //  Enumerate the available scanners on the device
            sendCommand('com.symbol.datawedge.api.ENUMERATE_SCANNERS', '')
            //  Functionality of the scan button is available
            document.getElementById('scanButton').style.display = 'block'
          }
          if (datawedgeVersion >= '6.4') {
            console.log('Datawedge 6.4 APIs are available')
            //  Documentation states the ability to set a profile config is only available from DW 6.4.
            //  For our purposes, this includes setting the decoders and configuring the associated app / output params of the profile.
            document.getElementById('info_datawedgeVersion').innerHTML = '6.4.'
            document.getElementById('info_datawedgeVersion').classList.remove('attention')
            //  Decoders are now available
            document.getElementById('chk_ean8').disabled = false
            document.getElementById('chk_ean13').disabled = false
            document.getElementById('chk_code39').disabled = false
            document.getElementById('chk_code128').disabled = false
            //  Configure the created profile (associated app and keyboard plugin)
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
            console.log('Datawedge 6.5 APIs are available')
            document.getElementById('info_datawedgeVersion').innerHTML = '6.5 or higher.'
            //  Instruct the API to send
            sendCommandResults = 'true'
            document.getElementById('header_lastApiMessage').style.display = 'block'
            document.getElementById('info_lastApiMessage').style.display = 'block'
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
    _this.scanEvents()
    window.addEventListener('batterystatus', this.updateBatteryStatus, false)
    _this.height = this.$q.screen.height - 170 + '' + 'px'
  },
  updated () {
  },
  beforeDestroy () {
    window.removeEventListener('batterystatus', this.updateBatteryStatus, false)
  },
  destroyed () {
  }
}
</script>
