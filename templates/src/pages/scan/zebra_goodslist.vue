<template>
  <q-page>
    <q-card v-show="!fab" flat :style="{ width: width,  height: height }">
      <q-card-section style="height: 75px">
        <div class="text-h6">{{ goods_code_label }}</div>
        <div class="text-subtitle2">{{ data_list.goods_code }}</div>
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
    </q-card>
  </q-page>
</template>
<router-view />

<script>
import { getauth } from 'boot/axios_request'
import { LocalStorage, Screen, throttle } from 'quasar'

export default {
  name: 'Pagezebra_goodslist',
  data () {
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
      data_list: {},
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
      barscan: '',
      goods_scan: ''
    }
  },
  methods: {
    datachange () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth('scanner/?bar_code=' + _this.barscan, {
        }).then(res => {
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
      }
    },
    getList () {
      var _this = this
      if (LocalStorage.has('auth')) {
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
      }
    },
    reFresh () {
      var _this = this
      _this.barscan = ''
      _this.bin_scan = ''
      _this.goods_scan = ''
      _this.getList()
    }
  },
  computed: {
    fab: {
      get () {
        return this.$store.state.fabchange.fab
      }
    }
    // barscan: {
    //   get () {
    //     console.log('scaned_x', this.$store.state.datashare.barscan)
    //     return this.$store.state.datashare.barscan
    //   },
    //   set (val) {
    //     console.log('scaned_y', val)
    //     this.$store.commit('datashare/updateBarscan', val)
    //   }
    // }
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
    _this.datachange = throttle(_this.datachange, 200)
  },
  mounted () {
    var _this = this
    _this.width = Screen.width * 1 + '' + 'px'
    _this.height = Screen.height - 50 + '' + 'px'
    _this.scroll_height = Screen.height - 175 + '' + 'px'
    _this.barscan = ''
    _this.goods_scan = ''
  },
  beforeDestroy () {
  }
}
</script>
