<template>
  <q-layout view="hHh lpR fFf">
    <input id="showThisMenu" v-model="menuShow" type="number" style="display:none" />
    <q-header elevated class="bg-primary text-white">
      <q-toolbar class="main-headers text-white shadow-18 rounded-borders">
        <q-toolbar-title @click="$router.push({ name: 'home' })">
          {{ apptitle }}
        </q-toolbar-title>
<!--        <q-btn @click="cordovaDevice()">device</q-btn>-->
          <q-btn
            round
            dense
            flat
            color="white"
            icon="translate"
            style="margin: 0 10px 0 10px"
          >
            <q-menu>
              <q-list style="min-width: 100px">
                <q-item
                  clickable
                  v-close-popup
                  v-for="(language, index) in langOptions"
                  :key="index"
                  @click="langChange(language.value)"
                >
                  <q-item-section>{{ language.label }}</q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </q-btn>
        <q-separator vertical />
        <template v-if="authin === '1'">
            <q-btn-dropdown
              stretch
              flat
              color="white-8"
              icon="account_circle"
            >
              <div class="row no-wrap q-pa-md">
                <div class="column" style="width: 150px">
                  <div
                    style="
                      width: 100%;
                      white-space: nowrap;
                      overflow: hidden;
                      text-overflow: ellipsis;
                    "
                  >
                    <span style="margin-left: 6%; font-weight: bold">{{
                      login_name
                    }}</span>
                  </div>
                  <hr
                    style="
                      height: 2px;
                      border: none;
                      border-top: 1px solid #e1e1e1;
                      width: 121%;
                      margin-left: -10.5%;
                      margin-top: 8%;
                    "
                  />
                  <q-btn
                    flat
                    rounded
                    class="full-width"
                    align="left"
                    :label="$t('index.change_user')"
                    :to="{ name: 'login' }"
                  >
                  </q-btn>
                </div>
              </div>
            </q-btn-dropdown>
        </template>
        <template v-if="authin === '0'">
            <q-btn
              :label="$t('index.login')"
              color="primary"
              style="margin-left: 10px"
              :to="{ name: 'login' }"
            >
            </q-btn>
        </template>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
      <q-page-sticky position="bottom-left"
                     :offset="Inbound"
                     v-show="menuShow === 0"
      >
        <q-fab
          v-model="fab1"
          icon="speaker_notes"
          :label="$t('menuItem.inbound')"
          label-position="bottom"
          external-label
          vertical-actions-align="left"
          direction="up"
          hide-label
          color="blue-grey-7"
          label-style="background-color: rgb(85 0 0 / 0%); color: black"
          @click="fabshow1"
        >
          <q-fab-action padding="10px"
                        :label="$t('inbound.asn')"
                        :to="{ name: 'asnlist' }"
                        flat
                        icon="img:statics/inbound/polist.png"
                        @click="onClick('asnlist')"
          />
          <q-fab-action padding="10px"
                        :label="$t('inbound.asnfinish')"
                        :to="{ name: 'asndetail' }"
                        flat
                        icon="img:statics/inbound/preloadstock.png"
                        @click="onClick('asndetail')"
          />
        </q-fab>
      </q-page-sticky>
      <q-page-sticky position="bottom-left"
                     :offset="Outbound"
                     v-show="menuShow === 0"
      >
        <q-fab
          v-model="fab2"
          icon="rv_hookup"
          :label="$t('menuItem.outbound')"
          label-position="bottom"
          external-label
          hide-label
          vertical-actions-align="left"
          direction="up"
          color="blue-grey-7"
          label-style="background-color: rgb(85 0 0 / 0%); color: black"
          @click="fabshow2"
        >
          <q-fab-action padding="10px"
                        :label="$t('outbound.dn')"
                        :to="{ name: 'dnlist' }"
                        flat
                        icon="img:statics/outbound/dnlist.png"
                        @click="onClick('dnlist')"
          />
          <q-fab-action padding="10px"
                        :label="$t('notice.mobile_dn.notice1')"
                        :to="{ name: 'dndetail' }"
                        flat
                        icon="img:statics/outbound/outbound.png"
                        @click="onClick('dndetail')"
          />
          <q-fab-action padding="10px"
                        :label="$t('outbound.pickinglist')"
                        :to="{ name: 'pickinglist' }"
                        flat
                        icon="img:statics/outbound/pickinglist.png"
                        @click="onClick('pickinglist')"
          />
        </q-fab>
      </q-page-sticky>
      <q-page-sticky position="bottom-left"
                     :offset="Stock"
                     v-show="menuShow === 0"
      >
        <q-fab
          v-model="fab3"
          icon="speaker_notes"
          :label="$t('menuItem.stock')"
          label-position="bottom"
          external-label
          hide-label
          vertical-actions-align="right"
          direction="up"
          color="blue-grey-7"
          label-style="background-color: rgb(85 0 0 / 0%); color: black"
          @click="fabshow3"
        >
          <q-fab-action padding="10px"
                        :label="$t('scan.scan_goodsquery')"
                        :to="{ name: 'goods' }"
                        flat
                        icon-right="img:statics/stock/stocklist.png"
                        @click="onClick('goods')"
          />
          <q-fab-action padding="10px"
                        :label="$t('stock.stocklist')"
                        :to="{ name: 'goodsstock' }"
                        flat
                        icon-right="img:statics/stock/stocklist.png"
                        @click="onClick('goodsstock')"
          />
          <q-fab-action padding="10px"
                        :label="$t('stock.stockbinlist')"
                        :to="{ name: 'binstock' }"
                        flat
                        icon-right="img:statics/stock/binset.png"
                        @click="onClick('binstock')"
          />
          <q-fab-action padding="10px"
                        :label="$t('stock.emptybin')"
                        :to="{ name: 'emptybin' }"
                        flat
                        icon-right="all_out"
                        @click="onClick('emptybin')"
          />
          <q-fab-action padding="10px"
              :label="$t('notice.handcount.notice2')"
              :to="{ name: 'handcount' }"
              flat
              icon-right="img:statics/stock/cyclecount.png"
              @click="onClick('handcount')"
          />
        </q-fab>
      </q-page-sticky>
      <q-page-sticky position="bottom-left"
                     :offset="Settings"
                     v-show="menuShow === 0"
      >
        <q-fab
          v-model="fab4"
          icon="widgets"
          :label="$t('Settings.index')"
          label-position="bottom"
          external-label
          hide-label
          vertical-actions-align="right"
          direction="up"
          color="blue-grey-7"
          label-style="background-color: rgb(85 0 0 / 0%); color: black"
          @click="fabshow4"
        >
          <q-fab-action padding="10px"
                        :label="$t('Settings.server')"
                        :to="{ name: 'server' }"
                        flat
                        icon-right="dns"
                        @click="onClick('server')"
          />
          <q-fab-action padding="10px"
                        :label="$t('Settings.equipment')"
                        :to="{ name: 'equipment' }"
                        flat
                        icon-right="barcode_reader"
                        @click="onClick('equipment')"
          />
        </q-fab>
      </q-page-sticky>
    </q-page-container>
  </q-layout>
</template>

<script>
import { computed, ref, onMounted, onUnmounted } from 'vue'
import { useStore } from 'vuex'
import { useRoute } from 'vue-router'
import { useMeta, useQuasar, openURL  } from 'quasar'
import { useI18n } from "vue-i18n"

export default {
  data () {
    return {
    }
  },
  setup () {
    const $store = useStore()
    const $q = useQuasar()
    const $route = useRoute()
    const { t } = useI18n()
    const Inbound = ref([ 18, 40 ])
    const Stock = ref([ 18, 40 ])
    const Settings = ref([ 18, 40 ])
    const Outbound = ref([ 18, 40 ])
    const menuShow = ref(0)
    const langOptions = [
        { value: 'en-US', label: 'English' },
        { value: 'zh-hans', label: '中文简体' },
        { value: 'zh-hant', label: '中文繁體' },
        { value: 'fr', label: 'Français' },
        { value: 'pt', label: 'Português' },
        { value: 'sp', label: 'Español' },
        { value: 'de', label: 'Deutsch' },
        { value: 'ru', label: 'русский язык' },
        { value: 'ar', label: 'Arabic' },
        { value: 'it', label: 'Italiano' },
        { value: 'ja', label: '日本語' }
      ]
    const lang = computed({
      get: () => $store.state.langchange.lang,
      set: val => {
        $store.commit('langchange/langChanged', val)
      }
    })
    const apptitle = computed({
      get: () => $store.state.settings.apptitle,
      set: val => {
        $store.commit('settings/APPTitle', val)
      }
    })
    const server = computed({
      get: () => $store.state.settings.server,
      set: val => {
        $store.commit('settings/Server', val)
      }
    })
    const openid = computed({
      get: () => $store.state.settings.openid,
      set: val => {
        $store.commit('settings/Openid', val)
      }
    })
    const fab1 = computed({
      get: () => $store.state.fabchange.fab1,
      set: val => {
        $store.commit('fabchange/fabChanged1', val)
      }
    })
    const fab2 = computed({
      get: () => $store.state.fabchange.fab2,
      set: val => {
        $store.commit('fabchange/fabChanged2', val)
      }
    })
    const fab3 = computed({
      get: () => $store.state.fabchange.fab3,
      set: val => {
        $store.commit('fabchange/fabChanged3', val)
      }
    })
    const fab4 = computed({
      get: () => $store.state.fabchange.fab4,
      set: val => {
        $store.commit('fabchange/fabChanged4', val)
      }
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
    const authin = computed({
      get: () => $store.state.loginauth.authin,
      set: val => {
        $store.commit('loginauth/loginAuth', val)
      }
    })
    const login_name = computed({
      get: () => $store.state.loginauth.login_name,
      set: val => {
        $store.commit('loginauth/loginName', val)
      }
    })
    const operator = computed({
      get: () => $store.state.loginauth.operator,
      set: val => {
        $store.commit('loginauth/loginId', val)
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

   useMeta(() => {
     return {
       title: apptitle.value
     }
    })
    function screanresize () {
      let screensizewidth = $q.screen.width
      let screensizeheight = $q.screen.height
      screenwidth.value = screensizewidth
      screenheight.value = screensizeheight
      Inbound.value = [ 18, 40 ]
      Outbound.value = [ 18 + ((screensizewidth - 86) / 3 ), 40 ]
      Stock.value = [ 18 + ((screensizewidth - 86) / 3 * 2 ), 40 ]
      Settings.value = [ 18 + (screensizewidth - 86), 40 ]
    }

    function keyboardShowHandler (e) {
      menuShow.value = e.keyboardHeight
    }

    function keyboardHideHandler (e) {
      menuShow.value = e.keyboardHeight || 0
    }

    onMounted(() => {
      if (window.device) {
        window.plugins.insomnia.keepAwake()
        navigator.splashscreen.hide();
      }
      screanresize()
      window.addEventListener('native.keyboardshow', keyboardShowHandler)
      window.addEventListener('native.keyboardhide', keyboardHideHandler)
    })

    onUnmounted(() => {
      window.removeEventListener('native.keyboardshow', keyboardShowHandler)
      window.removeEventListener('native.keyboardhide', keyboardHideHandler)
    })

    return {
      t,
      langOptions,
      apptitle,
      server,
      openid,
      lang,
      fab1,
      fab2,
      fab3,
      fab4,
      menuShow,
      oldlink,
      newlink,
      Outbound,
      Settings,
      Stock,
      Inbound,
      screenwidth,
      screenheight,
      authin,
      login_name,
      operator,

      cordovaDevice() {
         alert("Cordova version: " + device.cordova + "\n" +
            "Device model: " + device.model + "\n" +
            "Device platform: " + device.platform + "\n" +
            "Device UUID: " + device.uuid + "\n" +
            "Device version: " + device.version + "\n" +
            "Device Manufacturer: " + device.manufacturer + "\n" +
            "Device isVirtual: " + device.isVirtual + "\n" +
            "Device serial: " + device.serial);
      },

      langChange (e) {
        lang.value = e
      },
      fabshow1 () {
        if (fab1.value === true) {
          fab2.value = false
          fab3.value = false
          fab4.value = false
        }
      },
      fabshow2 () {
        if (fab2.value === true) {
          fab1.value = false
          fab3.value = false
          fab4.value = false
        }
      },
      fabshow3 () {
        if (fab3.value === true) {
          fab1.value = false
          fab2.value = false
          fab4.value = false
        }
      },
      fabshow4 () {
        if (fab4.value === true) {
          fab1.value = false
          fab2.value = false
          fab3.value = false
        }
      },
      onClick (e) {
        oldlink.value = $route.name
        newlink.value = e
      },
    }
  },
  watch: {
    lang (lang) {
      var _this = this
      _this.$i18n.locale = lang
    }
  }
}
</script>
