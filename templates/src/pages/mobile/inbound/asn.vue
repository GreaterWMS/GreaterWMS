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
            <q-btn
              :label="$t('refresh')"
              @click="reFresh()"
            >
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('refreshtip') }}</q-tooltip>
            </q-btn>
          </q-btn-group>
          <q-space />
          <q-input outlined rounded dense debounce="300" color="primary" v-model="filter" :placeholder="$t('search')" @blur="getSearchList()" @keyup.enter="getSearchList()">
          </q-input>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td key="asn_code" :props="props">{{ props.row.asn_code }}</q-td>
            <q-td key="asn_status" :props="props">{{ props.row.asn_status }}</q-td>
            <q-td key="total_weight" :props="props">{{ props.row.total_weight.toFixed(4) }}</q-td>
            <q-td key="total_volume" :props="props">{{ props.row.total_volume.toFixed(4) }}</q-td>
            <q-td key="supplier" :props="props">{{ props.row.supplier }}</q-td>
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
import { getauth, postauth, putauth, deleteauth, ViewPrintAuth, getfile } from 'boot/axios_request';
import { date, exportFile, SessionStorage, LocalStorage } from 'quasar';

export default {
  name: 'Pageasnlist',
  data() {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'asn/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      viewprint_table: [],
      bar_code: '',
      warehouse_detail: {},
      supplier_list: [],
      supplier_detail: {},
      columns: [
        { name: 'asn_code', required: true, label: this.$t('inbound.view_asn.asn_code'), align: 'left', field: 'asn_code' },
        { name: 'asn_status', label: this.$t('inbound.view_asn.asn_status'), field: 'asn_status', align: 'center' },
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
      options1: [],
      isEdit: false,
      listNumber: '',
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
      goodsData3: { code: '', qty: '' },
      goodsData4: { code: '', qty: '' },
      goodsData5: { code: '', qty: '' },
      goodsData6: { code: '', qty: '' },
      goodsData7: { code: '', qty: '' },
      goodsData8: { code: '', qty: '' },
      goodsData9: { code: '', qty: '' },
      goodsData10: { code: '', qty: '' },
      editid: 0,
      editFormData: {},
      sortedForm: false,
      sortedid: 0,
      sorted_list: {
        asn_code: '',
        supplier: '',
        goodsData: [],
        creater: ''
      },
      deleteForm: false,
      deleteid: 0,
      preloadForm: false,
      preloadid: 0,
      presortForm: false,
      presortid: 0,
      viewForm: false,
      viewAsn: '',
      viewid: 0,
      printObj: {
        id: 'printMe',
        popTitle: this.$t('inbound.asn')
      },
      devi: window.device,
      error1: this.$t('baseinfo.view_supplier.error1'),
      goodsListData: []
    };
  },
  methods: {
    getList() {
      var _this = this;
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname + 'list/', {})
          .then(res => {
            _this.table_list = [];
            res.results.forEach(item => {
              if (item.asn_status === 1) {
                item.asn_status = _this.$t('inbound.predeliverystock');
              } else if (item.asn_status === 2) {
                item.asn_status = _this.$t('inbound.preloadstock');
              } else if (item.asn_status === 3) {
                item.asn_status = _this.$t('inbound.presortstock');
              } else if (item.asn_status === 4) {
                item.asn_status = _this.$t('inbound.sortstock');
              } else if (item.asn_status === 5) {
                item.asn_status = _this.$t('inbound.asndone');
              } else {
                item.asn_status = 'N/A';
              }
              _this.table_list.push(item);
            });
            _this.supplier_list = res.supplier_list;
            _this.pathname_previous = res.previous;
            _this.pathname_next = res.next;
            _this.goodsListData = res.results;
            console.log(this.goodsListData, 777);
          })
          .catch(err => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            });
          });
      } else {
      }
    },
    getSearchList() {
      var _this = this;
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname + 'list/?asn_code__icontains=' + _this.filter, {})
          .then(res => {
            _this.table_list = [];
            res.results.forEach(item => {
              if (item.asn_status === 1) {
                item.asn_status = _this.$t('inbound.predeliverystock');
              } else if (item.asn_status === 2) {
                item.asn_status = _this.$t('inbound.preloadstock');
              } else if (item.asn_status === 3) {
                item.asn_status = _this.$t('inbound.presortstock');
              } else if (item.asn_status === 4) {
                item.asn_status = _this.$t('inbound.sortstock');
              } else if (item.asn_status === 5) {
                item.asn_status = _this.$t('inbound.asndone');
              } else {
                item.asn_status = 'N/A';
              }
              _this.table_list.push(item);
            });
            _this.supplier_list = res.supplier_list;
            _this.pathname_previous = res.previous;
            _this.pathname_next = res.next;
          })
          .catch(err => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            });
          });
      } else {
      }
    },
    getListPrevious() {
      var _this = this;
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname_previous, {})
          .then(res => {
            _this.table_list = [];
            res.results.forEach(item => {
              if (item.asn_status === 1) {
                item.asn_status = _this.$t('inbound.predeliverystock');
              } else if (item.asn_status === 2) {
                item.asn_status = _this.$t('inbound.preloadstock');
              } else if (item.asn_status === 3) {
                item.asn_status = _this.$t('inbound.presortstock');
              } else if (item.asn_status === 4) {
                item.asn_status = _this.$t('inbound.sortstock');
              } else if (item.asn_status === 5) {
                item.asn_status = _this.$t('inbound.asndone');
              } else {
                item.asn_status = 'N/A';
              }
              _this.table_list.push(item);
            });
            _this.supplier_list = res.supplier_list;
            _this.pathname_previous = res.previous;
            _this.pathname_next = res.next;
          })
          .catch(err => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            });
          });
      } else {
      }
    },
    getListNext() {
      var _this = this;
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname_next, {})
          .then(res => {
            _this.table_list = [];
            res.results.forEach(item => {
              if (item.asn_status === 1) {
                item.asn_status = _this.$t('inbound.predeliverystock');
              } else if (item.asn_status === 2) {
                item.asn_status = _this.$t('inbound.preloadstock');
              } else if (item.asn_status === 3) {
                item.asn_status = _this.$t('inbound.presortstock');
              } else if (item.asn_status === 4) {
                item.asn_status = _this.$t('inbound.sortstock');
              } else if (item.asn_status === 5) {
                item.asn_status = _this.$t('inbound.asndone');
              } else {
                item.asn_status = 'N/A';
              }
              _this.table_list.push(item);
            });
            _this.supplier_list = res.supplier_list;
            _this.pathname_previous = res.previous;
            _this.pathname_next = res.next;
          })
          .catch(err => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            });
          });
      } else {
      }
    },
    reFresh() {
      var _this = this;
      _this.table_list = [];
      _this.getList();
    },
    newFormOpen() {
      var _this = this;
      _this.isEdit = false;
      _this.goodsDataClear();
      _this.newForm = true;
      _this.newAsn.creater = _this.login_name;
      postauth(_this.pathname + 'list/', _this.newAsn)
        .then(res => {
          if (!res.detail) {
            _this.newFormData.asn_code = res.asn_code;
          }
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          });
        });
    },
    newDataSubmit() {
      var _this = this;
      _this.newFormData.creater = _this.login_name;
      let cancelRequest = false;
      for (let i = 0; i < 10; i++) {
        let goodsData = `goodsData${i + 1}`;
        if (_this[goodsData].code !== '' && _this[goodsData].qty !== '') {
          if (_this[goodsData].qty < 1) {
            _this.$q.notify({
              message: 'Total Quantity Must Be Positive Integer',
              icon: 'close',
              color: 'negative'
            });
            cancelRequest = true;
            break;
          } else {
            _this.newFormData.goods_code[i] = _this[goodsData].code;
            _this.newFormData.goods_qty[i] = _this[goodsData].qty;
          }
        }
      }
      if (!_this.newFormData.supplier) {
        cancelRequest = true;
        _this.$q.notify({
          message: 'Supplier Does Not Exists',
          icon: 'close',
          color: 'negative'
        });
      }
      if (!cancelRequest) {
        postauth(_this.pathname + 'detail/', _this.newFormData)
          .then(res => {
            _this.table_list = [];
            _this.getList();
            _this.newDataCancel();
            if (res.detail === 'success') {
              _this.$q.notify({
                message: 'Success Create',
                icon: 'check',
                color: 'green'
              });
            }
          })
          .catch(err => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            });
          });
      }
    },
    newDataCancel() {
      var _this = this;
      _this.newForm = false;
      _this.newFormData = {
        asn_code: '',
        supplier: '',
        goods_code: [],
        goods_qty: [],
        creater: ''
      };
      _this.goodsDataClear();
    },
    goodsDataClear() {
      var _this = this;
      for (let i = 1; i <= 10; i++) {
        _this[`goodsData${i}`] = { code: '', qty: '' };
      }
    },
    editData(e) {
      var _this = this;
      _this.isEdit = true;
      _this.goodsDataClear();
      if (e.asn_status !== _this.$t('inbound.predeliverystock')) {
        _this.$q.notify({
          message: e.asn_code + ' ASN Status Is Not ' + _this.$t('inbound.predeliverystock'),
          icon: 'close',
          color: 'negative'
        });
      } else {
        _this.newFormData.asn_code = e.asn_code;
        _this.newFormData.supplier = e.supplier;
        getauth(_this.pathname + 'detail/?asn_code=' + e.asn_code).then(res => {
          _this.newForm = true;
          _this.editid = e.id;
          res.results.forEach((detail, index) => {
            _this[`goodsData${index + 1}`] = { code: detail.goods_code, qty: detail.goods_qty };
          });
        });
      }
    },
    editDataSubmit() {
      var _this = this;
      _this.newFormData.creater = _this.login_name;
      let cancelRequest = false;
      for (let i = 0; i < 10; i++) {
        let goodsData = `goodsData${i + 1}`;
        if (_this[goodsData].code !== '' && _this[goodsData].qty !== '') {
          if (_this[goodsData].qty <= 0) {
            _this.$q.notify({
              message: 'Total Quantity Must Be Positive',
              icon: 'close',
              color: 'negative'
            });
            cancelRequest = true;
            break;
          } else {
            _this.newFormData.goods_code[i] = _this[goodsData].code;
            _this.newFormData.goods_qty[i] = _this[goodsData].qty;
          }
        }
      }
      if (!cancelRequest) {
        putauth(_this.pathname + 'detail/', _this.newFormData)
          .then(res => {
            _this.table_list = [];
            _this.editDataCancel();
            _this.getList();
            if (res.detail === 'success') {
              _this.$q.notify({
                message: 'Success Edit Data',
                icon: 'check',
                color: 'green'
              });
            }
          })
          .catch(err => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            });
          });
      }
    },
    editDataCancel() {
      var _this = this;
      _this.newForm = false;
      _this.editid = 0;
      _this.newFormData = {
        asn_code: '',
        supplier: '',
        goods_code: [],
        goods_qty: [],
        creater: ''
      };
      _this.goodsDataClear();
    },
    deleteData(e) {
      var _this = this;
      if (e.asn_status !== _this.$t('inbound.predeliverystock')) {
        _this.$q.notify({
          message: e.asn_code + ' ASN Status Is Not ' + _this.$t('inbound.predeliverystock'),
          icon: 'close',
          color: 'negative'
        });
      } else {
        _this.deleteForm = true;
        _this.deleteid = e.id;
      }
    },
    deleteDataSubmit() {
      var _this = this;
      deleteauth(_this.pathname + 'list/' + _this.deleteid + '/')
        .then(res => {
          _this.table_list = [];
          _this.deleteDataCancel();
          _this.getList();
          if (!res.data) {
            _this.$q.notify({
              message: 'Success Delete Data',
              icon: 'check',
              color: 'green'
            });
          }
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          });
        });
    },
    deleteDataCancel() {
      var _this = this;
      _this.deleteForm = false;
      _this.deleteid = 0;
    },
    preloadData(e) {
      var _this = this;
      if (e.asn_status !== _this.$t('inbound.predeliverystock')) {
        _this.$q.notify({
          message: e.asn_code + ' ASN Status Is Not ' + _this.$t('inbound.predeliverystock'),
          icon: 'close',
          color: 'negative'
        });
      } else {
        _this.preloadForm = true;
        _this.preloadid = e.id;
      }
    },
    preloadDataSubmit() {
      var _this = this;
      postauth(_this.pathname + 'preload/' + _this.preloadid + '/', {})
        .then(res => {
          _this.table_list = [];
          _this.preloadDataCancel();
          _this.getList();
          if (!res.detail) {
            _this.$q.notify({
              message: 'Success Confirm ASN Delivery',
              icon: 'check',
              color: 'green'
            });
          }
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          });
        });
    },
    preloadDataCancel() {
      var _this = this;
      _this.preloadForm = false;
      _this.preloadid = 0;
    },
    presortData(e) {
      var _this = this;
      if (e.asn_status !== _this.$t('inbound.preloadstock')) {
        _this.$q.notify({
          message: e.asn_code + ' ASN Status Is Not ' + _this.$t('inbound.preloadstock'),
          icon: 'close',
          color: 'negative'
        });
      } else {
        _this.presortForm = true;
        _this.presortid = e.id;
      }
    },
    presortDataSubmit() {
      var _this = this;
      postauth(_this.pathname + 'presort/' + _this.presortid + '/', {})
        .then(res => {
          _this.table_list = [];
          _this.presortDataCancel();
          _this.getList();
          if (!res.detail) {
            _this.$q.notify({
              message: 'Success Load ASN',
              icon: 'check',
              color: 'green'
            });
          }
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          });
        });
    },
    presortDataCancel() {
      var _this = this;
      _this.presortForm = false;
      _this.presortid = 0;
    },
    getFocus(number) {
      this.listNumber = number;
    },
    setOptions(val) {
      let _this = this;
      if (!val) {
        this[`goodsData${this.listNumber}`].code = '';
      }
      const needle = val.toLowerCase();
      getauth('goods/?goods_code__icontains=' + needle).then(res => {
        const goodscodelist = [];
        for (let i = 0; i < res.results.length; i++) {
          goodscodelist.push(res.results[i].goods_code);
          if (this.listNumber) {
            if (res.results[i].goods_code === val) {
              this[`goodsData${this.listNumber}`].code = val;
            }
          }
        }
        _this.options1 = goodscodelist;
      });
    },
    filterFn(val, update, abort) {
      if (val.length < 1) {
        abort();
        return;
      }
      update(() => {
        this.options = this.options1;
      });
    },
    sortedData(e) {
      var _this = this;
      _this.goodsDataClear();
      if (e.asn_status !== _this.$t('inbound.presortstock')) {
        _this.$q.notify({
          message: e.asn_code + ' ASN Status Is Not ' + _this.$t('inbound.presortstock'),
          icon: 'close',
          color: 'negative'
        });
      } else {
        _this.sorted_list.asn_code = e.asn_code;
        _this.sorted_list.supplier = e.supplier;
        getauth(_this.pathname + 'detail/?asn_code=' + e.asn_code).then(res => {
          _this.sortedForm = true;
          _this.sortedid = e.id;
          _this.sorted_list.goodsData = res.results;
        });
      }
    },
    sortedDataSubmit() {
      var _this = this;
      _this.sorted_list.creater = _this.login_name;
      postauth(_this.pathname + 'sorted/' + _this.sortedid + '/', _this.sorted_list)
        .then(res => {
          _this.table_list = [];
          _this.sortedDataCancel();
          _this.getList();
          if (!res.data) {
            _this.$q.notify({
              message: 'Success Sorted ASN',
              icon: 'check',
              color: 'green'
            });
          }
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          });
        });
    },
    sortedDataCancel() {
      var _this = this;
      _this.sortedForm = false;
      _this.sortedid = 0;
      _this.sorted_list = {
        asn_code: '',
        supplier: '',
        goodsData: [],
        creater: ''
      };
      _this.goodsDataClear();
    },
    viewData(e) {
      var _this = this;
      ViewPrintAuth(_this.pathname + 'viewprint/' + e.id + '/').then(res => {
        _this.viewprint_table = res.asn_detail;
        _this.warehouse_detail = res.warehouse_detail;
        _this.supplier_detail = res.supplier_detail;
        _this.viewAsn = e.asn_code;
        var QRCode = require('qrcode');
        QRCode.toDataURL(e.bar_code, [
          {
            errorCorrectionLevel: 'H',
            mode: 'byte',
            version: '2',
            type: 'image/jpeg'
          }
        ])
          .then(url => {
            _this.bar_code = url;
          })
          .catch(err => {
            console.error(err);
          });
        _this.viewForm = true;
      });
    }
  },
  created() {
    var _this = this;
    if (LocalStorage.has('openid')) {
      _this.openid = LocalStorage.getItem('openid');
    } else {
      _this.openid = '';
      LocalStorage.set('openid', '');
    }
    if (LocalStorage.has('login_name')) {
      _this.login_name = LocalStorage.getItem('login_name');
    } else {
      _this.login_name = '';
      LocalStorage.set('login_name', '');
    }
    if (LocalStorage.has('auth')) {
      _this.authin = '1';
      _this.table_list = [];
      _this.getList();
    } else {
      _this.authin = '0';
    }
    if (SessionStorage.has('goods_code')) {
    } else {
      SessionStorage.set('goods_code', []);
    }
  },
  mounted() {
    var _this = this;
    if (_this.$q.platform.is.electron) {
      _this.height = String(_this.$q.screen.height - 290) + 'px';
    } else {
      _this.height = _this.$q.screen.height - 290 + '' + 'px';
    }
  },
  updated() {},
  destroyed() {}
};
</script>
