<template>
  <q-layout
    view="hHh LpR fFf"
    :style="{ height: $q.screen.height, width: $q.screen.width }"
  >
    <q-header reveal elevated class="bg-primary text-white">
      <q-toolbar class="main-headers text-white shadow-18 rounded-borders">
        <transition appear enter-active-class="animated zoomIn">
          <q-btn flat @click="drawerleft = !drawerleft" round dense icon="menu">
            <q-tooltip
              content-class="bg-amber text-black shadow-4"
              :offset="[15, 15]"
              content-style="font-size: 12px"
              >{{ $t("index.hide_menu") }}</q-tooltip
            >
          </q-btn>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-toolbar-title shrink class="text-weight-bold" @click="$router.push({ name: 'web_index' })">{{
            $t("index.title")
          }}</q-toolbar-title>
        </transition>
        <q-space />
        <transition appear enter-active-class="animated zoomIn">
          <q-btn
            v-show="lang !== 'zh-hans'"
            icon="img:statics/icons/IOS.png"
            round
            dense
            flat
            @click="brownlink('https://www.56yhz.com/md/ios/zh-CN')"
            style="margin: 0 10px 0 10px"
          >
            <q-tooltip
              content-class="bg-amber text-black shadow-4"
              :offset="[15, 15]"
              content-style="font-size: 12px"
              >IOS APP
            </q-tooltip>
          </q-btn>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-btn
            v-show="lang === 'zh-hans'"
            icon="img:statics/icons/IOS.png"
            round
            dense
            flat
            @click="brownlink('https://www.56yhz.com/md/ios/en')"
            style="margin: 0 10px 0 10px"
          >
            <q-tooltip
              content-class="bg-amber text-black shadow-4"
              :offset="[15, 15]"
              content-style="font-size: 12px"
              >IOS APP
            </q-tooltip>
          </q-btn>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-btn
            v-show="lang !== 'zh-hans'"
            icon="img:statics/icons/android.png"
            round
            dense
            flat
            @click="brownlink('https://www.56yhz.com/md/android/zh-CN')"
            style="margin: 0 10px 0 10px"
          >
            <q-tooltip
              content-class="bg-amber text-black shadow-4"
              :offset="[15, 15]"
              content-style="font-size: 12px"
              >Android APP
            </q-tooltip>
          </q-btn>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-btn
            v-show="lang === 'zh-hans'"
            icon="img:statics/icons/android.png"
            round
            dense
            flat
            @click="brownlink('https://www.56yhz.com/md/android/en')"
            style="margin: 0 10px 0 10px"
          >
            <q-tooltip
              content-class="bg-amber text-black shadow-4"
              :offset="[15, 15]"
              content-style="font-size: 12px"
              >Android APP
            </q-tooltip>
          </q-btn>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-btn
            icon="img:statics/icons/GitHub.png"
            round
            dense
            flat
            @click="brownlink('https://github.com/GreaterWMS/GreaterWMS')"
            style="margin: 0 10px 0 10px"
          >
            <q-tooltip
              content-class="bg-amber text-black shadow-4"
              :offset="[15, 15]"
              content-style="font-size: 12px"
              >GitHub Link</q-tooltip
            >
          </q-btn>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-btn
            icon="api"
            round
            dense
            flat
            @click="apiLink()"
            style="margin: 0 10px 0 10px"
          >
            <q-tooltip
              content-class="bg-amber text-black shadow-4"
              :offset="[15, 15]"
              content-style="font-size: 12px"
              >{{ $t('index.api') }}</q-tooltip
            >
          </q-btn>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-btn
            square
            dense
            flat
            color="white"
            :label="warehouse_name"
            icon="maps_home_work"
            style="margin: 0 10px 0 10px"
          >
            <q-menu>
              <q-list style="min-width: 100px">
                <q-item
                  clickable
                  v-close-popup
                  v-for="(warehouse, index) in warehouseOptions"
                  :key="index"
                  @click="warehouseChange(index)"
                >
                  <q-item-section>{{ warehouse.warehouse_name }}</q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </q-btn>
        </transition>
        <transition appear enter-active-class="animated zoomIn">
          <q-btn
            round
            dense
            flat
            color="white"
            icon="translate"
            style="margin: 0 10px 0 10px"
          >
            <q-tooltip
              content-class="bg-amber text-black shadow-4"
              :offset="[15, 15]"
              content-style="font-size: 12px"
              >{{ $t("index.translate") }}</q-tooltip
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
        </transition>
        <q-separator vertical />
        <template v-if="authin === '1'">
          <transition appear enter-active-class="animated zoomIn">
            <q-btn-dropdown
              stretch
              flat
              color="white-8"
              icon="account_circle"
            >
              <div class="row no-wrap q-pa-md">
                <div class="column" style="width: 150px">
                  <div class="text-h6 q-mb-md">
                    {{ $t("index.user_center") }}
                  </div>
                  <q-btn
                    flat
                    rounded
                    class="full-width"
                    align="left"
                    :label="$t('index.change_user')"
                    @click="login = true"
                  >
                    <q-tooltip
                      content-class="bg-amber text-black shadow-4"
                      :offset="[10, 10]"
                      content-style="font-size: 12px"
                      >{{ $t("index.change_user") }}</q-tooltip
                    >
                  </q-btn>
                  <q-btn
                    flat
                    rounded
                    class="full-width"
                    align="left"
                    :label="$t('index.view_my_openid')"
                    @click="authid = true"
                  >
                    <q-tooltip
                      content-class="bg-amber text-black shadow-4"
                      :offset="[10, 10]"
                      content-style="font-size: 12px"
                      >{{ $t("index.view_my_openid") }}</q-tooltip
                    >
                  </q-btn>
                </div>
                <q-separator vertical inset class="q-mx-lg" />
                <div class="column items-center">
                  <q-avatar size="72px"
                    ><q-img src="statics/staff/stafftype.png"></q-img
                  ></q-avatar>
                  <div class="text-subtitle1 q-mt-md q-mb-xs">
                    {{ login_name }}
                  </div>
                  <q-btn
                    color="primary"
                    :label="$t('index.logout')"
                    push
                    size="sm"
                    v-close-popup
                    icon="img:statics/icons/logout.png"
                    @click="Logout()"
                  >
                    <q-tooltip
                      content-class="bg-amber text-black shadow-4"
                      :offset="[10, 10]"
                      content-style="font-size: 12px"
                      >{{ $t("index.logout") }}</q-tooltip
                    >
                  </q-btn>
                </div>
              </div>
            </q-btn-dropdown>
          </transition>
        </template>
        <template v-if="authin === '0'">
          <transition appear enter-active-class="animated zoomIn">
            <q-btn
              :label="$t('index.login')"
              color="primary"
              @click="login = true"
              style="margin-left: 10px"
            >
              <q-tooltip
                content-class="bg-amber text-black shadow-4"
                :offset="[15, 15]"
                content-style="font-size: 12px"
                >{{ $t("index.login_tip") }}</q-tooltip
              >
            </q-btn>
          </transition>
          <transition appear enter-active-class="animated zoomIn">
            <q-btn
              :label="$t('index.register')"
              color="primary"
              @click="register = true"
              style="margin-left: 10px"
            >
              <q-tooltip
                content-class="bg-amber text-black shadow-4"
                :offset="[15, 15]"
                content-style="font-size: 12px"
                >{{ $t("index.register_tip") }}</q-tooltip
              >
            </q-btn>
          </transition>
        </template>
      </q-toolbar>
    </q-header>
    <q-drawer
      v-model="drawerleft"
      show-if-above
      :width="200"
      :breakpoint="500"
      bordered
      content-class="bg-grey-3 shadow-24"
    >
      <q-scroll-area class="fit" style="overflow-y: auto">
        <q-list>
          <q-item
            clickable
            :to="{ name: 'outbounddashboard' }"
            @click="linkChange('outbounddashboard')"
            v-ripple
            exact
            :active="link === 'outbounddashboard' && link !== ''"
            :class="{
              'my-menu-link': link === 'outbounddashboard' && link !== '',
            }"
          >
            <q-item-section avatar><q-icon name="auto_graph" /></q-item-section>
            <q-item-section>{{ $t("menuItem.dashboard") }}</q-item-section>
          </q-item>
          <q-separator />
          <q-item
            clickable
            :to="{ name: 'asn' }"
            @click="linkChange('inbound')"
            v-ripple
            exact
            :active="link === 'inbound' && link !== ''"
            :class="{ 'my-menu-link': link === 'inbound' && link !== '' }"
          >
            <q-item-section avatar
              ><q-icon name="speaker_notes"
            /></q-item-section>
            <q-item-section>{{ $t("menuItem.inbound") }}</q-item-section>
          </q-item>
          <q-item
            clickable
            :to="{ name: 'dn' }"
            @click="linkChange('outbound')"
            v-ripple
            exact
            :active="link === 'outbound' && link !== ''"
            :class="{ 'my-menu-link': link === 'outbound' && link !== '' }"
          >
            <q-item-section avatar><q-icon name="rv_hookup" /></q-item-section>
            <q-item-section>{{ $t("menuItem.outbound") }}</q-item-section>
          </q-item>
          <q-item
            clickable
            :to="{ name: 'stocklist' }"
            @click="linkChange('stock')"
            v-ripple
            exact
            :active="link === 'stock' && link !== ''"
            :class="{ 'my-menu-link': link === 'stock' && link !== '' }"
          >
            <q-item-section avatar
              ><q-icon name="multiline_chart"
            /></q-item-section>
            <q-item-section>{{ $t("menuItem.stock") }}</q-item-section>
          </q-item>
          <q-separator />
          <q-item
            clickable
            :to="{ name: 'capitallist' }"
            @click="linkChange('finance')"
            v-ripple
            exact
            :active="link === 'finance' && link !== ''"
            :class="{ 'my-menu-link': link === 'finance' && link !== '' }"
          >
            <q-item-section avatar
              ><q-icon name="devices_other"
            /></q-item-section>
            <q-item-section>{{ $t("menuItem.finance") }}</q-item-section>
          </q-item>
          <q-item
            clickable
            :to="{ name: 'goodslist' }"
            @click="linkChange('goods')"
            v-ripple
            exact
            :active="link === 'goods' && link !== ''"
            :class="{ 'my-menu-link': link === 'goods' && link !== '' }"
          >
            <q-item-section avatar><q-icon name="shop_two" /></q-item-section>
            <q-item-section>{{ $t("menuItem.goods") }}</q-item-section>
          </q-item>
          <q-item
            clickable
            :to="{ name: 'company' }"
            @click="linkChange('baseinfo')"
            v-ripple
            exact
            :active="link === 'baseinfo' && link !== ''"
            :class="{ 'my-menu-link': link === 'baseinfo' && link !== '' }"
          >
            <q-item-section avatar><q-icon name="info" /></q-item-section>
            <q-item-section>{{ $t("menuItem.baseinfo") }}</q-item-section>
          </q-item>
          <q-item
            clickable
            :to="{ name: 'warehouseset' }"
            @click="linkChange('warehouse')"
            v-ripple
            exact
            :active="link === 'warehouse' && link !== ''"
            :class="{ 'my-menu-link': link === 'warehouse' && link !== '' }"
          >
            <q-item-section avatar><q-icon name="settings" /></q-item-section>
            <q-item-section>{{ $t("menuItem.warehouse") }}</q-item-section>
          </q-item>
          <q-separator />
          <q-item
            clickable
            :to="{ name: 'stafflist' }"
            @click="linkChange('staff')"
            v-ripple
            exact
            :active="link === 'staff' && link !== ''"
            :class="{ 'my-menu-link': link === 'staff' && link !== '' }"
          >
            <q-item-section avatar
              ><q-icon name="assignment_ind"
            /></q-item-section>
            <q-item-section>{{ $t("menuItem.staff") }}</q-item-section>
          </q-item>
          <q-item
            clickable
            :to="{ name: 'driverlist' }"
            @click="linkChange('driver')"
            v-ripple
            exact
            :active="link === 'driver' && link !== ''"
            :class="{ 'my-menu-link': link === 'driver' && link !== '' }"
          >
            <q-item-section avatar
              ><q-icon name="transfer_within_a_station"
            /></q-item-section>
            <q-item-section>{{ $t("menuItem.driver") }}</q-item-section>
          </q-item>
          <q-separator />
          <q-item
            clickable
            :to="{ name: 'initializeupload' }"
            @click="linkChange('uploadcenter')"
            v-ripple
            exact
            :active="link === 'uploadcenter' && link !== ''"
            :class="{ 'my-menu-link': link === 'uploadcenter' && link !== '' }"
          >
            <q-item-section avatar
              ><q-icon name="file_upload"
            /></q-item-section>
            <q-item-section>{{ $t("menuItem.uploadcenter") }}</q-item-section>
          </q-item>
          <q-item
            clickable
            :to="{ name: 'downloadinbound' }"
            @click="linkChange('downloadcenter')"
            v-ripple
            exact
            :active="link === 'downloadcenter' && link !== ''"
            :class="{
              'my-menu-link': link === 'downloadcenter' && link !== '',
            }"
          >
            <q-item-section avatar
              ><q-icon name="file_download"
            /></q-item-section>
            <q-item-section>{{ $t("menuItem.downloadcenter") }}</q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>
    </q-drawer>
    <q-page-container
      class="main-page"
      :style="{
        height: container_height,
        width: $q.screen.width,
      }"
    >
      <router-view />
    </q-page-container>
    <q-dialog
      v-model="authid"
      transition-show="jump-down"
      transition-hide="jump-up"
    >
      <q-card style="min-width: 350px">
        <q-bar
          class="bg-light-blue-10 text-white rounded-borders"
          style="height: 50px"
        >
          <div>{{ $t("index.your_openid") }}</div>
          <q-space></q-space>
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip
              content-class="bg-amber text-black shadow-4"
              :offset="[20, 20]"
              content-style="font-size: 12px"
              >{{ $t("index.close") }}</q-tooltip
            >
          </q-btn>
        </q-bar>
        <q-card-section class="q-pt-md"
          ><q-input
            dense
            outlined
            square
            label="Openid"
            v-model="openid"
            readonly
            disable
        /></q-card-section>
      </q-card>
    </q-dialog>
    <q-dialog
      v-model="login"
      transition-show="jump-down"
      transition-hide="jump-up"
    >
      <q-card style="min-width: 350px">
        <q-bar
          class="bg-light-blue-10 text-white rounded-borders"
          style="height: 50px"
        >
          <q-tabs v-model="activeTab" class="tabs">
            <q-tab name="user" @click="admin = false">
              {{ $t("index.user_login") }}
              <q-tooltip
                content-class="bg-amber text-black shadow-4"
                :offset="[5, 5]"
                content-style="font-size: 12px"
                >{{ $t("index.user_login") }}</q-tooltip
              >
            </q-tab>
            <q-tab name="admin" @click="admin = true">
              {{ $t("index.admin_login") }}
              <q-tooltip
                content-class="bg-amber text-black shadow-4"
                :offset="[5, 5]"
                content-style="font-size: 12px"
                >{{ $t("index.admin_login") }}</q-tooltip
              >
            </q-tab>
          </q-tabs>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip
              content-class="bg-amber text-black shadow-4"
              :offset="[20, 20]"
              content-style="font-size: 12px"
              >{{ $t("index.close") }}</q-tooltip
            >
          </q-btn>
        </q-bar>
        <q-card-section class="q-pt-md">
          <template v-if="admin">
            <q-input
              dense
              outlined
              square
              :label="$t('index.admin_name')"
              v-model="adminlogin.name"
              autofocus
              @keyup.enter="adminLogin()"
            />
            <q-input
              dense
              outlined
              square
              :label="$t('index.password')"
              :type="isPwd ? 'password' : 'text'"
              v-model="adminlogin.password"
              @keyup.enter="adminLogin()"
              style="margin-top: 5px"
            >
              <template v-slot:append>
                <q-icon
                  :name="isPwd ? 'visibility_off' : 'visibility'"
                  class="cursor-pointer"
                  @click="isPwd = !isPwd"
                />
              </template>
            </q-input>
          </template>
          <template v-if="!admin">
            <q-input
              dense
              outlined
              square
              :label="$t('index.your_openid')"
              v-model="openid"
              disable
              readonly
              @keyup.enter="Login()"
            />
            <q-input
              dense
              outlined
              square
              :label="$t('index.staff_name')"
              v-model="login_name"
              autofocus
              @keyup.enter="Login()"
              style="margin-top: 5px"
            />
            <q-input
              dense
              outlined
              square
              type="number"
              :label="$t('staff.check_code')"
              v-model.number="check_code"
              autofocus
              @keyup.enter="Login()"
              style="margin-top: 5px"
            />
          </template>
        </q-card-section>
        <q-card-actions align="left" class="text-primary">
          <q-space />
          <template>
            <q-btn
              color="primary"
              :label="$t('index.login')"
              style="font-size: 16px; margin: 0 8px; width: 100%"
              @click="admin ? adminLogin() : Login()"
            />
          </template>
          <div class="q-mx-auto">
            <q-btn
              flat
              class="text-teal-4 q-mt-sm"
              @click="
                login = false;
                register = true;
              "
            >
              {{ $t("index.register_tip") }}
            </q-btn>
          </div>
        </q-card-actions>
      </q-card>
    </q-dialog>
    <q-dialog
      v-model="register"
      transition-show="jump-down"
      transition-hide="jump-up"
    >
      <q-card style="min-width: 350px">
        <q-bar
          class="bg-light-blue-10 text-white rounded-borders"
          style="height: 50px"
        >
          <div>{{ $t("index.register_tip") }}</div>
          <q-space></q-space>
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip
              content-class="bg-amber text-black shadow-4"
              :offset="[20, 20]"
              content-style="font-size: 12px"
              >{{ $t("index.close") }}</q-tooltip
            >
          </q-btn>
        </q-bar>
        <q-card-section class="q-pt-md">
          <q-input
            dense
            outlined
            square
            :label="$t('index.staff_name')"
            v-model="registerform.name"
            autofocus
            @keyup.enter="Register()"
          />
          <q-input
            dense
            outlined
            square
            :label="$t('index.password')"
            v-model="registerform.password1"
            :type="isPwd ? 'password' : 'text'"
            @keyup.enter="Register()"
            style="margin-top: 5px"
          >
            <template v-slot:append>
              <q-icon
                :name="isPwd ? 'visibility_off' : 'visibility'"
                class="cursor-pointer"
                @click="isPwd = !isPwd"
              />
            </template>
          </q-input>
          <q-input
            dense
            outlined
            square
            :label="$t('index.confirm_password')"
            v-model="registerform.password2"
            :type="isPwd2 ? 'password' : 'text'"
            @keyup.enter="Register()"
            style="margin-top: 5px"
          >
            <template v-slot:append>
              <q-icon
                :name="isPwd2 ? 'visibility_off' : 'visibility'"
                class="cursor-pointer"
                @click="isPwd2 = !isPwd2"
              />
            </template>
          </q-input>
        </q-card-section>
        <q-card-actions align="right" class="text-primary q-mx-sm"
          ><q-btn
            class="full-width"
            color="primary"
            :label="$t('index.register')"
            @click="Register()"
        /></q-card-actions>
        <q-card-actions align="center" style="margin-top: -8px">
          <q-btn
            class="text-teal-4"
            flat
            :label="$t('index.return_to_login')"
            @click="
              login = true;
              register = false;
            "
          ></q-btn>
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-layout>
</template>
<script>
import { get, getauth, post, baseurl } from 'boot/axios_request'
import { LocalStorage, SessionStorage, openURL } from 'quasar'
import Bus from 'boot/bus.js'

export default {
  data () {
    return {
      device: LocalStorage.getItem('device'),
      device_name: LocalStorage.getItem('device_name'),
      lang: this.$i18n.locale,
      container_height: this.$q.screen.height + '' + 'px',
      warehouse_name: '',
      warehouseOptions: [],
      langOptions: [
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
      ],
      title: this.$t('index.webtitle'),
      admin: false,
      adminlogin: {
        name: '',
        password: ''
      },
      openid: '',
      isPwd: true,
      isPwd2: true,
      authin: '0',
      authid: false,
      left: false,
      drawerleft: false,
      tab: '',
      login: false,
      link: '',
      login_name: '',
      login_id: 0,
      check_code: '',
      register: false,
      registerform: {
        name: '',
        password1: '',
        password2: ''
      },
      needLogin: '',
      activeTab: ''
    }
  },
  methods: {
    linkChange (e) {
      var _this = this
      localStorage.removeItem('menulink')
      localStorage.setItem('menulink', e)
      _this.link = e
    },
    drawerClick (e) {
      var _this = this
      if (_this.miniState) {
        _this.miniState = false
        e.stopPropagation()
      }
    },
    brownlink (e) {
      openURL(e)
    },
    apiLink () {
      openURL(baseurl + '/api/docs/')
    },
    Login () {
      var _this = this
      if (_this.login_name === '') {
        _this.$q.notify({
          message: 'Please enter the login name',
          color: 'negative',
          icon: 'close'
        })
      } else {
        if (_this.openid === '') {
          _this.$q.notify({
            message: 'Please Enter The Openid',
            icon: 'close',
            color: 'negative'
          })
        } else {
          if (_this.check_code === '') {
            _this.$q.notify({
              message: 'Please Enter The Check Code',
              icon: 'close',
              color: 'negative'
            })
          } else {
            LocalStorage.set('openid', _this.openid)
            SessionStorage.set('axios_check', 'false')
            getauth(
              'staff/?staff_name=' +
                _this.login_name +
                '&check_code=' +
                _this.check_code
            )
              .then((res) => {
                if (res.count === 1) {
                  _this.authin = '1'
                  _this.login = false
                  _this.login_id = res.results[0].id
                  LocalStorage.set('auth', '1')
                  LocalStorage.set('login_name', _this.login_name)
                  LocalStorage.set('login_id', res.results[0].id)
                  LocalStorage.set('login_mode', 'user')
                  _this.$q.notify({
                    message: 'Success Login',
                    icon: 'check',
                    color: 'green'
                  })
                  localStorage.removeItem('menulink')
                  _this.link = ''
                  _this.$router.push({ name: 'web_index' })
                  window.setTimeout(() => {
                    location.reload()
                  }, 1)
                }
              })
              .catch((err) => {
                _this.$q.notify({
                  message: err.detail,
                  icon: 'close',
                  color: 'negative'
                })
              })
          }
        }
      }
    },
    adminLogin () {
      var _this = this
      if (!_this.adminlogin.name) {
        _this.$q.notify({
          message: 'Please enter the admin name',
          color: 'negative',
          icon: 'close'
        })
      } else {
        if (!_this.adminlogin.password) {
          _this.$q.notify({
            message: 'Please enter the admin password',
            icon: 'close',
            color: 'negative'
          })
        } else {
          SessionStorage.set('axios_check', 'false')
          post('login/', _this.adminlogin)
            .then((res) => {
              if (res.code === '200') {
                _this.authin = '1'
                _this.login = false
                _this.admin = false
                _this.openid = res.data.openid
                _this.login_name = res.data.name
                _this.login_id = res.data.user_id
                LocalStorage.set('auth', '1')
                LocalStorage.set('openid', res.data.openid)
                LocalStorage.set('login_name', _this.login_name)
                LocalStorage.set('login_id', _this.login_id)
                LocalStorage.set('login_mode', 'admin')
                _this.$q.notify({
                  message: 'Success Login',
                  icon: 'check',
                  color: 'green'
                })
                localStorage.removeItem('menulink')
                _this.link = ''
                _this.$router.push({ name: 'web_index' })
                window.setTimeout(() => {
                  location.reload()
                }, 1)
              } else {
                _this.$q.notify({
                  message: res.msg,
                  icon: 'close',
                  color: 'negative'
                })
              }
            })
            .catch((err) => {
              _this.$q.notify({
                message: err.detail,
                icon: 'close',
                color: 'negative'
              })
            })
        }
      }
    },
    Logout () {
      var _this = this
      _this.authin = '0'
      _this.login_name = ''
      LocalStorage.remove('auth')
      SessionStorage.remove('axios_check')
      LocalStorage.set('login_name', '')
      LocalStorage.set('login_id', '')
      _this.$q.notify({
        message: 'Success Logout',
        icon: 'check',
        color: 'negative'
      })
      // _this.staffType();
      localStorage.removeItem('menulink')
      _this.link = ''
      _this.$router.push({ name: 'web_index' })
      window.setTimeout(() => {
        location.reload()
      }, 1)
    },
    Register () {
      var _this = this
      SessionStorage.set('axios_check', 'false')
      post('register/', _this.registerform)
        .then((res) => {
          if (res.code === '200') {
            _this.register = false
            _this.openid = res.data.openid
            _this.login_name = _this.registerform.name
            _this.login_id = res.data.user_id
            _this.authin = '1'
            LocalStorage.set('openid', res.data.openid)
            LocalStorage.set('login_name', _this.registerform.name)
            LocalStorage.set('login_id', _this.login_id)
            LocalStorage.set('auth', '1')
            _this.registerform = {
              name: '',
              password1: '',
              password2: ''
            }
            _this.$q.notify({
              message: res.msg,
              icon: 'check',
              color: 'green'
            })
            _this.staffType()
            localStorage.removeItem('menulink')
            _this.link = ''
            _this.$router.push({ name: 'web_index' })
            window.setTimeout(() => {
              location.reload()
            }, 1)
          } else {
            _this.$q.notify({
              message: res.msg,
              icon: 'close',
              color: 'negative'
            })
          }
        })
        .catch((err) => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    staffType () {
      var _this = this
      getauth('staff/?staff_name=' + _this.login_name).then((res) => {
        LocalStorage.set('staff_type', res.results[0].staff_type)
      })
    },
    warehouseOptionsGet () {
      var _this = this
      get('warehouse/multiple/?max_page=30')
        .then((res) => {
          if (res.count === 1) {
            _this.openid = res.results[0].openid
            _this.warehouse_name = res.results[0].warehouse_name
            LocalStorage.set('openid', _this.openid)
          } else {
            _this.warehouseOptions = res.results
            if (LocalStorage.has('openid')) {
              _this.warehouseOptions.forEach((item, index) => {
                if (item.openid === LocalStorage.getItem('openid')) {
                  _this.warehouse_name = item.warehouse_name
                }
              })
            }
          }
        })
        .catch((err) => {
          console.log(err)
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    warehouseChange (e) {
      var _this = this
      _this.warehouse_name = _this.warehouseOptions[e].warehouse_name
      _this.openid = _this.warehouseOptions[e].openid
      LocalStorage.set('openid', _this.openid)
      LocalStorage.set('staff_type', 'Admin')
      _this.login_name = ''
      LocalStorage.set('login_name', '')
      _this.authin = '0'
      _this.isLoggedIn()
      LocalStorage.remove('auth')
      SessionStorage.remove('axios_check')
    },
    langChange (e) {
      var _this = this
      _this.lang = e
      window.setTimeout(() => {
        location.reload()
      }, 1)
    },
    isLoggedIn () {
      if (this.$q.localStorage.getItem('openid')) {
        this.login = true
      } else {
        this.register = true
      }
    }
  },
  created () {
    var _this = this
    if (LocalStorage.has('openid')) {
      _this.openid = LocalStorage.getItem('openid')
      _this.activeTab = LocalStorage.getItem('login_mode')
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
      _this.staffType()
    } else {
      LocalStorage.set('staff_type', 'Admin')
      _this.authin = '0'
      _this.isLoggedIn()
    }
  },
  mounted () {
    var _this = this
    _this.warehouseOptionsGet()
    _this.link = localStorage.getItem('menulink')
    Bus.$on('needLogin', (val) => {
      _this.isLoggedIn()
    })
  },
  updated () {
  },
  beforeDestroy () {
    Bus.$off('needLogin')
  },
  destroyed () {
  },
  watch: {
    lang (lang) {
      var _this = this
      LocalStorage.set('lang', lang)
      _this.$i18n.locale = lang
    },
    login (val) {
      if (val) {
        if (this.activeTab === 'admin') {
          this.admin = true
        } else {
          this.admin = false
        }
      }
    }
  }
}
</script>
<style>
.tabs .q-tab__indicator {
  width: 25%;
  height: 1.5px;
  margin: auto;
  color: #d6d7d7;
}
.tabs .absolute-bottom {
  bottom: 8px;
}
</style>
