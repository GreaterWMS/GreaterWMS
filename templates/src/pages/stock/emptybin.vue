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
               <q-td key="bin_name" :props="props">
                 {{ props.row.bin_name }}
               </q-td>
               <q-td key="bin_size" :props="props">
                 {{ props.row.bin_size }}
               </q-td>
               <q-td key="bin_property" :props="props">
                 {{ props.row.bin_property }}
               </q-td>
             <q-td key="empty_label" :props="props">
               {{ props.row.empty_label }}
             </q-td>
             <q-td key="creater" :props="props">
               {{ props.row.creater }}
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
  name: 'Pageemptybin',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'binset/?empty_label=true',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      bin_size_list: [],
      bin_property_list: [],
      warehouse_list: [],
      columns: [
        { name: 'bin_name', required: true, label: this.$t('warehouse.view_binset.bin_name'), align: 'left', field: 'bin_name' },
        { name: 'bin_size', label: this.$t('warehouse.view_binset.bin_size'), field: 'bin_size', align: 'center' },
        { name: 'bin_property', label: this.$t('warehouse.view_binset.bin_property'), field: 'bin_property', align: 'center' },
        { name: 'empty_label', label: this.$t('warehouse.view_binset.empty_label'), field: 'empty_label', align: 'center' },
        { name: 'creater', label: this.$t('creater'), field: 'creater', align: 'center' },
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
      if (_this.$q.localStorage.has('auth')) {
        getauth(_this.pathname + '&page=' + '' + _this.current, {
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
      if (_this.$q.localStorage.has('auth')) {
        _this.current = 1
        _this.paginationIpt = 1
        getauth(_this.pathname + '&bin_name__icontains=' + _this.filter + '&page=' + '' + _this.current, {
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
      if (_this.$q.localStorage.has('auth')) {
        getauth(_this.pathname_previous, {
        }).then(res => {
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
      if (_this.$q.localStorage.has('auth')) {
        getauth(_this.pathname_next, {
        }).then(res => {
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
