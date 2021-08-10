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
             <q-btn :label="$t('downloadasnlist')" icon="cloud_download" @click="downloadlistData()">
               <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                {{ $t('downloadasnlisttip') }}
               </q-tooltip>
             </q-btn>
             <q-btn :label="$t('downloadasnlist')" icon="cloud_download" @click="downloaddetailData()">
               <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                 {{ $t('downloadasndetailtip') }}
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
             <q-td key="asn_code" :props="props">
               {{ props.row.asn_code }}
             </q-td>
             <q-td key="total_weight" :props="props">
               {{ props.row.total_weight }}
             </q-td>
             <q-td key="total_volume" :props="props">
               {{ props.row.total_volume }}
             </q-td>
             <q-td key="supplier" :props="props">
               {{ props.row.supplier }}
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
        <div class="q-pa-md flex flex-center">
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
import { getauth, getfile } from 'boot/axios_request'
import { date, exportFile, SessionStorage, LocalStorage } from 'quasar'

export default {
  name: 'Pagesupplierasnlist',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'asn/list/?supplier=',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      viewprint_table: [],
      warehouse_detail: {},
      supplier_list: [],
      supplier_detail: {},
      columns: [
        { name: 'asn_code', required: true, label: this.$t('inbound.view_asn.asn_code'), align: 'left', field: 'asn_code' },
        { name: 'total_weight', label: this.$t('inbound.view_asn.total_weight'), field: 'total_weight', align: 'center' },
        { name: 'total_volume', label: this.$t('inbound.view_asn.total_volume'), field: 'total_volume', align: 'center' },
        { name: 'supplier', label: this.$t('baseinfo.view_supplier.supplier_name'), field: 'supplier', align: 'center' },
        { name: 'creater', label: this.$t('creater'), field: 'creater', align: 'center' },
        { name: 'create_time', label: this.$t('createtime'), field: 'create_time', align: 'center' },
        { name: 'update_time', label: this.$t('updatetime'), field: 'update_time', align: 'center' }
      ],
      filter: '',
      pagination: {
        page: 1,
        rowsPerPage: '30'
      },
      newForm: false,
      options: SessionStorage.getItem('goods_code'),
      newAsn: { creater: '' },
      newFormData: {
        asn_code: '',
        supplier: '',
        goods_code: [],
        goods_qty: [],
        creater: ''
      },
      goodsData1: { code: '', qty: '' },
      goodsData2: { code: '', qty: '' },
      editid: 0,
      editFormData: {},
      editMode: false,
      sortedForm: false,
      sortedid: 0,
      deleteForm: false,
      deleteid: 0,
      preloadForm: false,
      preloadid: 0,
      presortForm: false,
      presortid: 0,
      viewForm: false,
      viewAsn: '',
      viewid: 0
    }
  },
  methods: {
    getList () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname + _this.login_name, {
        }).then(res => {
          _this.table_list = res.results
          _this.supplier_list = res.supplier_list
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
        getauth(_this.pathname + _this.login_name + '&asn_code__icontains=' + _this.filter, {
        }).then(res => {
          _this.table_list = res.results
          _this.supplier_list = res.supplier_list
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
          _this.supplier_list = res.supplier_list
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
          _this.supplier_list = res.supplier_list
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
    downloadlistData () {
      var _this = this
      getfile(_this.pathname + 'filelist/?lang=' + LocalStorage.getItem('lang') + '&supplier=' + _this.login_name).then(res => {
        var timeStamp = Date.now()
        var formattedString = date.formatDate(timeStamp, 'YYYYMMDDHHmmssSSS')
        const status = exportFile(
          _this.pathname + 'list' + formattedString + '.csv',
          '\uFEFF' + res.data,
          'text/csv'
        )
        if (status !== true) {
          _this.$q.notify({
            message: 'Browser denied file download...',
            color: 'negative',
            icon: 'warning'
          })
        }
      })
    },
    downloaddetailData () {
      var _this = this
      getfile(_this.pathname + 'filedetail/?lang=' + LocalStorage.getItem('lang') + '&supplier=' + _this.login_name).then(res => {
        var timeStamp = Date.now()
        var formattedString = date.formatDate(timeStamp, 'YYYYMMDDHHmmssSSS')
        const status = exportFile(
          _this.pathname + 'detail' + formattedString + '.csv',
          '\uFEFF' + res.data,
          'text/csv'
        )
        if (status !== true) {
          _this.$q.notify({
            message: 'Browser denied file download...',
            color: 'negative',
            icon: 'warning'
          })
        }
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
    if (SessionStorage.has('goods_code')) {
    } else {
      SessionStorage.set('goods_code', [])
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
