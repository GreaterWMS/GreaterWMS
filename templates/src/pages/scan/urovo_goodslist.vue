<template>
  <q-page>
    <q-card v-show="!fab" class="shadow-24" :style="{ width: width, height: height }">
      <q-card-section style="height: 75px">
        <div class="text-h6">{{ goods_code_label }}</div>
        <div class="text-subtitle2">{{ data_list.goods_code }}</div>
      </q-card-section>
      <q-separator />
      <q-scroll-area :thumb-style="thumbStyle" :bar-style="barStyle" :style="{ height: scroll_height, width: width }">
        <q-list>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_desc_label }}</q-item-label>
              <q-item-label caption>{{ data_list.goods_desc }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_supplier_label }}</q-item-label>
              <q-item-label caption>{{ data_list.goods_supplier }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_weight_label }}</q-item-label>
              <q-item-label caption>{{ data_list.goods_weight }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_w_label }}</q-item-label>
              <q-item-label caption>{{ data_list.goods_w }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_d_label }}</q-item-label>
              <q-item-label caption>{{ data_list.goods_d }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_h_label }}</q-item-label>
              <q-item-label caption>{{ data_list.goods_h }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ unit_volume_label }}</q-item-label>
              <q-item-label caption>{{ data_list.unit_volume }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_unit_label }}</q-item-label>
              <q-item-label caption>{{ data_list.goods_unit }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_class_label }}</q-item-label>
              <q-item-label caption>{{ data_list.goods_class }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_brand_label }}</q-item-label>
              <q-item-label caption>{{ data_list.goods_brand }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_color_label }}</q-item-label>
              <q-item-label caption>{{ data_list.goods_color }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_shape_label }}</q-item-label>
              <q-item-label caption>{{ data_list.goods_shape }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_specs_label }}</q-item-label>
              <q-item-label caption>{{ data_list.goods_specs }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_origin_label }}</q-item-label>
              <q-item-label caption>{{ data_list.goods_origin }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_cost_label }}</q-item-label>
              <q-item-label caption>{{ data_list.goods_cost }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_price_label }}</q-item-label>
              <q-item-label caption>{{ data_list.goods_price }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ creater_label }}</q-item-label>
              <q-item-label caption>{{ data_list.creater }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ create_time_label }}</q-item-label>
              <q-item-label caption>{{ data_list.create_time }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ updatetime_label }}</q-item-label>
              <q-item-label caption>{{ data_list.update_time }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>
      <q-separator dark />
      <q-card-actions><input id="scannedBarcodes" v-model="barscan" type="text" @input="datachange()" readonly disabled /></q-card-actions>
    </q-card>
    <q-page-sticky v-show="device === 2" position="bottom-right" :offset="[18, 18]">
      <q-fab v-model="fab" icon="add" direction="up" color="accent" vertical-actions-align="left">
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_locationquery')"
          label-style="background-color:transparent"
          v-show="device_name === 'Urovo'"
          to="urovo_locationquery"
          :style="{
            'margin-top': fab8.top,
            'margin-bottom': fab8.bottom,
            'margin-left': fab8.left,
            'margin-right': fab8.right,
            height: touchheight,
            width: touchwidth
          }"
        >
          <q-img src="statics/stock/stocklist.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_locationquery')"
          label-style="background-color:transparent"
          v-show="device_name === 'Zebra Technologies'"
          to="zebra_locationquery"
          :style="{
            'margin-top': fab8.top,
            'margin-bottom': fab8.bottom,
            'margin-left': fab8.left,
            'margin-right': fab8.right,
            height: touchheight,
            width: touchwidth
          }"
        >
          <q-img src="statics/stock/stocklist.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_goodsquery')"
          label-style="background-color:transparent"
          v-show="device_name === 'Urovo'"
          to="urovo_goodslist"
          :style="{
            'margin-top': fab7.top,
            'margin-bottom': fab7.bottom,
            'margin-left': fab7.left,
            'margin-right': fab7.right,
            height: touchheight,
            width: touchwidth
          }"
        >
          <q-img src="statics/goods/goodslist.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_goodsquery')"
          label-style="background-color:transparent"
          v-show="device_name === 'Zebra Technologies'"
          to="zebra_goodslist"
          :style="{
            'margin-top': fab7.top,
            'margin-bottom': fab7.bottom,
            'margin-left': fab7.left,
            'margin-right': fab7.right,
            height: touchheight,
            width: touchwidth
          }"
        >
          <q-img src="statics/goods/goodslist.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          icon="img:statics/stock/cyclecount.png"
          :label="$t('scan.scan_inventory')"
          label-style="background-color:transparent"
          v-show="device_name === 'Urovo'"
          to="urovo_cyclecount"
          :style="{
            'margin-top': fab6.top,
            'margin-bottom': fab6.bottom,
            'margin-left': fab6.left,
            'margin-right': fab6.right,
            height: touchheight,
            width: touchwidth
          }"
        >
          <q-img src="statics/stock/cyclecount.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          icon="img:statics/stock/cyclecount.png"
          :label="$t('scan.scan_inventory')"
          label-style="background-color:transparent"
          v-show="device_name === 'Zebra Technologies'"
          to="zebra_cyclecount"
          :style="{
            'margin-top': fab6.top,
            'margin-bottom': fab6.bottom,
            'margin-left': fab6.left,
            'margin-right': fab6.right,
            height: touchheight,
            width: touchwidth
          }"
        >
          <q-img src="statics/stock/cyclecount.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_movetobin')"
          label-style="background-color:transparent"
          v-show="device_name === 'Urovo'"
          to="urovo_movetobin"
          :style="{
            'margin-top': fab5.top,
            'margin-bottom': fab5.bottom,
            'margin-left': fab5.left,
            'margin-right': fab5.right,
            height: touchheight,
            width: touchwidth
          }"
        >
          <q-img src="statics/icons/movetobin.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_movetobin')"
          label-style="background-color:transparent"
          v-show="device_name === 'Zebra Technologies'"
          to="zebra_movetobin"
          :style="{
            'margin-top': fab5.top,
            'margin-bottom': fab5.bottom,
            'margin-left': fab5.left,
            'margin-right': fab5.right,
            height: touchheight,
            width: touchwidth
          }"
        >
          <q-img src="statics/icons/movetobin.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_shipping')"
          label-style="background-color:transparent"
          v-show="device_name === 'Urovo'"
          to="urovo_shipping"
          :style="{
            'margin-top': fab4.top,
            'margin-bottom': fab4.bottom,
            'margin-left': fab4.left,
            'margin-right': fab4.right,
            height: touchheight,
            width: touchwidth
          }"
        >
          <q-img src="statics/icons/car.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_shipping')"
          label-style="background-color:transparent"
          v-show="device_name === 'Zebra Technologies'"
          to="zebra_shipping"
          :style="{
            'margin-top': fab4.top,
            'margin-bottom': fab4.bottom,
            'margin-left': fab4.left,
            'margin-right': fab4.right,
            height: touchheight,
            width: touchwidth
          }"
        >
          <q-img src="statics/icons/car.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_picking')"
          label-style="background-color:transparent"
          v-show="device_name === 'Urovo'"
          to="urovo_picking"
          :style="{
            'margin-top': fab3.top,
            'margin-bottom': fab3.bottom,
            'margin-left': fab3.left,
            'margin-right': fab3.right,
            height: touchheight,
            width: touchwidth
          }"
        >
          <q-img src="statics/outbound/picked.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_picking')"
          label-style="background-color:transparent"
          v-show="device_name === 'Zebra Technologies'"
          to="zebra_picking"
          :style="{
            'margin-top': fab3.top,
            'margin-bottom': fab3.bottom,
            'margin-left': fab3.left,
            'margin-right': fab3.right,
            height: touchheight,
            width: touchwidth
          }"
        >
          <q-img src="statics/outbound/picked.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_uptobin')"
          label-style="background-color:transparent"
          v-show="device_name === 'Urovo'"
          to="urovo_uptobin"
          :style="{
            'margin-top': fab2.top,
            'margin-bottom': fab2.bottom,
            'margin-left': fab2.left,
            'margin-right': fab2.right,
            height: touchheight,
            width: touchwidth
          }"
        >
          <q-img src="statics/inbound/presortstock.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_uptobin')"
          label-style="background-color:transparent"
          v-show="device_name === 'Zebra Technologies'"
          to="zebra_uptobin"
          :style="{
            'margin-top': fab2.top,
            'margin-bottom': fab2.bottom,
            'margin-left': fab2.left,
            'margin-right': fab2.right,
            height: touchheight,
            width: touchwidth
          }"
        >
          <q-img src="statics/inbound/presortstock.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_sorting')"
          label-style="background-color:transparent"
          v-show="device_name === 'Urovo'"
          to="urovo_sorting"
          :style="{
            'margin-top': fab1.top,
            'margin-bottom': fab1.bottom,
            'margin-left': fab1.left,
            'margin-right': fab1.right,
            height: touchheight,
            width: touchwidth
          }"
        >
          <q-img src="statics/inbound/preloadstock.png" />
        </q-fab-action>
        <q-fab-action
          square
          flat
          external-label
          label-position="bottom"
          label-class="text-black"
          :label="$t('scan.scan_sorting')"
          label-style="background-color:transparent"
          v-show="device_name === 'Zebra Technologies'"
          to="zebra_sorting"
          :style="{
            'margin-top': fab1.top,
            'margin-bottom': fab1.bottom,
            'margin-left': fab1.left,
            'margin-right': fab1.right,
            height: touchheight,
            width: touchwidth
          }"
        >
          <q-img src="statics/inbound/preloadstock.png" />
        </q-fab-action>
      </q-fab>
    </q-page-sticky>
  </q-page>
</template>
<router-view />

<script>
import { getauth } from 'boot/axios_request';

function getDeviceinfo() {
  Uplugin.getDeviceID(
    '',
    function(res) {
      console.log(res);
    },
    function(err) {
      console.log(err);
    }
  );
}

function startBarcode() {
  Uplugin.getBarcode(
    'start',
    function(res) {
      document.getElementById('scannedBarcodes').value = '';
      document.getElementById('scannedBarcodes').value = res;
      document.getElementById('scannedBarcodes').dispatchEvent(new Event('input'));
    },
    function(err) {
      console.log(err);
    }
  );
}

function stopBarcode() {
  Uplugin.getBarcode(
    'stop',
    function(res) {
      console.log(res);
    },
    function(err) {
      console.log(err);
    }
  );
}

export default {
  name: 'Pageurovo_goodslist',
  data() {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'goods/',
      separator: 'cell',
      loading: false,
      height: '',
      width: '',
      scroll_height: '',
      table_list: [],
      data_list: {
        goods_code: '',
        goods_desc: '',
        goods_supplier: '',
        goods_weight: '',
        goods_w: '',
        goods_d: '',
        goods_h: '',
        unit_volume: '',
        goods_unit: '',
        goods_class: '',
        goods_brand: '',
        goods_color: '',
        goods_shape: '',
        goods_specs: '',
        goods_origin: '',
        goods_cost: '',
        goods_price: '',
        creater: '',
        create_time: '',
        update_time: ''
      },
      goods_code_label: this.$t('goods.view_goodslist.goods_code'),
      goods_desc_label: this.$t('goods.view_goodslist.goods_desc'),
      goods_supplier_label: this.$t('goods.view_goodslist.goods_supplier'),
      goods_weight_label: this.$t('goods.view_goodslist.goods_weight'),
      goods_w_label: this.$t('goods.view_goodslist.goods_w'),
      goods_d_label: this.$t('goods.view_goodslist.goods_d'),
      goods_h_label: this.$t('goods.view_goodslist.goods_h'),
      unit_volume_label: this.$t('goods.view_goodslist.unit_volume'),
      goods_unit_label: this.$t('goods.view_goodslist.goods_unit'),
      goods_class_label: this.$t('goods.view_goodslist.goods_class'),
      goods_brand_label: this.$t('goods.view_goodslist.goods_brand'),
      goods_color_label: this.$t('goods.view_goodslist.goods_color'),
      goods_shape_label: this.$t('goods.view_goodslist.goods_shape'),
      goods_specs_label: this.$t('goods.view_goodslist.goods_specs'),
      goods_origin_label: this.$t('goods.view_goodslist.goods_origin'),
      goods_cost_label: this.$t('goods.view_goodslist.goods_cost'),
      goods_price_label: this.$t('goods.view_goodslist.goods_price'),
      creater_label: this.$t('creater'),
      create_time_label: this.$t('createtime'),
      updatetime_label: this.$t('updatetime'),
      thumbStyle: {
        right: '4px',
        borderRadius: '5px',
        backgroundColor: '#E0E0E0',
        width: '5px',
        opacity: 0.75
      },
      barStyle: {
        right: '2px',
        borderRadius: '9px',
        backgroundColor: '#EEEEEE',
        width: '9px',
        opacity: 0.2
      },
      device: 0,
      device_name: '',
      fab: false,
      touchheight: (this.$q.screen.width - 50) / 5 + '' + 'px',
      touchwidth: (this.$q.screen.width - 50) / 5 + '' + 'px',
      fab1: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      fab2: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      fab3: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      fab4: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      fab5: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      fab6: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      fab7: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      fab8: {
        top: '',
        bottom: '',
        left: '',
        right: ''
      },
      batteryStatus: 'determining...',
      barscan: '',
      goods_scan: ''
    };
  },
  methods: {
    datachange() {
      var _this = this;
      stopBarcode();
      if (_this.$q.localStorage.has('auth')) {
        getauth('scanner/?bar_code=' + _this.barscan, {})
          .then(res => {
            _this.barscan = res.results[0].code;
            if (res.results[0].mode === 'GOODS') {
              _this.goods_scan = res.results[0].code;
              _this.getList(res.results[0].code);
            }
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
    getList(e) {
      var _this = this;
      if (_this.$q.localStorage.has('auth')) {
        getauth(_this.pathname + '?goods_code=' + e, {})
          .then(res => {
            _this.table_list = res.results;
            if (_this.table_list[0]) {
              _this.data_list = _this.table_list[0];
            }
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
      _this.barscan = '';
      _this.goods_scan = '';
    },
    updateBatteryStatus(status) {
      var _this = this;
      _this.batteryStatus = `Level: ${status.level}, plugged: ${status.isPlugged}`;
    },
    scanEvents() {
      var _this = this;
      document.addEventListener('deviceready', _this.onDeviceReady, false);
    },
    onDeviceReady() {
      startBarcode();
    },
    onPause: function() {
      stopBarcode();
    },
    onResume() {}
  },
  created() {
    var _this = this;
    if (_this.$q.localStorage.has('openid')) {
      _this.openid = _this.$q.localStorage.getItem('openid');
    } else {
      _this.openid = '';
      _this.$q.localStorage.set('openid', '');
    }
    if (_this.$q.localStorage.has('login_name')) {
      _this.login_name = _this.$q.localStorage.getItem('login_name');
    } else {
      _this.login_name = '';
      _this.$q.localStorage.set('login_name', '');
    }
    if (_this.$q.localStorage.has('auth')) {
      _this.authin = '1';
    } else {
      _this.authin = '0';
    }
  },
  mounted() {
    var _this = this;
    if (window.device) {
      if (window.device.manufacturer === 'Urovo' || window.device.manufacturer === 'Zebra Technologies') {
        _this.device_name = window.device.manufacturer;
        _this.device = 2;
      } else {
        _this.device = 1;
      }
    } else {
      if (_this.$q.platform.is.mobile) {
        _this.device = 1;
      }
    }
    if (_this.$q.platform.is.electron) {
      _this.height = String(_this.$q.screen.height) + 'px';
    } else if (_this.$q.platform.is.cordova) {
      if (window.device) {
        window.plugins.insomnia.keepAwake();
        if (window.device.manufacturer === 'Urovo' || window.device.manufacturer === 'Zebra Technologies') {
          _this.fab1.top = '0px';
          _this.fab1.bottom = 0 - (_this.$q.screen.width - 50) / 5 + '' + 'px';
          _this.fab1.left = (_this.$q.screen.width - 50) / 6 - (_this.$q.screen.width / 12) * 10 + '' + 'px';
          _this.fab1.right = '0px';
          _this.fab2.top = '0px';
          _this.fab2.bottom = 0 - (_this.$q.screen.width - 50) / 5 + '' + 'px';
          _this.fab2.left = ((_this.$q.screen.width - 50) / 6 - (_this.$q.screen.width / 12) * 10) / 2 + '' + 'px';
          _this.fab2.right = '0px';
          _this.fab3.top = '0px';
          _this.fab3.bottom = '0px';
          _this.fab3.left = '-0px';
          _this.fab3.right = '0px';
          _this.fab4.top = (_this.$q.screen.width - 50) / 5 + '' + 'px';
          _this.fab4.bottom = 0 - (_this.$q.screen.width - 50) / 5 + '' + 'px';
          _this.fab4.left = (_this.$q.screen.width - 50) / 6 - (_this.$q.screen.width / 12) * 10 + '' + 'px';
          _this.fab4.right = '0px';
          _this.fab5.top = '0px';
          _this.fab5.bottom = 0 - (_this.$q.screen.width - 50) / 5 + '' + 'px';
          _this.fab5.left = ((_this.$q.screen.width - 50) / 6 - (_this.$q.screen.width / 12) * 10) / 2 + '' + 'px';
          _this.fab5.right = '0px';
          _this.fab6.top = '0px';
          _this.fab6.bottom = '0px';
          _this.fab6.left = '0px';
          _this.fab6.right = '0px';
          _this.fab7.top = (_this.$q.screen.width - 50) / 5 + '' + 'px';
          _this.fab7.bottom = 0 - (_this.$q.screen.width - 50) / 5 + '' + 'px';
          _this.fab7.left = (_this.$q.screen.width - 50) / 6 - (_this.$q.screen.width / 12) * 10 + '' + 'px';
          _this.fab7.right = '0px';
          _this.fab8.top = '0px';
          _this.fab8.bottom = (_this.$q.screen.width - 50) / 8 + '' + 'px';
          _this.fab8.left = ((_this.$q.screen.width - 50) / 6 - (_this.$q.screen.width / 12) * 10) / 2 + '' + 'px';
          _this.fab8.right = '0px';
        }
      }
    } else {
      _this.height = _this.$q.screen.height + '' + 'px';
    }
    window.addEventListener('batterystatus', _this.updateBatteryStatus, false);
    _this.width = _this.$q.screen.width * 1 + '' + 'px';
    _this.height = _this.$q.screen.height - 50 + '' + 'px';
    _this.scroll_height = _this.$q.screen.height - 175 + '' + 'px';
    _this.barscan = '';
    _this.goods_scan = '';
    _this.getList('A00001');
    _this.scanEvents();
    getDeviceinfo();
  },
  updated() {},
  beforeDestroy() {
    var _this = this;
    window.removeEventListener('batterystatus', _this.updateBatteryStatus, false);
    document.removeEventListener('deviceready', _this.onDeviceReady, false);
  },
  destroyed() {}
};
</script>
