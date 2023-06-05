<template>
  <q-page v-show="!fab1 && !fab2 && !fab3 && !fab4" class="flex flex-top">
    <div :style="{ width: wholewidth, height: wholeheight, marginTop: '10px', marginLeft: '10px' }">
      <q-input
         id="scannedBarcodes"
         dense
         outlined
         square
         debounce="500"
         v-model="scandata"
         :label="$t('search')"
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
             icon="restart_alt"
             @click="CancelScan"
           />
         </template>
      </q-input>
      <q-scroll-area
        @scroll="onScroll"
        :delay="500"
        :thumb-style="thumbStyle"
        :bar-style="barStyle"
        :style="{ width: handlewidth, height: handleheight, marginTop: '10px' }"
      >

        <router-view />
      </q-scroll-area>
    </div>
  </q-page>
</template>

<script>
import { ref, computed, watch, defineComponent, onMounted } from 'vue'
import { useStore } from "vuex";
import { useRoute } from 'vue-router'
import { useQuasar } from "quasar";
import axios from 'axios'
import { useI18n } from "vue-i18n"

export default defineComponent({
  name: 'ScanAPP',
  data () {
    return {
      wholewidth: (this.screenwidth - 20) + '' + 'px',
      wholeheight: (this.screenheight - 165) + '' + 'px',
      handlewidth: (this.screenwidth - 22) + '' + 'px',
      handleheight: (this.screenheight - 215) + '' + 'px'
    }
  },
  setup () {
    const $store = useStore()
    const $route = useRoute()
    const $q = useQuasar()
    const bar_check = ref('')
    const bar_scanned = ref('')
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

    function onScroll (position) {
      screenscroll.value = position.verticalPercentage
    }

    function getGoodsData (e) {
      axios.get(baseurl.value + '/goods/?goods_code=' + e,
        {
          headers: {
            "Content-Type": 'application/json, charset="utf-8"',
            "token" : openid.value,
            "language" : lang.value,
            "operator" : operator.value
          }
        }).then(res => {
          if (!res.data.detail) {
            datadetail.value = res.data.results[0]
          } else {
            $q.notify({
              type: 'negative',
              message: t('notice.mobile_scan.notice1')
            })
          }
        }).catch(err => {
          $q.notify({
            type: 'negative',
            message: t('notice.mobile_scan.notice3')
          })
        })
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
            scandata.value = res.data.code
            bar_scanned.value = res.data.request_time
            getGoodsData(res.data.code)
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
      window.onresize = () => {
        screanresize()
      }
    })

    return {
      t,
      fab1,
      fab2,
      fab3,
      fab4,
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
      scandata,
      datadetail,
      asndata,
      dndata,
      bindata,
      bar_scanned,
      bar_check,
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
      CancelScan () {
        scandata.value = ''
        datadetail.value = {}
      }
    }
  }
})
</script>
