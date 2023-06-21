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
              <q-btn
                :label="$t('downloadasndetail')"
                icon="cloud_download"
                @click="downloaddetailData()"
              >
              </q-btn>
            </q-btn-group>
          </div>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td key="asn_code" :props="props">{{ props.row.asn_code }}</q-td>
            <q-td key="asn_status" :props="props">{{
              props.row.asn_status
            }}</q-td>
            <q-td key="total_weight" :props="props">{{
              props.row.total_weight.toFixed(4)
            }}</q-td>
            <q-td key="total_volume" :props="props">{{
              props.row.total_volume.toFixed(4)
            }}</q-td>
            <q-td key="supplier" :props="props">{{ props.row.supplier }}</q-td>
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
  name: 'Pageinbounddownload',
  data () {
    return {
      login_name: '',
      authin: '0',
      pathname: 'asn/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      columns: [
        { name: 'asn_code', required: true, label: this.$t('inbound.view_asn.asn_code'), align: 'left', field: 'asn_code' },
        { name: 'asn_status', label: this.$t('inbound.view_asn.asn_status'), field: 'asn_status', align: 'center' },
        { name: 'total_weight', label: this.$t('inbound.view_asn.total_weight'), field: 'total_weight', align: 'center' },
        { name: 'total_volume', label: this.$t('inbound.view_asn.total_volume'), field: 'total_volume', align: 'center' },
        { name: 'supplier', label: this.$t('baseinfo.view_supplier.supplier_name'), field: 'supplier', align: 'center' },
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
      dateArray: '',
      searchUrl: '',
      downloadUrl: 'asn/filelist/',
      downloadDetailUrl: 'asn/filedetail/',
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
          this.downloadDetailUrl = this.pathname + 'filedetail/?' + 'create_time__range=' + this.date_range
        } else {
          this.createDate2 = `${val}`
          this.dateArray = val.split('/')
          this.searchUrl = this.pathname + 'list/?' + 'create_time__year=' + this.dateArray[0] + '&' + 'create_time__month=' + this.dateArray[1] + '&' + 'create_time__day=' + this.dateArray[2]
          this.downloadUrl = this.pathname + 'filelist/?' + 'create_time__year=' + this.dateArray[0] + '&' + 'create_time__month=' + this.dateArray[1] + '&' + 'create_time__day=' + this.dateArray[2]
          this.downloadDetailUrl = this.pathname + 'filedetail/?' + 'create_time__year=' + this.dateArray[0] + '&' + 'create_time__month=' + this.dateArray[1] + '&' + 'create_time__day=' + this.dateArray[2]
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
      getauth(_this.pathname + 'list/' + '?page=' + '' + _this.current)
        .then(res => {
          _this.table_list = []
          res.results.forEach(item => {
            if (item.asn_status === 1) {
              item.asn_status = _this.$t('inbound.predeliverystock')
            } else if (item.asn_status === 2) {
              item.asn_status = _this.$t('inbound.preloadstock')
            } else if (item.asn_status === 3) {
              item.asn_status = _this.$t('inbound.presortstock')
            } else if (item.asn_status === 4) {
              item.asn_status = _this.$t('inbound.sortstock')
            } else if (item.asn_status === 5) {
              item.asn_status = _this.$t('inbound.asndone')
            } else {
              item.asn_status = 'N/A'
            }
            _this.table_list.push(item)
          })
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
      _this.current = 1
      _this.paginationIpt = 1
      getauth(_this.searchUrl + '&page=' + '' + _this.current)
        .then(res => {
          _this.table_list = []
          res.results.forEach(item => {
            if (item.asn_status === 1) {
              item.asn_status = _this.$t('inbound.predeliverystock')
            } else if (item.asn_status === 2) {
              item.asn_status = _this.$t('inbound.preloadstock')
            } else if (item.asn_status === 3) {
              item.asn_status = _this.$t('inbound.presortstock')
            } else if (item.asn_status === 4) {
              item.asn_status = _this.$t('inbound.sortstock')
            } else if (item.asn_status === 5) {
              item.asn_status = _this.$t('inbound.asndone')
            } else {
              item.asn_status = 'N/A'
            }
            _this.table_list.push(item)
          })
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
          _this.table_list = []
          res.results.forEach(item => {
            if (item.asn_status === 1) {
              item.asn_status = _this.$t('inbound.predeliverystock')
            } else if (item.asn_status === 2) {
              item.asn_status = _this.$t('inbound.preloadstock')
            } else if (item.asn_status === 3) {
              item.asn_status = _this.$t('inbound.presortstock')
            } else if (item.asn_status === 4) {
              item.asn_status = _this.$t('inbound.sortstock')
            } else if (item.asn_status === 5) {
              item.asn_status = _this.$t('inbound.asndone')
            } else {
              item.asn_status = 'N/A'
            }
            _this.table_list.push(item)
          })
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
          _this.table_list = []
          res.results.forEach(item => {
            if (item.asn_status === 1) {
              item.asn_status = _this.$t('inbound.predeliverystock')
            } else if (item.asn_status === 2) {
              item.asn_status = _this.$t('inbound.preloadstock')
            } else if (item.asn_status === 3) {
              item.asn_status = _this.$t('inbound.presortstock')
            } else if (item.asn_status === 4) {
              item.asn_status = _this.$t('inbound.sortstock')
            } else if (item.asn_status === 5) {
              item.asn_status = _this.$t('inbound.asndone')
            } else {
              item.asn_status = 'N/A'
            }
            _this.table_list.push(item)
          })
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
    downloaddetailData () {
      var _this = this
      getfile(_this.downloadDetailUrl).then(res => {
        var timeStamp = Date.now()
        var formattedString = date.formatDate(timeStamp, 'YYYYMMDDHHmmssSSS')
        const status = exportFile(_this.pathname + 'detail' + formattedString + '.csv', '\uFEFF' + res.data, 'text/csv')
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
      this.downloadUrl = 'asn/filelist/'
      this.downloadDetailUrl = 'asn/filedetail/'
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
