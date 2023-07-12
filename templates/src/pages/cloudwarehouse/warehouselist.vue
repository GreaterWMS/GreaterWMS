<template>
  <div>
    <transition appear enter-active-class="animated fadeIn">
    <q-table
      class="my-sticky-header-table shadow-24"
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
           <q-btn :label="$t('refresh')" icon="refresh" @click="reFresh()">
             <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
               {{ $t('refreshtip') }}
             </q-tooltip>
           </q-btn>
         </q-btn-group>
         <q-space />
          <q-input outlined rounded dense debounce="300" color="primary" v-model="filter" :placeholder="$t('warehouse.view_warehouse.city_search')" @input="getSearchList()" @keyup.enter="getSearchList()">
            <template v-slot:append>
              <q-icon name="search" @click="getSearchList()" />
            </template>
          </q-input>
       </template>
       <template v-slot:body="props">
         <q-tr :props="props">
             <q-td key="warehouse_name" :props="props">
               {{ props.row.warehouse_name }}
             </q-td>
             <q-td key="warehouse_city" :props="props">
               {{ props.row.warehouse_city }}
             </q-td>
             <q-td key="warehouse_address" :props="props">
               {{ props.row.warehouse_address }}
             </q-td>
             <q-td key="warehouse_contact" :props="props">
               {{ props.row.warehouse_contact }}
             </q-td>
             <q-td key="warehouse_manager" :props="props">
               {{ props.row.warehouse_manager }}
             </q-td>
             <q-td key="square_measure" :props="props">
               {{ props.row.square_measure }}
             </q-td>
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
  </div>
</template>
  <router-view />

<script>
import { postauth, putauth, deleteauth } from 'boot/axios_request'
import { LocalStorage } from 'quasar'
import axios from 'axios'

export default {
  name: 'Pagewarehouselist',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'https://po.56yhz.com/warehouse/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      columns: [
        { name: 'warehouse_name', required: true, label: this.$t('warehouse.view_warehouse.warehouse_name'), align: 'left', field: 'warehouse_name' },
        { name: 'warehouse_city', label: this.$t('warehouse.view_warehouse.warehouse_city'), field: 'warehouse_city', align: 'center' },
        { name: 'warehouse_address', label: this.$t('warehouse.view_warehouse.warehouse_address'), field: 'warehouse_address', align: 'center' },
        { name: 'warehouse_contact', label: this.$t('warehouse.view_warehouse.warehouse_contact'), field: 'warehouse_contact', align: 'center' },
        { name: 'warehouse_manager', label: this.$t('warehouse.view_warehouse.warehouse_manager'), field: 'warehouse_manager', align: 'center' },
        { name: 'square_measure', label: this.$t('warehouse.view_warehouse.square_measure'), field: 'square_measure', align: 'center' },
      ],
      filter: '',
      pagination: {
        page: 1,
        rowsPerPage: '30'
      },
      newForm: false,
      newFormData: {
        warehouse_name: '',
        warehouse_city: '',
        warehouse_address: '',
        warehouse_contact: '',
        warehouse_manager: '',
        creater: ''
      },
      editid: 0,
      editFormData: {},
      editMode: false,
      deleteForm: false,
      deleteid: 0,
      error1: this.$t('warehouse.view_warehouseset.error1'),
      error2: this.$t('warehouse.view_warehouseset.error2'),
      error3: this.$t('warehouse.view_warehouseset.error3'),
      error4: this.$t('warehouse.view_warehouseset.error4'),
      error5: this.$t('warehouse.view_warehouseset.error5'),
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
        axios.get(_this.pathname + '?page=' + '' + _this.current.toString(), {
        }).then(res => {
          _this.table_list = res.data.results
          _this.total = res.data.count
          if (res.data.count === 0) {
            _this.max = 0
          } else {
            if (Math.ceil(res.data.count / 30) === 1) {
              _this.max = 0
            } else {
              _this.max = Math.ceil(res.data.count / 30)
            }
          }
          _this.pathname_previous = res.data.previous
          _this.pathname_next = res.data.next
        }).catch(err => {
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
    getListPrevious () {
      var _this = this
      if (LocalStorage.has('auth')) {
        axios.get(_this.pathname_previous, {
        }).then(res => {
          _this.table_list = res.data.results
          _this.pathname_previous = res.data.previous
          _this.pathname_next = res.data.next
        }).catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
      }
    },
    getListNext () {
      var _this = this
      if (LocalStorage.has('auth')) {
        axios.get(_this.pathname_next, {
        }).then(res => {
          _this.table_list = res.data.results
          _this.pathname_previous = res.data.previous
          _this.pathname_next = res.data.next
        }).catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
      } else {
      }
    },
    getSearchList () {
      var _this = this
      if (_this.$q.localStorage.has('auth')) {
        _this.current = 1
        _this.paginationIpt = 1
        axios.get(_this.pathname + '?warehouse_city__icontains=' + _this.filter + '&page=' + '' + _this.current.toString(), {})
          .then(res => {
            _this.table_list = res.data.results
            _this.total = res.data.count
            if (res.data.count === 0) {
              _this.max = 0
            } else {
              if (Math.ceil(res.data.count / 30) === 1) {
                _this.max = 0
              } else {
                _this.max = Math.ceil(res.data.count / 30)
              }
            }
            _this.pathname_previous = res.data.previous
            _this.pathname_next = res.data.next
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
    reFresh () {
      var _this = this
      _this.current = 1
      _this.getList()
    },
    newFormCheck () {
      var _this = this
      if (_this.table_list.length >= 1) {
        _this.$q.notify({
          message: 'You Just Can Create 1 Line Data',
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.newForm = true
      }
    },
    newDataSubmit () {
      var _this = this
      var warehousesets = []
      _this.table_list.forEach(i => {
        warehousesets.push(i.warehouse_name)
      })
      if (warehousesets.indexOf(_this.newFormData.warehouse_name) === -1 && _this.newFormData.warehouse_name.length !== 0) {
        _this.newFormData.creater = _this.login_name
        postauth(_this.pathname, _this.newFormData).then(res => {
          _this.getList()
          _this.newDataCancel()
          _this.$q.notify({
            message: 'Success Create',
            icon: 'check',
            color: 'green'
          })
        }).catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
      } else {
        _this.newFormData.creater = _this.login_name
        postauth(_this.pathname, _this.newFormData).then(res => {
          _this.getList()
          _this.newDataCancel()
          _this.$q.notify({
            message: '',
            icon: 'close',
            color: 'negative'
          })
        }).catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
      }
      warehousesets = []
    },
    newDataCancel () {
      var _this = this
      _this.newForm = false
      _this.newFormData = {
        warehouse_name: '',
        warehouse_city: '',
        warehouse_address: '',
        warehouse_contact: '',
        warehouse_manager: '',
        creater: ''
      }
    },
    editData (e) {
      var _this = this
      _this.editMode = true
      _this.editid = e.id
      _this.editFormData = {
        warehouse_name: e.warehouse_name,
        warehouse_city: e.warehouse_city,
        warehouse_address: e.warehouse_address,
        warehouse_contact: e.warehouse_contact,
        warehouse_manager: e.warehouse_manager,
        creater: _this.login_name
      }
    },
    editDataSubmit () {
      var _this = this
      putauth(_this.pathname + _this.editid + '/', _this.editFormData).then(res => {
        _this.editDataCancel()
        _this.getList()
        _this.$q.notify({
          message: 'Success Edit Data',
          icon: 'check',
          color: 'green'
        })
      }).catch(err => {
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
        warehouse_name: '',
        warehouse_city: '',
        warehouse_address: '',
        warehouse_contact: '',
        warehouse_manager: '',
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
      deleteauth(_this.pathname + _this.deleteid + '/').then(res => {
        _this.deleteDataCancel()
        _this.getList()
        _this.$q.notify({
          message: 'Success Edit Data',
          icon: 'check',
          color: 'green'
        })
      }).catch(err => {
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
  updated () {
  },
  destroyed () {
  }
}
</script>
