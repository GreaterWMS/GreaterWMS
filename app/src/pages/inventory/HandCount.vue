<template>
  <q-list bordered padding>
    <q-item>
      <q-item-section>
        <q-item-label overline>{{ $t("notice.handcount.notice2") }}</q-item-label>
        <q-item-label caption>{{
          $t("notice.handcount.notice8")
        }}</q-item-label>
      </q-item-section>
    </q-item>
    <q-separator spaced />
    <q-item>
      <q-item-section>{{ $t("notice.handcount.notice1") }}</q-item-section>
      <q-item-section side>
        <q-btn
          @click="state.affirmresultVisible = true"
          color="primary"
          size="sm"
          >{{ $t("notice.handcount.notice5") }}</q-btn
        >
      </q-item-section>
    </q-item>

    <template v-for="(item, index) in state.tableData" :key="index">
      <q-item>
        <q-item-section>
          <q-item-label>{{ item.bin_name }}</q-item-label>
          <q-item-label caption lines="2">
            {{ item.goods_code }}
          </q-item-label>
        </q-item-section>
        <q-item-section side top>
          <q-item-label caption
            >{{ $t("notice.handcount.notice3") }}：{{ item.goods_qty }}</q-item-label
          >
          <q-item-label caption>
            <!--  {{ $t("notice.handcount.tablepandiannum") }}： -->
            <q-input
              dense
              outlined
              square
              v-model.number="item.physical_inventory"
              type="number"
              :style="{ width: '100px' }"
              :label="$t('notice.handcount.notice4')"
            />
          </q-item-label>
        </q-item-section>
      </q-item>
      <q-separator
        v-show="index + 1 !== state.tableData.length"
        spaced
        inset="item"
      />
    </template>
  </q-list>

  <q-dialog v-model="state.affirmresultVisible">
    <q-card class="shadow-24">
      <q-bar
        class="bg-light-blue-10 text-white rounded-borders"
        style="height: 50px"
      >
        <div>{{ $t("notice.handcount.notice6") }}</div>
        <q-space />
        <q-btn dense flat icon="close" v-close-popup>
          <q-tooltip>{{ $t("index.close") }}</q-tooltip>
        </q-btn>
      </q-bar>
      <q-card-section class="scroll">{{ $t('deletetip') }}</q-card-section>
      <div style="float: right; padding: 15px">
        <q-btn
          color="white"
          text-color="black"
          style="margin-right: 25px"
          @click="state.affirmresultVisible = false"
          >{{ $t("cancel") }}</q-btn
        >
        <q-btn color="primary" @click="handleAffirmresultSubmit">{{
          $t("submit")
        }}</q-btn>
      </div>
    </q-card>
  </q-dialog>
</template>

<script>
import {
  reactive,
  computed,
  defineComponent,
  onMounted,
  ref,
  watch,
} from "vue";
import { useStore } from "vuex";
import { useQuasar } from "quasar";
import axios from "axios";
import { useI18n } from "vue-i18n";
import { useRouter } from "vue-router/dist/vue-router";

export default defineComponent({
  name: "HandCount",
  data() {
    return {};
  },
  setup() {
    const $store = useStore();
    const $router = useRouter();
    const $q = useQuasar();
    const requestauth = ref(0);
    const { t } = useI18n();
    const fab1 = computed({
      get: () => $store.state.fabchange.fab1,
    });
    const fab2 = computed({
      get: () => $store.state.fabchange.fab2,
    });
    const fab3 = computed({
      get: () => $store.state.fabchange.fab3,
    });
    const fab4 = computed({
      get: () => $store.state.fabchange.fab4,
    });
    const screenscroll = computed({
      get: () => $store.state.screenchange.screenscroll,
    });
    const authin = computed({
      get: () => $store.state.loginauth.authin,
    });
    const login_name = computed({
      get: () => $store.state.loginauth.login_name,
    });
    const operator = computed({
      get: () => $store.state.loginauth.operator,
    });
    const openid = computed({
      get: () => $store.state.settings.openid,
    });
    const lang = computed({
      get: () => $store.state.langchange.lang,
    });
    const baseurl = computed({
      get: () => $store.state.settings.server,
    });
    const scandata = computed({
      get: () => $store.state.scanchanged.scandata,
      set: (val) => {
        $store.commit("scanchanged/ScanChanged", val);
      },
    });
    const datadetail = computed({
      get: () => $store.state.scanchanged.datadetail,
      set: (val) => {
        $store.commit("scanchanged/ScanDataChanged", val);
      },
    });
    const dndata = computed({
      get: () => $store.state.scanchanged.dndata,
      set: (val) => {
        $store.commit("scanchanged/DNDataChanged", val);
      },
    });
    const bindata = computed({
      get: () => $store.state.scanchanged.bindata,
      set: (val) => {
        $store.commit("scanchanged/BinDataChanged", val);
      },
    });
    const tablelist = computed({
      get: () => $store.state.scanchanged.tablelist,
      set: (val) => {
        $store.commit("scanchanged/TableDataChanged", val);
      },
    });
    const scanmode = computed({
      get: () => $store.state.scanchanged.scanmode,
    });
    const bar_scanned = computed({
      get: () => $store.state.scanchanged.bar_scanned,
    });
    const apiurl = computed({
      get: () => $store.state.scanchanged.apiurl,
      set: (val) => {
        $store.commit("scanchanged/ApiUrlChanged", val);
      },
    });
    const apiurlnext = computed({
      get: () => $store.state.scanchanged.apiurlnext,
      set: (val) => {
        $store.commit("scanchanged/ApiUrlNextChanged", val);
      },
    });
    const apiurlprevious = computed({
      get: () => $store.state.scanchanged.apiurlprevious,
      set: (val) => {
        $store.commit("scanchanged/ApiUrlPreviousChanged", val);
      },
    });

    const state = reactive({
      tableData: [],
      bin_name: "",
      goods_code: "",
      affirmresultVisible: false,
    });

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

    function InitData() {
      state.tableData = [];
      //apiurl.value = baseurl.value + "cyclecount/manualcyclecount/";
      getTableData("");
    }

    function getTableData(e) {
      axios
        .get(
          baseurl.value +
            `/cyclecount/manualcyclecount/?bin_name=${state.bin_name}&goods_code=${state.goods_code}`,
          {
            headers: {
              "Content-Type": 'application/json, charset="utf-8"',
              token: openid.value,
              language: lang.value,
              operator: operator.value,
            },
          }
        )
        .then((res) => {
          if (res.data && res.data.length > 0) {
            state.tableData = res.data;
          }
        });
    }

    function handleAffirmresultSubmit() {
      axios
        .post(baseurl.value + "/cyclecount/manualcyclecount/", state.tableData, {
          headers: {
            "Content-Type": 'application/json',
            token: openid.value,
            language: lang.value,
            operator: operator.value,
          },
        })
        .then((res) => {
          $q.notify({
            message: t('notice.handcount.notice7'),
          });
          state.affirmresultVisible = false;
          InitData();
        });
    }

    watch(bar_scanned, (newValue, oldValue) => {
      if (scanmode.value === "GOODS") {
        state.goods_code = scandata.value;
      }
      if (scanmode.value === "BINSET") {
        state.bin_name = scandata.value;
      }
      InitData();
    });
    watch(screenscroll, (newValue, oldValue) => {
      if (newValue === 1) {
        if (apiurlnext.value !== null) {
          apiurl.value = apiurlnext.value;
          requestauth.value = 1;
        }
      } else {
        requestauth.value = 0;
      }
    });
    watch(requestauth, (newValue, oldValue) => {
      if (newValue === 1) {
        if (authin.value === "0") {
          $q.notify({
            type: "negative",
            message: t("notice.mobile_userlogin.notice9"),
          });
        } else {
          getTableData("");
        }
      }
    });

    onMounted(() => {
      if (authin.value === '0') {
        $q.notify({
          type: 'negative',
          message: t('notice.mobile_userlogin.notice9')
        })
      } else {
        InitData()
      }
    })

    return {
      state,
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
      dndata,
      bindata,
      scanmode,
      bar_scanned,
      handleAffirmresultSubmit,

    };
  },
});
</script>
