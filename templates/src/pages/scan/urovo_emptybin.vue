<template>
    <div>
      <transition appear enter-active-class="animated fadeIn">
      <q-table
        class="my-sticky-header-table shadow-24"
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
             <q-btn :label="$t('refresh')" icon="refresh" @click="reFresh()" />
           </q-btn-group>
           <q-space />
          <q-btn-group push>
            <q-btn color='purple' :label="$t('stock.view_stocklist.cyclecountresult')" @click="ConfirmCount()">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                {{ $t('stock.view_stocklist.cyclecountresulttip') }}
              </q-tooltip>
            </q-btn>
          </q-btn-group>
         </template>
         <template v-slot:body="props">
           <q-tr :props="props">
            <q-td key="bin_name" :props="props" :class="{ 'scan-background': bin_scan !== '' && bin_scan === props.row.bin_name }">
              {{ props.row.bin_name }}
            </q-td>
            <q-td key="goods_code" :props="props">
              {{ props.row.goods_code }}
            </q-td>
            <q-td key="physical_inventory" :props="props">
              {{ props.row.physical_inventory }}
            </q-td>
            <q-td key="action" :props="props" style="width: 50px">
              <q-btn round flat push color="purple" icon="repeat" @click="props.row.physical_inventory = 0">
              </q-btn>
            </q-td>
          </q-tr>
         </template>
        </q-table>
      </transition>
      <template>
        <div class="q-pa-lg flex cordova-footer">
            <input id="scannedBarcodes" v-model="barscan" type="text" @input="datachange()" readonly disabled/>
        </div>
      </template>
    </div>
</template>
    <router-view />

<script>
import { getauth, putauth } from 'boot/axios_request'
import Vconsole from 'vconsole'
import { LocalStorage } from 'quasar'
const vConsole = new Vconsole()

function getDeviceID () {
  var scannedData = scanData.extras['com.symbol.datawedge.data_string']
  document.getElementById('scannedBarcodes').value = ''
  document.getElementById('scannedBarcodes').value = scannedData
  document.getElementById('scannedBarcodes').dispatchEvent(new Event('input'))
}

function getDeviceinfo () {
  Uplugin.getDeviceID('',
    function (res) {
      console.log(res)
    },
    function (err) {
      console.log(err)
    }
  )
}

function startBarcode () {
  Uplugin.getBarcode('start',
    function (res) {
      document.getElementById('scannedBarcodes').value = ''
      document.getElementById('scannedBarcodes').value = res
      document.getElementById('scannedBarcodes').dispatchEvent(new Event('input'))
      console.log(1, res)
    },
    function (err) {
      console.log(err)
    }
  )
}

function stopBarcode () {
  Uplugin.getBarcode('stop',
    function (res) {
      console.log(res)
    },
    function (err) {
      console.log(err)
    }
  )
}

export default {
  name: 'Pageurovo_cyclecount',
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
        { name: 'physical_inventory', label: this.$t('stock.view_stocklist.physical_inventory'), field: 'physical_inventory', align: 'center' },
        { name: 'action', label: this.$t('action'), align: 'right' }
      ],
      filter: '',
      pagination: {
        page: 1,
        rowsPerPage: '10000'
      },
      screenq: this.$q.screen,
      IMEI: window.device,
      batteryStatus: 'determining...',
      barscan: '',
      bin_scan: '',
      goods_scan: ''
    }
  },
  methods: {
    datachange () {
      var _this = this
      console.log(3, document.getElementById('scannedBarcodes').value)
      if (_this.$q.localStorage.has('auth')) {
        getauth('scanner/?bar_code=' + _this.barscan, {
        }).then(res => {
          console.log(2, res)
          _this.barscan = res.results[0].code
          if (res.results[0].mode === 'BINSET') {
            _this.bin_scan = res.results[0].code
            _this.goods_scan = ''
          } else if (res.results[0].mode === 'GOODS') {
            _this.goods_scan = res.results[0].code
            _this.countAdd(_this.goods_scan)
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
    countAdd (e) {
      var _this = this
      _this.table_list.filter(function (value, index, array) {
        if (value.bin_name === _this.bin_scan && value.goods_code === e) {
          _this.table_list[index].physical_inventory += 1
        }
      })
    },
    getList () {
      var _this = this
      if (_this.$q.localStorage.has('auth')) {
        getauth(_this.pathname, {
        }).then(res => {
          _this.table_list = res.results
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
      _this.barscan = ''
      _this.bin_scan = ''
      _this.goods_scan = ''
      _this.getList()
    },
    ConfirmCount () {
      var _this = this
      if (LocalStorage.has('auth')) {
        putauth(_this.pathname, _this.table_list).then(res => {
          _this.$q.notify({
            message: 'Success Confirm Cycle Count',
            icon: 'check',
            color: 'green'
          })
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
    updateBatteryStatus (status) {
      var _this = this
      _this.batteryStatus = `Level: ${status.level}, plugged: ${status.isPlugged}`
    },
    scanEvents () {
      var _this = this
      document.addEventListener('deviceready', _this.onDeviceReady, false)
    },
    onDeviceReady () {
      startBarcode()
    },
    onPause: function () {
      stopBarcode()
    },
    onResume () {
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
    } else {
      _this.authin = '0'
    }
  },
  mounted () {
    var _this = this
    window.addEventListener('batterystatus', _this.updateBatteryStatus, false)
    _this.height = this.$q.screen.height - 175 + '' + 'px'
    _this.barscan = ''
    _this.bin_scan = ''
    _this.goods_scan = ''
    _this.getList()
    _this.scanEvents()
    getDeviceinfo()
  },
  updated () {
  },
  beforeDestroy () {
    var _this = this
    window.removeEventListener('batterystatus', _this.updateBatteryStatus, false)
    window.removeEventListener('deviceready', _this.onDeviceReady, false)
  },
  destroyed () {
  }
}
</script>
