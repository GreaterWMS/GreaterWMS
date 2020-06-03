<template>
    <q-page style="overflow-y: auto">

    <template>
    <div class="q-pa-md" style="width: 100%">
      <q-table
        title="Treats"
        :data="data"
        :columns="columns"
        row-key="name"
        selection="multiple"
        :selected.sync="selected"
        :filter="filter"
        grid
        hide-header
        :loading="loading"
        hide-bottom
        :pagination.sync="pagination"
        no-data-label="没有找到任何数据"
        no-results-label="没有找到您想要的数据"
        :table-style="{ height: height }"
      >
         <template v-slot:top>
           <q-btn-group push>
      <q-btn v-if="admin" unelevated label="新增" icon="add" @click="addConfirm()">
        <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
          新增一个用户
        </q-tooltip>
      </q-btn>
             <q-dialog v-model="addDialog" transition-show="jump-down" transition-hide="jump-up">
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">新建用户</div>
        </q-card-section>
        <q-card-section class="q-pt-none">
          <q-input dense label="用户名" v-model="addform.name" autofocus @keyup.enter="addSubmit()" style="margin-bottom: 20px"/>
          <q-input dense label="姓名" v-model="addform.nickname" @keyup.enter="addSubmit()" style="margin-bottom: 20px"/>
          <q-input dense label="密码" type="password" v-model="addform.password1" @keyup.enter="addSubmit()" style="margin-bottom: 20px"/>
          <q-input dense label="确认密码" type="password" v-model="addform.password2" @keyup.enter="addSubmit()" style="margin-bottom: 20px"/>
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="取消" v-close-popup @click="addCancel()"/>
          <q-btn color="primary" label="创建" @click="addSubmit()"/>
        </q-card-actions>
      </q-card>
    </q-dialog>
       <q-btn v-if="admin" unelevated label="修改" icon="edit" @click="editConfirm()">
        <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
         修改一个用户
        </q-tooltip>
      </q-btn>
             <q-dialog v-model="editDialog" transition-show="jump-down" transition-hide="jump-up">
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">修改用户</div>
        </q-card-section>
        <q-card-section class="q-pt-none">
          <q-input dense label="姓名" v-model="editform.nickname" autofocus @keyup.enter="editSubmit()" style="margin-bottom: 20px"/>
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="取消" v-close-popup @click="editCancel()"/>
          <q-btn color="primary" label="修改" @click="editSubmit()"/>
        </q-card-actions>
      </q-card>
    </q-dialog>
       <q-btn v-if="admin" unelevated label="删除" icon="delete" @click="deleteConfirm()">
         <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
          删除所选的数据
        </q-tooltip>
       </q-btn>
              <q-dialog v-model="deleteDialog" transition-show="jump-down" transition-hide="jump-up">
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">删除用户</div>
          删除操作不可逆，确认要删除吗？
        </q-card-section>
        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="取消" v-close-popup @click="deleteCancel()"/>
          <q-btn color="negative" label="确认删除" @click="deleteSubmit()"/>
        </q-card-actions>
      </q-card>
    </q-dialog>
    </q-btn-group>
             <q-space />
        <q-input outlined rounded dense debounce="300" color="primary" v-model="filter" placeholder="关键字进行搜索">
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
      </template>
        <template v-slot:no-data="{ icon, message, filter }">
        <div class="full-width row flex-center text-accent q-gutter-sm">
          <q-icon size="2em" name="sentiment_dissatisfied" />
          <span>
            Well this is sad... {{ message }}
          </span>
          <q-icon size="2em" :name="filter ? 'filter_b_and_w' : icon" />
        </div>
      </template>
        <template v-slot:top-right>
        <q-input borderless dense debounce="300" v-model="filter" placeholder="Search">
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
      </template>

      <template v-slot:item="props">
        <div
          class="q-pa-xs col-xs-12 col-sm-6 col-md-4 col-lg-3 grid-style-transition"
          :style="props.selected ? 'transform: scale(0.95);' : ''"
        >
          <q-card :class="props.selected ? 'bg-grey-2' : ''">
            <q-card-section>
              <q-checkbox dense v-model="props.selected" :label="props.row.name" />
            </q-card-section>
            <q-separator />
            <q-list dense>
              <q-item v-for="col in props.cols.filter(col => col.name !== 'name')" :key="col.name">
                <q-item-section>
                  <q-item-label>{{ col.label }}</q-item-label>
                </q-item-section>
                <q-item-section side>
                  <q-item-label caption>{{ col.value }}</q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
          </q-card>
        </div>
      </template>
      </q-table>
  </div>
</template>
    <router-view />
  </q-page>
</template>
<style lang="sass">
.grid-style-transition
  transition: transform .28s, background-color .28s
</style>
<script>
import { get, patch, del, post } from 'boot/axios'

export default {
  name: 'goodsunit',
  data () {
    return {
      admin: false,
      separator: 'vertical',
      loading: false,
      filter: '',
      height: '',
      selected: [],
      columns: [
        { name: 'name', required: true, field: row => row.name, format: val => `${val}` },
        { name: 'nickname', label: '姓名', field: 'nickname' },
        { name: 'create_time', label: '创建时间', field: 'create_time' },
        { name: 'last_update_time', label: '最后更新时间', field: 'last_update_time' }
      ],
      data: [],
      deleteDialog: false,
      deleteform: [],
      addDialog: false,
      addform: {
        name: '',
        nickname: '',
        password1: '',
        password2: ''
      },
      editDialog: false,
      editform: {
        nickname: '',
        transaction_code: ''
      },
      pagination: {
        sortBy: 'create_time',
        descending: false,
        page: 1,
        rowsPerPage: 100
      }
    }
  },
  methods: {
    getList () {
      var openid = this.$q.localStorage.getItem('openid')
      get('users/', { openid: openid }).then(response => {
        this.data = response.data.results.data
      }).catch(error => { console.log(error) })
    },
    addConfirm () {
      this.admincheck()
      if (this.admin) {
        this.addDialog = true
      } else {
        this.addDialog = false
        this.addform.name = ''
        this.addform.nickname = ''
        this.addform.password1 = ''
        this.addform.password2 = ''
        this.$q.notify({
          message: '非管理员账号，无法创建用户',
          icon: 'close',
          color: 'negative',
          position: 'right',
          timeout: 1500
        })
      }
    },
    addCancel () {
      this.addDialog = false
      this.addform.name = ''
      this.addform.nickname = ''
      this.addform.password1 = ''
      this.addform.password2 = ''
    },
    addSubmit () {
      if (this.addform.name === '') {
        this.$q.notify({
          message: '用户名不可以为空',
          icon: 'close',
          color: 'negative',
          position: 'right',
          timeout: 1500
        })
      } else if (this.addform.nickname === '') {
        this.$q.notify({
          message: '姓名不可以为空',
          icon: 'close',
          color: 'negative',
          position: 'right',
          timeout: 1500
        })
      } else if (this.addform.password1 === '') {
        this.$q.notify({
          message: '请输入密码',
          icon: 'close',
          color: 'negative',
          position: 'right',
          timeout: 1500
        })
      } else if (this.addform.password2 === '') {
        this.$q.notify({
          message: '请确认您的密码',
          icon: 'close',
          color: 'negative',
          position: 'right',
          timeout: 1500
        })
      } else if (this.addform.password1 !== this.addform.password2) {
        this.$q.notify({
          message: '二次输入的密码不一样，请重新输入',
          icon: 'close',
          color: 'negative',
          position: 'right',
          timeout: 1500
        })
      } else {
        var openid = this.$q.localStorage.getItem('openid')
        post('createuser/', { openid: openid }, { data: this.addform }).then(response => {
          if (response.data.code === '200') {
            this.$q.notify({
              message: '新建用户成功',
              icon: 'check',
              color: 'positive',
              position: 'right',
              timeout: 1500
            })
            this.getList()
            this.addDialog = false
            this.addform.name = ''
            this.addform.nickname = ''
            this.addform.password1 = ''
            this.addform.password2 = ''
          } else {
            this.$q.notify({
              message: response.data.msg,
              icon: 'close',
              color: 'negative',
              position: 'right',
              timeout: 1500
            })
            this.addDialog = false
          }
        }).catch(error => { console.log(error) })
      }
    },
    editConfirm () {
      this.admincheck()
      if (this.admin) {
        if (this.selected.length === 0) {
          this.$q.notify({
            message: '您还没有选中任何一个用户',
            icon: 'close',
            color: 'negative',
            position: 'right',
            timeout: 1500
          })
        } else if (this.selected.length > 1) {
          this.$q.notify({
            message: '一次只能修改一个用户',
            icon: 'close',
            color: 'negative',
            position: 'right',
            timeout: 1500
          })
        } else {
          this.editDialog = true
          this.$q.localStorage.set('nickname', this.selected[0].nickname)
          this.editform.nickname = this.selected[0].nickname
          this.editform.transaction_code = this.selected[0].transaction_code
        }
      } else {
        this.editDialog = false
        this.editform.nickname = ''
        this.editform.transaction_code = ''
        this.selected = []
        this.$q.notify({
          message: '非管理员账号，无法修改用户',
          icon: 'close',
          color: 'negative',
          position: 'right',
          timeout: 1500
        })
      }
    },
    editCancel () {
      this.editDialog = false
      this.editform.nickname = ''
      this.editform.transaction_code = ''
      this.$q.localStorage.remove('nickname')
      this.selected = []
    },
    editSubmit () {
      var nm = this.$q.localStorage.getItem('nickname')
      if (this.editform.nickname === nm) {
        this.$q.notify({
          message: '修改成功',
          icon: 'check',
          color: 'positive',
          position: 'right',
          timeout: 1500
        })
        this.editDialog = false
        this.$q.localStorage.remove('nickname')
      } else if (this.editform.nickname === '') {
        this.editDialog = false
        this.$q.localStorage.remove('nickname')
      } else {
        var openid = this.$q.localStorage.getItem('openid')
        patch('users/', { openid: openid }, { data: this.editform }).then(response => {
          if (response.data.code === '200') {
            this.editDialog = false
            this.$q.localStorage.remove('nickname')
            this.data.forEach(res => {
              if (res.transaction_code === response.data.data.transaction_code) {
                res.nickname = response.data.data.nickname
              }
            })
            this.$q.notify({
              message: '修改成功',
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
            this.editDialog = false
          }
        }).catch(error => { console.log(error) })
      }
      this.selected = []
    },
    deleteConfirm () {
      this.admincheck()
      if (this.admin) {
        if (this.selected.length === 0) {
          this.$q.notify({
            message: '您还没有选中任何一个用户',
            icon: 'close',
            color: 'negative',
            position: 'right',
            timeout: 1500
          })
        } else {
          this.deleteDialog = true
          this.selected.forEach(res => {
            this.deleteform.push({ transaction_code: res.transaction_code })
          })
        }
      } else {
        this.deleteDialog = false
        this.deleteform = []
        this.selected = []
        this.$q.notify({
          message: '非管理员账号，无法删除用户',
          icon: 'close',
          color: 'negative',
          position: 'right',
          timeout: 1500
        })
      }
    },
    deleteCancel () {
      this.deleteDialog = false
      this.deleteform = []
      this.selected = []
    },
    deleteSubmit () {
      var openid = this.$q.localStorage.getItem('openid')
      del('users/', { openid: openid }, { data: this.deleteform }).then(response => {
        if (response.data.code === '200') {
          this.deleteDialog = false
          this.data.forEach((res, index) => {
            response.data.data.forEach(result => {
              if (res.transaction_code === result.transaction_code) {
                this.data.splice(index, 1)
              }
            })
          })
          this.$q.notify({
            message: '删除成功',
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
          this.deleteDialog = false
        }
      }).catch(error => { console.log(error) })
      this.selected = []
    },
    admincheck () {
      var openid = this.$q.localStorage.getItem('openid')
      var authid = this.$q.localStorage.getItem('authid')
      if (openid === authid) {
        this.admin = true
      } else {
        this.admin = false
      }
    }
  },
  created () {
    this.admincheck()
  },
  mounted () {
    if (this.$q.localStorage.has('openid')) {
      this.getList()
    } else {}
    if (this.$q.platform.is.electron) {
      this.height = String(this.$q.screen.height - 275) + 'px'
    } else {
      this.height = this.$q.screen.height - 275 + '' + 'px'
    }
  },
  updated () {
  }
}
</script>
