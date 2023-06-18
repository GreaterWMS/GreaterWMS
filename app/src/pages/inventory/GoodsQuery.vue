<template>
    <q-list bordered padding>
      <q-item>
        <q-item-section>
          <q-item-label>{{ datadetail.goods_code }}</q-item-label>
          <q-item-label caption>{{ datadetail.goods_desc }}</q-item-label>
        </q-item-section>

        <q-item-section side top>
          <q-item-label caption>{{ datadetail.update_time }}</q-item-label>
        </q-item-section>
      </q-item>

      <q-separator spaced />

      <q-item>
        <q-item-section>{{ $t('goods.view_goodslist.goods_supplier') }}</q-item-section>
        <q-item-section side>
          <q-item-label caption>{{ datadetail.goods_supplier }}</q-item-label>
        </q-item-section>
      </q-item>
      <q-separator spaced inset="item" />
      <q-item>
        <q-item-section>{{ $t('goods.view_goodslist.goods_weight') }}</q-item-section>
        <q-item-section side>
          <q-item-label caption>{{ datadetail.goods_weight }}</q-item-label>
        </q-item-section>
      </q-item>
      <q-separator spaced inset="item" />
      <q-item>
        <q-item-section>{{ $t('goods.view_goodslist.goods_w') }}</q-item-section>
        <q-item-section side>
          <q-item-label caption>{{ datadetail.goods_w }}</q-item-label>
        </q-item-section>
      </q-item>
      <q-separator spaced inset="item" />
      <q-item>
        <q-item-section>{{ $t('goods.view_goodslist.goods_d') }}</q-item-section>
        <q-item-section side>
          <q-item-label caption>{{ datadetail.goods_d }}</q-item-label>
        </q-item-section>
      </q-item>
      <q-separator spaced inset="item" />
      <q-item>
        <q-item-section>{{ $t('goods.view_goodslist.goods_h') }}</q-item-section>
        <q-item-section side>
          <q-item-label caption>{{ datadetail.goods_h }}</q-item-label>
        </q-item-section>
      </q-item>
      <q-separator spaced inset="item" />
      <q-item>
        <q-item-section>{{ $t('goods.view_goodslist.unit_volume') }}</q-item-section>
        <q-item-section side>
          <q-item-label caption>{{ datadetail.unit_volume }}</q-item-label>
        </q-item-section>
      </q-item>
      <q-separator spaced inset="item" />
      <q-item>
        <q-item-section>{{ $t('goods.view_goodslist.goods_unit') }}</q-item-section>
        <q-item-section side>
          <q-item-label caption>{{ datadetail.goods_unit }}</q-item-label>
        </q-item-section>
      </q-item>
      <q-separator spaced inset="item" />
      <q-item>
        <q-item-section>{{ $t('goods.view_goodslist.goods_class') }}</q-item-section>
        <q-item-section side>
          <q-item-label caption>{{ datadetail.goods_class }}</q-item-label>
        </q-item-section>
      </q-item>
      <q-separator spaced inset="item" />
      <q-item>
        <q-item-section>{{ $t('goods.view_goodslist.goods_brand') }}</q-item-section>
        <q-item-section side>
          <q-item-label caption>{{ datadetail.goods_brand }}</q-item-label>
        </q-item-section>
      </q-item>
      <q-separator spaced inset="item" />
      <q-item>
        <q-item-section>{{ $t('goods.view_goodslist.goods_color') }}</q-item-section>
        <q-item-section side>
          <q-item-label caption>{{ datadetail.goods_color }}</q-item-label>
        </q-item-section>
      </q-item>
      <q-separator spaced inset="item" />
      <q-item>
        <q-item-section>{{ $t('goods.view_goodslist.goods_shape') }}</q-item-section>
        <q-item-section side>
          <q-item-label caption>{{ datadetail.goods_shape }}</q-item-label>
        </q-item-section>
      </q-item>
      <q-separator spaced inset="item" />
      <q-item>
        <q-item-section>{{ $t('goods.view_goodslist.goods_specs') }}</q-item-section>
        <q-item-section side>
          <q-item-label caption>{{ datadetail.goods_specs }}</q-item-label>
        </q-item-section>
      </q-item>
      <q-separator spaced inset="item" />
      <q-item>
        <q-item-section>{{ $t('goods.view_goodslist.goods_origin') }}</q-item-section>
        <q-item-section side>
          <q-item-label caption>{{ datadetail.goods_origin }}</q-item-label>
        </q-item-section>
      </q-item>
      <q-separator spaced inset="item" />
      <q-item>
        <q-item-section>{{ $t('goods.view_goodslist.goods_cost') }}</q-item-section>
        <q-item-section side>
          <q-item-label caption>{{ datadetail.goods_cost }}</q-item-label>
        </q-item-section>
      </q-item>
      <q-separator spaced inset="item" />
      <q-item>
        <q-item-section>{{ $t('goods.view_goodslist.goods_price') }}</q-item-section>
        <q-item-section side>
          <q-item-label caption>{{ datadetail.goods_price }}</q-item-label>
        </q-item-section>
      </q-item>
    </q-list>
</template>

<script>
import {computed, defineComponent, onMounted, ref, watch} from 'vue'
import { useStore } from "vuex";
import { useQuasar } from "quasar";
import { useI18n } from "vue-i18n";
import { useRouter } from "vue-router";
import axios from "axios";

export default defineComponent({
  name: 'GoodsQuery',
  data () {
    return {
    }
  },
  setup () {
    const $store = useStore()
    const $router = useRouter()
    const $q = useQuasar()
    const requestauth = ref(0)
    const { t } = useI18n()
    const fab1 = computed({
      get: () => $store.state.fabchange.fab1,
    })
    const fab2 = computed({
      get: () => $store.state.fabchange.fab2,
    })
    const fab3 = computed({
      get: () => $store.state.fabchange.fab3,
    })
    const fab4 = computed({
      get: () => $store.state.fabchange.fab4,
    })
    const screenscroll = computed({
      get: () => $store.state.screenchange.screenscroll,
    })
    const authin = computed({
      get: () => $store.state.loginauth.authin,
    })
    const login_name = computed({
      get: () => $store.state.loginauth.login_name,
    })
    const operator = computed({
      get: () => $store.state.loginauth.operator,
    })
    const openid = computed({
      get: () => $store.state.settings.openid,
    })
    const lang = computed({
      get: () => $store.state.langchange.lang,
    })
    const baseurl = computed({
      get: () => $store.state.settings.server,
    })
    const scandata = computed({
      get: () => $store.state.scanchanged.scandata,
      set: val => {
        $store.commit('scanchanged/ScanChanged', val)
      }
    })
    const datadetail = computed({
      get: () => $store.state.scanchanged.datadetail,
      set: val => {
        $store.commit('scanchanged/ScanDataChanged', val)
      }
    })
    const asndata = computed({
      get: () => $store.state.scanchanged.asndata,
      set: val => {
        $store.commit('scanchanged/ASNDataChanged', val)
      }
    })
    const dndata = computed({
      get: () => $store.state.scanchanged.dndata,
      set: val => {
        $store.commit('scanchanged/DNDataChanged', val)
      }
    })
    const bindata = computed({
      get: () => $store.state.scanchanged.bindata,
      set: val => {
        $store.commit('scanchanged/BinDataChanged', val)
      }
    })
    const tablelist = computed({
      get: () => $store.state.scanchanged.tablelist,
      set: val => {
        $store.commit('scanchanged/TableDataChanged', val)
      }
    })
    const scanmode = computed({
      get: () => $store.state.scanchanged.scanmode,
      set: val => {
        $store.commit('scanchanged/ScanModeChanged', val)
      }
    })
    const bar_scanned = computed({
      get: () => $store.state.scanchanged.bar_scanned,
    })
    const apiurl = computed({
      get: () => $store.state.scanchanged.apiurl,
      set: val => {
        $store.commit('scanchanged/ApiUrlChanged', val)
      }
    })
    const apiurlnext = computed({
      get: () => $store.state.scanchanged.apiurlnext,
      set: val => {
        $store.commit('scanchanged/ApiUrlNextChanged', val)
      }
    })
    const apiurlprevious = computed({
      get: () => $store.state.scanchanged.apiurlprevious,
      set: val => {
        $store.commit('scanchanged/ApiUrlPreviousChanged', val)
      }
    })

    function sslCheck (e) {
      if (e !== null) {
        var baseurlCheck = baseurl.value.split(':')
        var urlCheck = e.split(':')
        if (urlCheck.length === 2)
          if (baseurlCheck[0] !== urlCheck[0]) {
            return baseurlCheck[0] + ':' + urlCheck[1]
          } else {
            return e
          }
        else if (urlCheck.length === 3) {
          if (baseurlCheck[0] !== urlCheck[0]) {
            return baseurlCheck[0] + ':' + urlCheck[1] + ':' + urlCheck[2]
          } else {
            return e
          }
        }
      } else {
        return null
      }
    }

    function getTableData (e) {
      apiurl.value = baseurl.value + '/goods/?goods_code=' + e
      axios.get(apiurl.value,
        {
          headers: {
            "Content-Type": 'application/json, charset="utf-8"',
            "token" : openid.value,
            "language" : lang.value,
            "operator" : operator.value
          }
        }).then(res => {
        if (!res.data.detail) {
            datadetail.value = res.data.results[0]
          } else {
            $q.notify({
              type: 'negative',
              message: t('notice.mobile_scan.notice1')
            })
          }
        }).catch(err => {
          $q.notify({
            type: 'negative',
            message: t('notice.mobile_scan.notice3')
          })
      })
    }

    watch (bar_scanned,(newValue,oldValue)=>{
      if (scanmode.value === 'GOODS') {
        getTableData(scandata.value)
      }
    })
    watch (screenscroll,(newValue,oldValue)=>{
    })

    onMounted(() => {
      if (authin.value === '0') {
        $q.notify({
          type: 'negative',
          message: t('notice.mobile_userlogin.notice9')
        })
      } else {
        if (scanmode.value === 'GOODS') {
          getTableData(scandata.value)
        }
      }
    })

    return {
      t,
      fab1,
      fab2,
      fab3,
      fab4,
      screenscroll,
      authin,
      login_name,
      openid,
      operator,
      lang,
      requestauth,
      baseurl,
      apiurl,
      apiurlnext,
      apiurlprevious,
      scandata,
      datadetail,
      tablelist,
      asndata,
      dndata,
      bindata,
      scanmode,
      bar_scanned
    }
  }
})
</script>
