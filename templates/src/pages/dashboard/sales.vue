<template>
    <div class="q-pa-md" style="width: 100%; margin-top: -20px">
      <q-table
        title="Treats"
        dense
        :data="data"
        :columns="columns"
        row-key="t_code"
        :separator="separator"
        :filter="filter"
        :loading="loading"
        :selected-rows-label="getSelectedString"
        selection="multiple"
        :selected.sync="selected"
        hide-bottom
        :pagination.sync="pagination"
        no-data-label="没有找到任何数据"
        no-results-label="没有找到您想要的数据"
        :table-style="{ height: height }"
      >
         <template v-slot:top>
           <q-btn-group push>
       <q-btn label="新增" icon="add" @click="newForm = true">
         <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
          新增一条数据
        </q-tooltip>
    <q-dialog v-model="newForm">
      <q-card class="shadow-24">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <div>新增数据</div>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip>关闭</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section style="max-height: 325px; width: 500px" class="scroll">
          <q-input v-model="newFormData.name" :label="label_name.name1" :placeholder="placeholder_name.name1" autofocus @keyup.enter="newFormDataCheck()"/>
        </q-card-section>
        <div style="float: right; padding: 15px 15px 15px 0">
          <q-btn color="white" text-color="black" style="margin-right: 25px" @click="newFormDataCancel()">取消提交</q-btn>
          <q-btn color="secondary" @click="newFormDataCheck()">确认提交</q-btn>
        </div>
      </q-card>
    </q-dialog>
       </q-btn>
        <q-btn label="修改" icon="edit" @click="editFormDataCheck()">
         <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
          修改数据，一次只能修改一条数据
        </q-tooltip>
    <q-dialog v-model="editForm">
      <q-card class="shadow-24">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <div>修改数据</div>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip>关闭</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section style="max-height: 325px; width: 500px" class="scroll">
            <q-input v-model="editFormData.name" :label="label_name.name1" :placeholder="placeholder_name.name1" autofocus @keyup.enter="editFormDataSubmit()"/>
        </q-card-section>
        <div style="float: right; padding: 15px 15px 15px 0">
          <q-btn color="white" text-color="black" style="margin-right: 25px" @click="editFormDataCancel()">取消提交</q-btn>
          <q-btn color="secondary" @click="editFormDataSubmit()">确认提交</q-btn>
        </div>
      </q-card>
    </q-dialog>
       </q-btn>
        <q-btn label="删除" icon="delete" @click="deleteDataCheck()">
         <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
          删除选中条数据，可以批量删除
        </q-tooltip>
    <q-dialog v-model="deleteDialog">
      <q-card class="shadow-24">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <div>删除数据</div>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip>关闭</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section style="max-height: 325px; width: 500px" class="scroll">
            数据删除后不可逆
        </q-card-section>
        <div style="float: right; padding: 15px 15px 15px 0">
          <q-btn color="white" text-color="black" style="margin-right: 25px" @click="deleteDataCancel()">取消提交</q-btn>
          <q-btn color="secondary" @click="deleteDataSubmit()">确认提交</q-btn>
        </div>
      </q-card>
    </q-dialog>
       </q-btn>
        <q-btn label="刷新" icon="refresh" @click="reFresh()">
         <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
          刷新页面
        </q-tooltip>
       </q-btn>
         <q-btn label="下载" icon="cloud_download" @click="downloadexample()">
         <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
          将选中的数据下载下来
        </q-tooltip>
       </q-btn>
             <q-btn-dropdown
      menu-anchor="bottom right"
      label="日期筛选"
    >
      <div class="row no-wrap q-pa-md">
        <div class="column">
          <div class="text-h6">起始日期</div>
                <q-date
                  v-model="date1"
                  today-btn
                />
        </div>

        <q-separator vertical inset class="q-mx-lg" />
      <div class="column">
          <div class="text-h6">结束日期</div>
                <q-date
                  v-model="date2"
                  today-btn
                />
        </div>
      </div>
    </q-btn-dropdown>
                     <q-btn label="日期查询" icon="search" @click="DatereFresh()">
         <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
          确认以日期查询数据
        </q-tooltip>
       </q-btn>
         <q-btn v-show="selected.length >1" icon="done_all" >Selected: {{ JSON.stringify(selected.length) }}
           <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
          您选择了({{ JSON.stringify(selected.length) }})条数据
        </q-tooltip>
       </q-btn>
          <q-btn v-show="selected.length === 1" icon="done" >Selected: {{ JSON.stringify(selected.length) }}
         <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
          您选择了(1)条数据
        </q-tooltip>
       </q-btn>
          <q-btn v-show="selected.length === 0" icon="check_circle_outline" >Selected: {{ JSON.stringify(selected.length) }}
            <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
          您还没有选择任何数据
        </q-tooltip>
       </q-btn>
           </q-btn-group>
             <q-space />
           <q-input outlined rounded dense debounce="300" color="primary" v-model="filter" placeholder="本页关键字搜索">
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
      </q-table>
<template>
        <div class="q-pa-lg flex flex-center">
          <q-pagination
            v-model="current"
            color="purple"
            :max="totlepage"
            :max-pages="7"
            :boundary-links="true"
            :direction-links="true"
            :boundary-numbers="true"
            style="z-index: 1000"
            @click="pageChange()"
          >
          </q-pagination>
        </div>
      </template>
  </div>
</template>
    <router-view />

<script>
import { openURL } from 'quasar'
export default {
  name: 'Pageproperty',
  data () {
    return {
      baseurl: 'http://127.0.0.1:8000/',
      pathname: 'property/',
      authorization_get: false,
      authorization_post: false,
      authorization_getfile: false,
      authorization_delete: false,
      authorization_patch: false,
      label_name: {
        name1: '库位属性'
      },
      placeholder_name: {
        name1: '请输入库位属性名称'
      },
      separator: 'cell',
      loading: false,
      filter: '',
      selected: [],
      totlepage: 1,
      current: 1,
      height: '',
      columns: [
        { name: 'name', required: true, label: '库位属性', align: 'left', field: 'name' },
        { name: 'create_name', label: '创建人', field: 'create_name' },
        { name: 'create_time', label: '创建时间', field: 'create_time' },
        { name: 'last_update_time', label: '最后修改时间', field: 'last_update_time' }
      ],
      data: [
      ],
      pagination: {
        sortBy: 'create_time',
        descending: true,
        page: 1,
        rowsPerPage: 50
      },
      newForm: false,
      newFormData: {
        name: ''
      },
      editForm: false,
      editFormData: {
      },
      deleteDialog: false,
      deleteFormData: [],
      date1: '',
      date2: ''
    }
  },
  methods: {
    authCheck () {
      var openid = this.$q.localStorage.getItem('openid')
      this.$axios.get(this.baseurl + 'userauth/', {
        headers: {
          'Content-Type': 'application/json;charset=utf-8'
        },
        params: {
          openid: openid,
          authorization: '1'
        },
        data: {}
      }).then(response => {
        if (response.data.results.code === '200') {
          if (response.data.results.data.length === 0) {
            this.authorization_get = true
            this.authorization_post = true
            this.authorization_getfile = true
            this.authorization_delete = true
            this.authorization_patch = true
          } else if (response.data.results.data.length === 1) {
            if (response.data.results.data[0].aut1 === 0) {
              this.authorization_get = true
              this.getList()
            } else {
              this.authorization_get = false
            }
            if (response.data.results.data[0].aut2 === 0) {
              this.authorization_getfile = true
            } else {
              this.authorization_getfile = false
            }
            if (response.data.results.data[0].aut3 === 0) {
              this.authorization_post = true
            } else {
              this.authorization_post = false
            }
            if (response.data.results.data[0].aut4 === 0) {
              this.authorization_patch = true
            } else {
              this.authorization_patch = false
            }
            if (response.data.results.data[0].aut5 === 0) {
              this.authorization_delete = true
            } else {
              this.authorization_delete = false
            }
          } else {
            this.authorization = false
            this.$q.notify({
              message: response.data.results.msg,
              icon: 'close',
              color: 'negative',
              position: 'right',
              timeout: 2500
            })
          }
        } else {
          this.authorization_get = false
          this.authorization_post = false
          this.authorization_getfile = false
          this.authorization_delete = false
          this.authorization_patch = false
          this.$q.notify({
            message: response.data.results.msg,
            icon: 'close',
            color: 'negative',
            position: 'right',
            timeout: 2500
          })
        }
      }).catch(error => {
        this.authorization_get = false
        this.authorization_post = false
        this.authorization_getfile = false
        this.authorization_delete = false
        this.authorization_patch = false
        console.log(error)
      })
    },
    getList () {
      if (this.authorization_get) {
        if (this.$q.localStorage.has('openid')) {
          var openid = this.$q.localStorage.getItem('openid')
          this.$axios.get(this.baseurl + this.pathname, {
            headers: {
              'Content-Type': 'application/json;charset=utf-8'
            },
            params: {
              openid: openid,
              page: this.current,
              max_page: 50,
              date1: this.date1,
              date2: this.date2
            },
            data: {}
          }).then(response => {
            if (response.data.results.code === '200') {
              this.data = response.data.results.data
              this.totlepage = response.data.results.totlepage
            } else {
              this.$q.notify({
                message: response.data.results.msg,
                icon: 'close',
                color: 'negative',
                position: 'right',
                timeout: 2500
              })
            }
          }).catch(error => {
            console.log(error)
            this.$q.notify({
              message: '操作频率过快，请稍后再试',
              icon: 'close',
              color: 'negative',
              position: 'right',
              timeout: 2500
            })
          })
        } else {
          this.$q.notify({
            message: '请先登入后再进行操作',
            icon: 'login',
            color: 'accent',
            position: 'right',
            timeout: 2500
          })
        }
      } else {
        this.$q.notify({
          message: '您没有查询权限，请联系管理员提升权限',
          icon: 'close',
          color: 'dark',
          position: 'right',
          timeout: 2500
        })
      }
    },
    getSelectedString () {
      return this.selected.length === 0 ? '' : `${this.selected.length} record${this.selected.length > 1 ? 's' : ''} selected of ${this.data.length}`
    },
    pageChange () {
      this.getList()
    },
    reFresh () {
      this.current = 1
      this.date1 = ''
      this.date2 = ''
      this.getList()
    },
    DatereFresh () {
      this.current = 1
      this.getList()
    },
    newFormDataCheck () {
      if (this.newFormData.name === '') {
        this.$q.notify({
          message: '用户名不可以为空',
          icon: 'close',
          color: 'negative',
          position: 'right',
          timeout: 2500
        })
      } else {
        this.newFormDataSubmit()
      }
    },
    newFormDataSubmit () {
      if (this.authorization_post) {
        if (this.$q.localStorage.has('openid')) {
          var openid = this.$q.localStorage.getItem('openid')
          this.$axios.post(this.baseurl + this.pathname, { data: this.newFormData }, {
            headers: {
              'Content-Type': 'application/json;charset=utf-8'
            },
            params: {
              openid: openid
            }
          }).then(response => {
            if (response.data.code === '200') {
              this.$q.notify({
                message: response.data.msg,
                icon: 'check',
                color: 'positive',
                position: 'right',
                timeout: 2500
              })
              this.newFormDataCancel()
              this.getList()
            } else {
              this.$q.notify({
                message: response.data.msg,
                icon: 'close',
                color: 'negative',
                position: 'right',
                timeout: 2500
              })
            }
          }).catch(error => {
            console.log(error)
            this.newFormDataCancel()
            this.$q.notify({
              message: '操作频率过快，请稍后再试',
              icon: 'close',
              color: 'negative',
              position: 'right',
              timeout: 2500
            })
          })
        } else {
          this.$q.notify({
            message: '请先登入后再进行操作',
            icon: 'login',
            color: 'accent',
            position: 'right',
            timeout: 2500
          })
        }
      } else {
        this.$q.notify({
          message: '您没有添加数据权限，请联系管理员提升权限',
          icon: 'close',
          color: 'dark',
          position: 'right',
          timeout: 2500
        })
      }
    },
    newFormDataCancel () {
      this.newForm = false
      this.newFormData.name = ''
    },
    editFormDataCheck () {
      if (this.$q.localStorage.has('openid')) {
        if (this.selected.length === 0) {
          this.$q.notify({
            message: '您没有选中任何1条数据',
            icon: 'close',
            color: 'negative',
            position: 'right',
            timeout: 2500
          })
        } else if (this.selected.length > 1) {
          this.$q.notify({
            message: '一次只能修改一条数据',
            icon: 'close',
            color: 'negative',
            position: 'right',
            timeout: 2500
          })
        } else {
          this.$q.localStorage.set('editFormData', this.selected[0])
          var tdata = this.$q.localStorage.getItem('editFormData')
          this.editFormData = tdata
          this.editForm = true
        }
      } else {
        this.$q.notify({
          message: '请先登入后再进行操作',
          icon: 'login',
          color: 'accent',
          position: 'right',
          timeout: 2500
        })
      }
    },
    editFormDataSubmit () {
      var edata = this.$q.localStorage.getItem('editFormData')
      if (this.editFormData.name === edata.name) {
        this.$q.notify({
          message: '不可以提交相同的数据',
          icon: 'close',
          color: 'negative',
          position: 'right',
          timeout: 2500
        })
      } else {
        if (this.authorization_patch) {
          if (this.$q.localStorage.has('openid')) {
            var openid = this.$q.localStorage.getItem('openid')
            this.$axios.patch(this.baseurl + this.pathname, { data: this.editFormData }, {
              headers: {
                'Content-Type': 'application/json;charset=utf-8'
              },
              params: {
                openid: openid
              }
            }).then(response => {
              if (response.data.code === '200') {
                this.$q.notify({
                  message: response.data.msg,
                  icon: 'check',
                  color: 'positive',
                  position: 'right',
                  timeout: 2500
                })
                this.editFormDataCancel()
                this.getList()
              } else {
                this.$q.notify({
                  message: response.data.msg,
                  icon: 'close',
                  color: 'negative',
                  position: 'right',
                  timeout: 2500
                })
              }
            }).catch(error => {
              console.log(error)
              this.editFormDataCancel()
              this.$q.notify({
                message: '操作频率过快，请稍后再试',
                icon: 'close',
                color: 'negative',
                position: 'right',
                timeout: 2500
              })
            })
          } else {
            this.$q.notify({
              message: '请先登入后再进行操作',
              icon: 'login',
              color: 'accent',
              position: 'right',
              timeout: 2500
            })
          }
        } else {
          this.$q.notify({
            message: '您没有修改数据权限，请联系管理员提升权限',
            icon: 'close',
            color: 'dark',
            position: 'right',
            timeout: 2500
          })
        }
      }
    },
    editFormDataCancel () {
      this.editForm = false
      this.$q.localStorage.remove('editFormData')
      this.editFormData = {}
    },
    deleteDataCheck () {
      if (this.$q.localStorage.has('openid')) {
        if (this.selected.length === 0) {
          this.$q.notify({
            message: '您没有选中任何1条数据',
            icon: 'close',
            color: 'negative',
            position: 'right',
            timeout: 2500
          })
        } else if (this.selected.length > 0) {
          this.deleteDialog = true
        } else {
        }
      } else {
        this.$q.notify({
          message: '请先登入后再进行操作',
          icon: 'login',
          color: 'accent',
          position: 'right',
          timeout: 2500
        })
      }
    },
    deleteDataSubmit () {
      if (this.authorization_delete) {
        if (this.$q.localStorage.has('openid')) {
          this.selected.forEach(res => {
            var deletecode = {
              t_code: res.t_code
            }
            this.deleteFormData.push(deletecode)
          })
          var openid = this.$q.localStorage.getItem('openid')
          this.$axios.delete(this.baseurl + this.pathname, {
            headers: {
              'Content-Type': 'application/json;charset=utf-8'
            },
            params: {
              openid: openid
            },
            data: {
              data: this.deleteFormData
            }
          }).then(response => {
            if (response.data.code === '200') {
              this.$q.notify({
                message: response.data.msg,
                icon: 'check',
                color: 'positive',
                position: 'right',
                timeout: 2500
              })
              this.deleteDataCancel()
              this.getList()
            } else {
              this.$q.notify({
                message: response.data.msg,
                icon: 'close',
                color: 'negative',
                position: 'right',
                timeout: 2500
              })
            }
          }).catch(error => {
            console.log(error)
            this.deleteDataCancel()
            this.$q.notify({
              message: '操作频率过快，请稍后再试',
              icon: 'close',
              color: 'negative',
              position: 'right',
              timeout: 2500
            })
          })
        } else {
          this.$q.notify({
            message: '请先登入后再进行操作',
            icon: 'login',
            color: 'accent',
            position: 'right',
            timeout: 2500
          })
        }
      } else {
        this.$q.notify({
          message: '您没有删除数据权限，请联系管理员提升权限',
          icon: 'close',
          color: 'dark',
          position: 'right',
          timeout: 2500
        })
      }
    },
    deleteDataCancel () {
      this.deleteDialog = false
    },
    downloadexample () {
      if (this.authorization_getfile) {
        if (this.$q.localStorage.has('openid')) {
          openURL(this.baseurl + this.pathname + '?openid=' + this.$q.localStorage.getItem('openid') + '&getfile=1')
        } else {
          this.$q.notify({
            message: '请先登入后再进行操作',
            icon: 'login',
            color: 'accent',
            position: 'right',
            timeout: 2500
          })
        }
      } else {
        this.$q.notify({
          message: '您没有下载权限，请联系管理员提升权限',
          icon: 'close',
          color: 'dark',
          position: 'right',
          timeout: 2500
        })
      }
    }
  },
  created () {
    if (this.$q.localStorage.has('authid')) {
      var authid = this.$q.localStorage.getItem('authid')
      this.$axios.get('https://www.56yhz.com/baseurl/', {
        headers: {
          'Content-Type': 'application/json;charset=utf-8'
        },
        params: {
          authid: authid
        },
        data: {}
      }).then(response => {
        if (response.data.code === '200') {
          this.baseurl = response.data.data.baseurl
          if (this.$q.localStorage.has('openid')) {
            this.authCheck()
          } else {}
        } else {
        }
      }).catch(error => {
        console.log(error)
        this.$q.notify({
          message: '操作频率过快，请稍后再试',
          icon: 'close',
          color: 'negative',
          position: 'right',
          timeout: 2500
        })
      })
    } else {
    }
  },
  mounted () {
    if (this.$q.platform.is.electron) {
      this.height = String(this.$q.screen.height - 290) + 'px'
    } else {
      this.height = this.$q.screen.height - 290 + '' + 'px'
    }
  },
  updated () {
  }
}
</script>
