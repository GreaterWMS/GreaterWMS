<template>
  <div>
    <transition appear enter-active-class="animated fadeIn">
      <q-table
        id="table"
        class="my-sticky-header-column-table shadow-24"
        :data="table_list"
        row-key="id"
        :separator="separator"
        :loading="loading"
        :columns="columns"
        hide-bottom
        :pagination.sync="pagination"
        no-data-label="No data"
        no-results-label="No data you want"
        :table-style="{ height: height }"
        flat
        bordered
      >
        <template v-slot:top>
          <q-btn-group push>
            <q-btn
              :label="$t('new')"
              icon="add"
              @click="newForm = true"
            >
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('newtip') }}</q-tooltip>
            </q-btn>
            <q-btn :label="$t('refresh')" icon="refresh" @click="reFresh()">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('refreshtip') }}</q-tooltip>
            </q-btn>
            <q-btn :label="$t('download')" icon="cloud_download" @click="downloadData()">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('downloadtip') }}</q-tooltip>
            </q-btn>
          </q-btn-group>
          <q-space />
          <q-input outlined rounded dense debounce="300" color="primary" v-model="filter" :placeholder="$t('search')" @input="getSearchList()" @keyup.enter="getSearchList()">
            <template v-slot:append>
              <q-icon name="search" @click="getSearchList()"/>
            </template>
          </q-input>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <template v-if="props.row.id === editid">
              <q-td key="staff_name" :props="props">
                <q-input
                  dense
                  outlined
                  square
                  v-model="editFormData.staff_name"
                  :label="$t('staff.view_staff.staff_name')"
                  autofocus
                  :rules="[val => (val && val.length > 0) || error1]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="staff_name" :props="props">{{ props.row.staff_name }}</q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="staff_type" :props="props">
                <q-select
                  dense
                  outlined
                  square
                  v-model="editFormData.staff_type"
                  :options="staff_type_list"
                  transition-show="scale"
                  transition-hide="scale"
                  :label="$t('staff.view_staff.staff_type')"
                  :rules="[val => (val && val.length > 0) || error2]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="staff_type" :props="props">{{ props.row.staff_type }}</q-td>
            </template>
            <q-td key="create_time" :props="props">{{ props.row.create_time }}</q-td>
            <q-td key="update_time" :props="props">{{ props.row.update_time }}</q-td>
            <template v-if="!editMode">
              <q-td key="action" :props="props" style="width: 175px">
                <q-btn
                  round
                  flat
                  push
                  color="purple"
                  :icon="props.row.is_lock ? 'lock' : 'lock_open'"
                  @click="unlock(props.row)"
                >
                  <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                    {{ props.row.is_lock ? $t('staff.view_staff.unlock') : $t('staff.view_staff.lock') }}
                  </q-tooltip>
                </q-btn>
                <q-btn
                  round
                  flat
                  push
                  color="purple"
                  icon="edit"
                  @click="editData(props.row)"
                >
                  <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('edit') }}</q-tooltip>
                </q-btn>
                <q-btn
                  round
                  flat
                  push
                  color="dark"
                  icon="delete"
                  @click="deleteData(props.row.id)"
                >
                  <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('delete') }}</q-tooltip>
                </q-btn>
              </q-td>
            </template>
            <template v-else-if="editMode">
              <template v-if="props.row.id === editid">
                <q-td key="action" :props="props" style="width: 150px">
                  <q-btn round flat push color="secondary" icon="check" @click="editDataSubmit()">
                    <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('confirmedit') }}</q-tooltip>
                  </q-btn>
                  <q-btn round flat push color="red" icon="close" @click="editDataCancel()">
                    <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('canceledit') }}</q-tooltip>
                  </q-btn>
                </q-td>
              </template>
              <template v-else-if="props.row.id !== editid"></template>
            </template>
          </q-tr>
        </template>
      </q-table>
    </transition>
<template>
        <div v-show="max !== 0" class="q-pa-lg flex flex-center">
           <div>{{ total }} </div>
          <q-pagination
            v-model="current"
            color="black"
            :max="max"
            :max-pages="6"
            boundary-links
            @click="getList()"
          />
          <div>
            <input
              v-model="paginationIpt"
              @blur="changePageEnter"
              @keyup.enter="changePageEnter"
              style="width: 60px; text-align: center"
            />
          </div>
        </div>
        <div v-show="max === 0" class="q-pa-lg flex flex-center">
          <q-btn flat push color="dark" :label="$t('no_data')"></q-btn>
        </div>
    </template>
    <q-dialog v-model="newForm">
      <q-card class="shadow-24">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <div>{{ $t('newtip') }}</div>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-amber text-black shadow-4">{{ $t('index.close') }}</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section style="max-height: 325px; width: 400px" class="scroll">
          <q-input
            dense
            outlined
            square
            v-model.trim="newFormData.staff_name"
            :label="$t('staff.view_staff.staff_name')"
            autofocus
            :rules="[val => (val && val.length > 0) || error1]"
            @keyup.enter="newDataSubmit()"
          />
          <q-select
            dense
            outlined
            square
            v-model="newFormData.staff_type"
            :options="staff_type_list"
            transition-show="scale"
            transition-hide="scale"
            :label="$t('staff.view_staff.staff_type')"
            :rules="[val => (val && val.length > 0) || error2]"
            @keyup.enter="newDataSubmit()"
            style="margin-top: 5px"
          />
        </q-card-section>
        <div style="float: right; padding: 15px 15px 15px 0">
          <q-btn color="white" text-color="black" style="margin-right: 25px" @click="newDataCancel()">{{ $t('cancel') }}</q-btn>
          <q-btn color="primary" @click="newDataSubmit()">{{ $t('submit') }}</q-btn>
        </div>
      </q-card>
    </q-dialog>
    <q-dialog v-model="deleteForm">
      <q-card class="shadow-24">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <div>{{ $t('delete') }}</div>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-amber text-black shadow-4">{{ $t('index.close') }}</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section style="max-height: 325px; width: 400px" class="scroll">{{ $t('deletetip') }}</q-card-section>
        <div style="float: right; padding: 15px 15px 15px 0">
          <q-btn color="white" text-color="black" style="margin-right: 25px" @click="deleteDataCancel()">{{ $t('cancel') }}</q-btn>
          <q-btn color="primary" @click="deleteDataSubmit()">{{ $t('submit') }}</q-btn>
        </div>
      </q-card>
    </q-dialog>
  </div>
</template>
<router-view />

<script>
import { getauth, postauth, putauth, deleteauth, getfile } from 'boot/axios_request'
import { date, exportFile, LocalStorage } from 'quasar'

export default {
  name: 'Pagestafflist',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'staff/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      staff_type_list: [],
      columns: [
        { name: 'staff_name', required: true, label: this.$t('staff.view_staff.staff_name'), align: 'left', field: 'staff_name' },
        { name: 'staff_type', label: this.$t('staff.view_staff.staff_type'), field: 'staff_type', align: 'center' },
        { name: 'create_time', label: this.$t('createtime'), field: 'create_time', align: 'center' },
        { name: 'update_time', label: this.$t('updatetime'), field: 'update_time', align: 'center' },
        { name: 'action', label: this.$t('action'), align: 'right' }
      ],
      pagination: {
        page: 1,
        rowsPerPage: '30'
      },
      newForm: false,
      newFormData: {
        staff_name: '',
        staff_type: '',
        check_code: ''
      },
      editid: 0,
      editFormData: {},
      editMode: false,
      deleteForm: false,
      deleteid: 0,
      filter: '',
      error1: this.$t('staff.view_staff.error1'),
      error2: this.$t('staff.view_staff.error2'),
      current: 1,
      max: 0,
      total: 0,
      paginationIpt: 1
    }
  },
  methods: {
    getList () {
      var _this = this
      getauth(_this.pathname + '?page=' + '' + _this.current, {})
        .then(res => {
          _this.table_list = res.results
          _this.total = res.count
          if (res.count === 0) {
            _this.max = 0
          } else {
            if (Math.ceil(res.count / 30) === 1) {
              _this.max = 0
            } else {
              _this.max = Math.ceil(res.count / 30)
            }
          }
          if (LocalStorage.getItem('lang') === 'zh-hans') {
            _this.table_list.forEach((item, index) => {
              if (item.staff_type === 'Admin') {
                item.staff_type = '管理员'
              } else if (item.staff_type === 'Customer') {
                item.staff_type = '客户'
              } else if (item.staff_type === 'Supplier') {
                item.staff_type = '供应商'
              } else if (item.staff_type === 'Manager') {
                item.staff_type = '经理'
              } else if (item.staff_type === 'Supervisor') {
                item.staff_type = '主管'
              } else if (item.staff_type === 'Inbound') {
                item.staff_type = '收货组'
              } else if (item.staff_type === 'Outbound') {
                item.staff_type = '发货组'
              } else if (item.staff_type === 'StockControl') {
                item.staff_type = '库存管理'
              }
            })
          }
          _this.pathname_previous = res.previous
          _this.pathname_next = res.next
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    changePageEnter (e) {
      if (Number(this.paginationIpt) < 1) {
        this.current = 1
        this.paginationIpt = 1
      } else if (Number(this.paginationIpt) > this.max) {
        this.current = this.max
        this.paginationIpt = this.max
      } else {
        this.current = Number(this.paginationIpt)
      }
      this.getList()
    },
    getSearchList () {
      var _this = this
      _this.filter = _this.filter.replace(/\s+/g, '')
      _this.current = 1
      _this.paginationIpt = 1
      getauth(_this.pathname + '?staff_name__icontains=' + _this.filter + '&page=' + '' + _this.current, {})
        .then(res => {
          _this.table_list = res.results
          _this.total = res.count
          if (res.count === 0) {
            _this.max = 0
          } else {
            if (Math.ceil(res.count / 30) === 1) {
              _this.max = 0
            } else {
              _this.max = Math.ceil(res.count / 30)
            }
          }
          if (LocalStorage.getItem('lang') === 'zh-hans') {
            _this.table_list.forEach((item, index) => {
              if (item.staff_type === 'Admin') {
                item.staff_type = '管理员'
              } else if (item.staff_type === 'Customer') {
                item.staff_type = '客户'
              } else if (item.staff_type === 'Supplier') {
                item.staff_type = '供应商'
              } else if (item.staff_type === 'Manager') {
                item.staff_type = '经理'
              } else if (item.staff_type === 'Supervisor') {
                item.staff_type = '主管'
              } else if (item.staff_type === 'Inbound') {
                item.staff_type = '收货组'
              } else if (item.staff_type === 'Outbound') {
                item.staff_type = '发货组'
              } else if (item.staff_type === 'StockControl') {
                item.staff_type = '库存管理'
              }
            })
          }
          _this.pathname_previous = res.previous
          _this.pathname_next = res.next
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    getListPrevious () {
      var _this = this
      getauth(_this.pathname_previous, {})
        .then(res => {
          _this.table_list = res.results
          if (LocalStorage.getItem('lang') === 'zh-hans') {
            _this.table_list.forEach((item, index) => {
              if (item.staff_type === 'Admin') {
                item.staff_type = '管理员'
              } else if (item.staff_type === 'Customer') {
                item.staff_type = '客户'
              } else if (item.staff_type === 'Supplier') {
                item.staff_type = '供应商'
              } else if (item.staff_type === 'Manager') {
                item.staff_type = '经理'
              } else if (item.staff_type === 'Supervisor') {
                item.staff_type = '主管'
              } else if (item.staff_type === 'Inbound') {
                item.staff_type = '收货组'
              } else if (item.staff_type === 'Outbound') {
                item.staff_type = '发货组'
              } else if (item.staff_type === 'StockControl') {
                item.staff_type = '库存管理'
              }
            })
          }
          _this.pathname_previous = res.previous
          _this.pathname_next = res.next
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    getListNext () {
      var _this = this
      getauth(_this.pathname_next, {})
        .then(res => {
          _this.table_list = res.results
          if (LocalStorage.getItem('lang') === 'zh-hans') {
            _this.table_list.forEach((item, index) => {
              if (item.staff_type === 'Admin') {
                item.staff_type = '管理员'
              } else if (item.staff_type === 'Customer') {
                item.staff_type = '客户'
              } else if (item.staff_type === 'Supplier') {
                item.staff_type = '供应商'
              } else if (item.staff_type === 'Manager') {
                item.staff_type = '经理'
              } else if (item.staff_type === 'Supervisor') {
                item.staff_type = '主管'
              } else if (item.staff_type === 'Inbound') {
                item.staff_type = '收货组'
              } else if (item.staff_type === 'Outbound') {
                item.staff_type = '发货组'
              } else if (item.staff_type === 'StockControl') {
                item.staff_type = '库存管理'
              }
            })
          }
          _this.pathname_previous = res.previous
          _this.pathname_next = res.next
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    reFresh () {
      var _this = this
      _this.getList()
    },
    unlock (val) {
      putauth(this.pathname + val.id + '/', {
        is_lock: !val.is_lock,
        staff_name: val.staff_name,
        staff_type: val.staff_type
      })
        .then(res => {
          this.getList()
          let message = 'Success unlocked'
          if (!val.is_lock) {
            message = 'Success locked'
          }
          this.$q.notify({
            message: message,
            icon: 'check',
            color: 'green'
          })
        })
        .catch(err => {
          this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    RandomCheckCode () {
      var _this = this
      var code = ''
      var codeLength = 4
      var random = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
      for (var i = 0; i < codeLength; i++) {
        var index = Math.floor(Math.random() * 9)
        code += random[index]
      }
      _this.newFormData.check_code = code
    },
    newDataSubmit () {
      var _this = this
      var staffs = []
      _this.newFormData.is_lock = false
      _this.table_list.forEach(i => {
        staffs.push(i.staff_name)
      })
      if (staffs.indexOf(_this.newFormData.staff_name) === -1 && _this.newFormData.staff_name.length !== 0 && _this.newFormData.staff_type) {
        _this.RandomCheckCode()
        if (_this.newFormData.staff_type === '经理') {
          _this.newFormData.staff_type = 'Manager'
        } else if (_this.newFormData.staff_type === '主管') {
          _this.newFormData.staff_type = 'Supervisor'
        } else if (_this.newFormData.staff_type === '收货组') {
          _this.newFormData.staff_type = 'Inbound'
        } else if (_this.newFormData.staff_type === '发货组') {
          _this.newFormData.staff_type = 'Outbound'
        } else if (_this.newFormData.staff_type === '库存控制') {
          _this.newFormData.staff_type = 'StockControl'
        } else if (_this.newFormData.staff_type === '客户') {
          _this.newFormData.staff_type = 'Customer'
        } else if (_this.newFormData.staff_type === '供应商') {
          _this.newFormData.staff_type = 'Supplier'
        }
        postauth(_this.pathname, _this.newFormData)
          .then(res => {
            _this.getList()
            _this.newDataCancel()
            _this.$q.notify({
              message: 'Success Create',
              icon: 'check',
              color: 'green'
            })
          })
          .catch(err => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            })
          })
      } else if (staffs.indexOf(_this.newFormData.staff_name) !== -1) {
        _this.$q.notify({
          message: _this.$t('notice.userererror'),
          icon: 'close',
          color: 'negative'
        })
      } else if (_this.newFormData.staff_name.length === 0) {
        _this.$q.notify({
          message: _this.$t('staff.view_staff.error1'),
          icon: 'close',
          color: 'negative'
        })
      } else if (!_this.newFormData.staff_type) {
        _this.$q.notify({
          message: _this.$t('staff.view_staff.error2'),
          icon: 'close',
          color: 'negative'
        })
      }
    },
    newDataCancel () {
      var _this = this
      _this.newForm = false
      _this.newFormData = {
        staff_name: '',
        staff_type: ''
      }
    },
    editData (e) {
      var _this = this
      _this.editMode = true
      _this.editid = e.id
      _this.editFormData = {
        staff_name: e.staff_name,
        staff_type: e.staff_type
      }
    },
    editDataSubmit () {
      var _this = this
      if (_this.editFormData.staff_type === '经理') {
        _this.editFormData.staff_type = 'Manager'
      } else if (_this.editFormData.staff_type === '主管') {
        _this.editFormData.staff_type = 'Supervisor'
      } else if (_this.editFormData.staff_type === '收货组') {
        _this.editFormData.staff_type = 'Inbound'
      } else if (_this.editFormData.staff_type === '发货组') {
        _this.editFormData.staff_type = 'Outbound'
      } else if (_this.editFormData.staff_type === '库存控制') {
        _this.editFormData.staff_type = 'StockControl'
      } else if (_this.editFormData.staff_type === '客户') {
        _this.editFormData.staff_type = 'Customer'
      } else if (_this.editFormData.staff_type === '供应商') {
        _this.editFormData.staff_type = 'Supplier'
      }
      putauth(_this.pathname + _this.editid + '/', _this.editFormData)
        .then(res => {
          _this.editDataCancel()
          _this.getList()
          _this.$q.notify({
            message: 'Success Edit Data',
            icon: 'check',
            color: 'green'
          })
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    editDataCancel () {
      var _this = this
      _this.editMode = false
      _this.editid = 0
      _this.editFormData = {
        staff_name: '',
        staff_type: ''
      }
    },
    deleteData (e) {
      var _this = this
      _this.deleteForm = true
      _this.deleteid = e
    },
    deleteDataSubmit () {
      var _this = this
      deleteauth(_this.pathname + _this.deleteid + '/')
        .then(res => {
          _this.deleteDataCancel()
          _this.getList()
          _this.$q.notify({
            message: 'Success Edit Data',
            icon: 'check',
            color: 'green'
          })
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    deleteDataCancel () {
      var _this = this
      _this.deleteForm = false
      _this.deleteid = 0
    },
    downloadData () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getfile(_this.pathname + 'file/?lang=' + LocalStorage.getItem('lang')).then(res => {
          var timeStamp = Date.now()
          var formattedString = date.formatDate(timeStamp, 'YYYYMMDDHHmmssSSS')
          const status = exportFile(_this.pathname + formattedString + '.csv', '\uFEFF' + res.data, 'text/csv')
          if (status !== true) {
            this.$q.notify({
              message: 'Browser denied file download...',
              color: 'negative',
              icon: 'warning'
            })
          }
        })
      } else {
        _this.$q.notify({
          message: _this.$t('notice.loginerror'),
          color: 'negative',
          icon: 'warning'
        })
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
      _this.getList()
    } else {
      _this.authin = '0'
    }
  },
  mounted () {
    var _this = this
    if (_this.$q.platform.is.electron) {
      _this.height = String(_this.$q.screen.height - 290) + 'px'
    } else {
      _this.height = _this.$q.screen.height - 290 + '' + 'px'
    }
    if (LocalStorage.getItem('lang') === 'zh-hans') {
      _this.staff_type_list = ['经理', '主管', '收货组', '发货组', '库存控制', '客户', '供应商']
    } else {
      _this.staff_type_list = ['Manager', 'Supervisor', 'Inbount', 'Outbound', 'StockControl', 'Customer', 'Supplier']
    }
  },
  updated () {
  },
  destroyed () {
  }
}
</script>
