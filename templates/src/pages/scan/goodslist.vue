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
               <q-td key="goods_code" :props="props">
                 {{ props.row.goods_code }}
               </q-td>
               <q-td key="goods_desc" :props="props">
                 {{ props.row.goods_desc }}
               </q-td>
               <q-td key="goods_supplier" :props="props">
                 {{ props.row.goods_supplier }}
               </q-td>
               <q-td key="goods_weight" :props="props">
                 {{ props.row.goods_weight }}
               </q-td>
               <q-td key="goods_w" :props="props">
                 {{ props.row.goods_w }}
               </q-td>
               <q-td key="goods_d" :props="props">
                 {{ props.row.goods_d }}
               </q-td>
               <q-td key="goods_h" :props="props">
                 {{ props.row.goods_h }}
               </q-td>
             <q-td key="unit_volume" :props="props">
               {{ props.row.unit_volume }}
             </q-td>
               <q-td key="goods_unit" :props="props">
                 {{ props.row.goods_unit }}
               </q-td>
               <q-td key="goods_class" :props="props">
                 {{ props.row.goods_class }}
               </q-td>
               <q-td key="goods_brand" :props="props">
                 {{ props.row.goods_brand }}
               </q-td>
               <q-td key="goods_color" :props="props">
                 {{ props.row.goods_color }}
               </q-td>
               <q-td key="goods_shape" :props="props">
                 {{ props.row.goods_shape }}
               </q-td>
               <q-td key="goods_specs" :props="props">
                 {{ props.row.goods_specs }}
               </q-td>
               <q-td key="goods_origin" :props="props">
                 {{ props.row.goods_origin }}
               </q-td>
               <q-td key="goods_cost" :props="props">
                 {{ props.row.goods_cost }}
               </q-td>
               <q-td key="goods_price" :props="props">
                 {{ props.row.goods_price }}
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
        <div class="q-pa-lg flex flex-center" style="margin-top: -10px">
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
import { getauth, postauth, putauth, deleteauth, getfile } from 'boot/axios_request'
import { date, exportFile, LocalStorage } from 'quasar'

export default {
  name: 'Pagegoodslist_scan',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'goods/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      goods_unit_list: [],
      goods_class_list: [],
      goods_brand_list: [],
      goods_color_list: [],
      goods_shape_list: [],
      goods_specs_list: [],
      goods_origin_list: [],
      supplier_list: [],
      columns: [
        { name: 'goods_code', required: true, label: this.$t('goods.view_goodslist.goods_code'), align: 'left', field: 'goods_code' },
        { name: 'goods_desc', label: this.$t('goods.view_goodslist.goods_desc'), field: 'goods_desc', align: 'center' },
        { name: 'goods_supplier', label: this.$t('goods.view_goodslist.goods_supplier'), field: 'goods_supplier', align: 'center' },
        { name: 'goods_weight', label: this.$t('goods.view_goodslist.goods_weight'), field: 'goods_weight', align: 'center' },
        { name: 'goods_w', label: this.$t('goods.view_goodslist.goods_w'), field: 'goods_w', align: 'center' },
        { name: 'goods_d', label: this.$t('goods.view_goodslist.goods_d'), field: 'goods_d', align: 'center' },
        { name: 'goods_h', label: this.$t('goods.view_goodslist.goods_h'), field: 'goods_h', align: 'center' },
        { name: 'unit_volume', label: this.$t('goods.view_goodslist.unit_volume'), field: 'unit_volume', align: 'center' },
        { name: 'goods_unit', label: this.$t('goods.view_goodslist.goods_unit'), field: 'goods_unit', align: 'center' },
        { name: 'goods_class', label: this.$t('goods.view_goodslist.goods_class'), field: 'goods_class', align: 'center' },
        { name: 'goods_brand', label: this.$t('goods.view_goodslist.goods_brand'), field: 'goods_brand', align: 'center' },
        { name: 'goods_color', label: this.$t('goods.view_goodslist.goods_color'), field: 'goods_color', align: 'center' },
        { name: 'goods_shape', label: this.$t('goods.view_goodslist.goods_shape'), field: 'goods_shape', align: 'center' },
        { name: 'goods_specs', label: this.$t('goods.view_goodslist.goods_specs'), field: 'goods_specs', align: 'center' },
        { name: 'goods_origin', label: this.$t('goods.view_goodslist.goods_origin'), field: 'goods_origin', align: 'center' },
        { name: 'goods_cost', label: this.$t('goods.view_goodslist.goods_cost'), field: 'goods_cost', align: 'center' },
        { name: 'goods_price', label: this.$t('goods.view_goodslist.goods_price'), field: 'goods_price', align: 'center' },
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
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname, {
        }).then(res => {
          _this.table_list = res.results
          _this.goods_unit_list = res.goods_unit_list
          _this.goods_class_list = res.goods_class_list
          _this.goods_brand_list = res.goods_brand_list
          _this.goods_color_list = res.goods_color_list
          _this.goods_shape_list = res.goods_shape_list
          _this.goods_specs_list = res.goods_specs_list
          _this.goods_origin_list = res.goods_origin_list
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
        getauth(_this.pathname + '?goods_desc__icontains=' + _this.filter, {
        }).then(res => {
          _this.table_list = res.results
          _this.goods_unit_list = res.goods_unit_list
          _this.goods_class_list = res.goods_class_list
          _this.goods_brand_list = res.goods_brand_list
          _this.goods_color_list = res.goods_color_list
          _this.goods_shape_list = res.goods_shape_list
          _this.goods_specs_list = res.goods_specs_list
          _this.goods_origin_list = res.goods_origin_list
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
          _this.goods_unit_list = res.goods_unit_list
          _this.goods_class_list = res.goods_class_list
          _this.goods_brand_list = res.goods_brand_list
          _this.goods_color_list = res.goods_color_list
          _this.goods_shape_list = res.goods_shape_list
          _this.goods_specs_list = res.goods_specs_list
          _this.goods_origin_list = res.goods_origin_list
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
          _this.goods_unit_list = res.goods_unit_list
          _this.goods_class_list = res.goods_class_list
          _this.goods_brand_list = res.goods_brand_list
          _this.goods_color_list = res.goods_color_list
          _this.goods_shape_list = res.goods_shape_list
          _this.goods_specs_list = res.goods_specs_list
          _this.goods_origin_list = res.goods_origin_list
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
    if (this.$q.platform.is.electron) {
      this.height = String(this.$q.screen.height - 170) + 'px'
    } else {
      this.height = this.$q.screen.height - 170 + '' + 'px'
    }
  },
  updated () {
  },
  destroyed () {
  }
}
</script>
