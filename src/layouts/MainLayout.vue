<template>
  <q-layout view="hhh LpR lFf">
    <q-header reveal elevated class="bg-primary text-white">
      <q-toolbar class="bg-light-blue-10 text-white shadow-18 rounded-borders">
        <q-btn flat @click="drawerleft = !drawerleft" round dense icon="menu" />
          <q-toolbar-title to="/" shrink class="text-weight-bold">
            {{ title }}
          </q-toolbar-title>
      <q-space />
        <q-btn icon="home" stretch flat label="首页" @click="brownlink('https://www.56yhz.com/')">
          <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
            聚商汇首页
            </q-tooltip>
        </q-btn>
        <q-btn icon="menu_book" stretch flat label="开发文档">
          <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
              二次开发API文档,暂未开放
            </q-tooltip>
        </q-btn>
        <q-btn round flat @click="brownlink('https://github.com/Singosgu')">
          <q-avatar size="26px">
            <img src="statics/icons/GitHub.png">
          </q-avatar>
          <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                GitHub链接
                </q-tooltip>
        </q-btn>
          <q-btn round flat @click="brownlink('https://gitee.com/Singosgu')">
          <q-avatar size="26px">
            <img src="statics/icons/gitee.ico">
          </q-avatar>
          <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                码云链接
                </q-tooltip>
        </q-btn>
        <q-btn icon="contact_mail" stretch flat label="联系我们" @click="contact = true">
          <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
              商务合作或给我们建议
            </q-tooltip>
        </q-btn>
        <q-separator v-if="openid !== ''" dark vertical />
        <q-btn-dropdown v-if="openid !== ''" stretch flat icon="account_circle" auto-close>
        <q-list>
          <q-item @click="login = true" clickable v-close-popup tabindex="0">
            <q-item-section avatar>
              <q-avatar icon="supervisor_account" color="secondary" text-color="white" />
            </q-item-section>
            <q-item-section>
              <q-item-label>更改用户</q-item-label>
            </q-item-section>
          </q-item>
          <q-item @click="authDialog = true" clickable v-close-popup tabindex="1">
            <q-item-section avatar>
              <q-avatar icon="supervisor_account" color="secondary" text-color="white" />
            </q-item-section>
            <q-item-section>
              <q-item-label>我的授权码</q-item-label>
            </q-item-section>
          </q-item>
          <q-separator inset spaced />
          <q-item clickable @click="logout()" v-close-popup tabindex="0">
            <q-item-section avatar>
              <q-avatar icon="all_out" color="primary" text-color="white" />
            </q-item-section>
            <q-item-section>
              <q-item-label>用户退出</q-item-label>
            </q-item-section>
          </q-item>
          <q-item clickable @click="logoutAll()" v-close-popup tabindex="1">
            <q-item-section avatar>
              <q-avatar icon="settings_power" color="negative" text-color="white" />
            </q-item-section>
            <q-item-section>
              <q-item-label>初始化退出</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-btn-dropdown>
        <q-dialog v-model="authDialog">
      <q-card>
        <q-card-section>
          <div class="text-h6">授权码</div>
        </q-card-section>
        <q-card-section class="q-pt-none">
          {{ authid }}
        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat label="OK" color="primary" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>
<template>
  <q-btn label="登入" color="primary" @click="login = true" v-if="openid === ''" style="margin-right: 10px">
    <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
              管理员账号登入无需授权码
            </q-tooltip>
  </q-btn>
  <q-btn label="注册" color="primary" @click="register = true" v-if="openid === ''">
    <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
              注册获得管理员账号和授权码
            </q-tooltip>
  </q-btn>
          <q-dialog v-model="login" transition-show="jump-down" transition-hide="jump-up">
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">用户登入</div>
        </q-card-section>
        <q-card-section class="q-pt-none">
          <q-input dense label="用户名" v-model="loginform.name" autofocus @keyup.enter="loginSubmit()"/>
          <q-input type="password" label="密码" v-model="loginform.password" @keyup.enter="loginSubmit()"/>
          <q-input v-if="!auth" label="授权码" placeholder="请输入授权码" v-model="authid" @keyup.enter="loginSubmit()">
            <q-tooltip
          transition-show="scale"
          transition-hide="scale"
          content-class="bg-negative"
          :offset="[10, 10]"
          content-style="font-size: 14px"
        >
          <div>请询问管理拿到授权码，此授权码为首次登入时使用</div>
              <div>如果没有授权码，可以注册后拿到新的授权码，授权码为用户数据归类的统一标识</div>
              <div>管理员账号登入无需授权码</div>

        </q-tooltip>
          </q-input>
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="取消" v-close-popup />
          <q-btn v-show="!auth" color="accent" label="管理员登入" @click="handleAdminLogin()"/>
          <q-btn color="primary" label="用户登入" @click="loginSubmit()"/>
        </q-card-actions>
      </q-card>
    </q-dialog>
            <q-dialog v-model="register" transition-show="jump-down" transition-hide="jump-up">
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">管理员注册</div>
        </q-card-section>
        <q-card-section class="q-pt-none">
          <q-input dense label="用户名" v-model="registerform.name" autofocus @keyup.enter="registerSubmit()"/>
          <q-input type="password" label="密码" v-model="registerform.password1" @keyup.enter="registerSubmit()"/>
          <q-input type="password" label="确认密码" v-model="registerform.password2" @keyup.enter="registerSubmit()"/>
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="取消" v-close-popup />
          <q-btn color="primary" label="注册" @click="registerSubmit()"/>
        </q-card-actions>
      </q-card>
    </q-dialog>
</template>
        <q-btn v-if="openid !== ''" @click="getNoteData()" round dense flat color="white" icon="event_note">
            <q-badge color="red" text-color="white" floating>
              {{ note_num }}
            </q-badge>
            <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
              备忘录
            </q-tooltip>
          </q-btn>
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
            <q-item clickable :active="link === menuItem.link" :to="{ name: menuItem.link }"
                    @click="link === menuItem.link" v-ripple exact active-class="my-menu-link">
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
    <q-drawer
        side="right"
        v-model="drawerright"
        bordered
        :width="340"
        :breakpoint="500"
        content-class="bg-grey-3"
      >
        <q-scroll-area class="fit">
          <template>
      <div class="q-pa-md">
        <div class="q-gutter-md row items-start">
          <div class="flex flex-center" style="padding-top: 10px; height: 50px">
            选择日期即添加新的备忘信息
            <q-btn v-show="noteadd" @click="noteaddDialog = true" round color="secondary" icon="add" style="margin-left: 30px; height: 100%">
            <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
              新增备忘信息
            </q-tooltip>
              <q-dialog v-model="noteaddDialog" transition-show="jump-down" transition-hide="jump-up">
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">备忘信息</div>
        </q-card-section>
        <q-card-section class="q-pt-none">
          <q-input dense label="标题" v-model="noteform.title" autofocus @keyup.enter="noteSubmit()" style="margin-bottom: 20px"/>
          <textarea placeholder="备忘信息" v-model="noteform.desc" @keyup.enter="noteSubmit()" style="width: 100%"/>
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="取消" v-close-popup />
          <q-btn color="primary" label="记录" @click="noteSubmit()"/>
        </q-card-actions>
      </q-card>
    </q-dialog>
          </q-btn>
          </div>
          <q-date v-model="date"
                  :events="events"
                  :event-color="(date) => date === today ? 'orange' : 'teal'"
                  @click="Canlendadetail()"/>
    </div>
  </div>
            <template>
  <div class="q-px-lg q-pb-md">
    <q-timeline color="secondary">
      <div v-for="(Note, index) in noteData" :key="index">
      <q-timeline-entry
        :title="Note.title"
        :subtitle="Note.note_day"
        :color="Note.icon_color"
        :icon="Note.icon"
      >
        <q-badge outline :color="Note.label_color" :label="Note.label" />
        <div v-show="Note.edit === '0'">
          {{ Note.desc }}
        </div>
        <div v-show="Note.edit === '1' && Note.progress === '0'">
          <textarea dense v-model="Note.desc" autofocus @keyup.enter="contactSubmit()" style="width: 100%"/>
        </div>
         <q-btn v-show="Note.progress === '0' && Note.edit ==='0'" color="secondary" @click="doneNote(index)" label="完成" />
        <q-btn v-if="Note.progress === '0' && Note.edit ==='0'" color="accent" label="修改" @click="editNote(index)" style="margin-left: 10px"/>
        <q-btn v-show="Note.progress === '0' && Note.edit ==='0'" color="negative" label="删除" @click="deleteNote(index)" style="margin-left: 10px"/>
      <q-btn v-show="Note.progress === '0' && Note.edit ==='1'" color="secondary" label="取消" @click="CanceleditNote(index)"/>
        <q-btn v-show="Note.progress === '0' && Note.edit ==='1'" color="accent" label="修改" @click="ConfirmeditNote(index)" style="margin-left: 10px"/>
      </q-timeline-entry>
      </div>
    </q-timeline>
  </div>
</template>
</template>
        </q-scroll-area>
      </q-drawer>
    <q-page-container>
      <router-view />
        <q-page-sticky position="bottom-right" :offset="[18, 18]">
          <q-btn v-show="authid === openid" flat @click="brownlink('http://www.miit.gov.cn/')" color="black" label="版权所有 ICP证：沪ICP备16034540号-1" />
            <q-btn fab glossy icon="contact_mail" color="purple" @click="contact = true"/>
          <q-dialog v-model="contact" transition-show="jump-down" transition-hide="jump-up">
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">联系我们</div>
        </q-card-section>
        <q-card-section class="q-pt-none">
          <q-input dense label="称呼" v-model="contactform.name" autofocus @keyup.enter="contactSubmit()" style="padding-bottom: 10px"/>
          <q-input dense label="联系方式" v-model="contactform.mobile" @keyup.enter="contactSubmit()" style="padding-bottom: 25px"/>
          <textarea placeholder="备注信息" v-model="contactform.comments" @keyup.enter="contactSubmit()" style="width: 100%"/>
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="取消" v-close-popup />
          <q-btn color="primary" label="发送" @click="contactSubmit()"/>
        </q-card-actions>
      </q-card>
    </q-dialog>
          </q-page-sticky>
      <q-page-scroller position="bottom-right" :scroll-offset="150" :offset="[18, 18]">
            <q-btn fab icon="keyboard_arrow_up" color="accent" />
          </q-page-scroller>
    </q-page-container>
  </q-layout>
</template>
<style lang="sass">
.my-menu-link
  color: white
  background: #01579b
</style>
<script>
import { postlogin, postauth, post, get, del, patch } from 'boot/axios'
import { menulist } from 'boot/menulist'
import { openURL } from 'quasar'
export default {
  meta: {
    meta: {
      description: { name: 'description', content: '聚商汇--供应链计划管理分析工具' },
      keywords: { name: 'keywords', content: '聚商汇,scm system, 供应链计划管理分析工具, 供应链，采购计划，生产计划， 物料计划' },
      equiv: { 'http-equiv': 'Content-Type', content: 'text/html; charset=UTF-8' }
    }
  },
  data () {
    return {
      title: '聚商汇--供应链计划管理分析工具',
      left: false,
      drawerleft: false,
      drawerright: false,
      miniState: true,
      tab: '',
      logbtn: '1',
      auth: false,
      authDialog: false,
      authid: '',
      openid: '',
      login: false,
      register: false,
      link: '',
      contact: false,
      contactform: {
        name: '',
        mobile: '',
        comments: ''
      },
      loginform: {
        name: '',
        password: ''
      },
      registerform: {
        name: '',
        password1: '',
        password2: ''
      },
      menuList: menulist,
      date: '',
      today: '',
      events: [],
      noteadd: true,
      note_num: 0,
      noteaddDialog: false,
      noteform: {
        title: '',
        desc: ''
      },
      noteData: [],
      electronV: false
    }
  },
  methods: {
    registerSubmit () {
      if (this.registerform.name === '') {
        this.$q.notify({
          message: '用户名不可以为空',
          icon: 'close',
          color: 'negative',
          position: 'right',
          timeout: 1500
        })
      } else {
        if (this.registerform.password1 === '') {
          this.$q.notify({
            message: '密码不能为空',
            icon: 'close',
            color: 'negative',
            position: 'right',
            timeout: 1500
          })
        } else {
          if (this.registerform.password2 === '') {
            this.$q.notify({
              message: '请确认您第一次输入的密码',
              icon: 'close',
              color: 'negative',
              position: 'right',
              timeout: 1500
            })
          } else {
            if (this.registerform.password1 !== this.registerform.password2) {
              this.$q.notify({
                message: '2次输入的密码不一致',
                icon: 'close',
                color: 'negative',
                position: 'right',
                timeout: 1500
              })
            } else {
              this.handleRegisterSubmit()
            }
          }
        }
      }
    },
    loginSubmit () {
      if (this.authid === '') {
        this.$q.notify({
          message: '需要授权码才可以登入',
          icon: 'close',
          color: 'negative',
          position: 'right',
          timeout: 1500
        })
      } else {
        if (this.loginform.name === '') {
          this.$q.notify({
            message: '用户名不能为空',
            icon: 'close',
            color: 'negative',
            position: 'right',
            timeout: 1500
          })
        } else {
          if (this.loginform.password === '') {
            this.$q.notify({
              message: '密码不能为空',
              icon: 'close',
              color: 'negative',
              position: 'right',
              timeout: 1500
            })
          } else {
            postauth('authcheck', { data: this.authid }).then(response => {
              if (response.data.code === '200') {
                this.auth = true
                if (this.$q.localStorage.has('authid')) {
                  if (this.$q.localStorage.getItem('authid') === this.authid) {
                  } else {
                    this.$q.localStorage.set('authid', this.authid)
                  }
                } else {
                  this.$q.localStorage.set('authid', this.authid)
                }
                this.handleLogin()
              } else {
                this.auth = false
                this.$q.notify({
                  message: '授权码错误',
                  icon: 'close',
                  color: 'negative',
                  position: 'right',
                  timeout: 1500
                })
              }
            }).catch(error =>
              console.log(error)
            )
          }
        }
      }
    },
    authcheck () {
      if (this.$q.localStorage.has('authid')) {
        const authid = this.$q.localStorage.getItem('authid')
        if (this.$q.localStorage.has('openid')) {
          const openid = this.$q.localStorage.getItem('openid')
          postauth('initialdata/', { openid: openid, authid: authid }).then(response => {
            if (response.data.code === '1032') {
              this.authid = response.data.data.authid
              this.auth = true
              this.openid = response.data.data.openid
              this.note_num = response.data.note_num
              this.events = response.data.events
              this.events.map(train => {
                this.events.push(train.note_day)
              })
              this.events = [...new Set(this.events)]
              this.noteData = response.data.today_note
              this.noteData.forEach(response => {
                response.edit = '0'
                if (response.progress === '0') {
                  response.label = '待完成'
                  response.label_color = 'negative'
                } else {
                  response.label = '已完成'
                  response.label_color = 'primary'
                }
              })
              this.$q.localStorage.set('notedata', this.noteData)
              var value = this.$q.localStorage.getItem('notedata')
              this.noteData = value
              this.$q.localStorage.remove('notedata')
            } else {
              this.$q.localStorage.remove('authid')
              this.$q.localStorage.remove('openid')
              this.auth = false
              this.note_num = 0
              this.authid = ''
              this.openid = ''
              this.noteData = []
              this.events = []
            }
          }).catch(error => { console.log(error) })
        } else {
          postauth('initialdata/', { authid: authid }).then(response => {
            if (response.data.code === '1030') {
              this.authid = response.data.data.authid
              this.auth = true
            } else {
              this.$q.localStorage.remove('authid')
              this.auth = false
            }
          }).catch(error => { console.log(error) })
        }
      } else {
        if (this.$q.localStorage.has('openid')) {
          this.$q.localStorage.remove('openid')
        }
      }
    },
    handleLogin () {
      postlogin('userlogin/', this.loginform).then(response => {
        if (response.data.code === '200') {
          this.login = false
          this.drawerright = false
          this.upnewdate()
          this.openid = response.data.data.openid
          this.$q.localStorage.set('openid', response.data.data.openid)
          this.note_num = response.data.note_num
          this.note_num = response.data.note_num
          this.events = response.data.events
          this.events.map(train => {
            this.events.push(train.note_day)
          })
          this.events = [...new Set(this.events)]
          this.noteData = response.data.today_note
          this.noteData.forEach(response => {
            response.edit = '0'
            if (response.progress === '0') {
              response.label = '待完成'
              response.label_color = 'negative'
            } else {
              response.label = '已完成'
              response.label_color = 'primary'
            }
          })
          this.$q.localStorage.set('notedata', this.noteData)
          var value = this.$q.localStorage.getItem('notedata')
          this.noteData = value
          this.$q.localStorage.remove('notedata')
          this.noteNum()
          this.$q.notify({
            message: '登入成功',
            icon: 'check',
            color: 'positive',
            position: 'right',
            timeout: 1500
          })
        } else {
          this.$q.notify({
            message: response.data.msg,
            icon: 'close',
            color: 'negative',
            position: 'right',
            timeout: 1500
          })
        }
      }).catch(error =>
        console.log(error)
      )
    },
    handleAdminLogin () {
      if (this.loginform.name === '') {
        this.$q.notify({
          message: '用户名不能为空',
          icon: 'close',
          color: 'negative',
          position: 'right',
          timeout: 1500
        })
      } else {
        if (this.loginform.password === '') {
          this.$q.notify({
            message: '密码不能为空',
            icon: 'close',
            color: 'negative',
            position: 'right',
            timeout: 1500
          })
        } else {
          postauth('login', this.loginform).then(response => {
            console.log(response.data)
            if (response.data.code === '200') {
              this.login = false
              this.drawerright = false
              this.upnewdate()
              this.auth = true
              this.authid = response.data.data.authid
              this.openid = response.data.data.openid
              this.$q.localStorage.set('openid', response.data.data.openid)
              this.$q.localStorage.set('authid', response.data.data.openid)
              this.note_num = response.data.note_num
              this.events = response.data.events
              this.events.map(train => {
                this.events.push(train.note_day)
              })
              this.events = [...new Set(this.events)]
              this.noteData = response.data.today_note
              this.noteData.forEach(response => {
                response.edit = '0'
                if (response.progress === '0') {
                  response.label = '待完成'
                  response.label_color = 'negative'
                } else {
                  response.label = '已完成'
                  response.label_color = 'primary'
                }
              })
              this.$q.localStorage.set('notedata', this.noteData)
              var value = this.$q.localStorage.getItem('notedata')
              this.noteData = value
              this.$q.localStorage.remove('notedata')
              this.noteNum()
              this.$q.notify({
                message: '登入成功',
                icon: 'check',
                color: 'positive',
                position: 'right',
                timeout: 1500
              })
            } else {
              this.$q.notify({
                message: response.data.msg,
                icon: 'close',
                color: 'negative',
                position: 'right',
                timeout: 1500
              })
            }
          }).catch(error => { console.log(error) })
        }
      }
    },
    handleRegisterSubmit () {
      postauth('register', this.registerform).then(response => {
        if (response.data.code === '200') {
          this.register = false
          this.registerform.name = ''
          this.registerform.password1 = ''
          this.registerform.password2 = ''
          this.$q.localStorage.set('authid', response.data.data.openid)
          this.$q.localStorage.set('openid', response.data.data.openid)
          this.openid = response.data.data.openid
          this.auth = true
          this.authid = response.data.data.openid
          this.noteNum()
          this.$q.notify({
            message: '注册成功',
            icon: 'check',
            color: 'positive',
            position: 'right',
            timeout: 1500
          })
        } else {
          this.$q.notify({
            message: response.data.msg,
            icon: 'close',
            color: 'negative',
            position: 'right',
            timeout: 1500
          })
        }
      }).catch(error =>
        console.log(error)
      )
    },
    logout () {
      this.drawerright = false
      this.login = false
      this.openid = ''
      this.note_num = 0
      this.events = []
      this.$q.localStorage.remove('openid')
    },
    logoutAll () {
      this.drawerright = false
      this.login = false
      this.auth = false
      this.openid = ''
      this.authid = ''
      this.note_num = 0
      this.events = []
      this.$q.localStorage.remove('openid')
      this.$q.localStorage.remove('authid')
      this.$q.localStorage.remove('editnotetitle')
    },
    drawerClick (e) {
      if (this.miniState) {
        this.miniState = false
        e.stopPropagation()
      }
    },
    versionCheck () {
    },
    contactSubmit () {
      if (this.contactform.name === '') {
        this.$q.notify({
          message: '称呼不能为空',
          icon: 'close',
          color: 'negative',
          position: 'right',
          timeout: 1500
        })
      } else {
        if (this.contactform.mobile === '') {
          this.$q.notify({
            message: '联系方式不能为空',
            icon: 'close',
            color: 'negative',
            position: 'right',
            timeout: 1500
          })
        } else {
          if (this.contactform.comments === '') {
            this.$q.notify({
              message: '请输入您的需要和我们联系的信息',
              icon: 'close',
              color: 'negative',
              position: 'right',
              timeout: 1500
            })
          } else {
            this.$set(this.contactform, 'openid', this.openid)
            console.log(this.contactform)
            postauth('contact', this.contactform).then(response => {
              if (response.data.code === '200') {
                this.contact = false
                this.$q.notify({
                  message: '感谢您的反馈，我们会尽快联系您',
                  icon: 'check',
                  color: 'positive',
                  position: 'right',
                  timeout: 1500
                })
              } else {
                this.$q.notify({
                  message: '或许请求次数过多，或者网络原因引起的提交不成功',
                  icon: 'close',
                  color: 'negative',
                  position: 'right',
                  timeout: 1500
                })
              }
            }).catch(error => {
              console.log(error)
            })
          }
        }
      }
    },
    brownlink (e) {
      openURL(e)
    },
    upnewdate () {
      var _this = this
      const yy = new Date().getFullYear()
      const mm = new Date().getMonth() + 1
      const dd = new Date().getDate()
      if (mm < 10 && dd < 10) {
        _this.date = yy + '/0' + mm + '/0' + dd
      } else if (mm < 10 && dd >= 10) {
        _this.date = yy + '/0' + mm + '/' + dd
      } else if (mm >= 10 && dd >= 10) {
        _this.date = yy + '/' + mm + '/' + dd
      } else {
        _this.date = yy + '/' + mm + '/' + dd
      }
      this.today = this.date
      this.$q.localStorage.set('date', this.date)
    },
    editNote (e) {
      this.noteData[e].edit = '1'
      this.$q.localStorage.set('editnotedesc', this.noteData[e].desc)
      this.$q.localStorage.set('notedata', this.noteData)
      var value = this.$q.localStorage.getItem('notedata')
      this.noteData = value
      this.$q.localStorage.remove('notedata')
    },
    doneNote (e) {
      var openid = this.$q.localStorage.getItem('openid')
      patch('notebook/', { openid: openid }, { id: this.noteData[e].id, progress: 1 }).then(response => {
        this.noteData[e].progress = '1'
        this.noteData[e].icon = 'check'
        this.noteData[e].icon_color = 'green'
        this.noteData[e].label = '已完成'
        this.noteData[e].label_color = 'primary'
        this.$q.localStorage.set('notedata', this.noteData)
        var value = this.$q.localStorage.getItem('notedata')
        this.noteData = value
        this.$q.localStorage.remove('notedata')
        this.noteNum()
      }).catch(error => { console.log(error) })
    },
    deleteNote (e) {
      del('notebook/', { id: this.noteData[e].id }).then(response => {
        if (response.data.code === '200') {
          this.noteData.splice(e, 1)
          this.$q.localStorage.set('notedata', this.noteData)
          var value = this.$q.localStorage.getItem('notedata')
          this.noteData = value
          this.$q.localStorage.remove('notedata')
          this.noteNum()
        } else {}
      }).catch(error => { console.log(error) })
    },
    CanceleditNote (e) {
      this.noteData[e].edit = '0'
      var desc = this.$q.localStorage.getItem('editnotedesc')
      if (desc === this.noteData[e].desc) {
      } else {
        this.noteData[e].desc = desc
      }
      this.$q.localStorage.set('notedata', this.noteData)
      var value = this.$q.localStorage.getItem('notedata')
      this.noteData = value
      this.$q.localStorage.remove('notedata')
      this.$q.localStorage.remove('editnotedesc')
    },
    ConfirmeditNote (e) {
      this.noteData[e].edit = '0'
      var desc = this.$q.localStorage.getItem('editnotedesc')
      if (desc === this.noteData[e].desc) {
      } else {
        var openid = this.$q.localStorage.getItem('openid')
        patch('notebook/', { openid: openid }, { id: this.noteData[e].id, desc: this.noteData[e].desc }).then(response => {
          this.$q.localStorage.set('notedata', this.noteData)
          var value = this.$q.localStorage.getItem('notedata')
          this.noteData = value
          this.$q.localStorage.remove('notedata')
        }).catch(error => { console.log(error) })
      }
      this.$q.localStorage.set('notedata', this.noteData)
      var value = this.$q.localStorage.getItem('notedata')
      this.noteData = value
      this.$q.localStorage.remove('notedata')
      this.$q.localStorage.remove('editnotedesc')
    },
    Canlendadetail () {
      const yy = new Date().getFullYear()
      const mm = new Date().getMonth() + 1
      const dd = new Date().getDate()
      var checkdate = this.$q.localStorage.getItem('date')
      var chooseDate = this.date.split('/')
      if (checkdate === this.date) {} else {
        this.noteNum()
        var openid = this.$q.localStorage.getItem('openid')
        get('notebook/', { openid: openid, note_day: this.date, max_page: 50 }).then(response => {
          if (response.data.results.code === '200') {
            this.noteData = response.data.results.data
            this.$q.localStorage.set('notedata', this.noteData)
            var value = this.$q.localStorage.getItem('notedata')
            this.noteData = value
            this.$q.localStorage.remove('notedata')
            this.noteData.forEach(response => {
              response.edit = '0'
              if (response.progress === '0') {
                response.label = '待完成'
                response.label_color = 'negative'
              } else {
                response.label = '已完成'
                response.label_color = 'primary'
              }
            })
          } else {}
        }).catch(error => { console.log(error) })
        this.$q.localStorage.set('date', this.date)
        if (parseInt(chooseDate[0], 10) <= yy && parseInt(chooseDate[1], 10) <= mm && parseInt(chooseDate[2], 10) < dd) {
          this.noteadd = false
          console.log(chooseDate[0], chooseDate[1], chooseDate[2])
        } else {
          this.noteadd = true
        }
      }
    },
    noteSubmit () {
      var openid = this.$q.localStorage.getItem('openid')
      this.noteform.note_day = this.date
      post('notebook/', { openid: openid }, { data: this.noteform }).then(response => {
        this.noteaddDialog = false
        this.noteform.title = ''
        this.noteform.desc = ''
        this.noteNum()
        var openid = this.$q.localStorage.getItem('openid')
        get('notebook/', { openid: openid, note_day: this.date, max_page: 50 }).then(response => {
          if (response.data.results.code === '200') {
            this.noteData = response.data.results.data
            this.$q.localStorage.set('notedata', this.noteData)
            var value = this.$q.localStorage.getItem('notedata')
            this.noteData = value
            this.$q.localStorage.remove('notedata')
            this.noteData.forEach(response => {
              response.edit = '0'
              if (response.progress === '0') {
                response.label = '待完成'
                response.label_color = 'negative'
              } else {
                response.label = '已完成'
                response.label_color = 'primary'
              }
            })
          } else {}
        }).catch(error => { console.log(error) })
      }).catch(error => { console.log(error) })
    },
    getNoteData () {
      this.drawerright = !this.drawerright
    },
    noteNum () {
      if (this.$q.localStorage.has('openid')) {
        var openid = this.$q.localStorage.getItem('openid')
        get('notebook/note_num/', { openid: openid, note_day: this.date }).then(response => {
          this.note_num = response.data.data
        }).catch(error => { console.log(error) })
      } else {}
    }
  },
  created () {
    this.upnewdate()
    if (this.$q.localStorage.has('authid')) {
      this.authid = this.$q.localStorage.getItem('authid')
      this.auth = true
    } else {}
    if (this.$q.localStorage.has('openid')) {
      this.openid = this.$q.localStorage.getItem('openid')
    } else {}
    if (this.$q.platform.is.electron) {
      this.electronV = true
    } else {
      this.electronV = false
    }
  },
  mounted () {
    this.authcheck()
  }
}
</script>
