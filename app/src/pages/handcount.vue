<template>
  <q-list bordered padding>
    <q-item>
      <q-item-section>
        <q-item-label overline>{{ $t("twoKai.tabname") }}</q-item-label>
        <q-item-label caption>{{
          $t("notice.mobile_asn.notice7")
        }}</q-item-label>
      </q-item-section>
    </q-item>
    <q-separator spaced />
    <q-item>
      <q-item-section>{{ $t("twoKai.particulars") }}</q-item-section>
      <q-item-section side>
        <q-btn
          @click="state.affirmresultVisible = true"
          color="primary"
          size="sm"
          >{{ $t("twoKai.affirmresult") }}</q-btn
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
            >{{ $t("twoKai.tablekucun") }}：{{ item.goods_qty }}</q-item-label
          >
          <q-item-label caption>
            <!--  {{ $t("twoKai.tablepandiannum") }}： -->
            <q-input
              dense
              outlined
              square
              v-model.number="item.physical_inventory"
              type="number"
              :style="{ width: '100px' }"
              :label="$t('twoKai.tablepandiannum')"
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
  <q-dialog v-model="uploaddialog">
    <q-card class="shadow-24">
      <q-bar
        class="bg-light-blue-10 text-white rounded-borders"
        style="height: 50px"
      >
        <div>{{ submitdata.goods_code }}</div>
        <q-space />
        <q-btn dense flat icon="close" v-close-popup>
          <q-tooltip>{{ $t("index.close") }}</q-tooltip>
        </q-btn>
      </q-bar>
      <q-card-section class="scroll">
        <q-input
          dense
          outlined
          square
          debounce="500"
          v-model.number="submitdata.qty"
          type="number"
          :label="$t('stock.view_stocklist.goods_qty')"
          style="margin-bottom: 5px"
          @click="submitdata.qty = ''"
          :rules="[(val) => (val && val > 0) || moveerror]"
        >
          <template v-slot:before>
            <q-select
              dense
              outlined
              square
              use-input
              hide-selected
              fill-input
              v-model="submitdata.bin_name"
              :label="$t('warehouse.view_binset.bin_name')"
              :options="options"
              @filter="filterFn"
              style="width: 150px"
            >
              <template v-slot:no-option>
                <q-item>
                  <q-item-section class="text-grey">
                    No results
                  </q-item-section>
                </q-item>
              </template>
              <template v-if="submitdata.bin_name" v-slot:append>
                <q-icon
                  name="cancel"
                  @click.stop="submitdata.bin_name = ''"
                  class="cursor-pointer"
                />
              </template>
            </q-select>
          </template>
        </q-input>
      </q-card-section>
      <div style="float: right; padding: 15px 15px 15px 0">
        <q-btn
          color="white"
          text-color="black"
          style="margin-right: 25px"
          @click="cancelToBin"
          >{{ $t("cancel") }}</q-btn
        >
        <q-btn color="primary" @click="submitToBin">{{ $t("submit") }}</q-btn>
      </div>
    </q-card>
  </q-dialog>

  <q-dialog v-model="state.affirmresultVisible">
    <q-card class="shadow-24">
      <q-bar
        class="bg-light-blue-10 text-white rounded-borders"
        style="height: 50px"
      >
        <div>{{ $t("twoKai.affirmcheckresult") }}</div>
        <q-space />
        <q-btn dense flat icon="close" v-close-popup>
          <q-tooltip>{{ $t("index.close") }}</q-tooltip>
        </q-btn>
      </q-bar>
      <q-card-section class="scroll"> 此操作不可逆。 </q-card-section>
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
    const submitdata = ref({});
    const uploaddialog = ref(false);
    const options = ref([]);
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
            `cyclecount/manualcyclecount/?bin_name=${state.bin_name}&goods_code=${state.goods_code}`,
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
          console.log(res.data, "------");
          if (res.data && res.data.length > 0) {
            //tablelist.value = JSON.parse(JSON.stringify(res.data));
            state.tableData = res.data;
            /*   apiurlprevious.value = sslCheck(res.data.previous);
            apiurlnext.value = sslCheck(res.data.next); */
          }
        });
    }
    function upLoadToBin(e) {
      submitdata.value = JSON.parse(JSON.stringify(e));
      Object.assign(submitdata.value, { qty: "", bin_name: "" });
      uploaddialog.value = true;
    }
    function cancelToBin() {
      uploaddialog.value = false;
    }

    function submitToBin() {
      if (submitdata.value.bin_name === "") {
        $q.notify({
          type: "negative",
          message: "Please Enter the Bin Name",
        });
      } else {
        apiurl.value = baseurl.value + "/asn/movetobin/";
        axios
          .post(apiurl.value + submitdata.value.id + "/", submitdata.value, {
            headers: {
              "Content-Type": "application/json",
              token: openid.value,
              language: lang.value,
              operator: operator.value,
            },
          })
          .then((res) => {
            cancelToBin();
            InitData();
            if (!res.data.detail) {
              $q.notify({
                message: "Success Move To Bin",
              });
            }
          })
          .catch((err) => {
            $q.notify({
              message: err.detail,
            });
          });
      }
    }

    function handleAffirmresultSubmit() {
      console.log(state.tableData);
      axios
        .post(baseurl.value + "cyclecount/manualcyclecount/", state.tableData, {
          headers: {
            "Content-Type": 'application/json',
            token: openid.value,
            language: lang.value,
            operator: operator.value,
          },
        })
        .then((res) => {
          $q.notify({
            message: "Success Confirm Cycle Count",
            icon: "check",
            color: "green",
          });
          state.affirmresultVisible = false;
          InitData();
        });
    }

    watch(bar_scanned, (newValue, oldValue) => {
      console.log(8888);
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
      InitData();
      /* if (scanmode.value === "ASN") {
        InitData();
      } */
    });

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
      submitdata,
      uploaddialog,
      upLoadToBin,
      cancelToBin,
      submitToBin,
      options,
      handleAffirmresultSubmit,
      moveerror: t("notice.mobile_asn.notice11"),

      filterFn(val, update, abort) {
        if (val.length < 2) {
          abort();
          return;
        }
        update(() => {
          const needle = val.toLowerCase();
          apiurl.value = baseurl.value + "/binset/?bin_name__icontains=";
          axios
            .get(apiurl.value + val, {
              headers: {
                "Content-Type": 'application/json, charset="utf-8"',
                token: openid.value,
                language: lang.value,
                operator: operator.value,
              },
            })
            .then((res) => {
              if (!res.data.detail) {
                var binlist = [];
                res.data.results.forEach((item) => {
                  binlist.push(item.bin_name);
                });
                options.value = binlist.filter(
                  (v) => v.toLowerCase().indexOf(needle) > -1
                );
              }
            })
            .catch((err) => {
              $q.notify({
                type: "negative",
                message: t("notice.mobile_scan.notice3"),
              });
            });
        });
      },
    };
  },
});
</script>
