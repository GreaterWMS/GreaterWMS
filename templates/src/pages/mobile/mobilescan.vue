<template>
  <q-page>
    <router-view />
    <q-page-sticky position="bottom-left" :offset="[18, 18]">
      <input id="scannedBarcodes" v-model="barscan" type="text" readonly disabled/>
    </q-page-sticky>
    <q-page-sticky position="top-right" :offset="[18, 18]">
      <q-btn v-show="!fab" round color="accent" icon="barcode_reader" class="rotate-45" @click="scan()" style="transform: rotate(10deg)"/>
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
          :to="{ name: 'mobile_locationquery' }"
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
          :to="{ name: 'mobile_goodslist' }"
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
          :to="{ name: 'mobile_cyclecount' }"
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
          :to="{ name: 'mobile_movetobin' }"
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
          :to="{ name: 'mobile_shipping' }"
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
          :to="{ name: 'mobile_picking' }"
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
          :to="{ name: 'mobile_uptobin' }"
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
          :to="{ name: 'mobile_sorting' }"
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
import { scangetauth } from 'boot/axios_request'
import { LocalStorage, Screen, throttle } from 'quasar'

function mobilescan () {
  cordova.plugins.barcodeScanner.scan(
    function (result) {
      document.getElementById('scannedBarcodes').value = ''
      document.getElementById('scannedBarcodes').value = result.text
      document.getElementById('scannedBarcodes').dispatchEvent(new Event('input'))
    },
    function (error) {
      alert('Scanning failed: ' + error)
    },
    {
      preferFrontCamera: false,
      showFlipCameraButton: true,
      showTorchButton: true,
      disableSuccessBeep: false
    }
  )
}

export default {
  name: 'Pagemobile_scanbase',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'scan/',
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
      }
    }
  },
  methods: {
    datachange (e) {
      var _this = this
      if (_this.barscan !== '') {
        scangetauth('scanner/list/' + e + '/', {
        }).then(res => {
          if (!res.detail) {
            _this.scaneddata = res
          } else {
            navigator.vibrate(100)
            _this.$q.notify({
              message: res.detail,
              position: 'top',
              icon: 'close',
              color: 'negative'
            })
          }
        }).catch(err => {
          navigator.vibrate(100)
          console.log(err)
          _this.$q.notify({
            message: err.detail,
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        })
      }
    },
    scan () {
      mobilescan()
    },
    onBackKeyDown (e) {
      e.preventDefault()
      var _this = this
      var changelink
      changelink = _this.$route.path.split('/')[3]
      LocalStorage.set('changelink', changelink)
      if (LocalStorage.getItem('changelink') !== '') {
        console.log(LocalStorage.getItem('changelink'))
        this.$router.push({ name: LocalStorage.getItem('changelink') })
      } else {
        this.$router.push({ name: 'mobilescan' })
      }
    }
  },
  computed: {
    fab: {
      get () {
        return this.$store.state.fabchange.fab
      },
      set (val) {
        this.$store.commit('bardata/barScanned', '')
        this.$store.commit('scanedsolve/scanedData', '')
        this.$store.commit('fabchange/fabChanged', val)
      }
    },
    barscan: {
      get () {
        return this.$store.state.bardata.barscan
      },
      set (val) {
        this.$store.commit('bardata/barScanned', '')
        this.$store.commit('bardata/barScanned', val)
        this.datachange(val)
      }
    },
    scaneddata: {
      get () {
        return this.$store.state.scanedsolve.scaneddata
      },
      set (val) {
        this.$store.commit('scanedsolve/scanedData', '')
        this.$store.commit('scanedsolve/scanedData', val)
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
    document.addEventListener('backbutton', _this.onBackKeyDown, false)
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
  },
  beforeDestroy () {
    document.removeEventListener('backbutton', this.onBackKeyDown, false)
  },
  destroyed () {
  }
}
</script>
