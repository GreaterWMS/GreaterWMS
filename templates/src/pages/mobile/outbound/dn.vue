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
            <q-btn :label="$t('refresh')" @click="reFresh()">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('refreshtip') }}</q-tooltip>
            </q-btn>
          </q-btn-group>
          <q-space />
          <q-input outlined rounded dense debounce="300" color="primary" v-model="filter" :placeholder="$t('search')" @blur="getSearchList()" @keyup.enter="getSearchList()">
          </q-input>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td key="dn_code" :props="props">{{ props.row.dn_code }}</q-td>
            <q-td key="dn_status" :props="props">{{ props.row.dn_status }}</q-td>
            <q-td key="total_weight" :props="props">{{ props.row.total_weight.toFixed(4) }}</q-td>
            <q-td key="total_volume" :props="props">{{ props.row.total_volume.toFixed(4) }}</q-td>
            <q-td key="customer" :props="props">{{ props.row.customer }}</q-td>
            <q-td key="creater" :props="props">{{ props.row.creater }}</q-td>
            <q-td key="create_time" :props="props">{{ props.row.create_time }}</q-td>
            <q-td key="update_time" :props="props">{{ props.row.update_time }}</q-td>
            <template v-if="props.row.transportation_fee.detail !== []">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                <q-list>
                  <div v-for="(transportation_fee, index) in props.row.transportation_fee.detail" :key="index">
                    <q-item v-ripple>
                      <q-item-section>
                        <q-item-label>{{ transportation_fee.transportation_supplier }}</q-item-label>
                        <q-item-label>{{ $t('estimate') }}: {{ transportation_fee.transportation_cost }}</q-item-label>
                      </q-item-section>
                    </q-item>
                  </div>
                </q-list>
              </q-tooltip>
            </template>
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
<router-view />

<script>
import { getauth, postauth, putauth, deleteauth, ViewPrintAuth } from 'boot/axios_request'
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
      bar_code: '',
      pickinglist_print_table: [],
      pickinglist_check: 0,
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
        { name: 'update_time', label: this.$t('updatetime'), field: 'update_time', align: 'center' }
      ],
      filter: '',
      pagination: {
        page: 1,
        rowsPerPage: '30'
      },
      newForm: false,
      options1: [],
      isEdit: false,
      listNumber: '',
      options: LocalStorage.getItem('goods_code_list'),
      driver_options: LocalStorage.getItem('driver_name_list'),
      newdn: { creater: '' },
      newFormData: {
        dn_code: '',
        customer: '',
        goods_code: [],
        goods_qty: [],
        creater: ''
      },
      pickFormData: {
        dn_code: '',
        customer: '',
        goodsData: [],
        creater: ''
      },
      goodsData1: { bin: '', code: '', qty: '' },
      goodsData2: { bin: '', code: '', qty: '' },
      goodsData3: { bin: '', code: '', qty: '' },
      goodsData4: { bin: '', code: '', qty: '' },
      goodsData5: { bin: '', code: '', qty: '' },
      goodsData6: { bin: '', code: '', qty: '' },
      goodsData7: { bin: '', code: '', qty: '' },
      goodsData8: { bin: '', code: '', qty: '' },
      goodsData9: { bin: '', code: '', qty: '' },
      goodsData10: { bin: '', code: '', qty: '' },
      editid: 0,
      editFormData: {},
      pickedForm: false,
      pickedid: 0,
      deleteForm: false,
      deleteid: 0,
      neworderForm: false,
      neworderid: 0,
      orderreleaseForm: false,
      orderreleaseid: 0,
      viewForm: false,
      viewPLForm: false,
      viewdn: '',
      viewid: 0,
      dispatchid: 0,
      dispatchForm: false,
      dispatchFormData: {
        dn_code: '',
        driver: ''
      },
      podid: 0,
      podForm: false,
      podFormData: {
        dn_code: '',
        customer: '',
        goodsData: []
      },
      printObj: {
        id: 'printMe',
        popTitle: 'Advance Shipment Notice'
      },
      printPL: {
        id: 'printPL',
        popTitle: 'Picking List'
      },
      error1: this.$t('baseinfo.view_customer.error1'),
      error2: this.$t('notice.valerror'),
      isError1: false,
      isError2: false
    }
  },
  methods: {
    validate1 (val) {
      const reg = /^[1-9]\d*$/g
      const check = reg.test(val)
      if (check) {
        this.isError1 = false
      } else {
        this.isError1 = true
      }
    },
    validate2 (val1, val2) {
      const reg = /^[0-9]\d*$/g
      const check = reg.test(val1)
      if (check && val1 <= val2) {
        this.isError2 = false
      } else {
        this.isError2 = true
      }
    },
    getList () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname + 'list/', {})
          .then(res => {
            _this.table_list = []
            res.results.forEach(item => {
              if (item.dn_status === 1) {
                item.dn_status = _this.$t('outbound.freshorder')
              } else if (item.dn_status === 2) {
                item.dn_status = _this.$t('outbound.neworder')
              } else if (item.dn_status === 3) {
                item.dn_status = _this.$t('outbound.pickstock')
              } else if (item.dn_status === 4) {
                item.dn_status = _this.$t('outbound.pickedstock')
              } else if (item.dn_status === 5) {
                item.dn_status = _this.$t('outbound.shippedstock')
              } else if (item.dn_status === 6) {
                item.dn_status = _this.$t('outbound.received')
              } else {
                item.dn_status = 'N/A'
              }
              _this.table_list.push(item)
            })
            res.results.forEach(item => {
              if (item.asn_status === 1) {
                item.asn_status = _this.$t()
              }
            })
            _this.customer_list = res.customer_list
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
      } else {
      }
    },
    getSearchList () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname + 'list/?dn_code__icontains=' + _this.filter, {})
          .then(res => {
            _this.table_list = []
            res.results.forEach(item => {
              if (item.dn_status === 1) {
                item.dn_status = _this.$t('outbound.freshorder')
              } else if (item.dn_status === 2) {
                item.dn_status = _this.$t('outbound.neworder')
              } else if (item.dn_status === 3) {
                item.dn_status = _this.$t('outbound.pickstock')
              } else if (item.dn_status === 4) {
                item.dn_status = _this.$t('outbound.pickedstock')
              } else if (item.dn_status === 5) {
                item.dn_status = _this.$t('outbound.shippedstock')
              } else if (item.dn_status === 6) {
                item.dn_status = _this.$t('outbound.received')
              } else {
                item.dn_status = 'N/A'
              }
              _this.table_list.push(item)
            })
            _this.customer_list = res.customer_list
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
      } else {
      }
    },
    getListPrevious () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname_previous, {})
          .then(res => {
            _this.table_list = []
            res.results.forEach(item => {
              if (item.dn_status === 1) {
                item.dn_status = _this.$t('outbound.freshorder')
              } else if (item.dn_status === 2) {
                item.dn_status = _this.$t('outbound.neworder')
              } else if (item.dn_status === 3) {
                item.dn_status = _this.$t('outbound.pickstock')
              } else if (item.dn_status === 4) {
                item.dn_status = _this.$t('outbound.pickedstock')
              } else if (item.dn_status === 5) {
                item.dn_status = _this.$t('outbound.shippedstock')
              } else if (item.dn_status === 6) {
                item.dn_status = _this.$t('outbound.received')
              } else {
                item.dn_status = 'N/A'
              }
              _this.table_list.push(item)
            })
            _this.customer_list = res.customer_list
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
      } else {
      }
    },
    getListNext () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname_next, {})
          .then(res => {
            _this.table_list = []
            res.results.forEach(item => {
              if (item.dn_status === 1) {
                item.dn_status = _this.$t('outbound.freshorder')
              } else if (item.dn_status === 2) {
                item.dn_status = _this.$t('outbound.neworder')
              } else if (item.dn_status === 3) {
                item.dn_status = _this.$t('outbound.pickstock')
              } else if (item.dn_status === 4) {
                item.dn_status = _this.$t('outbound.pickedstock')
              } else if (item.dn_status === 5) {
                item.dn_status = _this.$t('outbound.shippedstock')
              } else if (item.dn_status === 6) {
                item.dn_status = _this.$t('outbound.received')
              } else {
                item.dn_status = 'N/A'
              }
              _this.table_list.push(item)
            })
            _this.customer_list = res.customer_list
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
      } else {
      }
    },
    reFresh () {
      var _this = this
      _this.table_list = []
      _this.getList()
    },
    newFormOpen () {
      var _this = this
      _this.isEdit = false
      _this.goodsDataClear()
      _this.newForm = true
      _this.newdn.creater = _this.login_name
      postauth(_this.pathname + 'list/', _this.newdn)
        .then(res => {
          if (!res.detail) {
            _this.newFormData.dn_code = res.dn_code
          }
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    newDataSubmit () {
      var _this = this
      _this.newFormData.creater = _this.login_name
      let cancelRequest = false
      for (let i = 0; i < 10; i++) {
        const goodsData = `goodsData${i + 1}`
        if (_this[goodsData].code !== '' && _this[goodsData].qty !== '') {
          if (_this[goodsData].qty < 1) {
            _this.$q.notify({
              message: 'Total Quantity Must Be Positive Integer',
              icon: 'close',
              color: 'negative'
            })
            cancelRequest = true
            break
          } else {
            _this.newFormData.goods_code[i] = _this[goodsData].code
            _this.newFormData.goods_qty[i] = _this[goodsData].qty
          }
        }
      }
      if (!_this.newFormData.customer) {
        cancelRequest = true
        _this.$q.notify({
          message: 'Supplier Does Not Exists',
          icon: 'close',
          color: 'negative'
        })
      }
      if (!cancelRequest) {
        postauth(_this.pathname + 'detail/', _this.newFormData)
          .then(res => {
            _this.table_list = []
            _this.getList()
            _this.newDataCancel()
            if (res.detail === 'success') {
              _this.$q.notify({
                message: 'Success Create',
                icon: 'check',
                color: 'green'
              })
            }
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
    newDataCancel () {
      var _this = this
      _this.newForm = false
      _this.newFormData = {
        dn_code: '',
        customer: '',
        goods_code: [],
        goods_qty: [],
        creater: ''
      }
      _this.goodsDataClear()
    },
    goodsDataClear () {
      var _this = this
      for (let i = 1; i <= 10; i++) {
        _this[`goodsData${i}`] = { code: '', qty: '' }
      }
    },
    editData (e) {
      var _this = this
      _this.isEdit = true
      _this.goodsDataClear()
      if (e.dn_status !== _this.$t('outbound.freshorder')) {
        _this.$q.notify({
          message: e.dn_code + ' DN Status Not ' + _this.$t('outbound.freshorder'),
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.newFormData.dn_code = e.dn_code
        _this.newFormData.customer = e.customer
        getauth(_this.pathname + 'detail/?dn_code=' + e.dn_code).then(res => {
          _this.newForm = true
          _this.editid = e.id
          res.results.forEach((detail, index) => {
            _this[`goodsData${index + 1}`] = { code: detail.goods_code, qty: detail.goods_qty }
          })
        })
      }
    },
    editDataSubmit () {
      var _this = this
      _this.newFormData.creater = _this.login_name
      let cancelRequest = false
      for (let i = 0; i < 10; i++) {
        const goodsData = `goodsData${i + 1}`
        if (_this[goodsData].code !== '' && _this[goodsData].qty !== '') {
          if (_this[goodsData].qty <= 0) {
            _this.$q.notify({
              message: 'Total Quantity Must Be Positive',
              icon: 'close',
              color: 'negative'
            })
            cancelRequest = true
            break
          } else {
            _this.newFormData.goods_code[i] = _this[goodsData].code
            _this.newFormData.goods_qty[i] = _this[goodsData].qty
          }
        }
      }
      if (!cancelRequest) {
        putauth(_this.pathname + 'detail/', _this.newFormData)
          .then(res => {
            _this.table_list = []
            _this.editDataCancel()
            _this.getList()
            if (!res.detail) {
              _this.$q.notify({
                message: 'Success Edit DN',
                icon: 'check',
                color: 'green'
              })
            }
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
    editDataCancel () {
      var _this = this
      _this.newForm = false
      _this.editid = 0
      _this.newFormData = {
        dn_code: '',
        customer: '',
        goods_code: [],
        goods_qty: [],
        creater: ''
      }
      _this.goodsDataClear()
    },
    deleteData (e) {
      var _this = this
      if (e.dn_status !== _this.$t('outbound.freshorder')) {
        _this.$q.notify({
          message: e.dn_code + ' DN Status Is Not ' + _this.$t('outbound.freshorder'),
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.deleteForm = true
        _this.deleteid = e.id
      }
    },
    deleteDataSubmit () {
      var _this = this
      deleteauth(_this.pathname + 'list/' + _this.deleteid + '/')
        .then(res => {
          _this.table_list = []
          _this.deleteDataCancel()
          _this.getList()
          if (!res.detail) {
            _this.$q.notify({
              message: 'Success Delete DN',
              icon: 'check',
              color: 'green'
            })
          }
        })
        .catch(err => {
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
    neworderData (e) {
      var _this = this
      if (e.dn_status !== _this.$t('outbound.freshorder')) {
        _this.$q.notify({
          message: e.dn_code + ' DN Status Is Not ' + _this.$t('outbound.freshorder'),
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.neworderForm = true
        _this.neworderid = e.id
      }
    },
    neworderDataSubmit () {
      var _this = this
      postauth(_this.pathname + 'neworder/' + _this.neworderid + '/', {})
        .then(res => {
          _this.table_list = []
          _this.neworderDataCancel()
          _this.getList()
          if (!res.detail) {
            _this.$q.notify({
              message: 'Success Confirm DN Delivery',
              icon: 'check',
              color: 'green'
            })
          }
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    neworderDataCancel () {
      var _this = this
      _this.neworderForm = false
      _this.neworderid = 0
    },
    orderreleaseData (e) {
      var _this = this
      if (e.dn_status !== _this.$t('outbound.neworder')) {
        _this.$q.notify({
          message: e.dn_code + ' DN Status Is Not ' + _this.$t('outbound.neworder'),
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.orderreleaseForm = true
        _this.orderreleaseid = e.id
      }
    },
    orderreleaseAllData () {
      var _this = this
      postauth(_this.pathname + 'orderrelease/', {})
        .then(res => {
          _this.table_list = []
          _this.getList()
          if (!res.detail) {
            _this.$q.notify({
              message: 'Success Release All Order',
              icon: 'check',
              color: 'green'
            })
          }
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    orderreleaseDataSubmit () {
      var _this = this
      putauth(_this.pathname + 'orderrelease/' + _this.orderreleaseid + '/', {})
        .then(res => {
          _this.table_list = []
          _this.orderreleaseDataCancel()
          _this.getList()
          if (!res.detail) {
            _this.$q.notify({
              message: 'Success Release DN Code',
              icon: 'check',
              color: 'green'
            })
          }
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    orderreleaseDataCancel () {
      var _this = this
      _this.orderreleaseForm = false
      _this.orderreleaseid = 0
    },
    getFocus (number) {
      this.listNumber = number
    },
    setOptions (val) {
      const _this = this
      if (!val) {
        _this[`goodsData${_this.listNumber}`].code = ''
      }
      const needle = val.toLowerCase()
      getauth('goods/?goods_code__icontains=' + needle).then(res => {
        const goodscodelist = []
        for (let i = 0; i < res.results.length; i++) {
          goodscodelist.push(res.results[i].goods_code)
          if (_this.listNumber) {
            if (res.results[i].goods_code === val) {
              _this[`goodsData${_this.listNumber}`].code = val
            }
          }
        }
        _this.options1 = goodscodelist
      })
    },
    filterFn (val, update, abort) {
      if (val.length < 1) {
        abort()
        return
      }
      update(() => {
        this.options = this.options1
      })
    },
    PrintPickingList (e) {
      var _this = this
      var QRCode = require('qrcode')
      QRCode.toDataURL(e.bar_code, [
        {
          errorCorrectionLevel: 'H',
          mode: 'byte',
          version: '2',
          type: 'image/jpeg'
        }
      ])
        .then(url => {
          _this.bar_code = url
        })
        .catch(err => {
          console.error(err)
        })
      _this.viewPLForm = true
      getauth(_this.pathname + 'pickinglist/' + e.id + '/')
        .then(res => {
          _this.pickinglist_print_table = []
          _this.picklist_check = 0
          res.forEach(item => {
            if (item.picked_qty > 0) {
              _this.picklist_check += 1
            } else {
            }
          })
          _this.pickinglist_print_table = res
          _this.viewPLForm = true
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    pickedData (e) {
      var _this = this
      if (e.dn_status !== _this.$t('outbound.pickstock')) {
        _this.$q.notify({
          message: e.dn_code + ' DN Status Is Not ' + _this.$t('outbound.pickstock'),
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.pickFormData.dn_code = e.dn_code
        _this.pickFormData.customer = e.customer
        getauth(_this.pathname + 'pickinglist/' + e.id + '/').then(res => {
          _this.pickedForm = true
          _this.pickedid = e.id
          _this.pickFormData.goodsData = res
        })
      }
    },
    pickedDataSubmit () {
      var _this = this
      _this.pickFormData.creater = _this.login_name
      postauth(_this.pathname + 'picked/' + _this.pickedid + '/', _this.pickFormData)
        .then(res => {
          _this.table_list = []
          _this.pickedDataCancel()
          _this.getList()
          if (!res.detail) {
            _this.$q.notify({
              message: 'Success Confirm Picking List',
              icon: 'check',
              color: 'green'
            })
          }
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    pickedDataCancel () {
      var _this = this
      _this.pickedForm = false
      _this.pickedid = 0
      _this.pickFormData = {
        dn_code: '',
        customer: '',
        goodsData: [],
        creater: ''
      }
      _this.goodsDataClear()
    },
    viewData (e) {
      var _this = this
      ViewPrintAuth(_this.pathname + 'viewprint/' + e.id + '/').then(res => {
        _this.viewprint_table = res.dn_detail
        _this.warehouse_detail = res.warehouse_detail
        _this.customer_detail = res.customer_detail
        _this.viewdn = e.dn_code
        var QRCode = require('qrcode')
        QRCode.toDataURL(e.bar_code, [
          {
            errorCorrectionLevel: 'H',
            mode: 'byte',
            version: '2',
            type: 'image/jpeg'
          }
        ])
          .then(url => {
            _this.bar_code = url
          })
          .catch(err => {
            console.error(err)
          })
        _this.viewForm = true
      })
    },
    filterFnDispatch (val, update, abort) {
      var _this = this
      if (val.length < 1) {
        abort()
        return
      }
      update(() => {
        const needle = val.toLowerCase()
        getauth('driver/?driver_name__icontains=' + needle)
          .then(res => {
            const drivernamelist = []
            for (let i = 0; i < res.results.length; i++) {
              drivernamelist.push(res.results[i].driver_name)
            }
            LocalStorage.set('driver_name_list', drivernamelist)
            _this.driver_options = LocalStorage.getItem('driver_name_list')
            _this.$forceUpdate()
          })
          .catch(err => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            })
          })
      })
    },
    DispatchDN (e) {
      var _this = this
      if (e.dn_status !== _this.$t('outbound.pickedstock')) {
        _this.$q.notify({
          message: e.dn_code + ' DN Status Is Not ' + _this.$t('outbound.pickedstock'),
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.dispatchFormData.dn_code = e.dn_code
        _this.dispatchid = e.id
        _this.dispatchForm = true
      }
    },
    dispatchDataCancel () {
      var _this = this
      _this.dispatchFormData = { dn_code: '', driver: '' }
      _this.dispatchForm = false
    },
    dispatchDataSubmit () {
      var _this = this
      postauth(_this.pathname + 'dispatch/' + _this.dispatchid + '/', _this.dispatchFormData)
        .then(res => {
          _this.table_list = []
          _this.dispatchDataCancel()
          _this.getList()
          if (!res.detail) {
            _this.$q.notify({
              message: 'Success Dispatch',
              icon: 'check',
              color: 'green'
            })
          }
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    PODData (e) {
      var _this = this
      if (e.dn_status !== _this.$t('outbound.shippedstock')) {
        _this.$q.notify({
          message: e.dn_code + ' DN Status Is Not ' + _this.$t('outbound.shippedstock'),
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.podFormData.dn_code = e.dn_code
        _this.podFormData.customer = e.customer
        getauth(_this.pathname + 'detail/?dn_code=' + e.dn_code).then(res => {
          _this.podForm = true
          _this.podid = e.id
          _this.podFormData.goodsData = res.results
        })
      }
    },
    PODDataCancel () {
      var _this = this
      _this.podForm = false
      _this.podid = 0
      _this.podFormData = {
        dn_code: '',
        customer: '',
        goodsData: []
      }
    },
    PODDataSubmit () {
      var _this = this
      if (!(_this.isError1 || _this.isError2)) {
        postauth(_this.pathname + 'pod/' + _this.podid + '/', _this.podFormData)
          .then(res => {
            _this.table_list = []
            _this.PODDataCancel()
            _this.getList()
            if (!res.detail) {
              _this.$q.notify({
                message: 'Success Dispatch',
                icon: 'check',
                color: 'green'
              })
            }
          })
          .catch(err => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            })
          })
      }
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
      _this.table_list = []
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
      _this.height = String(_this.$q.screen.height - 290) + 'px'
    } else {
      _this.height = _this.$q.screen.height - 290 + '' + 'px'
    }
  },
  updated () {},
  destroyed () {}
}
</script>
