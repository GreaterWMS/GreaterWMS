<template>
  <div>
    <transition appear enter-active-class="animated fadeIn">
      <q-table
        class="my-sticky-header-column-table shadow-24"
        :data="table_list"
        row-key="id"
        :separator="separator"
        :loading="loading"
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
              :label="$t('handcount.handcount')"
              icon="refresh"
              @click="handcountVisible = true"
            >
              <q-tooltip
                content-class="bg-amber text-black shadow-4"
                :offset="[10, 10]"
                content-style="font-size: 12px"
                >{{ $t("handcount.handcount") }}</q-tooltip
              >
            </q-btn>
            <q-btn
              :label="$t('stock.view_stocklist.downloadcyclecount')"
              icon="cloud_download"
              @click="downloadData()"
            >
              <q-tooltip
                content-class="bg-amber text-black shadow-4"
                :offset="[10, 10]"
                content-style="font-size: 12px"
              >
                {{ $t("stock.view_stocklist.downloadcyclecounttip") }}
              </q-tooltip>
            </q-btn>
          </q-btn-group>
          <q-space />
          <q-btn-group push>
            <q-btn
              color="purple"
              :label="$t('stock.view_stocklist.cyclecountresult')"
              @click="ConfirmCounts()"
            >
              <q-tooltip
                content-class="bg-amber text-black shadow-4"
                :offset="[10, 10]"
                content-style="font-size: 12px"
              >
                {{ $t("stock.view_stocklist.cyclecountresulttip") }}
              </q-tooltip>
            </q-btn>
          </q-btn-group>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td key="bin_name" :props="props">{{ props.row.bin_name }}</q-td>
            <q-td key="goods_code" :props="props">{{
              props.row.goods_code
            }}</q-td>
            <q-td key="goods_qty" :props="props">{{
              props.row.goods_qty
            }}</q-td>
            <q-td key="physical_inventory" :props="props">
              <q-input
                dense
                outlined
                square
                v-model.number="props.row.physical_inventory"
                type="number"
                :label="$t('stock.view_stocklist.physical_inventory')"
                :rules="[(val) => (val && val > 0) || val == 0 || error1]"
                @blur="blurHandler(props.row.physical_inventory)"
              />
            </q-td>
            <q-td key="difference" :props="props">{{
              props.row.physical_inventory - props.row.goods_qty
            }}</q-td>
            <q-td key="action" :props="props" style="width: 50px">
              <q-btn
                round
                flat
                push
                color="purple"
                icon="repeat"
                @click="props.row.physical_inventory = 0"
              >
                <q-tooltip
                  content-class="bg-amber text-black shadow-4"
                  :offset="[10, 10]"
                  content-style="font-size: 12px"
                >
                  {{ $t("stock.view_stocklist.recyclecounttip") }}
                </q-tooltip>
              </q-btn>
            </q-td>
          </q-tr>
        </template>
      </q-table>
    </transition>
    <template>
      <div class="q-pa-lg flex flex-center">
        <q-btn flat push color="dark" :label="$t('no_data')"></q-btn>
      </div>
    </template>
    <q-dialog v-model="CountFrom">
      <q-card class="shadow-24">
        <q-bar
          class="bg-light-blue-10 text-white rounded-borders"
          style="height: 50px"
        >
          <div>{{ $t("confirminventoryresults") }}</div>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-amber text-black shadow-4">{{
              $t("index.close")
            }}</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section
          style="max-height: 325px; width: 400px"
          class="scroll"
          >{{ $t("deletetip") }}</q-card-section
        >
        <div style="float: right; padding: 15px 15px 15px 0">
          <q-btn
            color="white"
            text-color="black"
            style="margin-right: 25px"
            @click="preloadDataCancel()"
            >{{ $t("cancel") }}</q-btn
          >
          <q-btn color="primary" @click="ConfirmCount()">{{
            $t("submit")
          }}</q-btn>
        </div>
      </q-card>
    </q-dialog>

    <q-dialog v-model="handcountVisible">
      <q-card class="shadow-24">
        <q-bar
          class="bg-light-blue-10 text-white rounded-borders"
          style="height: 50px"
        >
          <div>{{ $t("handcount.handcount") }}</div>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-amber text-black shadow-4">{{
              $t("index.close")
            }}</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section style="max-height: 325px; width: 400px" class="scroll">
          <q-select
            ref="one"
            dense
            outlined
            square
            use-input
            hide-selected
            fill-input
            v-model="handcountVal"
            :label="$t('goods.view_goodslist.goods_code')"
            :options="skuOptions"
            @input-value="setOptions"
            @filter="filterFn"
          >
            <template v-slot:no-option>
              <q-item
                ><q-item-section class="text-grey"
                  >No results</q-item-section
                ></q-item
              >
            </template>
            <template v-if="handcountVal" v-slot:append>
              <q-icon
                name="cancel"
                @click.stop="handcountVal = ''"
                class="cursor-pointer"
              />
            </template>
          </q-select>
          <div style="float: right; padding: 15px 15px 15px 0">
            <q-btn
              color="white"
              text-color="black"
              style="margin-right: 25px"
              @click="(handcountVisible = false), (handcountVal = '')"
              >{{ $t("cancel") }}</q-btn
            >
            <q-btn color="primary" @click="handleHandcountSubmit">{{
              $t("submit")
            }}</q-btn>
          </div>
        </q-card-section>
      </q-card>
    </q-dialog>
  </div>
</template>
<router-view />
<script>
import { date, exportFile, LocalStorage, SessionStorage } from 'quasar'
import { getauth, getfile, postauth } from 'boot/axios_request'

export default {
  name: 'cyclyecount',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'cyclecount/getgoodscyclecount/',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      bin_size_list: [],
      bin_property_list: [],
      warehouse_list: [],
      columns: [
        {
          name: 'bin_name',
          required: true,
          label: this.$t('warehouse.view_binset.bin_name'),
          align: 'left',
          field: 'bin_name'
        },
        {
          name: 'goods_code',
          label: this.$t('stock.view_stocklist.goods_code'),
          field: 'goods_code',
          align: 'center'
        },
        {
          name: 'goods_qty',
          label: this.$t('stock.view_stocklist.on_hand_inventory'),
          field: 'goods_qty',
          align: 'center'
        },
        {
          name: 'physical_inventory',
          label: this.$t('stock.view_stocklist.physical_inventory'),
          field: 'physical_inventory',
          align: 'center'
        },
        {
          name: 'difference',
          label: this.$t('stock.view_stocklist.difference'),
          field: 'difference',
          align: 'center'
        },
        { name: 'action', label: this.$t('action'), align: 'right' }
      ],
      pagination: {
        page: 1,
        rowsPerPage: '10000'
      },
      options: [],
      error1: this.$t('stock.view_stocklist.error1'),
      CountFrom: false,
      handcountVisible: false,
      handcountVal: '',
      skuOptions: SessionStorage.getItem('goods_code'),
      options1: []
    }
  },
  methods: {
    setOptions (val) {
      const _this = this
      const needle = val.toLowerCase()
      getauth('goods/?goods_code__icontains=' + needle).then((res) => {
        const goodscodelist = []
        for (let i = 0; i < res.results.length; i++) {
          goodscodelist.push(res.results[i].goods_code)
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
        this.skuOptions = this.options1
      })
    },
    getList () {
      var _this = this
      getauth('cyclecount/manualcyclecount/')
        .then((res) => {
          _this.table_list = res
          _this.handcountVisible = false
        })
        .catch((err) => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    reFresh () {
      var _this = this
      _this.getList()
    },
    ConfirmCount () {
      var _this = this
      if (!_this.table_list.length) {
        _this.CountFrom = false
        _this.$q.notify({
          message: _this.$t('notice.cyclecounterror'),
          icon: 'close',
          color: 'negative'
        })
      } else {
        postauth('cyclecount/manualcyclecount/', _this.table_list)
          .then((res) => {
            _this.CountFrom = false
            _this.$q.notify({
              message: 'Success Confirm Cycle Count',
              icon: 'check',
              color: 'green'
            })
            _this.table_list = []
            _this.reFresh()
          })
          .catch((err) => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            })
          })
      }
    },
    preloadDataCancel () {
      var _this = this
      _this.CountFrom = false
    },
    downloadData () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getfile(
          'cyclecount/manualfilecyclecount/?lang=' +
            LocalStorage.getItem('lang')
        ).then((res) => {
          var timeStamp = Date.now()
          var formattedString = date.formatDate(timeStamp, 'YYYYMMDDHHmmssSSS')
          const status = exportFile(
            'manualcyclecountday_' + formattedString + '.csv',
            '\uFEFF' + res.data,
            'text/csv'
          )
          if (status !== true) {
            _this.$q.notify({
              message: 'Browser denied file download...',
              color: 'negative',
              icon: 'warning'
            })
          }
        })
      } else {
        _this.$q.notify({
          message: _this.$t('notice.loginerror'),
          color: 'negative',
          icon: 'warning'
        })
      }
    },
    ConfirmCounts () {
      var _this = this
      _this.CountFrom = true
    },
    blurHandler (val) {
      val = val.toString().replace(/^(0+)|[^\d]+/g, '')
    },
    handleHandcountSubmit () {
      if (!this.handcountVal) {
        this.$q.notify({
          message: 'Please Enter SKU',
          icon: 'close',
          color: 'negative'
        })
        return
      }
      var _this = this
      getauth(
        'cyclecount/getgoodscyclecount/' + `?goods_code=${this.handcountVal}`
      )
        .then((res) => {
          this.getList()
          this.handcountVal = ''
        })
        .catch((err) => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
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
      _this.getList()
    } else {
      _this.authin = '0'
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
