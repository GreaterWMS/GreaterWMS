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
            <q-td key="goods_supplier" :props="props">{{
              props.row.goods_supplier
            }}</q-td>
            <q-td key="goods_weight" :props="props">{{
              props.row.goods_weight
            }}</q-td>
            <q-td key="goods_w" :props="props">{{ props.row.goods_w }}</q-td>
            <q-td key="goods_d" :props="props">{{ props.row.goods_d }}</q-td>
            <q-td key="goods_h" :props="props">{{ props.row.goods_h }}</q-td>
            <q-td key="unit_volume" :props="props">{{
              props.row.unit_volume
            }}</q-td>
            <q-td key="goods_unit" :props="props">{{
              props.row.goods_unit
            }}</q-td>
            <q-td key="goods_class" :props="props">{{
              props.row.goods_class
            }}</q-td>
            <q-td key="goods_brand" :props="props">{{
              props.row.goods_brand
            }}</q-td>
            <q-td key="goods_color" :props="props">{{
              props.row.goods_color
            }}</q-td>
            <q-td key="goods_shape" :props="props">{{
              props.row.goods_shape
            }}</q-td>
            <q-td key="goods_specs" :props="props">{{
              props.row.goods_specs
            }}</q-td>
            <q-td key="goods_origin" :props="props">{{
              props.row.goods_origin
            }}</q-td>
            <q-td key="goods_cost" :props="props">{{
              props.row.goods_cost
            }}</q-td>
            <q-td key="goods_price" :props="props">{{
              props.row.goods_price
            }}</q-td>
            <q-td key="creater" :props="props">{{ props.row.creater }}</q-td>
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
  name: 'Pagegoodsdownload',
  data () {
    return {
      login_name: '',
      authin: '0',
      pathname: 'goods/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      columns: [
        { name: 'goods_code', required: true, label: this.$t('goods.view_goodslist.goods_code'), align: 'left', field: 'goods_code' },
        { name: 'goods_desc', label: this.$t('goods.view_goodslist.goods_desc'), field: 'goods_desc', align: 'center' },
        { name: 'goods_supplier', label: this.$t('goods.view_goodslist.goods_supplier'), field: 'goods_supplier', align: 'center' },
        { name: 'goods_weight', label: this.$t('goods.view_goodslist.goods_weight'), field: 'goods_weight', align: 'center' },
        { name: 'goods_w', label: this.$t('goods.view_goodslist.goods_w'), field: 'goods_w', align: 'center' },
        { name: 'goods_d', label: this.$t('goods.view_goodslist.goods_d'), field: 'goods_d', align: 'center' },
        { name: 'goods_h', label: this.$t('goods.view_goodslist.goods_h'), field: 'goods_h', align: 'center' },
        { name: 'unit_volume', label: this.$t('goods.view_goodslist.unit_volume'), field: 'unit_volume', align: 'center' },
        { name: 'goods_unit', label: this.$t('goods.view_goodslist.goods_unit'), field: 'goods_unit', align: 'center' },
        { name: 'goods_class', label: this.$t('goods.view_goodslist.goods_class'), field: 'goods_class', align: 'center' },
        { name: 'goods_brand', label: this.$t('goods.view_goodslist.goods_brand'), field: 'goods_brand', align: 'center' },
        { name: 'goods_color', label: this.$t('goods.view_goodslist.goods_color'), field: 'goods_color', align: 'center' },
        { name: 'goods_shape', label: this.$t('goods.view_goodslist.goods_shape'), field: 'goods_shape', align: 'center' },
        { name: 'goods_specs', label: this.$t('goods.view_goodslist.goods_specs'), field: 'goods_specs', align: 'center' },
        { name: 'goods_origin', label: this.$t('goods.view_goodslist.goods_origin'), field: 'goods_origin', align: 'center' },
        { name: 'goods_cost', label: this.$t('goods.view_goodslist.goods_cost'), field: 'goods_cost', align: 'center' },
        { name: 'goods_price', label: this.$t('goods.view_goodslist.goods_price'), field: 'goods_price', align: 'center' },
        { name: 'creater', label: this.$t('creater'), field: 'creater', align: 'center' },
        { name: 'create_time', label: this.$t('createtime'), field: 'create_time', align: 'center' },
        { name: 'update_time', label: this.$t('updatetime'), field: 'update_time', align: 'right' }
      ],
      pagination: {
        page: 1,
        rowsPerPage: '30'
      },
      createDate1: '',
      createDate2: '',
      date_range: '',
      searchUrl: '',
      downloadUrl: 'goods/file/',
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
          this.searchUrl = this.pathname + '?' + 'create_time__range=' + this.date_range
          this.downloadUrl = this.pathname + 'file/?' + 'create_time__range=' + this.date_range
        } else {
          this.createDate2 = `${val}`
          this.dateArray = val.split('/')
          this.searchUrl = this.pathname + '?' + 'create_time__year=' + this.dateArray[0] + '&' + 'create_time__month=' + this.dateArray[1] + '&' + 'create_time__day=' + this.dateArray[2]
          this.downloadUrl = this.pathname + 'file/?' + 'create_time__year=' + this.dateArray[0] + '&' + 'create_time__month=' + this.dateArray[1] + '&' + 'create_time__day=' + this.dateArray[2]
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
      getauth(_this.pathname + '?page=' + '' + _this.current, {})
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
    changePageEnter(e) {
      if (Number(this.paginationIpt) < 1) {
        this.current = 1;
        this.paginationIpt = 1;
      } else if (Number(this.paginationIpt) > this.max) {
        this.current = this.max;
        this.paginationIpt = this.max;
      } else {
        this.current = Number(this.paginationIpt);
      }
      this.getList();
    },
    getSearchList () {
      var _this = this
      _this.current = 1
      _this.paginationIpt = 1
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
      this.downloadUrl = 'goods/file/'
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
