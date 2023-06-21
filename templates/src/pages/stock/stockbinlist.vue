<template>
  <div>
    <transition appear enter-active-class="animated fadeIn">
      <q-table
        class="my-sticky-header-column-table shadow-24"
        :data="table_list"
        row-key="id"
        :separator="separator"
        :loading="loading"
        :filter="filter"
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
            <q-btn :label="$t('refresh')" icon="refresh" @click="reFresh()">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('refreshtip') }}</q-tooltip>
            </q-btn>
          </q-btn-group>
          <q-space />
          <q-input outlined rounded dense debounce="300" color="primary" v-model="filter" :placeholder="$t('search')" @input="getSearchList()" @keyup.enter="getSearchList()">
            <template v-slot:append>
              <q-icon name="search" @click="getSearchList()" />
            </template>
          </q-input>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td key="bin_name" :props="props">{{ props.row.bin_name }}</q-td>
            <q-td key="goods_code" :props="props">{{ props.row.goods_code }}</q-td>
            <q-td key="goods_desc" :props="props">{{ props.row.goods_desc }}</q-td>
            <q-td key="goods_qty" :props="props">{{ props.row.goods_qty }}</q-td>
            <q-td key="pick_qty" :props="props">{{ props.row.pick_qty }}</q-td>
            <q-td key="picked_qty" :props="props">{{ props.row.picked_qty }}</q-td>
            <q-td key="bin_size" :props="props">{{ props.row.bin_size }}</q-td>
            <q-td key="bin_property" :props="props">{{ props.row.bin_property }}</q-td>
            <q-td key="create_time" :props="props">{{ props.row.create_time }}</q-td>
            <q-td key="update_time" :props="props">{{ props.row.update_time }}</q-td>
            <q-td key="action" :props="props" style="width: 50px">
              <q-btn
                v-show="$q.localStorage.getItem('staff_type') !== 'Inbound' && $q.localStorage.getItem('staff_type') !== 'Outbound'"
                round
                flat
                push
                color="purple"
                icon="move_to_inbox"
                @click="BinMove(props.row)"
              >
                <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('movetobin') }}</q-tooltip>
              </q-btn>
            </q-td>
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
    <q-dialog v-model="moveForm">
      <q-card class="shadow-24">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <div>{{ movedata.goods_code }} {{ $t('frombin') }} {{ movedata.bin_name }}</div>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip>{{ $t('index.close') }}</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section style="max-height: 325px; width: 400px" class="scroll">
          <q-input
            dense
            outlined
            square
            debounce="500"
            v-model.number="movedata.move_qty"
            type="number"
            :label="$t('stock.view_stocklist.goods_qty')"
            style="margin-bottom: 5px"
            :rules="[val => (val && val > 0) || error1]"
            @keyup.enter="MoveToBinSubmit()"
          >
            <template v-slot:before>
              <q-select
                dense
                outlined
                square
                use-input
                hide-selected
                fill-input
                v-model="movedata.move_to_bin"
                :label="$t('warehouse.view_binset.bin_name')"
                :options="options"
                @filter="filterFn"
                @keyup.enter="MoveToBinSubmit()"
              >
                <template v-slot:no-option>
                  <q-item><q-item-section class="text-grey">No results</q-item-section></q-item>
                </template>
                <template v-if="movedata.move_to_bin" v-slot:append>
                  <q-icon name="cancel" @click.stop="movedata.move_to_bin = ''" class="cursor-pointer" />
                </template>
              </q-select>
            </template>
          </q-input>
        </q-card-section>
        <div style="float: right; padding: 15px 15px 15px 0">
          <q-btn color="white" text-color="black" style="margin-right: 25px" @click="MoveToBinCancel()">{{ $t('cancel') }}</q-btn>
          <q-btn color="primary" @click="MoveToBinSubmit()">{{ $t('submit') }}</q-btn>
        </div>
      </q-card>
    </q-dialog>
  </div>
</template>
<router-view />

<script>
import { getauth, postauth } from 'boot/axios_request'
import { SessionStorage, LocalStorage } from 'quasar'

export default {
  name: 'Pagestockbinlist',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'stock/bin/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      bin_size_list: [],
      bin_property_list: [],
      warehouse_list: [],
      columns: [
        { name: 'bin_name', required: true, label: this.$t('warehouse.view_binset.bin_name'), align: 'left', field: 'bin_name' },
        { name: 'goods_code', label: this.$t('stock.view_stocklist.goods_code'), field: 'goods_code', align: 'center' },
        { name: 'goods_desc', label: this.$t('stock.view_stocklist.goods_desc'), field: 'onhand_stock', align: 'center' },
        { name: 'goods_qty', label: this.$t('stock.view_stocklist.onhand_stock'), field: 'goods_qty', align: 'center' },
        { name: 'pick_qty', label: this.$t('stock.view_stocklist.pick_stock'), field: 'pick_qty', align: 'center' },
        { name: 'picked_qty', label: this.$t('stock.view_stocklist.picked_stock'), field: 'picked_qty', align: 'center' },
        { name: 'bin_size', label: this.$t('warehouse.view_binset.bin_size'), field: 'bin_size', align: 'center' },
        { name: 'bin_property', label: this.$t('warehouse.view_binset.bin_property'), field: 'bin_property', align: 'center' },
        { name: 'create_time', label: this.$t('createtime'), field: 'create_time', align: 'center' },
        { name: 'update_time', label: this.$t('updatetime'), field: 'update_time', align: 'center' },
        { name: 'action', label: this.$t('action'), align: 'right' }
      ],
      filter: '',
      pagination: {
        page: 1,
        rowsPerPage: '30'
      },
      options: [],
      moveForm: false,
      movedata: {},
      error1: this.$t('inbound.view_sortstock.error1'),
      current: 1,
      max: 0,
      total: 0,
      paginationIpt: 1
    }
  },
  methods: {
    getList () {
      var _this = this
      if (LocalStorage.has('auth')) {
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
            if (LocalStorage.getItem('lang') === 'zh-hans') {
              _this.table_list.forEach((item, index) => {
                if (item.bin_property === 'Damage') {
                  item.bin_property = '破损'
                } else if (item.bin_property === 'Inspection') {
                  item.bin_property = '质检'
                } else if (item.bin_property === 'Holding') {
                  item.bin_property = '锁货'
                } else if (item.bin_property === 'Normal') {
                  item.bin_property = '正常库位'
                }
              })
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
      }
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
      if (LocalStorage.has('auth')) {
        _this.current = 1
        _this.paginationIpt = 1
        getauth(_this.pathname + '?bin_name__icontains=' + _this.filter + '&page=' + '' + _this.current, {})
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
            if (LocalStorage.getItem('lang') === 'zh-hans') {
              _this.table_list.forEach((item, index) => {
                if (item.bin_property === 'Damage') {
                  item.bin_property = '破损'
                } else if (item.bin_property === 'Inspection') {
                  item.bin_property = '质检'
                } else if (item.bin_property === 'Holding') {
                  item.bin_property = '锁货'
                } else if (item.bin_property === 'Normal') {
                  item.bin_property = '正常库位'
                }
              })
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
      } else {
      }
    },
    getListPrevious () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname_previous, {})
          .then(res => {
            _this.table_list = res.results
            if (LocalStorage.getItem('lang') === 'zh-hans') {
              _this.table_list.forEach((item, index) => {
                if (item.bin_property === 'Damage') {
                  item.bin_property = '破损'
                } else if (item.bin_property === 'Inspection') {
                  item.bin_property = '质检'
                } else if (item.bin_property === 'Holding') {
                  item.bin_property = '锁货'
                } else if (item.bin_property === 'Normal') {
                  item.bin_property = '正常库位'
                }
              })
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
      }
    },
    getListNext () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname_next, {})
          .then(res => {
            _this.table_list = res.results
            if (LocalStorage.getItem('lang') === 'zh-hans') {
              _this.table_list.forEach((item, index) => {
                if (item.bin_property === 'Damage') {
                  item.bin_property = '破损'
                } else if (item.bin_property === 'Inspection') {
                  item.bin_property = '质检'
                } else if (item.bin_property === 'Holding') {
                  item.bin_property = '锁货'
                } else if (item.bin_property === 'Normal') {
                  item.bin_property = '正常库位'
                }
              })
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
      } else {
      }
    },
    reFresh () {
      var _this = this
      _this.getList()
    },
    BinMove (e) {
      var _this = this
      _this.moveForm = true
      _this.movedata = e
    },
    MoveToBinCancel () {
      var _this = this
      _this.moveForm = false
      _this.movedata = {}
    },
    MoveToBinSubmit () {
      var _this = this
      postauth(_this.pathname + _this.movedata.id + '/', _this.movedata)
        .then(res => {
          _this.getList()
          _this.MoveToBinCancel()
          _this.$q.notify({
            message: 'Bin Moving Success',
            icon: 'check',
            color: 'green'
          })
        })
        .catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
    },
    filterFn (val, update, abort) {
      var _this = this
      if (val.length < 1) {
        abort()
        return
      }
      update(() => {
        const needle = val.toLowerCase()
        getauth('binset/?bin_name__icontains=' + needle)
          .then(res => {
            var binlist = []
            res.results.forEach(detail => {
              binlist.push(detail.bin_name)
            })
            SessionStorage.set('bin_name', binlist)
            _this.options = SessionStorage.getItem('bin_name')
          })
          .catch(err => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            })
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
