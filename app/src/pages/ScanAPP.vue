<template>
  <q-page v-show="!fab1 && !fab2 && !fab3 && !fab4" class="flex flex-top">
    <div :style="{ width: wholewidth, height: wholeheight, marginTop: '10px', marginLeft: '10px' }">
      <input id="scannedBarcodes" v-model="bar_check" type="text" style="display:none" />
      <q-input
         dense
         outlined
         square
         readonly
         disable
         debounce="500"
         v-model="scandata"
         :label="$t('scan.scan')"
       >
         <template v-slot:append>
           <q-icon name="search" />
         </template>
         <template v-slot:after>
           <q-btn
             round
             dense
             flat
             icon="border_horizontal"
             @click="StartScan"
           />
         </template>
        <template v-slot:before>
           <q-btn
             round
             dense
             flat
             icon="keyboard_return"
             @click="BackButton"
           />
         </template>
      </q-input>
      <q-scroll-area
        @scroll="onScroll"
        :delay="500"
        :thumb-style="thumbStyle"
        :bar-style="barStyle"
        :style="{ maxWidth: handlewidth, width: handlewidth, height: handleheight, marginTop: '10px' }"
      >

        <router-view />
      </q-scroll-area>
    </div>
  </q-page>
</template>

<script>
import {ref, computed, watch, defineComponent, onMounted, onBeforeUnmount} from 'vue'
import { useStore } from "vuex";
import { useRouter, useRoute } from 'vue-router'
import { useQuasar } from "quasar";
import axios from 'axios'
import { useI18n } from "vue-i18n"

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
    console.log(0, window.Media)
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
        scanner_selection: 'auto'
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
      PACKAGE_NAME: 'org.greaterwms.scanner.app',
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

function seuicDevice () {
  document.addEventListener('deviceready', seuicOndeviceReady, false)
}

function seuicOndeviceReady () {
  window.addEventListener('getcodedata', getData, false)
}

function getData (data) {
  document.getElementById('scannedBarcodes').value = ''
  document.getElementById('scannedBarcodes').value = data.data
  document.getElementById('scannedBarcodes').dispatchEvent(new Event('input'))
}

function iDataDevice () {
  document.addEventListener('deviceready', iDataOndeviceReady, false)
}

function iDataOndeviceReady () {
  window.addEventListener('idatadata', getiData, false)
}

function getiData (data) {
  document.getElementById('scannedBarcodes').value = ''
  document.getElementById('scannedBarcodes').value = data.data
  document.getElementById('scannedBarcodes').dispatchEvent(new Event('input'))
}

function playSuccAudio () {
  navigator.notification.beep(1)
}

export default defineComponent({
  name: 'ScanAPP',
  data () {
    return {
      wholewidth: (this.screenwidth - 20) + '' + 'px',
      wholeheight: (this.screenheight - 165) + '' + 'px',
      handlewidth: (this.screenwidth - 22) + '' + 'px',
      handleheight: (this.screenheight - 225) + '' + 'px'
    }
  },
  setup () {
    const $store = useStore()
    const $router = useRouter()
    const $route = useRoute()
    const $q = useQuasar()
    const bar_check = ref('')
    const { t } = useI18n()
    const fab1 = computed({
      get: () => $store.state.fabchange.fab1,
    })
    const fab2 = computed({
      get: () => $store.state.fabchange.fab2,
    })
    const fab3 = computed({
      get: () => $store.state.fabchange.fab3,
    })
    const fab4 = computed({
      get: () => $store.state.fabchange.fab4,
    })
    const oldlink = computed({
      get: () => $store.state.linkchange.oldlink,
      set: val => {
        $store.commit('linkchange/OldLinkChanged', val)
      }
    })
    const newlink = computed({
      get: () => $store.state.linkchange.newlink,
      set: val => {
        $store.commit('linkchange/NewLinkChanged', val)
      }
    })
    const screenwidth = computed({
      get: () => $store.state.screenchange.screenwidth,
      set: val => {
        $store.commit('screenchange/screenwidthChanged', val)
      }
    })
    const screenheight = computed({
      get: () => $store.state.screenchange.screenheight,
      set: val => {
        $store.commit('screenchange/screenheightChanged', val)
      }
    })
    const screenscroll = computed({
      get: () => $store.state.screenchange.screenscroll,
      set: val => {
        $store.commit('screenchange/screenScrollChanged', val)
      }
    })
    const authin = computed({
      get: () => $store.state.loginauth.authin,
    })
    const login_name = computed({
      get: () => $store.state.loginauth.login_name,
    })
    const operator = computed({
      get: () => $store.state.loginauth.operator,
    })
    const openid = computed({
      get: () => $store.state.settings.openid,
    })
    const lang = computed({
      get: () => $store.state.langchange.lang,
    })
    const baseurl = computed({
      get: () => $store.state.settings.server,
    })
    const scandata = computed({
      get: () => $store.state.scanchanged.scandata,
      set: val => {
        $store.commit('scanchanged/ScanChanged', val)
      }
    })
    const datadetail = computed({
      get: () => $store.state.scanchanged.datadetail,
      set: val => {
        $store.commit('scanchanged/ScanDataChanged', val)
      }
    })
    const asndata = computed({
      get: () => $store.state.scanchanged.asndata,
      set: val => {
        $store.commit('scanchanged/ASNDataChanged', val)
      }
    })
    const dndata = computed({
      get: () => $store.state.scanchanged.dndata,
      set: val => {
        $store.commit('scanchanged/DNDataChanged', val)
      }
    })
    const bindata = computed({
      get: () => $store.state.scanchanged.bindata,
      set: val => {
        $store.commit('scanchanged/BinDataChanged', val)
      }
    })
    const tablelist = computed({
      get: () => $store.state.scanchanged.tablelist,
      set: val => {
        $store.commit('scanchanged/TableDataChanged', val)
      }
    })
    const scanmode = computed({
      get: () => $store.state.scanchanged.scanmode,
      set: val => {
        $store.commit('scanchanged/ScanModeChanged', val)
      }
    })
    const bar_scanned = computed({
      get: () => $store.state.scanchanged.bar_scanned,
      set: val => {
        $store.commit('scanchanged/BarScannedChanged', val)
      }
    })
    const apiurl = computed({
      get: () => $store.state.scanchanged.apiurl,
      set: val => {
        $store.commit('scanchanged/ApiUrlChanged', val)
      }
    })
    const apiurlnext = computed({
      get: () => $store.state.scanchanged.apiurlnext,
      set: val => {
        $store.commit('scanchanged/ApiUrlNextChanged', val)
      }
    })
    const apiurlprevious = computed({
      get: () => $store.state.scanchanged.apiurlprevious,
      set: val => {
        $store.commit('scanchanged/ApiUrlPreviousChanged', val)
      }
    })
    const device_auth = computed({
      get: () => $store.state.appversion.device_auth,
      set: val => {
        $store.commit('appversion/DeviceAuthChanged', val)
      }
    })

    function onScroll (position) {
      screenscroll.value = position.verticalPercentage
    }

    function getMobileData (e) {
      axios.get(baseurl.value + '/scanner/list/' + e + '/',
        {
          headers: {
            "Content-Type": 'application/json, charset="utf-8"',
            "token" : openid.value,
            "language" : lang.value,
            "operator" : operator.value
          }
        }).then(res => {
          if (!res.data.detail) {
            scandata.value = ''
            datadetail.value = ''
            scanmode.value = ''
            asndata.value = ''
            dndata.value = ''
            bindata.value = ''
            scandata.value = res.data.code
            scanmode.value = res.data.mode
            bar_scanned.value = res.data.request_time
            if (scanmode.value === 'ASN') {
              asndata.value = res.data.code
            } else if (scanmode.value === 'DN') {
              dndata.value = res.data.code
            } else if (scanmode.value === 'GOODS') {
              scandata.value = res.data.code
            } else if (scanmode.value === 'BINSET') {
              bindata.value = res.data.code
            }
          } else {
            $q.notify({
              type: 'negative',
              message: t('notice.mobile_scan.notice2')
            })
          }
        }).catch(err => {
          $q.notify({
            type: 'negative',
            message: t('notice.mobile_scan.notice3')
          })
        })
    }

    function MobileScan () {
      cordova.plugins.barcodeScanner.scan(
        function (result) {
          bar_check.value = result.text
          navigator.vibrate(100)
        },
        function (error) {
          navigator.vibrate(100)
        },
        {
          preferFrontCamera : false,
          showFlipCameraButton : true,
          showTorchButton : true,
          disableSuccessBeep: false
        }
      );
    }

    function screanresize () {
      let screensizewidth = $q.screen.width
      let screensizeheight = $q.screen.height
      screenwidth.value = screensizewidth
      screenheight.value = screensizeheight
    }

    watch (bar_check,(newValue,oldValue)=>{
      if (newValue !== oldValue) {
        if (authin.value === '0') {
          $q.notify({
            type: 'negative',
            message: t('notice.mobile_userlogin.notice9')
          })
        } else {
          getMobileData(newValue)
        }
      }
    })

    onMounted(() => {
      screanresize()
      if (window.device) {
        if (window.device.manufacturer === "Zebra Technologies") {
            scanner.initialize()
        } else if (window.device.manufacturer === "SEUIC") {
          seuicDevice()
        } else if (window.device.manufacturer === "iData") {
          iDataDevice()
        }
      }
    })

    onBeforeUnmount(() => {
      if (window.device) {
        if  (window.device.manufacturer === "Zebra Technologies") {
          window.removeEventListener('deviceready', scanner.onDeviceReady, false)
        } else if (window.device.manufacturer === "SEUIC") {
          window.removeEventListener('deviceready', seuicOndeviceReady, false)
        } else if (window.device.manufacturer === "iData") {
          window.removeEventListener('deviceready', iDataOndeviceReady, false)
        }
      }
    })

    return {
      t,
      fab1,
      fab2,
      fab3,
      fab4,
      oldlink,
      newlink,
      screenwidth,
      screenheight,
      screenscroll,
      onScroll,
      authin,
      login_name,
      openid,
      operator,
      lang,
      baseurl,
      apiurl,
      apiurlnext,
      apiurlprevious,
      scandata,
      datadetail,
      tablelist,
      asndata,
      dndata,
      bindata,
      scanmode,
      bar_scanned,
      bar_check,
      device_auth,
      thumbStyle: {
        right: '4px',
        borderRadius: '5px',
        backgroundColor: '#027be3',
        width: '5px',
        opacity: 0.75
      },
      barStyle: {
        right: '2px',
        borderRadius: '9px',
        backgroundColor: '#027be3',
        width: '9px',
        opacity: 0.2
      },
      StartScan () {
        if (window.device) {
          MobileScan()
        } else {
          $q.notify({
            type: 'negative',
            message: t('notice.mobile_scan.notice4')
          })
        }
      },
      BackButton () {
        $router.push({ name: oldlink.value })
      }
    }
  }
})
</script>
