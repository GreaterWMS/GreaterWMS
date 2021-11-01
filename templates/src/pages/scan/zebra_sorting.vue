<template>
    <div>
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
           {{Scandata}}
           <div id="scandata"></div>
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
            <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
              {{ $t('previous') }}
            </q-tooltip>
          </q-btn>
          <q-btn v-show="pathname_next" flat push color="purple" :label="$t('next')" icon-right="navigate_next" @click="getListNext()">
            <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
              {{ $t('next') }}
            </q-tooltip>
          </q-btn>
          <q-btn v-show="!pathname_previous && !pathname_next" flat push color="dark" :label="$t('no_data')"></q-btn>
        </div>
      </template>
    </div>
</template>
    <router-view />
<script>
import { getauth } from 'boot/axios_request'
var VConsole = require('vconsole')
var vConsole = new VConsole()
console.log(111)
var sendCommandResults = 'false'
const scandata = ''
function resurlt (data) {
  return data
}
document.addEventListener('mousedown', function (e) {
  if (e.target.id !== 'scandata') {
    e.preventDefault()
  }
}, false)
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
}
function activeProfile (theActiveProfile) {
}
function barcodeScanned (scanData, timeOfScan) {
  var scannedData = scanData.extras['com.symbol.datawedge.data_string']
  document.getElementById('scandata').value = scannedData
  scannedData = scandata
  console.log(222)
  console.log(scannedData)
  resurlt(scannedData)
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
      barscan: [],
      Scandata: scandata,
      scans: []
    }
  },
  methods: {
    // barcodeScanned (scanData, timeOfScan) {
    //   var _this = this
    //   var scannedData = scanData.extras['com.symbol.datawedge.data_string']
    //   var scannedType = scanData.extras['com.symbol.datawedge.label_type']
    //   document.getElementById('scandata').innerHTML = scannedData
    //   _this.scans.unshift({ data: scannedData, decoder: scannedType, timeAtDecode: timeOfScan })
    //   console.log(_this.scans)
    //   scannedData = scandata
    //   console.log(222)
    //   console.log(scannedData)
    // },
    getSearchList () {
      var _this = this
      if (_this.$q.localStorage.has('auth')) {
        getauth(_this.pathname + '?bin_name=' + _this.filter, {
        }).then(res => {
          _this.table_list = res.results
          _this.pathname_previous = res.previous
          _this.pathname_next = res.next
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
          _this.pathname_previous = res.previous
          _this.pathname_next = res.next
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
          _this.pathname_previous = res.previous
          _this.pathname_next = res.next
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
      this.registerBroadcastReceiver()
      this.determineVersion()
    },
    onPause: function () {
      unregisterBroadcastReceiver()
    },
    onResume () {
      this.registerBroadcastReceiver()
    },
    receivedEvent (id) {
    },
    startSoftTrigger () {
      sendCommand('com.symbol.datawedge.api.SOFT_SCAN_TRIGGER', 'START_SCANNING')
    },
    determineVersion () {
      sendCommand('com.symbol.datawedge.api.GET_VERSION_INFO', '')
    },
    setDecoders () {
      var profileConfig = {
        PROFILE_NAME: 'wms',
        PROFILE_ENABLED: 'true',
        CONFIG_MODE: 'UPDATE',
        PLUGIN_CONFIG: {
          PLUGIN_NAME: 'BARCODE',
          PARAM_LIST: {
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
        if (intent.extras.hasOwnProperty('RESULT_INFO')) {
          var commandResult = intent.extras.RESULT + ' (' +
                    intent.extras.COMMAND.substring(intent.extras.COMMAND.lastIndexOf('.') + 1, intent.extras.COMMAND.length) + ')'// + JSON.stringify(intent.extras.RESULT_INFO);
          commandReceived(commandResult.toLowerCase())
        }
        if (intent.extras.hasOwnProperty('com.symbol.datawedge.api.RESULT_GET_VERSION_INFO')) {
          var versionInfo = intent.extras['com.symbol.datawedge.api.RESULT_GET_VERSION_INFO']
          var datawedgeVersion = versionInfo.DATAWEDGE
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
            setTimeout(function () {
              sendCommand('com.symbol.datawedge.api.GET_ACTIVE_PROFILE', '')
            }, 1000)
          }
          if (datawedgeVersion >= '6.5') {
            sendCommandResults = 'true'
          }
        } else if (intent.extras.hasOwnProperty('com.symbol.datawedge.api.RESULT_ENUMERATE_SCANNERS')) {
          var enumeratedScannersObj = intent.extras['com.symbol.datawedge.api.RESULT_ENUMERATE_SCANNERS']
          enumerateScanners(enumeratedScannersObj)
        } else if (intent.extras.hasOwnProperty('com.symbol.datawedge.api.RESULT_GET_ACTIVE_PROFILE')) {
          var activeProfileObj = intent.extras['com.symbol.datawedge.api.RESULT_GET_ACTIVE_PROFILE']
          activeProfile(activeProfileObj)
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
  watch: {
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
