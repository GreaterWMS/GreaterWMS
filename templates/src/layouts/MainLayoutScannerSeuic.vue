<template>
  <q-layout view="hHh LpR fFf" :style="{ height: $q.screen.height, width: $q.screen.width }">
    <q-header reveal elevated class="bg-primary text-white">
      <q-toolbar class="main-headers text-white rounded-borders">
        <transition appear enter-active-class="animated zoomIn">
          <q-btn round dense flat color="white" icon="translate" style="margin: 0 10px 0 10px">
            <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[15, 15]" content-style="font-size: 12px">{{ $t('index.translate') }}</q-tooltip>
            <q-menu>
              <q-list style="min-width: 100px">
                <q-item clickable v-close-popup v-for="(language, index) in langOptions" :key="index" @click="langChange(language.value)">
                  <q-item-section>{{ language.label }}</q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </q-btn>
        </transition>
        <q-space />
        <template v-if="authin === '1'">
          <transition appear enter-active-class="animated zoomIn">
            <q-btn-dropdown stretch flat color="white-8" icon="account_circle" @click="chat = false">
              <div class="row no-wrap q-pa-md">
                <div class="column" style="width: 150px">
                  <div style="width: 100%; white-space:nowrap; overflow:hidden; text-overflow:ellipsis">
                    <span style="margin-left: 9%;font-weight: bold">{{ $t('index.current_user') }}:</span>
                    <span style="margin-left: 6%;font-weight: bold">{{ login_name }}</span>
                  </div>
                  <hr style="height: 2px;border:none;border-top:1px solid #e1e1e1;width: 121%;margin-left: -10.5%; margin-top: 8%" />
                  <q-btn flat rounded class="full-width" align="left" :label="$t('index.change_user')" @click="login = true">
                    <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('index.change_user') }}</q-tooltip>
                  </q-btn>
                  <q-btn flat rounded class="full-width" align="left" :label="$t('index.view_my_openid')" @click="authid = true">
                    <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('index.view_my_openid') }}</q-tooltip>
                  </q-btn>
                  <hr style="height: 2px;border:none;border-top:1px solid #e1e1e1;width: 121%;margin-left: -10.5%; margin-top: 8%" />
                  <q-btn flat rounded class="full-width" align="left" :label="$t('index.logout')" @click="Logout()">
                    <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('index.contact_list') }}</q-tooltip>
                  </q-btn>
                </div>
              </div>
            </q-btn-dropdown>
          </transition>
        </template>
        <template v-if="authin === '0'">
          <transition appear enter-active-class="animated zoomIn">
            <q-btn :label="$t('index.login')" color="primary" @click="login = true" style="margin-left: 10px">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[15, 15]" content-style="font-size: 12px">{{ $t('index.login_tip') }}</q-tooltip>
            </q-btn>
          </transition>
          <transition appear enter-active-class="animated zoomIn">
            <q-btn :label="$t('index.register')" color="primary" @click="register = true" style="margin-left: 10px">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[15, 15]" content-style="font-size: 12px">{{ $t('index.register_tip') }}</q-tooltip>
            </q-btn>
          </transition>
        </template>
      </q-toolbar>
    </q-header>
    <q-page-container
      class="main-page"
      :style="{
        height: container_height,
        width: $q.screen.width
      }"
    >
      <router-view />
    </q-page-container>
    <q-dialog v-model="authid" transition-show="jump-down" transition-hide="jump-up">
      <q-card style="min-width: 350px">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <div>{{ $t('index.your_openid') }}</div>
          <q-space></q-space>
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[20, 20]" content-style="font-size: 12px">{{ $t('index.close') }}</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section class="q-pt-md"><q-input dense outlined square label="Openid" v-model="openid" readonly /></q-card-section>
      </q-card>
    </q-dialog>
    <q-dialog v-model="login" transition-show="jump-down" transition-hide="jump-up">
      <q-card style="min-width: 350px">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <q-tabs v-model="activeTab" class="tabs">
            <q-tab name="user" @click="admin = false">
              {{ $t('index.user_login') }}
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[5, 5]" content-style="font-size: 12px">{{ $t('index.user_login') }}</q-tooltip>
            </q-tab>
            <q-tab name="admin" @click="admin = true">
              {{ $t('index.admin_login') }}
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[5, 5]" content-style="font-size: 12px">{{ $t('index.admin_login') }}</q-tooltip>
            </q-tab>
          </q-tabs>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[20, 20]" content-style="font-size: 12px">{{ $t('index.close') }}</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section class="q-pt-md">
          <template v-if="admin">
            <q-input dense outlined square :label="$t('index.admin_name')" v-model="adminlogin.name" @keyup.enter="adminLogin()" />
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
                <q-icon :name="isPwd ? 'visibility_off' : 'visibility'" class="cursor-pointer" @click="isPwd = !isPwd" />
              </template>
            </q-input>
          </template>
          <template v-if="!admin">
            <q-input dense outlined square :label="$t('index.your_openid')" v-model="openid" @keyup.enter="Login()" />
            <q-input dense outlined square :label="$t('index.staff_name')" v-model="login_name" @keyup.enter="Login()" style="margin-top: 5px" />
            <q-input dense outlined square :label="$t('staff.check_code')" v-model="check_code" @keyup.enter="Login()" style="margin-top: 5px" />
          </template>
        </q-card-section>
        <q-card-actions align="left" class="text-primary">
          <q-space />
          <template>
            <q-btn color="primary" :label="$t('index.login')" style="font-size: 16px; margin: 0 8px; width: 100%;" @click="admin ? adminLogin() : Login()" />
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
              {{ $t('index.register_tip') }}
            </q-btn>
          </div>
        </q-card-actions>
      </q-card>
    </q-dialog>
    <q-dialog v-model="register" transition-show="jump-down" transition-hide="jump-up">
      <q-card style="min-width: 350px">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <div>{{ $t('index.register_tip') }}</div>
          <q-space></q-space>
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[20, 20]" content-style="font-size: 12px">{{ $t('index.close') }}</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section class="q-pt-md">
          <q-input dense outlined square :label="$t('index.staff_name')" v-model="registerform.name" @keyup.enter="Register()" />
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
              <q-icon :name="isPwd ? 'visibility_off' : 'visibility'" class="cursor-pointer" @click="isPwd = !isPwd" />
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
              <q-icon :name="isPwd2 ? 'visibility_off' : 'visibility'" class="cursor-pointer" @click="isPwd2 = !isPwd2" />
            </template>
          </q-input>
        </q-card-section>
        <q-card-actions align="right" class="text-primary q-mx-sm"><q-btn class="full-width" color="primary" :label="$t('index.register')" @click="Register()" /></q-card-actions>
        <q-card-actions align="center" style="margin-top: -8px;">
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
import { getauth, post } from 'boot/axios_request'
import { LocalStorage, SessionStorage } from 'quasar'
import Bus from 'boot/bus.js'

export default {
  data () {
    return {
      activeTab: '',
      lang: this.$i18n.locale,
      container_height: this.$q.screen.height + '' + 'px',
      langOptions: [
        { value: 'en-us', label: 'English' },
        { value: 'zh-hans', label: '中文简体' },
        { value: 'zh-hant', label: '中文繁體' },
        { value: 'fr', label: 'Français' },
        { value: 'pt', label: 'Português' },
        { value: 'ru', label: 'Español' },
        { value: 'de', label: 'Deutsch' },
        { value: 'ru', label: 'русский язык' },
        { value: 'ar', label: 'Arabic' },
        { value: 'fr', label: 'Italiano' },
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
      check_code: '',
      register: false,
      registerform: {
        name: '',
        password1: '',
        password2: ''
      },
      needLogin: ''
    }
  },
  methods: {
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
            getauth('staff/?staff_name=' + _this.login_name + '&check_code=' + _this.check_code)
              .then(res => {
                if (res.count === 1) {
                  _this.authin = '1'
                  _this.login = false
                  LocalStorage.set('auth', '1')
                  LocalStorage.set('login_name', _this.login_name)
                  LocalStorage.set('login_mode', 'user')
                  _this.$q.notify({
                    message: 'Success Login',
                    icon: 'check',
                    color: 'green'
                  })
                  _this.$router.push({ name: 'seuicscan' })
                } else {
                  _this.$q.notify({
                    message: "No User's Data Or Check Code Wrong",
                    icon: 'close',
                    color: 'negative'
                  })
                }
              })
              .catch(err => {
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
            .then(res => {
              if (res.code === '200') {
                _this.authin = '1'
                _this.login = false
                _this.admin = false
                _this.openid = res.data.openid
                _this.login_name = res.data.name
                LocalStorage.set('auth', '1')
                LocalStorage.set('openid', res.data.openid)
                LocalStorage.set('login_name', _this.login_name)
                LocalStorage.set('login_mode', 'admin')
                _this.$q.notify({
                  message: 'Success Login',
                  icon: 'check',
                  color: 'green'
                })
                _this.$router.push({ name: 'seuicscan' })
              } else {
                _this.$q.notify({
                  message: res.msg,
                  icon: 'close',
                  color: 'negative'
                })
              }
            })
            .catch(err => {
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
      _this.$q.notify({
        message: 'Success Logout',
        icon: 'check',
        color: 'negative'
      })
      // _this.staffType();
      _this.$router.push({ name: 'seuicscan' })
    },
    Register () {
      var _this = this
      SessionStorage.set('axios_check', 'false')
      post('register/', _this.registerform)
        .then(res => {
          if (res.code === '200') {
            _this.register = false
            _this.openid = res.data.openid
            _this.login_name = _this.registerform.name
            _this.authin = '1'
            LocalStorage.set('openid', res.data.openid)
            LocalStorage.set('login_name', _this.registerform.name)
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
            _this.$router.push({ name: 'seuicscan' })
          } else {
            _this.$q.notify({
              message: res.msg,
              icon: 'close',
              color: 'negative'
            })
          }
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    staffType () {
      var _this = this
      getauth('staff/?staff_name=' + _this.login_name).then(res => {
        LocalStorage.set('staff_type', res.results[0].staff_type)
      })
    },
    langChange (e) {
      var _this = this
      _this.lang = e
      window.setTimeout(() => {
        location.reload()
      }, 1)
    },
    isLoggedIn () {
      this.activeTab = this.$q.localStorage.getItem('login_mode')
      if (this.$q.localStorage.getItem('openid')) {
        this.login = true
        if (this.activeTab === 'admin') {
          this.admin = true
        } else {
          this.admin = false
        }
      } else {
        this.register = true
      }
    }
  },
  beforeCreate () {
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
      _this.staffType()
    } else {
      LocalStorage.set('staff_type', 'Admin')
      _this.authin = '0'
      _this.isLoggedIn()
    }
  },
  mounted () {
    var _this = this
    _this.link = LocalStorage.getItem('menulink')
    Bus.$on('needLogin', val => {
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
