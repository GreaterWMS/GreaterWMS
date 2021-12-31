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
          <q-input outlined rounded dense debounce="300" color="primary" v-model="filter" :placeholder="$t('search')" @input="getSearchList()">
            <template v-slot:append>
              <q-icon name="search" @click="getSearchList()" />
            </template>
          </q-input>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td key="goods_code" :props="props">{{ props.row.goods_code }}</q-td>
            <q-td key="bin_name" :props="props">{{ props.row.bin_name }}</q-td>
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
      <div class="q-pa-lg flex flex-center">
        <q-btn v-show="pathname_previous" flat push color="purple" :label="$t('previous')" icon="navigate_before" @click="getListPrevious()">
          <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('previous') }}</q-tooltip>
        </q-btn>
        <q-btn v-show="pathname_next" flat push color="purple" :label="$t('next')" icon-right="navigate_next" @click="getListNext()">
          <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('next') }}</q-tooltip>
        </q-btn>
        <q-btn v-show="!pathname_previous && !pathname_next" flat push color="dark" :label="$t('no_data')"></q-btn>
      </div>
    </template>
  </div>
</template>

<script>
import { getauth } from 'boot/axios_request.js';
export default {
  name: 'PageInbAndOutb',
  data() {
    return {
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
        { name: 'mode_code', required: true, label: this.$t('dashboards.view_tradelist.mode_code'), align: 'center', field: 'mode_code' },
        { name: 'goods_qty', label: this.$t('dashboards.view_tradelist.goods_qty'), field: 'goods_qty', align: 'center' },
        { name: 'creater', label: this.$t('dashboards.view_tradelist.creater'), field: 'creater', align: 'center' },
        { name: 'create_time', label: this.$t('dashboards.view_tradelist.create_time'), field: 'create_time', align: 'center' },
        { name: 'update_time', label: this.$t('dashboards.view_tradelist.update_time'), field: 'update_time', align: 'right' }
      ],
      pagination: {
        page: 1,
        rowsPerPage: '30'
      }
    };
  },
  methods: {
    getList() {
      getauth('cyclecount/qtyrecorviewset/', {})
        .then(res => {
          this.table_list = res.results;
          this.pathname_previous = res.previous;
          this.pathname_next = res.next;
          this.table_list.forEach((item, index) => {
            if (item.mode_code.substr(0, 3) == 'ASN') {
              item.mode_code = this.$t('dashboards.view_tradelist.inbound');
            } else {
              item.mode_code = this.$t('dashboards.view_tradelist.outbound');
            }
          });
        })
        .catch(err => {
          this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          });
        });
    },
    getSearchList() {
      var _this = this;
      getauth('cyclecount/qtyrecorviewset/?goods_code__icontains='+ _this.filter, {})
        .then(res => {
          _this.table_list = res.results;
          _this.pathname_previous = res.previous;
          _this.pathname_next = res.next;
          this.table_list.forEach((item, index) => {
            if (item.mode_code.substr(0, 3) == 'ASN') {
              item.mode_code = this.$t('dashboards.view_tradelist.inbound');
            } else {
              item.mode_code = this.$t('dashboards.view_tradelist.outbound');
            }
          });
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          });
        });
    },
    getListPrevious() {
      if (this.$q.localStorage.has('auth')) {
        getauth(this.pathname_previous, {})
          .then(res => {
            this.table_list = res.results;
            this.pathname_previous = res.previous;
            this.pathname_next = res.next;
          })
          .catch(err => {
            this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            });
          });
      } else {
      }
    },
    getListNext() {
      if (this.$q.localStorage.has('auth')) {
        getauth(this.pathname_next, {})
          .then(res => {
            this.table_list = res.results;
            this.pathname_previous = res.previous;
            this.pathname_next = res.next;
          })
          .catch(err => {
            this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            });
          });
      } else {
      }
    },
    reFresh() {
      this.table_list = [];
      this.getList();
    }
  },
  created() {
    this.getList();
  },
  mounted() {
    if (this.$q.platform.is.electron) {
      this.height = String(this.$q.screen.height - 290) + 'px';
    } else {
      this.height = this.$q.screen.height - 290 + '' + 'px';
    }
  }
};
</script>

<style>
</style>
