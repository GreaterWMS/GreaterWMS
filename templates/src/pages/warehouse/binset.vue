<template>
  <div>
    <transition appear enter-active-class="animated fadeIn">
      <q-table
        class="my-sticky-header-column-table shadow-24"
        :data="table_list"
        row-key="id"
        :separator="separator"
        :loading="loading"
        :filter="filter"
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
            <q-btn :label="$t('new')" icon="add" @click="newForm = true">
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
              <q-icon name="search" @click="getSearchList()" />
            </template>
          </q-input>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td key="bin_name" :props="props">{{ props.row.bin_name }}</q-td>
            <template v-if="props.row.id === editid">
              <q-td key="bin_size" :props="props">
                <q-select
                  dense
                  outlined
                  square
                  v-model="editFormData.bin_size"
                  :options="bin_size_list"
                  transition-show="scale"
                  transition-hide="scale"
                  :label="$t('warehouse.view_binset.bin_size')"
                  :rules="[val => (val && val.length > 0) || error2]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="bin_size" :props="props">{{ props.row.bin_size }}</q-td>
            </template>
            <q-td key="bin_property" :props="props">{{ props.row.bin_property }}</q-td>
            <q-td key="empty_label" :props="props">{{ props.row.empty_label }}</q-td>
            <q-td key="creater" :props="props">{{ props.row.creater }}</q-td>
            <q-td key="create_time" :props="props">{{ props.row.create_time }}</q-td>
            <q-td key="update_time" :props="props">{{ props.row.update_time }}</q-td>
            <template v-if="!editMode">
              <q-td key="action" :props="props" style="width: 100px">
                <q-btn
                  round
                  flat
                  push
                  color="info"
                  icon="print"
                  @click="viewData(props.row)"
                >
                  <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('warehouse.printbin') }}</q-tooltip>
                </q-btn>
                <q-btn round flat push color="purple" icon="edit" @click="editData(props.row)">
                  <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('edit') }}</q-tooltip>
                </q-btn>
                <q-btn round flat push color="dark" icon="delete" @click="deleteData(props.row.id)">
                  <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('delete') }}</q-tooltip>
                </q-btn>
              </q-td>
            </template>
            <template v-else-if="editMode">
              <template v-if="props.row.id === editid">
                <q-td key="action" :props="props" style="width: 100px">
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
            v-model="newFormData.bin_name"
            :label="$t('warehouse.view_binset.bin_name')"
            autofocus
            :rules="[val => (val && val.length > 0) || error1]"
            @keyup.enter="newDataSubmit()"
          />
          <q-select
            dense
            outlined
            square
            v-model="newFormData.bin_size"
            :options="bin_size_list"
            transition-show="scale"
            transition-hide="scale"
            :label="$t('warehouse.view_binset.bin_size')"
            :rules="[val => (val && val.length > 0) || error2]"
          />
          <q-select
            dense
            outlined
            square
            v-model="newFormData.bin_property"
            :options="bin_property_list"
            transition-show="scale"
            transition-hide="scale"
            :label="$t('warehouse.view_binset.bin_property')"
            :rules="[val => (val && val.length > 0) || error3]"
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
    <q-dialog v-model="viewForm">
      <div id="printMe" style="width: 400px;height:280px;background-color: white">
        <q-card-section>
          <div class="row" style="height: 50px">
            <div class="col-3"><img src="statics/goods/logo.png" style="width: 60px;height: 50px;margin-top: 5px;margin-left: 5px" /></div>
            <div class="col-9" style="height: 50px;float: contour;margin-top: 10px">
              <p style="font-size: 20px;font-weight: 550">{{ $t('warehouse.view_binset.bin_name') + ':' + bin_name }}</p>
            </div>
          </div>
          <hr />
          <div class="row">
            <div class="col-8" style="margin-top: 30px;padding-left: 3%">
              <p style="font-size: 20px;font-weight: 550">{{ $t('warehouse.view_binset.bin_property') + ':' }}</p>
              <p style="font-size: 20px;font-weight: 550">{{ bin_property }}</p>
            </div>
            <div class="col-4" style="margin-top: 25px;"><img :src="bar_code" style="width: 70%;margin-left: 23px" /></div>
          </div>
        </q-card-section>
      </div>
      <div style="float: right; padding: 15px 15px 15px 0"><q-btn color="primary" icon="print" v-print="printObj">print</q-btn></div>
    </q-dialog>
  </div>
</template>
<router-view />

<script>
import { date, exportFile, LocalStorage } from 'quasar'
import { getauth, postauth, putauth, deleteauth, getfile } from 'boot/axios_request'

export default {
  name: 'Pagebinset',
  data () {
    return {
      bin_name: '',
      bin_property: '',
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'binset/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      bin_size_list: [],
      bin_property_list: [],
      viewForm: false,
      printObj: {
        id: 'printMe',
        popTitle: this.$t('inbound.asn')
      },
      columns: [
        { name: 'bin_name', required: true, label: this.$t('warehouse.view_binset.bin_name'), align: 'left', field: 'bin_name' },
        { name: 'bin_size', label: this.$t('warehouse.view_binset.bin_size'), field: 'bin_size', align: 'center' },
        { name: 'bin_property', label: this.$t('warehouse.view_binset.bin_property'), field: 'bin_property', align: 'center' },
        { name: 'empty_label', label: this.$t('warehouse.view_binset.empty_label'), field: 'empty_label', align: 'center' },
        { name: 'creater', label: this.$t('creater'), field: 'creater', align: 'center' },
        { name: 'create_time', label: this.$t('createtime'), field: 'create_time', align: 'center' },
        { name: 'update_time', label: this.$t('updatetime'), field: 'update_time', align: 'center' },
        { name: 'action', label: this.$t('action'), align: 'right' }
      ],
      filter: '',
      pagination: {
        page: 1,
        rowsPerPage: '30'
      },
      newForm: false,
      newFormData: {
        bin_name: '',
        bin_size: '',
        bin_property: '',
        creater: ''
      },
      editid: 0,
      editFormData: {},
      editMode: false,
      deleteForm: false,
      deleteid: 0,
      bar_code: '',
      error1: this.$t('warehouse.view_binset.error1'),
      error2: this.$t('warehouse.view_binset.error2'),
      error3: this.$t('warehouse.view_binset.error3'),
      current: 1,
      max: 0,
      total: 0,
      paginationIpt: 1
    }
  },
  methods: {
    getList () {
      var _this = this
      if (LocalStorage.has('auth')) {
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
                if (item.bin_property === 'Damage') {
                  item.bin_property = '破损'
                } else if (item.bin_property === 'Inspection') {
                  item.bin_property = '质检'
                } else if (item.bin_property === 'Holding') {
                  item.bin_property = '锁货'
                } else if (item.bin_property === 'Normal') {
                  item.bin_property = '正常库位'
                }
                if (!item.empty_label) {
                  item.empty_label = '否'
                } else if (item.empty_label) {
                  item.empty_label = '是'
                }
              })
            }
            _this.bin_property_list = res.bin_property_list
            if (LocalStorage.getItem('lang') === 'zh-hans') {
              _this.bin_property_list.forEach((item, index) => {
                console.log(item)
                if (item === 'Damage') {
                  _this.bin_property_list[index] = '破损'
                } else if (item === 'Inspection') {
                  _this.bin_property_list[index] = '质检'
                } else if (item === 'Holding') {
                  _this.bin_property_list[index] = '锁货'
                } else if (item === 'Normal') {
                  _this.bin_property_list[index] = '正常库位'
                }
              })
            }
            _this.bin_size_list = res.bin_size_list
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
      }
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
      if (LocalStorage.has('auth')) {
        _this.current = 1
        _this.paginationIpt = 1
        getauth(_this.pathname + '?bin_name__icontains=' + _this.filter + '&page=' + '' + _this.current, {})
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
                if (item.bin_property === 'Damage') {
                  item.bin_property = '破损'
                } else if (item.bin_property === 'Inspection') {
                  item.bin_property = '质检'
                } else if (item.bin_property === 'Holding') {
                  item.bin_property = '锁货'
                } else if (item.bin_property === 'Normal') {
                  item.bin_property = '正常库位'
                }
                if (!item.empty_label) {
                  item.empty_label = '否'
                } else if (item.empty_label) {
                  item.empty_label = '是'
                }
              })
            }

            _this.bin_property_list = res.bin_property_list
            if (LocalStorage.getItem('lang') === 'zh-hans') {
              _this.bin_property_list.forEach((item, index) => {
                if (item === 'Damage') {
                  _this.bin_property_list[index] = '破损'
                } else if (item === 'Inspection') {
                  _this.bin_property_list[index] = '质检'
                } else if (item === 'Holding') {
                  _this.bin_property_list[index] = '锁货'
                } else if (item === 'Normal') {
                  _this.bin_property_list[index] = '正常库位'
                }
              })
            }
            _this.bin_size_list = res.bin_size_list
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
      } else {
      }
    },
    getListPrevious () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname_previous, {})
          .then(res => {
            _this.table_list = res.results
            if (LocalStorage.getItem('lang') === 'zh-hans') {
              _this.table_list.forEach((item, index) => {
                if (item.bin_property === 'Damage') {
                  item.bin_property = '破损'
                } else if (item.bin_property === 'Inspection') {
                  item.bin_property = '质检'
                } else if (item.bin_property === 'Holding') {
                  item.bin_property = '锁货'
                } else if (item.bin_property === 'Normal') {
                  item.bin_property = '正常库位'
                }
                if (!item.empty_label) {
                  item.empty_label = '否'
                } else if (item.empty_label) {
                  item.empty_label = '是'
                }
              })
            }
            _this.bin_property_list = res.bin_property_list
            _this.bin_property_list.forEach((item, index) => {
              if (item === 'Damage') {
                _this.bin_property_list[index] = '破损'
              } else if (item === 'Inspection') {
                _this.bin_property_list[index] = '质检'
              } else if (item === 'Holding') {
                _this.bin_property_list[index] = '锁货'
              } else if (item === 'Normal') {
                _this.bin_property_list[index] = '正常库位'
              }
            })
            _this.bin_size_list = res.bin_size_list
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
      } else {
      }
    },
    getListNext () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname_next, {})
          .then(res => {
            _this.table_list = res.results
            if (LocalStorage.getItem('lang') === 'zh-hans') {
              _this.table_list.forEach((item, index) => {
                if (item.bin_property === 'Damage') {
                  item.bin_property = '破损'
                } else if (item.bin_property === 'Inspection') {
                  item.bin_property = '质检'
                } else if (item.bin_property === 'Holding') {
                  item.bin_property = '锁货'
                } else if (item.bin_property === 'Normal') {
                  item.bin_property = '正常库位'
                }
                if (!item.empty_label) {
                  item.empty_label = '否'
                } else if (item.empty_label) {
                  item.empty_label = '是'
                }
              })
            }
            _this.bin_property_list = res.bin_property_list
            if (LocalStorage.getItem('lang') === 'zh-hans') {
              _this.bin_property_list.forEach((item, index) => {
                if (item === 'Damage') {
                  _this.bin_property_list[index] = '破损'
                } else if (item === 'Inspection') {
                  _this.bin_property_list[index] = '质检'
                } else if (item === 'Holding') {
                  _this.bin_property_list[index] = '锁货'
                } else if (item === 'Normal') {
                  _this.bin_property_list[index] = '正常库位'
                }
              })
            }
            _this.bin_size_list = res.bin_size_list
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
      } else {
      }
    },
    reFresh () {
      var _this = this
      _this.getList()
    },
    newDataSubmit () {
      var _this = this
      var binsets = []
      _this.table_list.forEach(i => {
        binsets.push(i.bin_name)
      })
      if (binsets.indexOf(_this.newFormData.bin_name) === -1 && _this.newFormData.bin_name.length !== 0) {
        _this.newFormData.creater = _this.login_name
        if (LocalStorage.getItem('lang') === 'zh-hans') {
          if (_this.newFormData.bin_property === '破损') {
            _this.newFormData.bin_property = 'Damage'
          } else if (_this.newFormData.bin_property === '质检') {
            _this.newFormData.bin_property = 'Inspection'
          } else if (_this.newFormData.bin_property === '锁货') {
            _this.newFormData.bin_property = 'Holding'
          } else if (_this.newFormData.bin_property === '正常库位') {
            _this.newFormData.bin_property = 'Normal'
          }
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
      } else if (binsets.indexOf(_this.newFormData.bin_name) !== -1) {
        _this.$q.notify({
          message: _this.$t('notice.warehouseerror.binseterror'),
          icon: 'close',
          color: 'negative'
        })
      } else if (_this.newFormData.bin_name.length === 0) {
        _this.$q.notify({
          message: _this.$t('warehouse.view_binset.error1'),
          icon: 'close',
          color: 'negative'
        })
      }
      binsets = []
    },
    newDataCancel () {
      var _this = this
      _this.newForm = false
      _this.newFormData = {
        bin_name: '',
        bin_size: '',
        bin_property: '',
        creater: ''
      }
    },
    editData (e) {
      var _this = this
      _this.editMode = true
      _this.editid = e.id
      _this.editFormData = {
        bin_name: e.bin_name,
        bin_size: e.bin_size,
        bin_property: e.bin_property,
        creater: _this.login_name
      }
    },
    editDataSubmit () {
      var _this = this
      if (_this.editFormData.bin_name) {
        if (LocalStorage.getItem('lang') === 'zh-hans') {
          if (_this.editFormData.bin_property === '破损') {
            _this.editFormData.bin_property = 'Damage'
          } else if (_this.editFormData.bin_property === '质检') {
            _this.editFormData.bin_property = 'Inspection'
          } else if (_this.editFormData.bin_property === '锁货') {
            _this.editFormData.bin_property = 'Holding'
          } else if (_this.editFormData.bin_property === '正常库位') {
            _this.editFormData.bin_property = 'Normal'
          }
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
      } else {
        _this.$q.notify({
          message: 'Content Cannot Be Empty',
          icon: 'close',
          color: 'negative'
        })
      }
    },
    editDataCancel () {
      var _this = this
      _this.editMode = false
      _this.editid = 0
      _this.editFormData = {
        bin_name: '',
        bin_size: '',
        bin_property: '',
        empty_label: '',
        creater: ''
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
            _this.$q.notify({
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
    },
    viewData (e) {
      var _this = this
      var QRCode = require('qrcode')
      QRCode.toDataURL(e.bar_code, [
        {
          errorCorrectionLevel: 'H',
          mode: 'byte',
          version: '2',
          type: 'image/jpeg'
        }
      ])
        .then(url => {
          _this.bin_name = e.bin_name
          _this.bin_property = e.bin_property
          _this.bar_code = url
        })
        .catch(err => {
          console.error(err)
        })
      _this.viewForm = true
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
  },
  updated () {},
  destroyed () {}
}
</script>
