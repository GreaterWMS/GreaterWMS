<template>
  <div style="margin-top: 42px;">
    <transition appear enter-active-class="animated fadeIn">
      <q-table
        class="shadow-24"
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
            <q-btn :label="$t('refresh')" icon="refresh" @click="reFresh()">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('refreshtip') }}</q-tooltip>
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
            <q-td key="goods_code" :props="props">{{ props.row.goods_code }}</q-td>
            <q-td key="bin_name" :props="props">{{ props.row.bin_name }}</q-td>
            <q-td key="goods_desc" :props="props">{{ props.row.goods_desc }}</q-td>
            <q-td key="mode_code" :props="props">{{ props.row.mode_code }}</q-td>
            <q-td key="goods_qty" :props="props">{{ props.row.goods_qty }}</q-td>
            <q-td key="creater" :props="props">{{ props.row.creater }}</q-td>
            <q-td key="create_time" :props="props">{{ props.row.create_time }}</q-td>
            <q-td key="update_time" :props="props">{{ props.row.update_time }}</q-td>
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

<script>
import { getauth } from 'boot/axios_request.js'
import { LocalStorage } from 'quasar'

export default {
  name: 'PageInbAndOutb',
  data () {
    return {
      login_name: '',
      authin: '0',
      pathname: 'dashboard/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      filter: '',
      staff_type_list: ['Manager', 'Inbound', 'Outbound', 'Supervisor', 'StockControl', 'Customer', 'Supplier'],
      columns: [
        { name: 'goods_code', label: this.$t('dashboards.view_tradelist.goods_code'), field: 'goods_code', align: 'left' },
        { name: 'bin_name', label: this.$t('dashboards.view_tradelist.bin_name'), field: 'bin_name', align: 'center' },
        { name: 'goods_desc', label: this.$t('goods.view_goodslist.goods_desc'), field: 'goods_desc', align: 'center' },
        { name: 'mode_code', required: true, label: this.$t('dashboards.view_tradelist.mode_code'), align: 'center', field: 'mode_code' },
        { name: 'goods_qty', label: this.$t('dashboards.view_tradelist.goods_qty'), field: 'goods_qty', align: 'center' },
        { name: 'creater', label: this.$t('dashboards.view_tradelist.creater'), field: 'creater', align: 'center' },
        { name: 'create_time', label: this.$t('dashboards.view_tradelist.create_time'), field: 'create_time', align: 'center' },
        { name: 'update_time', label: this.$t('dashboards.view_tradelist.update_time'), field: 'update_time', align: 'right' }
      ],
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
      getauth('cyclecount/qtyrecorviewset/' + '?page=' + '' + _this.current, {})
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
      _this.current = 1
      _this.paginationIpt = 1
      getauth('cyclecount/qtyrecorviewset/?goods_code__icontains=' + _this.filter + '&page=' + '' + _this.current, {})
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
      if (this.$q.localStorage.has('auth')) {
        getauth(this.pathname_previous, {})
          .then(res => {
            this.table_list = res.results
            this.pathname_previous = res.previous
            this.pathname_next = res.next
          })
          .catch(err => {
            this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            })
          })
      }
    },
    getListNext () {
      if (this.$q.localStorage.has('auth')) {
        getauth(this.pathname_next, {})
          .then(res => {
            this.table_list = res.results
            this.pathname_previous = res.previous
            this.pathname_next = res.next
          })
          .catch(err => {
            this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            })
          })
      }
    },
    reFresh () {
      this.table_list = []
      this.getList()
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
      this.height = String(this.$q.screen.height - 290) + 'px'
    } else {
      this.height = this.$q.screen.height - 290 + '' + 'px'
    }
  }
}
</script>

<style>
</style>
