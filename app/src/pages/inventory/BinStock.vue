<template>
  <q-list bordered padding>
    <q-item>
      <q-item-section>
        <q-item-label overline>{{ $t('notice.mobile_binstock.notice1') }}</q-item-label>
        <q-item-label caption>{{ $t('notice.mobile_binstock.notice2') }}</q-item-label>
      </q-item-section>
    </q-item>
    <q-separator spaced/>
    <template v-for="(item, index) in tablelist" :key="index">
      <q-item>
        <q-item-section @click="dataSubmit(item)">
          <q-item-label>{{ item.goods_code }}</q-item-label>
          <q-item-label caption lines="2">
            {{ item.goods_desc }}
          </q-item-label>
        </q-item-section>
        <q-item-section side top>
          <q-item-label caption>{{ $t('notice.mobile_binstock.notice3') }}{{ item.bin_name }}</q-item-label>
           <q-item-label caption>{{ $t('notice.mobile_binstock.notice4') }}{{ item.goods_qty }}</q-item-label>
        </q-item-section>
      </q-item>
      <q-separator v-show="index + 1 !== tablelist.length" spaced inset="item" />
    </template>
  </q-list>
   <q-dialog v-model="dialogForm">
       <q-card class="shadow-24">
         <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
           <div>{{ submitdata.goods_code }}</div>
           <q-space />
           <q-btn dense flat icon="close" v-close-popup>
             <q-tooltip>{{ $t('index.close') }}</q-tooltip>
           </q-btn>
         </q-bar>
         <q-card-section class="scroll">
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="submitdata.move_qty"
                    type="number"
                    :label="$t('stock.view_stocklist.goods_qty')"
                    style="margin-bottom: 5px"
                    @click="submitdata.move_qty = ''"
                    :rules="[ val => val && val > 0 || moveerror]"
                    >
             <template v-slot:before>
               <q-select dense
                         outlined
                         square
                         use-input
                         hide-selected
                         fill-input
                         v-model="submitdata.move_to_bin"
                         :label="$t('warehouse.view_binset.bin_name')"
                         :options="options"
                         @filter="filterFn"
                         @input-value="setOptions"
                         style="width: 150px"
                         >
                 <template v-slot:no-option>
                   <q-item>
                     <q-item-section class="text-grey">
                       No results
                     </q-item-section>
                   </q-item>
                 </template>
                 <template v-if="submitdata.move_to_bin" v-slot:append>
                   <q-icon name="cancel" @click.stop="submitdata.move_to_bin = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
         </q-card-section>
         <div style="float: right; padding: 15px 15px 15px 0">
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="cancelDataSubmit">{{ $t('cancel') }}</q-btn>
           <q-btn color="primary" @click="submitData">{{ $t('submit') }}</q-btn>
         </div>
       </q-card>
     </q-dialog>
</template>

<script>
import { computed, defineComponent, onMounted, ref, watch } from 'vue'
import { useStore } from "vuex";
import { useQuasar } from "quasar";
import axios from 'axios';
import { useI18n } from "vue-i18n";
import { useRouter } from "vue-router";

export default defineComponent({
  name: 'BinStock',
  data () {
    return {
    }
  },
  setup () {
    const $store = useStore()
    const $router = useRouter()
    const $q = useQuasar()
    const requestauth = ref(0)
    const submitdata = ref({})
    const dialogForm = ref(false)
    const options = ref([])
    const optionsChange = ref('')
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

    function InitData (e) {
      tablelist.value = []
      apiurl.value = baseurl.value + '/stock/bin/?goods_code='
      getTableData(e)
    }

    function getTableData (e) {
      axios.get(apiurl.value + e,
        {
          headers: {
            "Content-Type": 'application/json, charset="utf-8"',
            "token" : openid.value,
            "language" : lang.value,
            "operator" : operator.value
          }
        }).then(res => {
          if (!res.data.detail) {
            var tablepush = []
            tablelist.value.forEach(i => {
              tablepush.push(i)
            })
            res.data.results.forEach(item => {
              tablepush.push(item)
            })
            tablelist.value = tablepush
            apiurlprevious.value = sslCheck(res.data.previous)
            apiurlnext.value = sslCheck(res.data.next)
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
    function dataSubmit (e) {
      submitdata.value = JSON.parse(JSON.stringify(e))
      Object.assign(submitdata.value,{"move_qty": '', "move_to_bin": ''})
      dialogForm.value = true
    }
    function cancelDataSubmit () {
      dialogForm.value = false
    }

    function submitData () {
      if (submitdata.value.move_to_bin === '') {
        $q.notify({
          type: 'negative',
          message: t('notice.mobile_binstock.notice5')
        })
      } else {
        apiurl.value = baseurl.value + '/stock/bin/'
        axios.post(apiurl.value + submitdata.value.id + '/', submitdata.value,
          {
            headers: {
              "Content-Type": 'application/json',
              "token" : openid.value,
              "language" : lang.value,
              "operator" : operator.value
            }
          }).then(res => {
          cancelDataSubmit()
          InitData('')
          if (!res.data.detail) {
            $q.notify({
              message: t('notice.mobile_binstock.notice6'),
            })
          }
        }).catch(err => {
          $q.notify({
            message: t('notice.network_error'),
          })
        })
      }
    }

    function setOptions (e) {
      apiurl.value = baseurl.value + '/binset/?bin_name__icontains='
      axios.get(apiurl.value + e,
        {
          headers: {
            "Content-Type": 'application/json, charset="utf-8"',
            "token": openid.value,
            "language": lang.value,
            "operator": operator.value
          }
        }).then(res => {
        if (!res.data.detail) {
          var binlist = []
          options.value = []
          res.data.results.forEach(item => {
            binlist.push(item.bin_name)
          })
          options.value = binlist
        }
      }).catch(err => {
        $q.notify({
          type: 'negative',
          message: t('notice.mobile_scan.notice3')
        })
      })
    }

    watch (optionsChange,(newValue,oldValue)=>{
      if (newValue.length >= 2) {
        setOptions(newValue)
      }
    })

    watch (bar_scanned,(newValue,oldValue)=>{
      if (scanmode.value === 'GOODS') {
        InitData(scandata.value)
      }
    })

    watch (screenscroll,(newValue,oldValue)=>{
      if (newValue === 1) {
        if (apiurlnext.value !== null) {
          apiurl.value = apiurlnext.value
          requestauth.value = 1
        }
      } else {
        requestauth.value = 0
      }
    })

   watch (requestauth,(newValue,oldValue)=>{
      if (newValue === 1) {
         if (authin.value === '0') {
          $q.notify({
            type: 'negative',
            message: t('notice.mobile_userlogin.notice9')
          })
        } else {
          getTableData('')
        }
      }
    })

    onMounted(() => {
      if (authin.value === '0') {
        $q.notify({
          type: 'negative',
          message: t('notice.mobile_userlogin.notice9')
        })
      } else {
        if (scanmode.value === 'GOODS') {
          InitData(scandata.value)
        } else {
          scanmode.value = 'GOODS'
          InitData('')
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
      bar_scanned,
      submitdata,
      dialogForm,
      dataSubmit,
      cancelDataSubmit,
      submitData,
      options,
      optionsChange,
      moveerror: t('notice.mobile_asn.notice11'),
      setOptions,
      filterFn (val, update, abort) {
        if (val.length < 2) {
          abort()
          return
        }
        update(() => {
          const needle = val.toLowerCase()
          optionsChange.value = needle
        })
      }
    }
  }
})
</script>
