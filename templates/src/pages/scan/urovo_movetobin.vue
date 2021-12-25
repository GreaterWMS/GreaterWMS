<template>
  <q-page>
    <q-card v-show="!fab" class="shadow-24" :style="{ width: width, height: height }">
      <q-card-section>
        <q-bar class="bg-white shadow-1 ">
          <div style="font-size: 12px;width: 100%;">{{ $t('scan.scan_goods_label') }}: {{ goods_scan }}</div>
        </q-bar>
        <q-bar class="bg-white shadow-1 q-mt-sm q-mb-sm">
          <div style="font-size: 12px;width: 100%;">{{ $t('scan.view_binmove.new_bin_name') }}: {{ bin_scan }}</div>
        </q-bar>
        <q-btn-group push>
          <q-btn :label="$t('refresh')" @click="reFresh()" />
          <q-btn color="purple" :label="$t('stock.view_stocklist.cyclecountresult')" @click="ConfirmCount()" />
        </q-btn-group>
      </q-card-section>
      <q-scroll-area :thumb-style="thumbStyle" :bar-style="barStyle" :style="{ height: scroll_height, width: width }">
        <q-markup-table>
          <thead>
            <tr>
              <th class="text-left">{{ scan_goods_code }}</th>
              <th class="text-right">{{ old_bin_name }}</th>
              <th class="text-right">{{ new_bin_name }}</th>
              <th class="text-right">{{ qty }}</th>
            </tr>
          </thead>
          <tbody :class="showBg ? 'tbody' : ''">
            <template>
              <tr v-for="(item, index) in table_list" :key="index">
                <td class="text-left">{{ item.bin_name }}</td>
                <td class="text-right">{{ item.goods_code }}</td>
                <td class="text-right">{{ item.physical_inventory }}</td>
                <td class="text-right">{{}}</td>
              </tr>
            </template>
          </tbody>
        </q-markup-table>
      </q-scroll-area>
      <q-separator dark />
      <q-card-actions><input id="scannedBarcodes" v-model="bin_name" type="text" readonly disabled /></q-card-actions>
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
import { getauth, putauth } from 'boot/axios_request';
import { LocalStorage } from 'quasar';

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
  name: 'Pageurovo_cyclecount',
  data() {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'uptobin/',
      separator: 'cell',
      loading: false,
      device: 0,
      device_name: '',
      width: '',
      height: '',
      scroll_height: '',
      table_list: [],
      scan_goods_code: this.$t('scan.scan_goods_code'),
      old_bin_name: this.$t('scan.view_binmove.old_bin_name'),
      new_bin_name: this.$t('scan.view_binmove.new_bin_name'),
      qty: this.$t('scan.view_binmove.qty'),
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
      bin_scan: '',
      goods_scan: '',
      showBg: false,
      error1: this.$t('scan.scan_goods_label_error'),
      error2: this.$t('scan.view_binmove.qty_error')
    };
  },
  methods: {
    startBarcode() {
      let _this = this;
      Uplugin.getBarcode(
        'start',
        function(res) {
          _this.barscan = res;
          _this.datachange();
        },
        function(err) {
          console.log(err);
        }
      );
    },
    datachange() {
      var _this = this;
      getauth('scanner/?bar_code=' + _this.barscan, {})
        .then(res => {
          if (res.results[0].mode === 'GOODS') {
            _this.goods_scan = res.results[0].code;
            _this.bin_scan = '';
            _this.getDataList(_this.goods_scan);
            // _this.countAdd(_this.goods_scan);
          } else if (res.results[0].mode === 'BINSET') {
            _this.bin_scan = res.results[0].code;
            _this.goods_scan = '';
          } else {
            if (!res.results) {
              _this.$q.notify({
                message: '单号不存在',
                icon: 'close',
                color: 'negative'
              });
            }
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
    getDataList(code) {
      getauth('stock/bin/?' + code).then(res => {
        res.results.forEach(item=>{
          this.table_list.push(item);
        })
      });
    },
    countAdd(e) {
      var _this = this;
      _this.table_list.filter(function(value, index, array) {
        if (value.goods_code === e) {
          _this.table_list[index].picked_qty += 1;
          if (_this.currentIndex) {
            document.getElementById(`dom${_this.currentIndex - 1}`).style.background = 'white';
          }
          let offset = index * 50;
          document.getElementById(`dom${index}`).style.background = 'lightskyblue';
          _this.currentIndex = index + 1;
          if (_this.table_list[index].picked_qty > _this.table_list[index].goods_qty) {
            _this.$q.notify({
              message: _this.error2,
              icon: 'close',
              color: 'negative'
            });
            _this.table_list[index].picked_qty = _this.table_list[index].picked_qty - 1;
          } else {
            _this.$refs.scrollArea.setScrollPosition(offset, 200);
          }
        }
      });
    },
    getList(e) {
      var _this = this;
      getauth(_this.pathname + '&asn_code=' + e, {})
        .then(res => {
          _this.table_list = res.results;
          _this.sorted_list.goodsData = res.results;
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          });
        });
    },
    reFresh() {
      var _this = this;
      _this.barscan = '';
      _this.bin_scan = '';
      _this.goods_scan = '';
      // _this.getList();
    },
    repeatCount(e) {
      var _this = this;
      _this.table_list[e].physical_inventory = 0;
    },
    ConfirmCount() {
      var _this = this;
      if (LocalStorage.has('auth')) {
        putauth(_this.pathname, _this.table_list)
          .then(res => {
            _this.table_list = [];
            _this.$q.notify({
              message: 'Success Confirm Cycle Count',
              icon: 'check',
              color: 'green'
            });
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
    updateBatteryStatus(status) {
      var _this = this;
      _this.batteryStatus = `Level: ${status.level}, plugged: ${status.isPlugged}`;
    },
    scanEvents() {
      var _this = this;
      document.addEventListener('deviceready', _this.onDeviceReady, false);
      document.addEventListener('resume', _this.onResume, false);
      document.addEventListener('pause', _this.onPause, false);
    },
    onDeviceReady() {
      this.startBarcode();
    },
    onPause: function() {
      stopBarcode();
    },
    onResume() {
      this.startBarcode();
    }
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
    _this.scroll_height = _this.$q.screen.height - 255 + '' + 'px';
    _this.barscan = '';
    _this.bin_scan = '';
    _this.goods_scan = '';
    // _this.getList();
    _this.scanEvents();
    getDeviceinfo();
  },
  updated() {},
  beforeDestroy() {
    var _this = this;
    stopBarcode();
    window.removeEventListener('batterystatus', _this.updateBatteryStatus, false);
    document.removeEventListener('deviceready', _this.onDeviceReady, false);
    document.removeEventListener('resume', _this.onResume, false);
    document.removeEventListener('pause', _this.onPause, false);
  },
  destroyed() {}
};
</script>
<style scoped>
.tbody tr:first-child {
  background-color: royalblue;
}
</style>
