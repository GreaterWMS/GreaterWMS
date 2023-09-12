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
           <q-input outlined rounded dense debounce="300" color="primary" v-model="filter" :placeholder="$t('search')" @input="getSearchList()" @keyup.enter="getSearchList()">
             <template v-slot:append>
               <q-icon name="search" @click="getSearchList()"/>
             </template>
           </q-input>
         </template>
         <template v-slot:body="props">
           <q-tr :props="props">
               <q-td key="staff_name" :props="props">
                 {{ props.row.staff_name }}
               </q-td>
               <q-td key="staff_type" :props="props">
                 {{ props.row.staff_type }}
               </q-td>
             <q-td key="check_code" :props="props">
               {{ props.row.check_code }}
             </q-td>
             <q-td key="create_time" :props="props">
               {{ props.row.create_time }}
             </q-td>
             <q-td key="update_time" :props="props">
               {{ props.row.update_time }}
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
import { getauth } from 'boot/axios_request'
import { LocalStorage } from 'quasar'

export default {
  name: 'Pagestafflistcheckcode',
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
      staff_type_list: ['Manager', 'Inbound', 'Outbound', 'Supervisor', 'StockControl', 'Customer', 'Supplier'],
      columns: [
        { name: 'staff_name', required: true, label: this.$t('staff.view_staff.staff_name'), align: 'left', field: 'staff_name' },
        { name: 'staff_type', label: this.$t('staff.view_staff.staff_type'), field: 'staff_type', align: 'center' },
        { name: 'check_code', label: this.$t('staff.check_code'), field: 'check_code', align: 'center' },
        { name: 'create_time', label: this.$t('createtime'), field: 'create_time', align: 'center' },
        { name: 'update_time', label: this.$t('updatetime'), field: 'update_time', align: 'center' }
      ],
      filter: '',
      pagination: {
        page: 1,
        rowsPerPage: '30'
      },
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
        getauth(_this.pathname + '?page=' + '' + _this.current, {
        }).then(res => {
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
        }).catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
      }
    },
    changePageEnter(e) {
      if (Number(this.paginationIpt) < 1) {
        this.current = 1;
        this.paginationIpt = 1;
      } else if (Number(this.paginationIpt) > this.max) {
        this.current = this.max;
        this.paginationIpt = this.max;
      } else {
        this.current = Number(this.paginationIpt);
      }
      this.getList();
    },
    getSearchList () {
      var _this = this
      if (LocalStorage.has('auth')) {
        _this.current = 1
        _this.paginationIpt = 1
        getauth(_this.pathname + '?staff_name__icontains=' + _this.filter + '&page=' + '' + _this.current, {
        }).then(res => {
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
    getListPrevious () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname_previous, {
        }).then(res => {
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
    getListNext () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname_next, {
        }).then(res => {
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
    reFresh () {
      var _this = this
      _this.getList()
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
    if (document.getElementById('chat_scroll')) {
      document.getElementById('chat_scroll').scrollTop = document.getElementById('chat_scroll').scrollHeight
    } else {
    }
  },
  destroyed () {
  }
}
</script>
