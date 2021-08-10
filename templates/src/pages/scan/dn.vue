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
             <q-btn :label="$t('refresh')" @click="reFresh()" />
           </q-btn-group>
           <q-space />
           <q-input class="cordova-search" outlined rounded dense debounce="300" color="primary" v-model="filter" :placeholder="$t('search')" @blur="getSearchList()" @keyup.enter="getSearchList()">
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
             <q-td key="dn_status" :props="props">
               {{ props.row.dn_status }}
             </q-td>
             <q-td key="total_weight" :props="props">
               {{ props.row.total_weight }}
             </q-td>
             <q-td key="total_volume" :props="props">
               {{ props.row.total_volume }}
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
             <q-td key="action" :props="props" style="width: 100px">
               <q-btn v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                              $q.localStorage.getItem('staff_type') !== 'Customer' &&
                              $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                              $q.localStorage.getItem('staff_type') !== 'StockControl'
                             "
                      round flat push color="info" icon="visibility" @click="viewData(props.row)">
               </q-btn>
             </q-td>
           </q-tr>
         </template>
      </q-table>
      </transition>
      <template>
        <div class="q-pa-md flex flex-center cordova-footer">
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
      <q-dialog v-model="viewForm">
       <q-card id="printMe">
         <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
           <div>{{ viewdn }}</div>
           <q-space />
         </q-bar>
         <q-card-section>
           <div class="text-h6">Sender: {{ warehouse_detail.warehouse_name }}</div>
           <div class="text-subtitle2">Address: {{ warehouse_detail.warehouse_city }}{{ warehouse_detail.warehouse_address }}</div>
           <div class="text-subtitle2">Tel: {{ warehouse_detail.warehouse_contact }}</div>
           <div class="text-h6">Receiver: {{ customer_detail.customer_name }}</div>
           <div class="text-subtitle2">Address: {{ customer_detail.customer_city }}{{ customer_detail.customer_address }}</div>
           <div class="text-subtitle2">Tel: {{ customer_detail.customer_contact }}</div>
         </q-card-section>
         <q-markup-table>
          <thead>
            <tr>
              <th class="text-left">Goods Code</th>
              <th class="text-right">Goods Weight(Unit: KG)</th>
              <th class="text-right">Goods Volume(Unit: Cubic Metres)</th>
              <th class="text-right">Shipping QTY</th>
              <th class="text-right">Comments</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(view, index) in viewprint_table" :key="index">
              <td class="text-left">{{ view.goods_code }}</td>
              <td class="text-right">{{ view.goods_weight }}</td>
              <td class="text-right">{{ view.goods_volume }}</td>
              <td class="text-right">{{ view.picked_qty + view.intransit_qty }}</td>
              <td class="text-right"></td>
            </tr>
          </tbody>
        </q-markup-table>
       </q-card>
     </q-dialog>
    </div>
</template>
    <router-view />

<script>
import { getauth, ViewPrintAuth } from 'boot/axios_request'
import { LocalStorage } from 'quasar'

export default {
  name: 'Pagednlist',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'dn/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      viewprint_table: [],
      pickinglist_print_table: [],
      warehouse_detail: {},
      customer_list: [],
      driver_list: [],
      customer_detail: {},
      columns: [
        { name: 'dn_code', required: true, label: this.$t('outbound.view_dn.dn_code'), align: 'left', field: 'dn_code' },
        { name: 'dn_status', label: this.$t('outbound.view_dn.dn_status'), field: 'dn_status', align: 'center' },
        { name: 'total_weight', label: this.$t('outbound.view_dn.total_weight'), field: 'total_weight', align: 'center' },
        { name: 'total_volume', label: this.$t('outbound.view_dn.total_volume'), field: 'total_volume', align: 'center' },
        { name: 'customer', label: this.$t('outbound.view_dn.customer'), field: 'customer', align: 'center' },
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
      viewForm: false,
      viewdn: '',
      viewid: 0,
      printObj: {
        id: 'printMe',
        popTitle: 'Advance Shipment Notice'
      }
    }
  },
  methods: {
    getList () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname + 'list/', {
        }).then(res => {
          _this.table_list = res.results
          _this.customer_list = res.customer_list
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
    getSearchList () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname + 'list/?dn_code__icontains=' + _this.filter, {
        }).then(res => {
          _this.table_list = res.results
          _this.customer_list = res.customer_list
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
          _this.customer_list = res.customer_list
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
          _this.customer_list = res.customer_list
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
    },
    viewData (e) {
      var _this = this
      ViewPrintAuth(_this.pathname + 'viewprint/' + e.id + '/').then(res => {
        _this.viewprint_table = res.dn_detail
        _this.warehouse_detail = res.warehouse_detail
        _this.customer_detail = res.customer_detail
        _this.viewdn = e.dn_code
        _this.viewForm = true
      })
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
    if (LocalStorage.has('goods_code_list')) {
    } else {
      LocalStorage.set('goods_code_list', [])
    }
  },
  mounted () {
    var _this = this
    if (_this.$q.platform.is.electron) {
      _this.height = String(_this.$q.screen.height - 170) + 'px'
    } else {
      _this.height = _this.$q.screen.height - 170 + '' + 'px'
    }
  },
  updated () {
  },
  destroyed () {
  }
}
</script>
