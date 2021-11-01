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
            <q-btn :label="$t('submit')" icon='refresh' @click="downloadData()">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                {{ $t('submit') }}
              </q-tooltip>
            </q-btn>
            <q-btn :label="$t('submit')" icon='refresh' @click="getID()">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                {{ $t('submit') }}
              </q-tooltip>
            </q-btn>
          </q-btn-group>
          <q-space />
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td key="bin_name" :props="props">
              {{ props.row.bin_name }}
            </q-td>
            <q-td key="goods_code" :props="props">
              {{ props.row.goods_code }}
            </q-td>
            <q-td key="goods_qty" :props="props">
              {{ props.row.goods_qty }}
            </q-td>
            <q-td key="physical_inventory" :props="props">
              {{ props.row.physical_inventory }}
            </q-td>
            <q-td key="action" :props="props" style="width: 50px">
              <q-btn v-show="$q.localStorage.getItem('staff_type') !== 'Inbound' &&
                              $q.localStorage.getItem('staff_type') !== 'Outbound'
                             "
                     round flat push color="purple" icon="repeat" @click="BinMove(props.row)">
                <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                  {{ $t('stock.view_stocklist.recyclecounttip') }}
                </q-tooltip>
              </q-btn>
            </q-td>
          </q-tr>
        </template>
      </q-table>
    </transition>
  </div>
</template>
  <router-view />

<script>

import { LocalStorage } from 'quasar'
import { getauth } from 'boot/axios_request'
import Vconsole from 'vconsole'
const vConsole = new Vconsole()
console.log(1)

function getDevideID () {
  Uplugin.getDeviceID('', function (result) { console.log(result) }, function (err) { console.log(err) })
}

function startBarcode () {
  Uplugin.getBarcode('start', function (result) { console.log(result) }, function (err) { console.log(err) })
}

function stopScanedData () {
  Uplugin.getBarcode('stop', function (result) { console.log(result) }, function (err) { console.log(err) })
}

export default {
  name: 'Urovo_cyclyecount',
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
      columns: [
        { name: 'bin_name', required: true, label: this.$t('warehouse.view_binset.bin_name'), align: 'left', field: 'bin_name' },
        { name: 'goods_code', label: this.$t('stock.view_stocklist.goods_code'), field: 'goods_code', align: 'center' },
        { name: 'goods_qty', label: this.$t('stock.view_stocklist.on_hand_inventory'), field: 'goods_qty', align: 'center' },
        { name: 'physical_inventory', label: this.$t('stock.view_stocklist.physical_inventory'), field: 'physical_inventory', align: 'center' },
        { name: 'action', label: this.$t('action'), align: 'right' }
      ],
      pagination: {
        page: 1,
        rowsPerPage: '10000'
      }
    }
  },
  methods: {
    getID () {
      getDevideID()
    },
    getList () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname, {
        }).then(res => {
          var dataDetail = []
          res.results.forEach(item => {
            console.log(item)
            var dataChang = {
              bin_name: item.bin_name,
              goods_code: item.goods_code,
              goods_qty: item.goods_qty,
              physical_inventory: 0,
              difference: item.goods_qty
            }
            dataDetail.push(dataChang)
          })
          _this.table_list = dataDetail
          dataDetail = []
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
    scanEvents () {
      var _this = this
      document.addEventListener('deviceready', _this.onDeviceReady, false)
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
      _this.height = String(_this.$q.screen.height - 115) + 'px'
    } else {
      _this.height = _this.$q.screen.height - 115 + '' + 'px'
    }
    getDevideID()
  },
  updated () {
  },
  destroyed () {
  }
}

</script>
