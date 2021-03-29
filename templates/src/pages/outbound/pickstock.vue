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
               <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                 {{ $t('refreshtip') }}
               </q-tooltip>
             </q-btn>
           </q-btn-group>
           <q-space />
           <q-input outlined rounded dense debounce="300" color="primary" v-model="filter" :placeholder="$t('search')" @blur="getSearchList()" @keyup.enter="getSearchList()">
             <template v-slot:append>
               <q-icon name="search" @click="getSearchList()"/>
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
          <q-btn v-show="pathname_previous" flat push color="purple" :label="$t('previous')" icon="navigate_before" @click="getListPrevious()">
            <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
              {{ $t('previous') }}
            </q-tooltip>
          </q-btn>
          <q-btn v-show="pathname_next" flat push color="purple" :label="$t('next')" icon-right="navigate_next" @click="getListNext()">
            <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
              {{ $t('next') }}
            </q-tooltip>
          </q-btn>
          <q-btn v-show="!pathname_previous && !pathname_next" flat push color="dark" :label="$t('no_data')"></q-btn>
        </div>
      </template>
    </div>
</template>
    <router-view />

<script>
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
        { name: 'dn_code', required: true, label: this.$t('outbound.view_dn.dn_code'), align: 'left', field: 'dn_code' },
        { name: 'goods_code', label: this.$t('goods.view_goodslist.goods_code'), field: 'goods_code', align: 'center' },
        { name: 'goods_qty', label: this.$t('outbound.view_dn.goods_qty'), field: 'goods_qty', align: 'center' },
        { name: 'pick_qty', label: this.$t('stock.view_stocklist.pick_stock'), field: 'pick_qty', align: 'center' },
        { name: 'picked_qty', label: this.$t('stock.view_stocklist.picked_stock'), field: 'picked_qty', align: 'center' },
        { name: 'customer', label: this.$t('baseinfo.view_customer.customer_name'), field: 'customer', align: 'center' },
        { name: 'creater', label: this.$t('creater'), field: 'creater', align: 'center' },
        { name: 'create_time', label: this.$t('createtime'), field: 'create_time', align: 'center' },
        { name: 'update_time', label: this.$t('updatetime'), field: 'update_time', align: 'center' }
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
            var previouspage = res.previous.replace(previous, window.location.href.split(':')[0])
            _this.pathname_previous = previouspage
          } else {
            _this.pathname_previous = res.previous
          }
          if (res.next) {
            var next = res.next.split(':')[0]
            var nextpage = res.next.replace(next, window.location.href.split(':')[0])
            _this.pathname_next = nextpage
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
    getSearchList () {
      var _this = this
      if (_this.$q.localStorage.has('auth')) {
        getauth(_this.pathname + '&dn_code__icontains=' + _this.filter, {
        }).then(res => {
          _this.table_list = res.results
          if (res.previous) {
            var previous = res.previous.split(':')[0]
            var previouspage = res.previous.replace(previous, window.location.href.split(':')[0])
            _this.pathname_previous = previouspage
          } else {
            _this.pathname_previous = res.previous
          }
          if (res.next) {
            var next = res.next.split(':')[0]
            var nextpage = res.next.replace(next, window.location.href.split(':')[0])
            _this.pathname_next = nextpage
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
            var previouspage = res.previous.replace(previous, window.location.href.split(':')[0])
            _this.pathname_previous = previouspage
          } else {
            _this.pathname_previous = res.previous
          }
          if (res.next) {
            var next = res.next.split(':')[0]
            var nextpage = res.next.replace(next, window.location.href.split(':')[0])
            _this.pathname_next = nextpage
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
            var previouspage = res.previous.replace(previous, window.location.href.split(':')[0])
            _this.pathname_previous = previouspage
          } else {
            _this.pathname_previous = res.previous
          }
          if (res.next) {
            var next = res.next.split(':')[0]
            var nextpage = res.next.replace(next, window.location.href.split(':')[0])
            _this.pathname_next = nextpage
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
