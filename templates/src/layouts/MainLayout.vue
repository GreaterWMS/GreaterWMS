<template>
  <q-layout view="hhh LpR lFf">
    <q-header reveal elevated class="bg-primary text-white">
      <q-toolbar class="bg-light-blue-10 text-white shadow-18 rounded-borders">
        <q-btn flat @click="drawerleft = !drawerleft" round dense icon="menu" />
        <q-toolbar-title shrink class="text-weight-bold">
          GreaterWMS
        </q-toolbar-title>
        <q-space />
        <q-btn icon="img:statics/icons/logo.png" stretch flat label="Home" to="/">
          <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
            GreaterWMS Home
          </q-tooltip>
        </q-btn>
        <q-separator vertical />
        <template v-if="authin === '1'">
        <q-btn round dense flat color="white" icon="notifications" @click="read = true" style="margin: 0 10px 0 10px">
          <q-badge color="red" text-color="white" floating>
            {{ read_num }}
          </q-badge>
          <q-tooltip content-class="bg-indigo" :offset="[20, 20]" content-style="font-size: 12px">
              Unread messages
          </q-tooltip>
        </q-btn>
        <q-btn-dropdown stretch flat color="white-8" icon="account_circle" @click="chat = false">
          <div class="row no-wrap q-pa-md">
            <div class="column" style="width: 200px">
              <div class="text-h6 q-mb-md">
                User Center
              </div>
                <q-btn flat rounded class="full-width" align="left" icon="connect_without_contact" label="Change User" @click="login = true">
                    <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                        Change User
                    </q-tooltip>
                </q-btn>
                <q-btn flat rounded class="full-width" align="left" icon="list" label="My Openid" @click="authid = true">
                    <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                        View my Openid
                    </q-tooltip>
                </q-btn>
                <q-btn flat rounded class="full-width" align="left" icon="img:statics/icons/profile.png" label="Contact List" @click="Friend()">
                    <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                        Contact List
                    </q-tooltip>
                </q-btn>
              </div>
              <q-separator vertical inset class="q-mx-lg" />
            <div class="column items-center">
              <q-avatar size="72px">
                  <q-img src="statics/staff/staffauth.png"></q-img>
              </q-avatar>
              <div class="text-subtitle1 q-mt-md q-mb-xs">{{ login_name }}</div>
              <q-btn
                color="primary"
                label="Logout"
                push
                size="sm"
                v-close-popup
                icon="img:statics/icons/logout.png"
                @click="Logout('')"
              ><q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">Logout</q-tooltip></q-btn>
            </div>
          </div>
        </q-btn-dropdown>
        </template>
        <template v-if="authin === '0'">
          <q-btn label="Login" color="primary" @click="login = true" style="margin-left: 10px">
            <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
              Enter your login_name & openid
            </q-tooltip>
          </q-btn>
          <q-btn label="Register" color="primary" @click="register = true" style="margin-left: 10px">
            <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
              Register an Admin
            </q-tooltip>
          </q-btn>
        </template>
      </q-toolbar>
    </q-header>
    <q-drawer
        v-model="drawerleft"
        show-if-above
        :mini="!drawerleft || miniState"
        @click.capture="drawerClick"
        :width="200"
        :breakpoint="500"
        bordered
        content-class="bg-grey-3 shadow-24"
      >
      <q-scroll-area class="fit" style="overflow-y: hidden">
        <q-list v-for="(menuItem, index) in menuList" :key="index">
          <q-item clickable :active="link === menuItem.link" :to="{ name: menuItem.link }" @click="link === menuItem.link" v-ripple exact active-class="my-menu-link">
            <q-item-section avatar>
              <q-icon :name="menuItem.icon" />
            </q-item-section>
            <q-item-section>
              {{ menuItem.label }}
            </q-item-section>
          </q-item>
          <q-separator v-if="menuItem.separator" />
        </q-list>
      </q-scroll-area>
      <div class="q-mini-drawer-hide absolute" style="top: 15px; right: -17px">
        <q-btn
            dense
            round
            glossy
            unelevated
            color="purple"
            icon="chevron_left"
            @click="miniState = true"
        />
      </div>
    </q-drawer>
    <q-page-container style="width: 100%">
      <router-view />
      <q-page-sticky position="bottom-right" :offset="[18, 18]">
        <q-btn flat @click="brownlink('http://www.miit.gov.cn/')" color="black" label='版权所有 ICP证：沪ICP备16034540号-1' />
      </q-page-sticky>
    </q-page-container>
    <q-dialog v-model="chat">
    <q-card style="width: 600px">
      <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
        <div>{{ receiver }}</div>
        <q-space/>
        <q-btn dense flat icon="close" v-close-popup>
          <q-tooltip content-class="bg-indigo" :offset="[20, 20]" content-style="font-size: 12px" @click="ChatClose()">Close</q-tooltip>
        </q-btn>
      </q-bar>
      <q-separator/>
      <q-card-section id="chat_scroll" style="max-height: 50vh; height: 50vh" class="scroll">
        <template>
          <div class="q-pa-md row justify-center">
            <q-btn flat rounded label="Load More" @click="LoadChatList()" v-show="chat_next !== null"></q-btn>
            <div style="width: 100%">
              <q-chat-message v-show="chat_next === null" label="No more message" />
              <div v-for="item in chat_list" :key="item.id">
                <q-chat-message v-if="item.sender === sender + '-' + openid"
                                :name="sender"
                                :text="[item.detail]"
                                bg-color="light-green-4"
                                name-sanitize
                                sent
                                text-sanitize
                />
                <q-chat-message v-else
                                :name="receiver"
                                :text="[item.detail]"
                                text-sanitize
                                name-sanitize
                                bg-color="grey-4"
                />
              </div>
            </div>
          </div>
        </template>
      </q-card-section>
      <q-separator/>
      <q-card-actions align="right">
        <q-input autofocus dense outlined square v-model="chat_text" placeholder="Send Message" class="bg-white col" @keyup.enter="websocketsend()" @keyup.esc="ChatClose()" />
        <q-btn flat label="Send" color="primary" @click="websocketsend()"></q-btn>
      </q-card-actions>
    </q-card>
    </q-dialog>
    <q-dialog v-model="read" position="right">
      <q-card style="width: 300px">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
            <div>Unread messages({{ read_num }})</div>
            <q-space></q-space>
            <q-btn dense flat icon="close" v-close-popup>
                <q-tooltip content-class="bg-indigo" :offset="[20, 20]" content-style="font-size: 12px">Close</q-tooltip>
            </q-btn>
        </q-bar>
        <q-separator></q-separator>
        <q-card-section style="max-height: 50vh; height: 50vh" class="scroll">
          <q-list>
            <div v-for="item in read_list" :key="item.id">
              <q-item clickable v-ripple>
                <q-item-section>
                  <q-item-label @click="ChatWith(item.sender.split('-')[0])">{{ item.sender.split('-')[0] }}</q-item-label>
                  <q-item-label caption lines="2" @click="ChatWith(item.sender.split('-')[0])">{{ item.detail }}</q-item-label>
                </q-item-section>
              </q-item>
            </div>
          </q-list>
        </q-card-section>
        <q-separator v-show="read_num > 30"></q-separator>
        <q-card-actions align="left">
          <q-btn flat v-show="read_previous !== null" label="Previous" color="primary" @click="ReadnumPrevious()"></q-btn>
          <q-btn flat v-show="read_next !== null" label="Next" color="primary" @click="ReadnumNext()"></q-btn>
        </q-card-actions>
      </q-card>
  </q-dialog>
  <q-dialog v-model="authid" transition-show="jump-down" transition-hide="jump-up">
    <q-card style="min-width: 350px">
      <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
        <div>Your Openid</div>
        <q-space></q-space>
        <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-indigo" :offset="[20, 20]" content-style="font-size: 12px">Close</q-tooltip>
        </q-btn>
      </q-bar>
      <q-card-section class="q-pt-md">
        <q-input dense outlined square label="Openid" v-model="openid" readonly />
      </q-card-section>
    </q-card>
  </q-dialog>
  <q-dialog v-model="friend" position="right">
    <q-card style="width: 300px">
      <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
        <div>List total({{ friend_num }})</div>
        <q-space />
        <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-indigo" :offset="[20, 20]" content-style="font-size: 12px">关闭</q-tooltip>
        </q-btn>
      </q-bar>
      <q-separator />
      <q-card-section style="max-height: 50vh; height: 50vh" class="scroll">
        <q-list>
          <template v-for="item in friend_list">
            <q-item clickable v-ripple v-bind:key="item.id">
              <q-item-section>
                <q-item-label @click="ChatWith(item.staff_name)">{{ item.staff_name }}</q-item-label>
              </q-item-section>
            </q-item>
          </template>
        </q-list>
      </q-card-section>
      <q-separator v-show="friend_num > 30"></q-separator>
      <q-card-actions align="left">
        <q-btn flat v-show="friend_previous !== null" label="Previous" color="primary" @click="Friend_previous()"></q-btn>
        <q-btn flat v-show="friend_next !== null" label="Next" color="primary" @click="Friend_next()"></q-btn>
      </q-card-actions>
    </q-card>
  </q-dialog>
  <q-dialog v-model="login" transition-show="jump-down" transition-hide="jump-up">
    <q-card style="min-width: 350px">
      <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
        <div>User Login</div>
        <q-space></q-space>
        <template v-if="admin">
          <q-btn dense flat label="User Login" @click="admin = false">
              <q-tooltip content-class="bg-indigo" :offset="[20, 20]" content-style="font-size: 12px">User Login</q-tooltip>
          </q-btn>
        </template>
        <template v-else-if="!admin">
          <q-btn dense flat label="Admin Login"  @click="admin = true">
              <q-tooltip content-class="bg-indigo" :offset="[20, 20]" content-style="font-size: 12px">Admin Login</q-tooltip>
          </q-btn>
        </template>
        <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-indigo" :offset="[20, 20]" content-style="font-size: 12px">Close</q-tooltip>
        </q-btn>
      </q-bar>
      <q-card-section class="q-pt-md">
        <template v-if="admin">
          <q-input dense outlined square label="Admin Name" v-model="adminlogin.name" autofocus @keyup.enter="adminLogin()"/>
          <q-input dense outlined square label="Password" v-model="adminlogin.password" @keyup.enter="adminLogin()" style="margin-top: 5px"/>
        </template>
        <template v-if="!admin">
          <q-input dense outlined square label="Openid" v-model="openid" autofocus @keyup.enter="Login()"/>
          <q-input dense outlined square label="Staff_name" v-model="login_name" autofocus @keyup.enter="Login()" style="margin-top: 5px"/>
        </template>
      </q-card-section>
      <q-card-actions align="right" class="text-primary">
        <q-btn flat label="Cancel" v-close-popup />
        <template v-if="admin">
          <q-btn color="primary" label="Login" @click="adminLogin()"/>
        </template>
        <template v-if="!admin">
          <q-btn color="primary" label="Login" @click="Login()"/>
        </template>
      </q-card-actions>
    </q-card>
  </q-dialog>
<q-dialog v-model="register" transition-show="jump-down" transition-hide="jump-up">
    <q-card style="min-width: 350px">
      <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
        <div>Register an Admin</div>
        <q-space></q-space>
        <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-indigo" :offset="[20, 20]" content-style="font-size: 12px">Close</q-tooltip>
        </q-btn>
      </q-bar>
      <q-card-section class="q-pt-md">
        <q-input dense outlined square label="Staff_name" v-model="registerform.name" autofocus @keyup.enter="Register()"/>
        <q-input dense outlined square
                 label="Password" v-model="registerform.password1"
                 :type="isPwd ? 'password' : 'text'"
                 @keyup.enter="Register()" style="margin-top: 5px">
          <template v-slot:append>
            <q-icon
              :name="isPwd ? 'visibility_off' : 'visibility'"
              class="cursor-pointer"
              @click="isPwd = !isPwd"
            />
          </template>
        </q-input>
        <q-input dense outlined square
                 label="Confirm Password" v-model="registerform.password2"
                 :type="isPwd2 ? 'password' : 'text'"
                 @keyup.enter="Register()" style="margin-top: 5px">
          <template v-slot:append>
            <q-icon
              :name="isPwd2 ? 'visibility_off' : 'visibility'"
              class="cursor-pointer"
              @click="isPwd2 = !isPwd2"
            />
          </template>
        </q-input>
      </q-card-section>
      <q-card-actions align="right" class="text-primary">
        <q-btn flat label="Cancel" v-close-popup />
        <q-btn color="primary" label="Register" @click="Register()"/>
      </q-card-actions>
    </q-card>
  </q-dialog>
  </q-layout>
</template>

<style lang="sass">
.my-menu-link
  color: white
  background: #01579b
</style>
<script>
import { menulist } from 'boot/menulist'
import { wsurl, post, getauth } from 'boot/axios_request'
import { openURL, date } from 'quasar'

var ws
export default {
  data () {
    return {
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
      miniState: true,
      tab: '',
      login: false,
      link: '',
      login_name: '',
      register: false,
      registerform: {
        name: '',
        password1: '',
        password2: ''
      },
      friend: false,
      friend_num: 0,
      friend_list: [],
      friend_previous: null,
      friend_next: null,
      sender: '',
      receiver: '',
      chat: false,
      chat_list: '',
      chat_text: '',
      chat_next: null,
      read: false,
      read_num: 0,
      read_list: [],
      read_previous: '',
      read_next: '',
      menuList: menulist
    }
  },
  methods: {
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
            message: 'Please enter the openid',
            icon: 'close',
            color: 'negative'
          })
        } else {
          _this.$q.localStorage.set('openid', _this.openid)
          getauth('staff/?staff_name=' + _this.login_name).then(res => {
            if (res.count === 1) {
              _this.authin = '1'
              _this.login = false
              _this.$q.localStorage.set('auth', '1')
              _this.$q.localStorage.set('login_name', _this.login_name)
              _this.$q.notify({
                message: 'Success Login',
                icon: 'check',
                color: 'green'
              })
              window.location.reload()
            } else {
              _this.$q.notify({
                message: "No user's Data",
                icon: 'close',
                color: 'negative'
              })
            }
          }).catch(err => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            })
          })
        }
      }
    },
    adminLogin () {
      var _this = this
      if (_this.admin_name === '') {
        _this.$q.notify({
          message: 'Please enter the admin name',
          color: 'negative',
          icon: 'close'
        })
      } else {
        if (_this.admin_password === '') {
          _this.$q.notify({
            message: 'Please enter the admin password',
            icon: 'close',
            color: 'negative'
          })
        } else {
          post('login/', _this.adminlogin).then(res => {
            if (res.code === '200') {
              _this.authin = '1'
              _this.login = false
              _this.admin = false
              _this.openid = res.data.openid
              _this.login_name = res.data.name
              _this.$q.localStorage.set('auth', '1')
              _this.$q.localStorage.set('login_name', _this.login_name)
              _this.$q.notify({
                message: 'Success Login',
                icon: 'check',
                color: 'green'
              })
              window.location.reload()
            } else {
              _this.$q.notify({
                message: "No user's Data",
                icon: 'close',
                color: 'negative'
              })
            }
          }).catch(err => {
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
      _this.$q.localStorage.remove('auth')
      _this.$q.localStorage.set('login_name', '')
      _this.$q.notify({
        message: 'Success Logout',
        icon: 'check',
        color: 'negative'
      })
      window.location.reload()
    },
    Register () {
      var _this = this
      post('register/', _this.registerform).then(res => {
        if (res.code === '200') {
          _this.register = false
          _this.openid = res.data.openid
          _this.login_name = _this.registerform.name
          _this.authin = '1'
          _this.$q.localStorage.set('openid', res.data.openid)
          _this.$q.localStorage.set('login_name', _this.registerform.name)
          _this.$q.localStorage.set('auth', '1')
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
          window.location.reload()
        } else {
          _this.$q.notify({
            message: res.msg,
            icon: 'close',
            color: 'negative'
          })
        }
      }).catch(err => {
        _this.$q.notify({
          message: err.detail,
          icon: 'close',
          color: 'negative'
        })
      })
    },
    initWebSocket () {
      var _this = this
      ws = new WebSocket(wsurl + '?sender=' + _this.login_name + '&receiver=' + _this.receiver + '&openid=' + _this.openid)
      ws.onmessage = _this.websocketonmessage
      ws.onopen = _this.websocketonopen
      ws.onerror = _this.websocketonerror
      ws.onclose = _this.websocketclose
    },
    websocketonopen () {
      console.log('Success Connect')
    },
    websocketonerror () {
      var _this = this
      _this.initWebSocket()
    },
    websocketonmessage (e) {
      var _this = this
      if (_this.$q.sessionStorage.getItem('receiver') === JSON.parse(e.data).sender) {
        _this.chat_list.push(JSON.parse(e.data))
      } else {
      }
      _this.Readnum()
      _this.$q.notify({
        message: JSON.parse(e.data).sender + 'Send you a message',
        color: 'deep-purple',
        icon: 'textsms',
        position: 'right',
        actions: [
          {
            label: '查看',
            color: 'yellow',
            handler: () => {
              _this.ChatWith(JSON.parse(e.data).sender)
            }
          }
        ]
      })
    },
    websocketsend () {
      var _this = this
      if (_this.chat_text === '') {
      } else {
        ws.send(_this.chat_text)
        _this.chat_list.push({
          sender: _this.sender + '-' + _this.openid,
          receiver: _this.receiver,
          detail: _this.chat_text,
          create_time: date.formatDate(Date.now(), 'YYYY-MM-DD HH:mm:ss')
        })
        _this.chat_text = ''
      }
    },
    websocketclose (e) {
      console.log('Disconnect', e)
    },
    ChatWith (e) {
      var _this = this
      _this.sender = _this.login_name
      _this.receiver = e
      _this.$q.sessionStorage.set('receiver', e)
      if (_this.sender === _this.receiver) {
        _this.$q.notify({
          message: 'Cannot Chat with yourself',
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.chat = true
        _this.chat_text = ''
        _this.initWebSocket()
        getauth('chat/?' + 'sender=' + _this.sender + '&receiver=' + _this.receiver).then(res => {
          _this.chat_list = res.results.reverse()
          _this.Readnum()
          if (res.next) {
            var next = res.next.split(':')[0]
            res.next.replace(next, window.location.href.split(':')[0])
            _this.chat_next = res.next
          } else {
            _this.chat_next = res.next
          }
        }).catch(err => {
          console.log(err)
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
      }
    },
    LoadChatList () {
      var _this = this
      getauth(_this.chat_next).then(res => {
        res.results.forEach(c => {
          _this.chat_list.unshift(c)
        })
        if (res.next) {
          var next = res.next.split(':')[0]
          res.next.replace(next, window.location.href.split(':')[0])
          _this.chat_next = res.next
        } else {
          _this.chat_next = res.next
        }
      }).catch(err => {
        _this.$q.notify({
          message: err.detail,
          icon: 'close',
          color: 'negative'
        })
      })
    },
    ChatClose () {
      var _this = this
      _this.receiver = ''
      _this.$q.sessionStorage.set('receiver', '')
      _this.chat_list = []
      _this.chat_text = ''
      _this.chat_next = null
    },
    Readnum () {
      var _this = this
      getauth('chat/read/?' + 'sender=' + _this.login_name).then(res => {
        if (res.previous) {
          var previous = res.previous.split(':')[0]
          res.previous.replace(previous, window.location.href.split(':')[0])
          _this.read_previous = res.previous
        } else {
          _this.read_previous = res.previous
        }
        if (res.next) {
          var next = res.next.split(':')[0]
          res.next.replace(next, window.location.href.split(':')[0])
          _this.read_next = res.next
        } else {
          _this.read_next = res.next
        }
        _this.read_list = res.results
        _this.read_num = res.count
      }).catch(err => {
        console.log(err)
        _this.$q.notify({
          message: err.detail,
          icon: 'close',
          color: 'negative'
        })
      })
    },
    ReadnumPrevious () {
      var _this = this
      getauth(_this.read_previous, {
      }).then(res => {
        _this.read_list = res.results
        if (res.previous) {
          var previous = res.previous.split(':')[0]
          res.previous.replace(previous, window.location.href.split(':')[0])
          _this.read_previous = res.previous
        } else {
          _this.read_previous = res.previous
        }
        if (res.next) {
          var next = res.next.split(':')[0]
          res.next.replace(next, window.location.href.split(':')[0])
          _this.read_next = res.next
        } else {
          _this.read_next = res.next
        }
      }).catch(err => {
        _this.$q.notify({
          message: err.detail,
          icon: 'close',
          color: 'negative'
        })
      })
    },
    ReadnumNext () {
      var _this = this
      getauth(_this.read_next, {
      }).then(res => {
        _this.read_list = res.results
        if (res.previous) {
          var previous = res.previous.split(':')[0]
          res.previous.replace(previous, window.location.href.split(':')[0])
          _this.read_previous = res.previous
        } else {
          _this.read_previous = res.previous
        }
        if (res.next) {
          var next = res.next.split(':')[0]
          res.next.replace(next, window.location.href.split(':')[0])
          _this.read_next = res.next
        } else {
          _this.read_next = res.next
        }
      }).catch(err => {
        _this.$q.notify({
          message: err.detail,
          icon: 'close',
          color: 'negative'
        })
      })
    },
    Friend () {
      var _this = this
      _this.friend = true
      getauth('staff/', {
      }).then(res => {
        _this.friend_list = res.results
        if (res.previous) {
          var previous = res.previous.split(':')[0]
          res.previous.replace(previous, window.location.href.split(':')[0])
          _this.friend_previous = res.previous
        } else {
          _this.friend_previous = res.previous
        }
        if (res.next) {
          var next = res.next.split(':')[0]
          res.next.replace(next, window.location.href.split(':')[0])
          _this.friend_next = res.next
        } else {
          _this.friend_next = res.next
        }
        _this.friend_num = res.count
      }).catch(err => {
        _this.$q.notify({
          message: err.detail,
          icon: 'close',
          color: 'negative'
        })
      })
    },
    Friend_previous () {
      var _this = this
      getauth(_this.friend_previous, {
      }).then(res => {
        _this.friend_list = res.results
        if (res.previous) {
          var previous = res.previous.split(':')[0]
          res.previous.replace(previous, window.location.href.split(':')[0])
          _this.friend_previous = res.previous
        } else {
          _this.friend_previous = res.previous
        }
        if (res.next) {
          var next = res.next.split(':')[0]
          res.next.replace(next, window.location.href.split(':')[0])
          _this.friend_next = res.next
        } else {
          _this.friend_next = res.next
        }
      }).catch(err => {
        _this.$q.notify({
          message: err.detail,
          icon: 'close',
          color: 'negative'
        })
      })
    },
    Friend_next () {
      var _this = this
      getauth(_this.friend_next, {
      }).then(res => {
        _this.friend_list = res.results
        if (res.previous) {
          var previous = res.previous.split(':')[0]
          res.previous.replace(previous, window.location.href.split(':')[0])
          _this.friend_previous = res.previous
        } else {
          _this.friend_previous = res.previous
        }
        if (res.next) {
          var next = res.next.split(':')[0]
          res.next.replace(next, window.location.href.split(':')[0])
          _this.friend_next = res.next
        } else {
          _this.friend_next = res.next
        }
      }).catch(err => {
        _this.$q.notify({
          message: err.detail,
          icon: 'close',
          color: 'negative'
        })
      })
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
      _this.initWebSocket()
      _this.Readnum()
    } else {
      _this.authin = '0'
    }
  },
  mounted () {
  },
  updated () {
    if (document.getElementById('chat_scroll')) {
      document.getElementById('chat_scroll').scrollTop = document.getElementById('chat_scroll').scrollHeight
    } else {
    }
  },
  destroyed () {
    if (ws) {
      if (ws.readyState === ws.OPEN) {
        ws.close()
      }
    }
  }
}
</script>
