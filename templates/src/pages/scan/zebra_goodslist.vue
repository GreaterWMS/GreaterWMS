<template>
  <div>
    <q-input v-model="scaneddata.request_time" style="display:none" />
    <q-card v-show="!fab" flat :style="{ width: width,  height: height }">
      <q-card-section style="height: 75px">
        <div class="text-h6">{{ goods_code_label }}</div>
        <div class="text-subtitle2">{{ goods_scan.goods_code }}</div>
      </q-card-section>
      <q-separator />
      <q-scroll-area
        :thumb-style="thumbStyle"
        :bar-style="barStyle"
        :style="{ height: scroll_height, width: width }"
      >
        <q-list>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_desc_label }}</q-item-label>
              <q-item-label caption>{{ goods_scan.goods_desc }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_supplier_label }}</q-item-label>
              <q-item-label caption>{{ goods_scan.goods_supplier }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_weight_label }}</q-item-label>
              <q-item-label caption>{{ goods_scan.goods_weight }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_w_label }}</q-item-label>
              <q-item-label caption>{{ goods_scan.goods_w }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_d_label }}</q-item-label>
              <q-item-label caption>{{ goods_scan.goods_d }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_h_label }}</q-item-label>
              <q-item-label caption>{{ goods_scan.goods_h }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ unit_volume_label }}</q-item-label>
              <q-item-label caption>{{ goods_scan.unit_volume }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_unit_label }}</q-item-label>
              <q-item-label caption>{{ goods_scan.goods_unit }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_class_label }}</q-item-label>
              <q-item-label caption>{{ goods_scan.goods_class }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_brand_label }}</q-item-label>
              <q-item-label caption>{{ goods_scan.goods_brand }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_color_label }}</q-item-label>
              <q-item-label caption>{{ goods_scan.goods_color }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_shape_label }}</q-item-label>
              <q-item-label caption>{{ goods_scan.goods_shape }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_specs_label }}</q-item-label>
              <q-item-label caption>{{ goods_scan.goods_specs }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_origin_label }}</q-item-label>
              <q-item-label caption>{{ goods_scan.goods_origin }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_cost_label }}</q-item-label>
              <q-item-label caption>{{ goods_scan.goods_cost }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ goods_price_label }}</q-item-label>
              <q-item-label caption>{{ goods_scan.goods_price }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ creater_label }}</q-item-label>
              <q-item-label caption>{{ goods_scan.creater }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ create_time_label }}</q-item-label>
              <q-item-label caption>{{ goods_scan.create_time }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label>{{ updatetime_label }}</q-item-label>
              <q-item-label caption>{{ goods_scan.update_time }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>
      <q-separator dark />
    </q-card>
  </div>
</template>
<router-view />

<script>
import { getauth } from 'boot/axios_request'
import { LocalStorage, Screen } from 'quasar'

export default {
  name: 'Pagezebra_goodslist',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'goods/',
      height: '',
      width: '',
      scroll_height: '',
      goods_scan: {},
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
      bar_scanned: ''
    }
  },
  methods: {
    getGoodsList (e) {
      var _this = this
      getauth(_this.pathname + '?goods_code=' + e, {
      }).then(res => {
        if (res.results.length === 0) {
          navigator.vibrate(100)
          _this.$q.notify({
            message: 'No Goods Data',
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        } else if (res.results.length === 1) {
          _this.goods_scan = res.results[0]
        } else {
          navigator.vibrate(100)
          _this.$q.notify({
            message: 'Repeating Data',
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        }
      }).catch(err => {
        navigator.vibrate(100)
        _this.$q.notify({
          message: err.detail,
          position: 'top',
          icon: 'close',
          color: 'negative'
        })
      })
    }
  },
  computed: {
    fab: {
      get () {
        return this.$store.state.fabchange.fab
      }
    },
    scaneddata: {
      get () {
        return this.$store.state.scanedsolve.scaneddata
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
    } else {
      _this.authin = '0'
    }
  },
  mounted () {
    var _this = this
    _this.width = Screen.width * 1 + '' + 'px'
    _this.height = Screen.height - 50 + '' + 'px'
    _this.scroll_height = Screen.height - 175 + '' + 'px'
    _this.goods_scan = ''
  },
  updated () {
    var _this = this
    if (_this.scaneddata !== '') {
      if (_this.bar_scanned !== _this.scaneddata.request_time) {
        if (_this.scaneddata.mode === 'GOODS') {
          _this.bar_scanned = _this.scaneddata.request_time
          _this.getGoodsList(_this.scaneddata.code)
        } else {
          _this.$q.notify({
            message: 'No Goods Data',
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        }
      }
    }
  },
  beforeDestroy () {
  }
}
</script>
