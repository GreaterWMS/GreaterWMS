<template>
  <div>
    <transition appear enter-active-class="animated fadeIn">
      <q-table
        class="my-sticky-header-column-table shadow-24"
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
            <q-btn :label="$t('stock.view_stocklist.cyclecount')" icon="refresh" @click="getList()">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('stock.view_stocklist.cyclecounttip') }}</q-tooltip>
            </q-btn>
            <q-btn :label="$t('stock.view_stocklist.downloadcyclecount')" icon="cloud_download" @click="downloadData()">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                {{ $t('stock.view_stocklist.downloadcyclecounttip') }}
              </q-tooltip>
            </q-btn>
          </q-btn-group>
          <q-space />
          <q-btn-group push>
            <q-btn color="purple" :label="$t('stock.view_stocklist.cyclecountresult')" @click="ConfirmCounts()">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                {{ $t('stock.view_stocklist.cyclecountresulttip') }}
              </q-tooltip>
            </q-btn>
          </q-btn-group>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td key="bin_name" :props="props">{{ props.row.bin_name }}</q-td>
            <q-td key="goods_code" :props="props">{{ props.row.goods_code }}</q-td>
            <q-td key="goods_qty" :props="props">{{ props.row.goods_qty }}</q-td>
            <q-td key="physical_inventory" :props="props">
              <q-input
                dense
                outlined
                square
                v-model.number="props.row.physical_inventory"
                type="number"
                :label="$t('stock.view_stocklist.physical_inventory')"
                :rules="[val => (val && val > 0) || val == 0 || error1]"
                @blur="blurHandler(props.row.physical_inventory)"
              />
            </q-td>
            <q-td key="difference" :props="props">{{ props.row.physical_inventory - props.row.goods_qty }}</q-td>
            <q-td key="action" :props="props" style="width: 50px">
              <q-btn
                v-show="$q.localStorage.getItem('staff_type') !== 'Inbound' && $q.localStorage.getItem('staff_type') !== 'Outbound'"
                round
                flat
                push
                color="purple"
                icon="repeat"
                @click="props.row.physical_inventory = 0"
              >
                <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                  {{ $t('stock.view_stocklist.recyclecounttip') }}
                </q-tooltip>
              </q-btn>
            </q-td>
          </q-tr>
        </template>
      </q-table>
    </transition>
    <template>
      <div class="q-pa-lg flex flex-center"><q-btn flat push color="dark" :label="$t('no_data')"></q-btn></div>
    </template>
    <q-dialog v-model="CountFrom">
      <q-card class="shadow-24">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <div>{{ $t('confirminventoryresults') }}</div>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-amber text-black shadow-4">{{ $t('index.close') }}</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section style="max-height: 325px; width: 400px" class="scroll">{{ $t('deletetip') }}</q-card-section>
        <div style="float: right; padding: 15px 15px 15px 0">
          <q-btn color="white" text-color="black" style="margin-right: 25px" @click="preloadDataCancel()">{{ $t('cancel') }}</q-btn>
          <q-btn color="primary" @click="ConfirmCount()">{{ $t('submit') }}</q-btn>
        </div>
      </q-card>
    </q-dialog>
  </div>
</template>
<router-view />
<script>
import { date, exportFile, LocalStorage } from 'quasar'
import { getauth, getfile, postauth } from 'boot/axios_request'

export default {
  name: 'cyclyecount',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'cyclecount/',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      bin_size_list: [],
      bin_property_list: [],
      warehouse_list: [],
      columns: [
        { name: 'bin_name', required: true, label: this.$t('warehouse.view_binset.bin_name'), align: 'left', field: 'bin_name' },
        { name: 'goods_code', label: this.$t('stock.view_stocklist.goods_code'), field: 'goods_code', align: 'center' },
        { name: 'goods_qty', label: this.$t('stock.view_stocklist.on_hand_inventory'), field: 'goods_qty', align: 'center' },
        { name: 'physical_inventory', label: this.$t('stock.view_stocklist.physical_inventory'), field: 'physical_inventory', align: 'center' },
        { name: 'difference', label: this.$t('stock.view_stocklist.difference'), field: 'difference', align: 'center' },
        { name: 'action', label: this.$t('action'), align: 'right' }
      ],
      pagination: {
        page: 1,
        rowsPerPage: '10000'
      },
      options: [],
      error1: this.$t('stock.view_stocklist.error1'),
      CountFrom: false
    }
  },
  methods: {
    getList () {
      var _this = this
      getauth(_this.pathname, {})
        .then(res => {
          _this.table_list = res
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    reFresh () {
      var _this = this
      _this.getList()
    },
    ConfirmCount () {
      var _this = this
      if (!_this.table_list.length) {
        _this.CountFrom = false
        _this.$q.notify({
          message: _this.$t('notice.cyclecounterror'),
          icon: 'close',
          color: 'negative'
        })
      } else {
        postauth(_this.pathname, _this.table_list)
          .then(res => {
            _this.CountFrom = false
            _this.$q.notify({
              message: 'Success Confirm Cycle Count',
              icon: 'check',
              color: 'green'
            })
            _this.reFresh()
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
    preloadDataCancel () {
      var _this = this
      _this.CountFrom = false
    },
    downloadData () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getfile('cyclecount/filecyclecountday/?lang=' + LocalStorage.getItem('lang')).then(res => {
          var timeStamp = Date.now()
          var formattedString = date.formatDate(timeStamp, 'YYYYMMDDHHmmssSSS')
          const status = exportFile('cyclecountday_' + formattedString + '.csv', '\uFEFF' + res.data, 'text/csv')
          if (status !== true) {
            _this.$q.notify({
              message: 'Browser denied file download...',
              color: 'negative',
              icon: 'warning'
            })
          }
        })
      } else {
        _this.$q.notify({
          message: _this.$t('notice.loginerror'),
          color: 'negative',
          icon: 'warning'
        })
      }
    },
    ConfirmCounts () {
      var _this = this
      _this.CountFrom = true
    },
    blurHandler (val) {
      val = val.toString().replace(/^(0+)|[^\d]+/g, '')
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
  updated () {},
  destroyed () {}
}
</script>
