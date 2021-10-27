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
            <q-btn :label="$t('refresh')" icon="refresh" @click="reFresh()">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                {{ $t('refreshtip') }}
              </q-tooltip>
            </q-btn>
          </q-btn-group>
          <q-space />
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <template v-if="props.row.id === editid">
              <q-td key="goods_code" :props="props">
                <q-input dense
                         outlined
                         square
                         v-model="editFormData.goods_code"
                         :label="$t('goods.view_goodslist.goods_code')"
                         autofocus
                         :rules="[ val => val && val.length > 0 || error1]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_code" :props="props">
                {{ props.row.goods_code }}
              </q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_desc" :props="props">
                <q-input dense
                         outlined
                         square
                         v-model="editFormData.goods_desc"
                         :label="$t('goods.view_goodslist.goods_desc')"
                         :rules="[ val => val && val.length > 0 || error2]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_desc" :props="props">
                {{ props.row.goods_desc }}
              </q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_supplier" :props="props">
                <q-select dense
                          outlined
                          square
                          v-model="editFormData.goods_supplier"
                          :options="supplier_list"
                          transition-show="scale"
                          transition-hide="scale"
                          :label="$t('goods.view_goodslist.goods_supplier')"
                          :rules="[ val => val && val.length > 0 || error3]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_supplier" :props="props">
                {{ props.row.goods_supplier }}
              </q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_weight" :props="props">
                <q-input dense
                         outlined
                         square
                         v-model.number="editFormData.goods_weight"
                         type="number"
                         :label="$t('goods.view_goodslist.goods_weight')"
                         :rules="[ val => val && val > 0 || error4]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_weight" :props="props">
                {{ props.row.goods_weight }}
              </q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_w" :props="props">
                <q-input dense
                         outlined
                         square
                         v-model.number="editFormData.goods_w"
                         type="number"
                         :label="$t('goods.view_goodslist.goods_w')"
                         :rules="[ val => val && val > 0 || error5]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_w" :props="props">
                {{ props.row.goods_w }}
              </q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_d" :props="props">
                <q-input dense
                         outlined
                         square
                         v-model.number="editFormData.goods_d"
                         type="number"
                         :label="$t('goods.view_goodslist.goods_d')"
                         :rules="[ val => val && val > 0 || error6]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_d" :props="props">
                {{ props.row.goods_d }}
              </q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_h" :props="props">
                <q-input dense
                         outlined
                         square
                         v-model.number="editFormData.goods_h"
                         type="number"
                         :label="$t('goods.view_goodslist.goods_h')"
                         :rules="[ val => val && val > 0 || error7]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_h" :props="props">
                {{ props.row.goods_h }}
              </q-td>
            </template>
            <q-td key="unit_volume" :props="props">
              {{ props.row.unit_volume }}
            </q-td>
            <template v-if="props.row.id === editid">
              <q-td key="goods_unit" :props="props">
                <q-select dense
                          outlined
                          square
                          v-model="editFormData.goods_unit"
                          :options="goods_unit_list"
                          transition-show="scale"
                          transition-hide="scale"
                          :label="$t('goods.view_goodslist.goods_unit')"
                          :rules="[ val => val && val.length > 0 || error8]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_unit" :props="props">
                {{ props.row.goods_unit }}
              </q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_class" :props="props">
                <q-select dense
                          outlined
                          square
                          v-model="editFormData.goods_class"
                          :options="goods_class_list"
                          transition-show="scale"
                          transition-hide="scale"
                          :label="$t('goods.view_goodslist.goods_class')"
                          :rules="[ val => val && val.length > 0 || error9]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_class" :props="props">
                {{ props.row.goods_class }}
              </q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_brand" :props="props">
                <q-select dense
                          outlined
                          square
                          v-model="editFormData.goods_brand"
                          :options="goods_brand_list"
                          transition-show="scale"
                          transition-hide="scale"
                          :label="$t('goods.view_goodslist.goods_brand')"
                          :rules="[ val => val && val.length > 0 || error10]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_brand" :props="props">
                {{ props.row.goods_brand }}
              </q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_color" :props="props">
                <q-select dense
                          outlined
                          square
                          v-model="editFormData.goods_color"
                          :options="goods_color_list"
                          transition-show="scale"
                          transition-hide="scale"
                          :label="$t('goods.view_goodslist.goods_color')"
                          :rules="[ val => val && val.length > 0 || error11]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_color" :props="props">
                {{ props.row.goods_color }}
              </q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_shape" :props="props">
                <q-select dense
                          outlined
                          square
                          v-model="editFormData.goods_shape"
                          :options="goods_shape_list"
                          transition-show="scale"
                          transition-hide="scale"
                          :label="$t('goods.view_goodslist.goods_shape')"
                          :rules="[ val => val && val.length > 0 || error12]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_shape" :props="props">
                {{ props.row.goods_shape }}
              </q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_specs" :props="props">
                <q-select dense
                          outlined
                          square
                          v-model="editFormData.goods_specs"
                          :options="goods_specs_list"
                          transition-show="scale"
                          transition-hide="scale"
                          :label="$t('goods.view_goodslist.goods_specs')"
                          :rules="[ val => val && val.length > 0 || error13]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_specs" :props="props">
                {{ props.row.goods_specs }}
              </q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_origin" :props="props">
                <q-select dense
                          outlined
                          square
                          v-model="editFormData.goods_origin"
                          :options="goods_origin_list"
                          transition-show="scale"
                          transition-hide="scale"
                          :label="$t('goods.view_goodslist.goods_origin')"
                          :rules="[ val => val && val.length > 0 || error14]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_origin" :props="props">
                {{ props.row.goods_origin }}
              </q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_cost" :props="props">
                <q-input dense
                         outlined
                         square
                         v-model.number="editFormData.goods_cost"
                         type="number"
                         :label="$t('goods.view_goodslist.goods_cost')"
                         :rules="[ val => val && val > 0 || error15]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_cost" :props="props">
                {{ props.row.goods_cost }}
              </q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_price" :props="props">
                <q-input dense
                         outlined
                         square
                         v-model.number="editFormData.goods_price"
                         type="number"
                         :label="$t('goods.view_goodslist.goods_price')"
                         :rules="[ val => val && val > 0 || error16]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_price" :props="props">
                {{ props.row.goods_price }}
              </q-td>
            </template>
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
          <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
            {{ $t('previous') }}
          </q-tooltip>
        </q-btn>
      </div>
    </template>
  </div>
</template>
<router-view />

<script>
import { getauth, postauth, putauth, deleteauth, getfile } from 'boot/axios_request'
import { date, exportFile, LocalStorage } from 'quasar'
var sendCommandResults = 'false'
var scans = []

function sendCommand (extraName, extraValue) {
  console.log('Sending Command: ' + extraName + ', ' + JSON.stringify(extraValue))
  var broadcastExtras = {}
  broadcastExtras[extraName] = extraValue
  broadcastExtras.SEND_RESULT = sendCommandResults
  window.plugins.intentShim.sendBroadcast({
    action: 'com.symbol.datawedge.api.ACTION',
    extras: broadcastExtras
  },
  function () { },
  function () { }
  )
}

function unregisterBroadcastReceiver () {
  window.plugins.intentShim.unregisterBroadcastReceiver()
}
function commandReceived (commandText) {
  document.getElementById('info_lastApiMessage').innerHTML = commandText
}
function enumerateScanners (enumeratedScanners) {
  var humanReadableScannerList = ''
  for (var i = 0; i < enumeratedScanners.length; i++) {
    console.log('Scanner found: name= ' + enumeratedScanners[i].SCANNER_NAME + ', id=' + enumeratedScanners[i].SCANNER_INDEX + ', connected=' + enumeratedScanners[i].SCANNER_CONNECTION_STATE)
    humanReadableScannerList += enumeratedScanners[i].SCANNER_NAME
    if (i < enumeratedScanners.length - 1) { humanReadableScannerList += ', ' }
  }
  document.getElementById('info_availableScanners').innerHTML = humanReadableScannerList
}
function activeProfile (theActiveProfile) {
  document.getElementById('info_activeProfile').innerHTML = theActiveProfile
}
function barcodeScanned (scanData, timeOfScan) {
  var scannedData = scanData.extras['com.symbol.datawedge.data_string']
  var scannedType = scanData.extras['com.symbol.datawedge.label_type']
  console.log('Scan: ' + scannedData)
  scans.unshift({ data: scannedData, decoder: scannedType, timeAtDecode: timeOfScan })
  console.log(scans)
  var scanDisplay = ''
  for (var i = 0; i < scans.length; i++) {
    scanDisplay += '<b><small>' + scans[i].decoder + ' (' + scans[i].timeAtDecode + ')</small></b><br>' + scans[i].data + '<br><br>'
  }
  document.getElementById('scannedBarcodes').innerHTML = scanDisplay
}
export default {
  name: 'Pagegoodslist',
  data () {
    return {
      goods_code: '',
      goods_desc: '',
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'goods/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      viewForm: false,
      printObj: {
        id: 'printMe',
        popTitle: this.$t('inbound.asn')
      },
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
      },
      newForm: false,
      newFormData: {
        goods_code: '',
        goods_desc: '',
        goods_supplier: '',
        goods_weight: '',
        goods_w: '',
        goods_d: '',
        goods_h: '',
        goods_unit: '',
        goods_class: '',
        goods_brand: '',
        goods_color: '',
        goods_shape: '',
        goods_specs: '',
        goods_origin: '',
        goods_cost: '',
        goods_price: '',
        creater: ''
      },
      editid: 0,
      editFormData: {},
      editMode: false,
      deleteForm: false,
      deleteid: 0,
      bar_code: '',
      error1: this.$t('goods.view_goodslist.error1'),
      error2: this.$t('goods.view_goodslist.error2'),
      error3: this.$t('goods.view_goodslist.error3'),
      error4: this.$t('goods.view_goodslist.error4'),
      error5: this.$t('goods.view_goodslist.error5'),
      error6: this.$t('goods.view_goodslist.error6'),
      error7: this.$t('goods.view_goodslist.error7'),
      error8: this.$t('goods.view_unit.error1'),
      error9: this.$t('goods.view_class.error1'),
      error10: this.$t('goods.view_brand.error1'),
      error11: this.$t('goods.view_color.error1'),
      error12: this.$t('goods.view_shape.error1'),
      error13: this.$t('goods.view_specs.error1'),
      error14: this.$t('goods.view_origin.error1'),
      error15: this.$t('goods.view_goodslist.error8'),
      error16: this.$t('goods.view_goodslist.error9'),
      scandata: ''
    }
  },
  methods: {
    getList () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname + '?goodscode=' + _this.scandata, {
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
    },
    newDataSubmit () {
      var _this = this
      _this.newFormData.creater = _this.login_name
      postauth(_this.pathname, _this.newFormData).then(res => {
        _this.getList()
        _this.newDataCancel()
        _this.$q.notify({
          message: 'Success Create',
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
    },
    newDataCancel () {
      var _this = this
      _this.newForm = false
      _this.newFormData = {
        goods_code: '',
        goods_desc: '',
        goods_supplier: '',
        goods_weight: '',
        goods_w: '',
        goods_d: '',
        goods_h: '',
        goods_unit: '',
        goods_class: '',
        goods_brand: '',
        goods_color: '',
        goods_shape: '',
        goods_specs: '',
        goods_origin: '',
        goods_cost: '',
        goods_price: '',
        creater: ''
      }
    },
    editData (e) {
      var _this = this
      _this.editMode = true
      _this.editid = e.id
      _this.editFormData = {
        goods_code: e.goods_code,
        goods_desc: e.goods_desc,
        goods_supplier: e.goods_supplier,
        goods_weight: e.goods_weight,
        goods_w: e.goods_w,
        goods_d: e.goods_d,
        goods_h: e.goods_h,
        goods_unit: e.goods_unit,
        goods_class: e.goods_class,
        goods_brand: e.goods_brand,
        goods_color: e.goods_color,
        goods_shape: e.goods_shape,
        goods_specs: e.goods_specs,
        goods_origin: e.goods_origin,
        goods_cost: e.goods_cost,
        goods_price: e.goods_price,
        creater: _this.login_name,
        bar_code: e.bar_code
      }
    },
    editDataSubmit () {
      var _this = this
      putauth(_this.pathname + _this.editid + '/', _this.editFormData).then(res => {
        _this.editDataCancel()
        _this.getList()
        _this.$q.notify({
          message: 'Success Edit Data',
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
    },
    editDataCancel () {
      var _this = this
      _this.editMode = false
      _this.editid = 0
      _this.editFormData = {
        goods_code: '',
        goods_desc: '',
        goods_supplier: '',
        goods_weight: '',
        goods_w: '',
        goods_d: '',
        goods_h: '',
        goods_unit: '',
        goods_class: '',
        goods_brand: '',
        goods_color: '',
        goods_shape: '',
        goods_specs: '',
        goods_origin: '',
        goods_cost: '',
        goods_price: '',
        creater: ''
      }
    },
    deleteData (e) {
      var _this = this
      _this.deleteForm = true
      _this.deleteid = e
    },
    deleteDataSubmit () {
      var _this = this
      deleteauth(_this.pathname + _this.deleteid + '/').then(res => {
        _this.deleteDataCancel()
        _this.getList()
        _this.$q.notify({
          message: 'Success Edit Data',
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
    },
    deleteDataCancel () {
      var _this = this
      _this.deleteForm = false
      _this.deleteid = 0
    },
    downloadData () {
      var _this = this
      getfile(_this.pathname + 'file/?lang=' + LocalStorage.getItem('lang')).then(res => {
        var timeStamp = Date.now()
        var formattedString = date.formatDate(timeStamp, 'YYYYMMDDHHmmssSSS')
        const status = exportFile(
          _this.pathname + formattedString + '.csv',
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
    viewData (e) {
      var _this = this
      var QRCode = require('qrcode')
      QRCode.toDataURL(e.goods_code, [{
        errorCorrectionLevel: 'H',
        mode: 'byte',
        version: '2',
        type: 'image/jpeg'
      }]
      ).then(url => {
        _this.goods_code = e.goods_code
        _this.goods_desc = e.goods_desc
        _this.bar_code = url
      }).catch(err => {
        console.error(err)
      })
      _this.viewForm = true
    }
  },
  reFresh () {
    var _this = this
    _this.getList()
  },
  updateBatteryStatus (status) {
    this.batteryStatus = `Level: ${status.level}, plugged: ${status.isPlugged}`
  },
  scanEvents () {
    var _this = this
    document.addEventListener('deviceready', _this.onDeviceReady, false)
  },
  onDeviceReady () {
    this.receivedEvent('deviceready')
    document.getElementById('scanButton').addEventListener('touchstart', this.startSoftTrigger)
    document.getElementById('scanButton').addEventListener('click', this.startSoftTrigger)
    // document.getElementById('disableScanningButton').addEventListener('click', this.disableEnableScanning)
    document.getElementById('scanButton').addEventListener('touchend', this.stopSoftTrigger)
    document.getElementById('scanButton').style.display = 'none'
    document.getElementById('header_lastApiMessage').style.display = 'none'
    document.getElementById('info_lastApiMessage').style.display = 'none'
    document.getElementById('chk_ean8').disabled = true
    document.getElementById('chk_ean13').disabled = true
    document.getElementById('chk_code39').disabled = true
    document.getElementById('chk_code128').disabled = true
    this.registerBroadcastReceiver()
    this.determineVersion()
  },
  onPause: function () {
    console.log('Paused')
    unregisterBroadcastReceiver()
  },
  onResume () {
    console.log('Resumed')
    this.registerBroadcastReceiver()
  },
  receivedEvent (id) {
    console.log('Received Event: ' + id)
  },
  startSoftTrigger () {
    sendCommand('com.symbol.datawedge.api.SOFT_SCAN_TRIGGER', 'START_SCANNING')
  },
  stopSoftTrigger () {
    sendCommand('com.symbol.datawedge.api.SOFT_SCAN_TRIGGER', 'STOP_SCANNING')
  },
  determineVersion () {
    sendCommand('com.symbol.datawedge.api.GET_VERSION_INFO', '')
  },
  setDecoders () {
    var ean8Decoder = '' + document.getElementById('chk_ean8').checked
    var ean13Decoder = '' + document.getElementById('chk_ean13').checked
    var code39Decoder = '' + document.getElementById('chk_code39').checked
    var code128Decoder = '' + document.getElementById('chk_code128').checked
    //  Set the new configuration
    var profileConfig = {
      PROFILE_NAME: 'wms',
      PROFILE_ENABLED: 'true',
      CONFIG_MODE: 'UPDATE',
      PLUGIN_CONFIG: {
        PLUGIN_NAME: 'BARCODE',
        PARAM_LIST: {
          // "current-device-id": this.selectedScannerId,
          scanner_selection: 'auto',
          decoder_ean8: '' + ean8Decoder,
          decoder_ean13: '' + ean13Decoder,
          decoder_code128: '' + code128Decoder,
          decoder_code39: '' + code39Decoder
        }
      }
    }
    sendCommand('com.symbol.datawedge.api.SET_CONFIG', profileConfig)
  },
  registerBroadcastReceiver () {
    window.plugins.intentShim.registerBroadcastReceiver({
      filterActions: [
        'com.greaterwms.app.ACTION',
        'com.symbol.datawedge.api.RESULT_ACTION'
      ],
      filterCategories: [
        'android.intent.category.DEFAULT'
      ]
    },
    function (intent) {
      console.log('Received Intent: ' + JSON.stringify(intent))
      // eslint-disable-next-line no-prototype-builtins
      if (intent.extras.hasOwnProperty('RESULT_INFO')) {
        var commandResult = intent.extras.RESULT + ' (' +
            intent.extras.COMMAND.substring(intent.extras.COMMAND.lastIndexOf('.') + 1, intent.extras.COMMAND.length) + ')'// + JSON.stringify(intent.extras.RESULT_INFO);
        commandReceived(commandResult.toLowerCase())
      }
      // eslint-disable-next-line no-prototype-builtins
      if (intent.extras.hasOwnProperty('com.symbol.datawedge.api.RESULT_GET_VERSION_INFO')) {
        //  The version has been returned (DW 6.3 or higher).  Includes the DW version along with other subsystem versions e.g MX
        var versionInfo = intent.extras['com.symbol.datawedge.api.RESULT_GET_VERSION_INFO']
        console.log('Version Info: ' + JSON.stringify(versionInfo))
        var datawedgeVersion = versionInfo.DATAWEDGE
        console.log('Datawedge version: ' + datawedgeVersion)
        //  Fire events sequentially so the application can gracefully degrade the functionality available on earlier DW versions
        if (datawedgeVersion >= '6.3') {
          console.log('Datawedge 6.3 APIs are available')
          //  Create a profile for our application
          sendCommand('com.symbol.datawedge.api.CREATE_PROFILE', 'wms')
          document.getElementById('info_datawedgeVersion').innerHTML = '6.3.  Please configure profile manually.  See ReadMe for more details.'
          //  Although we created the profile we can only configure it with DW 6.4.
          sendCommand('com.symbol.datawedge.api.GET_ACTIVE_PROFILE', '')
          //  Enumerate the available scanners on the device
          sendCommand('com.symbol.datawedge.api.ENUMERATE_SCANNERS', '')
          //  Functionality of the scan button is available
          document.getElementById('scanButton').style.display = 'block'
        }
        if (datawedgeVersion >= '6.4') {
          console.log('Datawedge 6.4 APIs are available')
          //  Documentation states the ability to set a profile config is only available from DW 6.4.
          //  For our purposes, this includes setting the decoders and configuring the associated app / output params of the profile.
          document.getElementById('info_datawedgeVersion').innerHTML = '6.4.'
          document.getElementById('info_datawedgeVersion').classList.remove('attention')
          //  Decoders are now available
          document.getElementById('chk_ean8').disabled = false
          document.getElementById('chk_ean13').disabled = false
          document.getElementById('chk_code39').disabled = false
          document.getElementById('chk_code128').disabled = false
          //  Configure the created profile (associated app and keyboard plugin)
          var profileConfig = {
            PROFILE_NAME: 'wms',
            PROFILE_ENABLED: 'true',
            CONFIG_MODE: 'UPDATE',
            PLUGIN_CONFIG: {
              PLUGIN_NAME: 'BARCODE',
              RESET_CONFIG: 'true',
              PARAM_LIST: {}
            },
            APP_LIST: [{
              PACKAGE_NAME: 'com.greaterwms.app',
              ACTIVITY_LIST: ['*']
            }]
          }
          sendCommand('com.symbol.datawedge.api.SET_CONFIG', profileConfig)
          //  Configure the created profile (intent plugin)
          var profileConfig2 = {
            PROFILE_NAME: 'wms',
            PROFILE_ENABLED: 'true',
            CONFIG_MODE: 'UPDATE',
            PLUGIN_CONFIG: {
              PLUGIN_NAME: 'INTENT',
              RESET_CONFIG: 'true',
              PARAM_LIST: {
                intent_output_enabled: 'true',
                intent_action: 'com.greaterwms.app.ACTION',
                intent_delivery: '2'
              }
            }
          }
          sendCommand('com.symbol.datawedge.api.SET_CONFIG', profileConfig2)
          //  Give some time for the profile to settle then query its value
          setTimeout(function () {
            sendCommand('com.symbol.datawedge.api.GET_ACTIVE_PROFILE', '')
          }, 1000)
        }
        if (datawedgeVersion >= '6.5') {
          console.log('Datawedge 6.5 APIs are available')
          document.getElementById('info_datawedgeVersion').innerHTML = '6.5 or higher.'
          //  Instruct the API to send
          sendCommandResults = 'true'
          document.getElementById('header_lastApiMessage').style.display = 'block'
          document.getElementById('info_lastApiMessage').style.display = 'block'
        }
        // eslint-disable-next-line no-prototype-builtins
      } else if (intent.extras.hasOwnProperty('com.symbol.datawedge.api.RESULT_ENUMERATE_SCANNERS')) {
        //  Return from our request to enumerate the available scanners
        var enumeratedScannersObj = intent.extras['com.symbol.datawedge.api.RESULT_ENUMERATE_SCANNERS']
        enumerateScanners(enumeratedScannersObj)
        // eslint-disable-next-line no-prototype-builtins
      } else if (intent.extras.hasOwnProperty('com.symbol.datawedge.api.RESULT_GET_ACTIVE_PROFILE')) {
        //  Return from our request to obtain the active profile
        var activeProfileObj = intent.extras['com.symbol.datawedge.api.RESULT_GET_ACTIVE_PROFILE']
        activeProfile(activeProfileObj)
        // eslint-disable-next-line no-prototype-builtins
      } else if (!intent.extras.hasOwnProperty('RESULT_INFO')) {
        //  A barcode has been scanned
        barcodeScanned(intent, new Date().toLocaleString())
      }
    }
    )
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
  },
  updated () {
  },
  destroyed () {
  }
}
</script>
