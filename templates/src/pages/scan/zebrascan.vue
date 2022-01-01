<template>
  <q-page>
    <router-view />
    <q-page-sticky position="bottom-left" :offset="[18, 18]">
      <input id="scannedBarcodes" v-model="barscan" type="text" readonly disabled/>
    </q-page-sticky>
    <q-page-sticky position="bottom-right" :offset="[18, 18]">
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
          :to="{ name: 'zebra_locationquery' }"
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
          :to="{ name: 'zebra_goodslist' }"
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
          :to="{ name: 'zebra_cyclecount' }"
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
          :to="{ name: 'zebra_movetobin' }"
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
          :to="{ name: 'zebra_shipping' }"
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
          :to="{ name: 'zebra_picking' }"
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
          :to="{ name: 'zebra_uptobin' }"
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
          :to="{ name: 'zebra_sorting' }"
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

<script>
import { getauth } from 'boot/axios_request'
import { LocalStorage, Screen, throttle } from 'quasar'

var sendCommandResults = 'false'

var scanner = {
  initialize: function () {
    this.bindEvents()
  },
  bindEvents: function () {
    document.addEventListener('deviceready', this.onDeviceReady, false)
  },
  onDeviceReady: function () {
    scanner.receivedEvent('deviceready')
    registerBroadcastReceiver()
    determineVersion()
  },
  onPause: function () {
    console.log('Paused')
    unregisterBroadcastReceiver()
  },
  onResume: function () {
    console.log('Resumed')
    registerBroadcastReceiver()
  },
  receivedEvent: function (id) {
    console.log('Received Event: ' + id)
  }
}

scanner.initialize()

function startSoftTrigger () {
  sendCommand('com.symbol.datawedge.api.SOFT_SCAN_TRIGGER', 'START_SCANNING')
}

function stopSoftTrigger () {
  sendCommand('com.symbol.datawedge.api.SOFT_SCAN_TRIGGER', 'STOP_SCANNING')
}

function determineVersion () {
  sendCommand('com.symbol.datawedge.api.GET_VERSION_INFO', '')
}

function setDecoders () {
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
      }
    }
  }
  sendCommand('com.symbol.datawedge.api.SET_CONFIG', profileConfig)
}

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

function registerBroadcastReceiver () {
  window.plugins.intentShim.registerBroadcastReceiver({
    filterActions: [
      'com.zebra.cordovademo.ACTION',
      'com.symbol.datawedge.api.RESULT_ACTION'
    ],
    filterCategories: [
      'android.intent.category.DEFAULT'
    ]
  },
  function (intent) {
    //  Broadcast received
    console.log('Received Intent: ' + JSON.stringify(intent.extras))
    if (intent.extras.hasOwnProperty('RESULT_INFO')) {
      var commandResult = intent.extras.RESULT + ' (' +
                    intent.extras.COMMAND.substring(intent.extras.COMMAND.lastIndexOf('.') + 1, intent.extras.COMMAND.length) + ')'// + JSON.stringify(intent.extras.RESULT_INFO);
      commandReceived(commandResult.toLowerCase())
    }

    if (intent.extras.hasOwnProperty('com.symbol.datawedge.api.RESULT_GET_VERSION_INFO')) {
      //  The version has been returned (DW 6.3 or higher).  Includes the DW version along with other subsystem versions e.g MX
      var versionInfo = intent.extras['com.symbol.datawedge.api.RESULT_GET_VERSION_INFO']
      console.log('Version Info: ' + JSON.stringify(versionInfo))
      var datawedgeVersion = versionInfo.DATAWEDGE
      datawedgeVersion = datawedgeVersion.padStart(5, '0')
      console.log('Datawedge version: ' + datawedgeVersion)

      //  Fire events sequentially so the application can gracefully degrade the functionality available on earlier DW versions
      if (datawedgeVersion >= '006.3') { datawedge63() }
      if (datawedgeVersion >= '006.4') { datawedge64() }
      if (datawedgeVersion >= '006.5') { datawedge65() }
    } else if (intent.extras.hasOwnProperty('com.symbol.datawedge.api.RESULT_ENUMERATE_SCANNERS')) {
      //  Return from our request to enumerate the available scanners
      var enumeratedScannersObj = intent.extras['com.symbol.datawedge.api.RESULT_ENUMERATE_SCANNERS']
      enumerateScanners(enumeratedScannersObj)
    } else if (intent.extras.hasOwnProperty('com.symbol.datawedge.api.RESULT_GET_ACTIVE_PROFILE')) {
      //  Return from our request to obtain the active profile
      var activeProfileObj = intent.extras['com.symbol.datawedge.api.RESULT_GET_ACTIVE_PROFILE']
      activeProfile(activeProfileObj)
    } else if (!intent.extras.hasOwnProperty('RESULT_INFO')) {
      //  A barcode has been scanned
      barcodeScanned(intent, new Date().toLocaleString())
    }
  }
  )
}

function unregisterBroadcastReceiver () {
  window.plugins.intentShim.unregisterBroadcastReceiver()
}

function datawedge63 () {
  console.log('Datawedge 6.3 APIs are available')
  sendCommand('com.symbol.datawedge.api.CREATE_PROFILE', 'ZebraCordovaDemo')
  sendCommand('com.symbol.datawedge.api.GET_ACTIVE_PROFILE', '')
  sendCommand('com.symbol.datawedge.api.ENUMERATE_SCANNERS', '')
}

function datawedge64 () {
  console.log('Datawedge 6.4 APIs are available')
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
      PACKAGE_NAME: 'org.greaterwms.app',
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
        intent_action: 'com.zebra.cordovademo.ACTION',
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

function datawedge65 () {
  console.log('Datawedge 6.5 APIs are available')
  sendCommandResults = 'true'
}

function commandReceived (commandText) {
  console.log('commandReceived:', commandText)
}

function enumerateScanners (enumeratedScanners) {
  var humanReadableScannerList = ''
  for (var i = 0; i < enumeratedScanners.length; i++) {
    console.log('Scanner found: name= ' + enumeratedScanners[i].SCANNER_NAME + ', id=' + enumeratedScanners[i].SCANNER_INDEX + ', connected=' + enumeratedScanners[i].SCANNER_CONNECTION_STATE)
    humanReadableScannerList += enumeratedScanners[i].SCANNER_NAME
    if (i < enumeratedScanners.length - 1) { humanReadableScannerList += ', ' }
  }
  console.log('enumerateScanners:', humanReadableScannerList)
}

function activeProfile (theActiveProfile) {
  console.log('activeProfile:', theActiveProfile)
}

function barcodeScanned (scanData, timeOfScan) {
  var scannedData = scanData.extras['com.symbol.datawedge.data_string']
  console.log('scaned Data:' + scannedData)
  document.getElementById('scannedBarcodes').value = ''
  document.getElementById('scannedBarcodes').value = scannedData
  document.getElementById('scannedBarcodes').dispatchEvent(new Event('input'))
}

export default {
  name: 'Pagezebra_scanbase',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'cyclecount/',
      separator: 'cell',
      loading: false,
      width: '',
      height: '',
      scroll_height: '',
      table_list: [],
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
    }
  },
  methods: {
    datachange (e) {
      if (LocalStorage.has('auth')) {
        getauth('scanner/?bar_code=' + e, {
        }).then(res => {
          return res
        }).catch(err => {
          return { detai: err.detail }
        })
      }
    }
  },
  computed: {
    fab: {
      get () {
        console.log('x', this.$store.state.fabchange.fab)
        return this.$store.state.fabchange.fab
      },
      set (val) {
        console.log('y', val)
        this.$store.commit('bardata/barScanned', '')
        this.$store.commit('fabchange/fabChanged', val)
      }
    },
    barscan: {
      get () {
        console.log('scaned_x', this.$store.state.bardata.barscan)
        return this.$store.state.bardata.barscan
      },
      set (val) {
        console.log('scaned_y', val)
        this.$store.commit('bardata/barScanned', '')
        this.$store.commit('bardata/barScanned', val)
        var barapi = this.datachange(val)
        barapi.push('111')
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
    _this.datachange = throttle(_this.datachange, 200)
  },
  mounted () {
    var _this = this
    window.plugins.insomnia.keepAwake()
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
    _this.barscan = ''
    _this.bin_scan = ''
    _this.goods_scan = ''
  },
  beforeDestroy () {
    window.removeEventListener('deviceready', scanner.onDeviceReady, false)
  },
  destroyed () {
    unregisterBroadcastReceiver()
  }
}
</script>
