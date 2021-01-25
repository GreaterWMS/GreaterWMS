<template>
    <div class="q-pa-md" style="width: 100%; margin-top: -20px">
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
             <q-btn label="refresh" icon="refresh" @click="reFresh()">
               <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                 Refresh data
               </q-tooltip>
             </q-btn>
           </q-btn-group>
           <q-space />
           <q-input outlined rounded dense debounce="300" color="primary" v-model="filter" placeholder="Search word">
             <template v-slot:append>
               <q-icon name="search" />
             </template>
           </q-input>
         </template>
         <template v-slot:body="props">
           <q-tr :props="props">
               <q-td key="dn_code" :props="props">
                 {{ props.row.dn_code }}
               </q-td>
               <q-td key="goods_code" :props="props">
                 {{ props.row.goods_code }}
               </q-td>
               <q-td key="goods_qty" :props="props">
                 {{ props.row.goods_qty }}
               </q-td>
               <q-td key="pick_qty" :props="props">
                 {{ props.row.pick_qty }}
               </q-td>
             <q-td key="picked_qty" :props="props">
               {{ props.row.picked_qty }}
             </q-td>
             <q-td key="customer" :props="props">
               {{ props.row.customer }}
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
        <div class="q-pa-lg flex flex-center">
          <q-btn v-show="pathname_previous" flat push color="purple" label="Previous" icon="navigate_before" @click="getListPrevious()">
            <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
              Previous
            </q-tooltip>
          </q-btn>
          <q-btn v-show="pathname_next" flat push color="purple" label="Next" icon-right="navigate_next" @click="getListNext()">
            <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
              Next
            </q-tooltip>
          </q-btn>
        </div>
      </template>
    </div>
</template>
    <router-view />

<script>
// import { openURL } from 'quasar'
import { getauth } from 'boot/axios_request'

export default {
  name: 'Pagednprepick',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'dn/detail/?dn_status=3&pick_qty__gt=0',
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
        { name: 'dn_code', required: true, label: 'DN Code', align: 'left', field: 'dn_code' },
        { name: 'goods_code', label: 'Goods Code', field: 'goods_code', align: 'center' },
        { name: 'goods_qty', label: 'Goods Qty', field: 'goods_qty', align: 'center' },
        { name: 'pick_qty', label: 'Pick QTY', field: 'pick_qty', align: 'center' },
        { name: 'picked_qty', label: 'Picked Qty', field: 'picked_qty', align: 'center' },
        { name: 'customer', label: 'customer', field: 'customer', align: 'center' },
        { name: 'creater', label: 'Creater', field: 'creater', align: 'center' },
        { name: 'create_time', label: 'Create Time', field: 'create_time', align: 'center' },
        { name: 'update_time', label: 'Update Time', field: 'update_time', align: 'center' }
      ],
      filter: '',
      pagination: {
        page: 1,
        rowsPerPage: '30'
      }
    }
  },
  methods: {
    getList () {
      var _this = this
      if (_this.$q.localStorage.has('auth')) {
        getauth(_this.pathname, {
        }).then(res => {
          _this.table_list = res.results
          if (res.previous) {
            var previous = res.previous.split(':')[0]
            res.previous.replace(previous, window.location.href.split(':')[0])
            _this.pathname_previous = res.previous
          } else {
            _this.pathname_previous = res.previous
          }
          if (res.next) {
            var next = res.next.split(':')[0]
            res.next.replace(next, window.location.href.split(':')[0])
            _this.pathname_next = res.next
          } else {
            _this.pathname_next = res.next
          }
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
          if (res.previous) {
            var previous = res.previous.split(':')[0]
            res.previous.replace(previous, window.location.href.split(':')[0])
            _this.pathname_previous = res.previous
          } else {
            _this.pathname_previous = res.previous
          }
          if (res.next) {
            var next = res.next.split(':')[0]
            res.next.replace(next, window.location.href.split(':')[0])
            _this.pathname_next = res.next
          } else {
            _this.pathname_next = res.next
          }
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
          if (res.previous) {
            var previous = res.previous.split(':')[0]
            res.previous.replace(previous, window.location.href.split(':')[0])
            _this.pathname_previous = res.previous
          } else {
            _this.pathname_previous = res.previous
          }
          if (res.next) {
            var next = res.next.split(':')[0]
            res.next.replace(next, window.location.href.split(':')[0])
            _this.pathname_next = res.next
          } else {
            _this.pathname_next = res.next
          }
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
    if (this.$q.platform.is.electron) {
      this.height = String(this.$q.screen.height - 290) + 'px'
    } else {
      this.height = this.$q.screen.height - 290 + '' + 'px'
    }
  },
  updated () {
  },
  destroyed () {
  }
}
</script>
