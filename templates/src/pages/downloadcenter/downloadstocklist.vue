<template>
  <div>
    <transition appear enter-active-class="animated fadeIn">
      <q-table
        class="shadow-24"
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
          <div class="flex items-center">
            <div class="q-mr-md">{{ $t("download_center.createTime") }}</div>
            <q-input
              readonly
              outlined
              dense
              v-model="createDate2"
              :placeholder="interval"
            >
              <template v-slot:append>
                <q-icon name="event" class="cursor-pointer">
                  <q-popup-proxy
                    ref="qDateProxy"
                    transition-show="scale"
                    transition-hide="scale"
                    ><q-date v-model="createDate1" range
                  /></q-popup-proxy>
                </q-icon>
              </template>
            </q-input>
            <q-btn-group push class="q-ml-md">
              <q-btn
                :label="$t('download_center.reset')"
                icon="img:statics/downloadcenter/reset.svg"
                @click="reset()"
              >
              </q-btn>
              <q-btn
                :label="$t('downloadasnlist')"
                icon="cloud_download"
                @click="downloadlistData()"
              >
              </q-btn>
            </q-btn-group>
          </div>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td key="goods_code" :props="props">{{
              props.row.goods_code
            }}</q-td>
            <q-td key="goods_desc" :props="props">{{
              props.row.goods_desc
            }}</q-td>
            <q-td key="goods_qty" :props="props">{{
              props.row.goods_qty
            }}</q-td>
            <q-td key="onhand_stock" :props="props">{{
              props.row.onhand_stock
            }}</q-td>
            <q-td key="can_order_stock" :props="props">{{
              props.row.can_order_stock
            }}</q-td>
            <q-td key="ordered_stock" :props="props">{{
              props.row.ordered_stock
            }}</q-td>
            <q-td key="inspect_stock" :props="props">{{
              props.row.inspect_stock
            }}</q-td>
            <q-td key="hold_stock" :props="props">{{
              props.row.hold_stock
            }}</q-td>
            <q-td key="damage_stock" :props="props">{{
              props.row.damage_stock
            }}</q-td>
            <q-td key="asn_stock" :props="props">{{
              props.row.asn_stock
            }}</q-td>
            <q-td key="dn_stock" :props="props">{{ props.row.dn_stock }}</q-td>
            <q-td key="pre_load_stock" :props="props">{{
              props.row.pre_load_stock
            }}</q-td>
            <q-td key="pre_sort_stock" :props="props">{{
              props.row.pre_sort_stock
            }}</q-td>
            <q-td key="sorted_stock" :props="props">{{
              props.row.sorted_stock
            }}</q-td>
            <q-td key="pick_stock" :props="props">{{
              props.row.pick_stock
            }}</q-td>
            <q-td key="picked_stock" :props="props">{{
              props.row.picked_stock
            }}</q-td>
            <q-td key="back_order_stock" :props="props">{{
              props.row.back_order_stock
            }}</q-td>
            <q-td key="create_time" :props="props">{{
              props.row.create_time
            }}</q-td>
            <q-td key="update_time" :props="props">{{
              props.row.update_time
            }}</q-td>
          </q-tr>
        </template>
      </q-table>
    </transition>
    <template>
        <div v-show="max !== 0" class="q-pa-lg flex flex-center">
           <div>{{ total }} </div>
          <q-pagination
            v-model="current"
            color="black"
            :max="max"
            :max-pages="6"
            boundary-links
            @click="getList()"
          />
          <div>
            <input
              v-model="paginationIpt"
              @blur="changePageEnter"
              @keyup.enter="changePageEnter"
              style="width: 60px; text-align: center"
            />
          </div>
        </div>
        <div v-show="max === 0" class="q-pa-lg flex flex-center">
          <q-btn flat push color="dark" :label="$t('no_data')"></q-btn>
        </div>
    </template>
  </div>
</template>
<router-view />

<script>
import { getauth, getfile } from 'boot/axios_request'
import { date, exportFile, LocalStorage } from 'quasar'

export default {
  name: 'Pagestockdownload',
  data () {
    return {
      login_name: '',
      authin: '0',
      pathname: 'stock/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      columns: [
        { name: 'goods_code', required: true, label: this.$t('stock.view_stocklist.goods_code'), align: 'left', field: 'goods_code' },
        { name: 'goods_desc', label: this.$t('stock.view_stocklist.goods_desc'), field: 'goods_desc', align: 'center' },
        { name: 'goods_qty', label: this.$t('stock.view_stocklist.goods_qty'), field: 'goods_qty', align: 'center' },
        { name: 'onhand_stock', label: this.$t('stock.view_stocklist.onhand_stock'), field: 'onhand_stock', align: 'center' },
        { name: 'can_order_stock', label: this.$t('stock.view_stocklist.can_order_stock'), field: 'can_order_stock', align: 'center' },
        { name: 'ordered_stock', label: this.$t('stock.view_stocklist.ordered_stock'), field: 'ordered_stock', align: 'center' },
        { name: 'inspect_stock', label: this.$t('stock.view_stocklist.inspect_stock'), field: 'inspect_stock', align: 'center' },
        { name: 'hold_stock', label: this.$t('stock.view_stocklist.hold_stock'), field: 'hold_stock', align: 'center' },
        { name: 'damage_stock', label: this.$t('stock.view_stocklist.damage_stock'), field: 'damage_stock', align: 'center' },
        { name: 'asn_stock', label: this.$t('stock.view_stocklist.asn_stock'), field: 'asn_stock', align: 'center' },
        { name: 'dn_stock', label: this.$t('stock.view_stocklist.dn_stock'), field: 'dn_stock', align: 'center' },
        { name: 'pre_load_stock', label: this.$t('stock.view_stocklist.pre_load_stock'), field: 'pre_load_stock', align: 'center' },
        { name: 'pre_sort_stock', label: this.$t('stock.view_stocklist.pre_sort_stock'), field: 'pre_sort_stock', align: 'center' },
        { name: 'sorted_stock', label: this.$t('stock.view_stocklist.sorted_stock'), field: 'sorted_stock', align: 'center' },
        { name: 'pick_stock', label: this.$t('stock.view_stocklist.pick_stock'), field: 'pick_stock', align: 'center' },
        { name: 'picked_stock', label: this.$t('stock.view_stocklist.picked_stock'), field: 'picked_stock', align: 'center' },
        { name: 'back_order_stock', label: this.$t('stock.view_stocklist.back_order_stock'), field: 'back_order_stock', align: 'center' },
        { name: 'create_time', label: this.$t('createtime'), field: 'create_time', align: 'center' },
        { name: 'update_time', label: this.$t('updatetime'), field: 'update_time', align: 'center' }
      ],
      pagination: {
        page: 1,
        rowsPerPage: '30'
      },
      createDate1: '',
      createDate2: '',
      date_range: '',
      searchUrl: '',
      downloadUrl: 'stock/filelist/',
      current: 1,
      max: 0,
      total: 0,
      paginationIpt: 1
    }
  },
  computed: {
    interval () {
      return this.$t('download_center.start') + ' - ' + this.$t('download_center.end')
    }
  },
  watch: {
    createDate1 (val) {
      if (val) {
        if (val.to) {
          this.createDate2 = `${val.from} - ${val.to}`
          this.date_range = `${val.from},${val.to} 23:59:59`
          this.searchUrl = this.pathname + 'list/?' + 'create_time__range=' + this.date_range
          this.downloadUrl = this.pathname + 'filelist/?' + 'create_time__range=' + this.date_range
        } else {
          this.createDate2 = `${val}`
          this.dateArray = val.split('/')
          this.searchUrl = this.pathname + 'list/?' + 'create_time__year=' + this.dateArray[0] + '&' + 'create_time__month=' + this.dateArray[1] + '&' + 'create_time__day=' + this.dateArray[2]
          this.downloadUrl = this.pathname + 'filelist/?' + 'create_time__year=' + this.dateArray[0] + '&' + 'create_time__month=' + this.dateArray[1] + '&' + 'create_time__day=' + this.dateArray[2]
        }
        this.date_range = this.date_range.replace(/\//g, '-')
        this.getSearchList()
        this.$refs.qDateProxy.hide()
      }
    }
  },
  methods: {
    getList () {
      var _this = this
      getauth(_this.pathname + 'list/?ordering=-update_time' + '&page=' + '' + _this.current, {})
        .then(res => {
          _this.table_list = res.results
          _this.total = res.count
          if (res.count === 0) {
            _this.max = 0
          } else {
            if (Math.ceil(res.count / 30) === 1) {
              _this.max = 0
            } else {
              _this.max = Math.ceil(res.count / 30)
            }
          }
          _this.pathname_previous = res.previous
          _this.pathname_next = res.next
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    changePageEnter (e) {
      if (Number(this.paginationIpt) < 1) {
        this.current = 1
        this.paginationIpt = 1
      } else if (Number(this.paginationIpt) > this.max) {
        this.current = this.max
        this.paginationIpt = this.max
      } else {
        this.current = Number(this.paginationIpt)
      }
      this.getList()
    },
    getSearchList () {
      var _this = this
      getauth(_this.searchUrl + '&page=' + '' + _this.current)
        .then(res => {
          _this.table_list = res.results
          _this.total = res.count
          if (res.count === 0) {
            _this.max = 0
          } else {
            if (Math.ceil(res.count / 30) === 1) {
              _this.max = 0
            } else {
              _this.max = Math.ceil(res.count / 30)
            }
          }
          _this.pathname_previous = res.previous
          _this.pathname_next = res.next
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    getListPrevious () {
      var _this = this
      getauth(_this.pathname_previous, {})
        .then(res => {
          _this.table_list = res.results
          _this.pathname_previous = res.previous
          _this.pathname_next = res.next
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    getListNext () {
      var _this = this
      getauth(_this.pathname_next, {})
        .then(res => {
          _this.table_list = res.results
          _this.pathname_previous = res.previous
          _this.pathname_next = res.next
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    downloadlistData () {
      var _this = this
      getfile(_this.downloadUrl).then(res => {
        var timeStamp = Date.now()
        var formattedString = date.formatDate(timeStamp, 'YYYYMMDDHHmmssSSS')
        const status = exportFile(_this.pathname + 'list' + formattedString + '.csv', '\uFEFF' + res.data, 'text/csv')
        if (status !== true) {
          _this.$q.notify({
            message: 'Browser denied file download...',
            color: 'negative',
            icon: 'warning'
          })
        }
      })
    },
    reset () {
      this.getList()
      this.downloadUrl = 'stock/filelist/'
      this.createDate2 = ''
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
