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
        <div class="q-pa-lg flex cordova-footer">
            <input id="scannedBarcodes" v-model="barscan" type="text" @input="datachange()" readonly disabled/>
        </div>
      </template>
    </div>
</template>
    <router-view />

<script>
import { getauth } from 'boot/axios_request'
import Vconsole from 'vconsole'
if (process.env.NODE_ENV !== 'production') {
  const vConsole = new Vconsole()
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
  name: 'Pageurovo_goodslist',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'goods/',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
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
        rowsPerPage: '10000'
      },
      screenq: this.$q.screen,
      IMEI: window.device,
      batteryStatus: 'determining...',
      barscan: '',
      goods_scan: ''
    }
  },
  methods: {
    datachange () {
      var _this = this
      if (_this.$q.localStorage.has('auth')) {
        getauth('scanner/?bar_code=' + _this.barscan, {
        }).then(res => {
          _this.barscan = res.results[0].code
          if (res.results[0].mode === 'GOODS') {
            _this.goods_scan = res.results[0].code
            _this.getList(res.results[0].code)
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
    getList (e) {
      var _this = this
      if (_this.$q.localStorage.has('auth')) {
        getauth(_this.pathname + '?goods_code=' + e, {
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
      _this.goods_scan = ''
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
    _this.goods_scan = ''
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
