<template>
  <div>
    <q-input v-model="scaneddata.request_time" style="display:none" />
    <q-card v-show="!fab" :style="{ width: width,  height: height }">
      <q-card-section>
        <q-btn-group push>
          <q-btn color='purple' :label="$t('stock.view_stocklist.cyclecountresult')" @click="ConfirmCount()" />
        </q-btn-group>
      </q-card-section>
      <q-scroll-area
        :thumb-style="thumbStyle"
        :bar-style="barStyle"
        :style="{ height: scroll_height, width: width }"
      >
        <q-markup-table>
          <thead>
          <tr>
            <th class="text-center">{{ bin_name_label }}</th>
            <th class="text-center">{{ goods_code_label }}</th>
            <th class="text-center">{{ physical_label }}</th>
            <th class="text-center">{{ action_label }}</th>
          </tr>
          </thead>
          <tbody>
          <template>
            <tr v-for='(item, index) in table_list' :key='index'>
              <td :class="{'scan-background text-center': item.bin_name === bin_scan, 'text-center': item.bin_name !== bin_scan }">{{ item.bin_name }}</td>
              <td :class="{'scan-background text-center': item.bin_name === bin_scan && item.goods_code === goods_scan, 'text-center': item.bin_name !== bin_scan && item.goods_code !== goods_scan }">{{ item.goods_code }}</td>
              <td :class="{'scan-background text-center': item.bin_name === bin_scan && item.goods_code === goods_scan, 'text-center': item.bin_name !== bin_scan && item.goods_code !== goods_scan }">
                <input
                  v-model.number="item.physical_inventory"
                  type="number"
                  :label="physical_label"
                />
              </td>
              <td class="text-center">
                <q-btn round flat push color="purple" icon="repeat" @click="repeatCount(index)" style="width: 50px" />
              </td>
            </tr>
          </template>
          </tbody>
        </q-markup-table>
      </q-scroll-area>
      <q-separator dark />
    </q-card>
  </div>
</template>
<router-view />

<script>
import { getauth, putauth } from 'boot/axios_request'
import { LocalStorage, Screen } from 'quasar'

export default {
  name: 'Page_cyclecount',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'cyclecount/',
      width: '',
      height: '',
      scroll_height: '',
      table_list: [],
      bin_name_label: this.$t('warehouse.view_binset.bin_name'),
      goods_code_label: this.$t('stock.view_stocklist.goods_code'),
      physical_label: this.$t('stock.view_stocklist.physical_inventory'),
      action_label: this.$t('action'),
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
      bar_scanned: '',
      bin_scan: '',
      goods_scan: ''
    }
  },
  methods: {
    getList () {
      var _this = this
      getauth(_this.pathname, {
      }).then(res => {
        _this.table_list = res
      }).catch(err => {
        _this.$q.notify({
          message: err.detail,
          icon: 'close',
          color: 'negative'
        })
      })
    },
    getGoodsList (e) {
      var _this = this
      getauth('goods/?goods_code=' + e, {
      }).then(res => {
        if (res.results.length === 0) {
          navigator.vibrate(100)
          _this.$q.notify({
            message: 'No Goods Data',
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        } else if (res.results.length === 1) {
          _this.table_list.filter(item => {
            if (item.bin_name.includes(_this.bin_scan) && item.goods_code.includes(res.results[0].goods_code)) {
              _this.goods_scan = res.results[0].goods_code
              item.physical_inventory += 1
              item.difference = item.physical_inventory - item.goods_qty
              return false
            }
          })
        } else {
          navigator.vibrate(100)
          _this.$q.notify({
            message: 'Repeating Data',
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        }
      }).catch(err => {
        navigator.vibrate(100)
        _this.$q.notify({
          message: err.detail,
          position: 'top',
          icon: 'close',
          color: 'negative'
        })
      })
    },
    getBinList (e) {
      var _this = this
      getauth('binset/?bin_name=' + e, {
      }).then(res => {
        if (res.results.length === 0) {
          navigator.vibrate(100)
          _this.$q.notify({
            message: 'No Bin Data',
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        } else if (res.results.length === 1) {
          _this.bin_scan = res.results[0].bin_name
        } else {
          navigator.vibrate(100)
          _this.$q.notify({
            message: 'Repeating Data',
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        }
      }).catch(err => {
        navigator.vibrate(100)
        _this.$q.notify({
          message: err.detail,
          position: 'top',
          icon: 'close',
          color: 'negative'
        })
      })
    },
    repeatCount (e) {
      var _this = this
      _this.goods_scan = ''
      _this.table_list[e].physical_inventory = 0
    },
    ConfirmCount () {
      var _this = this
      putauth(_this.pathname, _this.table_list).then(res => {
        _this.reFresh()
        _this.$q.notify({
          message: 'Success Confirm Cycle Count',
          position: 'top',
          icon: 'check',
          color: 'green'
        })
      }).catch(err => {
        _this.$q.notify({
          message: err.detail,
          position: 'top',
          icon: 'close',
          color: 'negative'
        })
      })
    },
    reFresh () {
      var _this = this
      _this.table_list = []
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
    },
    scaneddata: {
      get () {
        return this.$store.state.scanedsolve.scaneddata
      }
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
    _this.width = Screen.width * 1 + '' + 'px'
    _this.height = Screen.height - 50 + '' + 'px'
    _this.scroll_height = Screen.height - 175 + '' + 'px'
  },
  updated () {
    var _this = this
    if (_this.scaneddata !== '') {
      if (_this.bar_scanned !== _this.scaneddata.request_time) {
        if (_this.scaneddata.mode === 'BINSET') {
          _this.bar_scanned = _this.scaneddata.request_time
          _this.getBinList(_this.scaneddata.code)
        } else if (_this.scaneddata.mode === 'GOODS') {
          if (_this.bin_scan !== '') {
            _this.bar_scanned = _this.scaneddata.request_time
            _this.getGoodsList(_this.scaneddata.code)
          } else {
            _this.$q.notify({
              message: 'No Bin Query Data',
              position: 'top',
              icon: 'close',
              color: 'negative'
            })
          }
        } else {
          _this.$q.notify({
            message: 'No Query Data',
            position: 'top',
            icon: 'close',
            color: 'negative'
          })
        }
      }
    }
  },
  beforeDestroy () {
  },
  destroyed () {
  }
}
</script>
