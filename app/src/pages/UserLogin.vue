<template>
  <q-page v-show="!fab1 && !fab2 && !fab3 && !fab4" class="flex flex-top">
    <div :style="{ width: screenwidth + '' + 'px', height: (screenheight - 160) + '' + 'px', marginTop: '10px'}">
      <q-tabs
        v-model="tab"
        dense
        class="text-grey"
        active-color="primary"
        indicator-color="primary"
        align="justify"
        narrow-indicator
      >
        <q-tab name="stafflogin" :label="$t('index.login')" />
        <q-tab name="adminlogin" :label="$t('index.admin_login')" />
      </q-tabs>
      <q-separator />
      <q-tab-panels v-model="tab" animated>
        <q-tab-panel name="stafflogin">
            <q-input
              dense
              outlined
              square
              v-model="staff_name"
              :label="$t('index.staff_name')"
              @update:model-value="LoginMode(0)"
            />
            <q-input
              dense
              outlined
              square
              v-model="check_code"
              :label="$t('staff.check_code')"
              style="margin-top: 15px"
              @update:model-value="LoginMode(0)"
            />
        </q-tab-panel>
        <q-tab-panel name="adminlogin">
          <q-input
              dense
              outlined
              square
              v-model="adminlogin.name"
              :label="$t('index.admin_name')"
              @update:model-value="LoginMode(1)"
          />
            <q-input
              dense
              outlined
              square
              v-model="adminlogin.password"
              :label="$t('index.password')" style="margin-top: 15px"
              @update:model-value="LoginMode(1)"
            />
        </q-tab-panel>
      </q-tab-panels>
    </div>
  </q-page>
  <q-page-sticky v-show="!fab1 && !fab2 && !fab3 && !fab4" position="bottom-left" :offset="[18, 120]">
    <q-btn square color="primary" :label="$t('index.cancel')" @click="LoginCancel"/>
  </q-page-sticky>
  <q-page-sticky v-show="!fab1 && !fab2 && !fab3 && !fab4" position="bottom-right" :offset="[18, 120]">
    <q-btn square color="primary" :label="$t('index.submit')" @click="Login"/>
  </q-page-sticky>
</template>

<script>
import { computed, defineComponent, onMounted, ref } from "vue";
import { useStore } from "vuex";

export default defineComponent({
  data () {
    return {
      staff_name: '',
      check_code: '',
      adminlogin: {
        name: '',
        password: ''
      },
      login_mode: 0,
    }
  },
  computed: {
    screenwidth: {
      get() {
        return this.$store.state.screenchange.screenwidth
      },
    },
    screenheight: {
      get() {
        return this.$store.state.screenchange.screenheight
      },
    },
    lang: {
      get () {
        return this.$store.state.langchange.lang
      }
    },
    authin: {
      get () {
        return this.$store.state.loginauth.authin
      },
      set (val) {
        this.$store.commit('loginauth/loginAuth', val)
      }
    },
    login_name: {
      get () {
        return this.$store.state.loginauth.login_name
      },
      set (val) {
        this.$store.commit('loginauth/loginName', val)
      }
    },
    operator: {
      get () {
        return this.$store.state.loginauth.operator
      },
      set (val) {
        this.$store.commit('loginauth/loginId', val)
      }
    },
    openid: {
      get () {
        return this.$store.state.settings.openid
      },
      set (val) {
        this.$store.commit('settings/Openid', val)
      }
    },
    baseurl: {
      get () {
        return this.$store.state.settings.server
      },
      set (val) {
        this.$store.commit('settings/Server', val)
      }
    },
  },
  methods: {
    LoginMode(e) {
      var _this = this
      _this.login_mode = e
      if (e === 0) {
        if (_this.adminlogin.name.length !== 0) {
          _this.adminlogin.name = ''
        }
        if (_this.adminlogin.password.length !== 0) {
          _this.adminlogin.password = ''
        }
      } else {
        if (_this.staff_name.length !== 0) {
          _this.staff_name = ''
        }
        if (_this.check_code.length !== 0) {
          _this.check_code = ''
        }
      }
    },
    LoginCancel () {
      var _this = this
      _this.staff_name = ''
      _this.check_code = ''
      _this.adminlogin = {
        name: '',
        password: ''
      }
    },
    Login () {
      var _this = this
      if (_this.login_mode === 0) {
        _this.staffLogin()
      } else {
        _this.adminLogin()
      }
    },
    staffLogin () {
      var _this = this
      if (_this.openid.length === 0) {
        _this.$q.notify({
          type: 'negative',
          message: _this.$t('notice.mobile_userlogin.notice5')
        })
      } else {
        if (_this.staff_name.length === 0) {
          _this.$q.notify({
            type: 'negative',
            message: _this.$t('notice.mobile_userlogin.notice3')
          })
        } else {
          if (_this.check_code.length === 0) {
            _this.$q.notify({
              type: 'negative',
              message: _this.$t('notice.mobile_userlogin.notice4')
            })
          } else {
            _this.$axios.get(
              _this.baseurl + '/staff/?staff_name=' + _this.staff_name + '&check_code=' + _this.check_code,
              {
                headers: {
                  "Content-Type": 'application/json, charset="utf-8"',
                  "token" : _this.openid,
                  "language" : _this.lang
                }
              })
              .then((res) => {
                if (res.data.count === 1) {
                  _this.$store.commit('loginauth/loginAuth', '1')
                  _this.$store.commit('loginauth/loginName',  _this.staff_name)
                  _this.$store.commit('loginauth/loginId', res.data.results[0].id)
                  _this.$q.notify({
                    message: _this.$t('notice.mobile_userlogin.notice6')
                  })
                  _this.$router.push({ name: 'home' })
                } else {
                  _this.$q.notify({
                    type: 'negative',
                    message: _this.$t('notice.mobile_userlogin.notice8')
                  })
                }
              })
              .catch((err) => {
                _this.$q.notify({
                  type: 'negative',
                  message: _this.$t('notice.mobile_userlogin.notice8')
                })
              })
          }
        }
      }
    },
    adminLogin () {
      var _this = this
      if (_this.adminlogin.name.length === 0) {
        _this.$q.notify({
          type: 'negative',
          message: _this.$t('notice.mobile_userlogin.notice1')
        })
      } else {
        if (_this.adminlogin.password.length === 0) {
          _this.$q.notify({
            type: 'negative',
            message: _this.$t('notice.mobile_userlogin.notice2')
          })
        } else {
          if (_this.adminlogin.name === '3' && _this.adminlogin.password === '3') {
            _this.$store.commit('settings/Server', 'https://production.56yhz.com/')
          }
          _this.$axios.post(_this.baseurl + '/login/', _this.adminlogin)
            .then((res) => {
              if (res.data.code === '200') {
                _this.$store.commit('settings/Openid', res.data.data.openid)
                _this.$store.commit('loginauth/loginAuth', '1')
                _this.$store.commit('loginauth/loginName', res.data.data.name)
                _this.$store.commit('loginauth/loginId', res.data.data.user_id)
                _this.$q.notify({
                  message: _this.$t('notice.mobile_userlogin.notice6')
                })
                _this.$router.push({ name: 'home' })
              } else {
                _this.$q.notify({
                  type: 'negative',
                  message: _this.$t('notice.mobile_userlogin.notice7')
                })
              }
            })
            .catch((err) => {
              _this.$q.notify({
                type: 'negative',
                message: _this.$t('notice.mobile_userlogin.notice7')
              })
            })
        }
      }
    }
  },
  setup () {
    const $store = useStore()
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

    onMounted(() => {

    })
    return {
      fab1,
      fab2,
      fab3,
      fab4,
      tab: ref('stafflogin')
    }
  }
})
</script>

<style scoped>

</style>
