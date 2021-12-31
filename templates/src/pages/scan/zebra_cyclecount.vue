<template>
  <q-page>
    <q-card v-show="!fab" :style="{ width: width,  height: height }">
      <q-card-section>
        <q-btn-group push>
          <q-btn :label="$t('refresh')" @click="reFresh()" />
          <q-btn color='purple' :label="$t('stock.view_stocklist.cyclecountresult')" @click="ConfirmCount()" />
          <q-btn>{{barscan}}</q-btn>
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
            <th class="text-left">{{ bin_name_label }}</th>
            <th class="text-right">{{ goods_code_label }}</th>
            <th class="text-right">{{ physical_label }}</th>
            <th class="text-right">{{ action_label }}</th>
          </tr>
          </thead>
          <tbody>
          <template>
            <tr v-for='(item, index) in table_list' :key='index'>
              <td class="text-left">{{ item.bin_name }}</td>
              <td class="text-right">{{ item.goods_code }}</td>
              <td class="text-right">{{ item.physical_inventory }}</td>
              <td class="text-right">
                <q-btn round flat push color="purple" icon="repeat" @click="repeatCount(index)" style="width: 50px" />
              </td>
            </tr>
          </template>
          </tbody>
        </q-markup-table>
      </q-scroll-area>
      <q-separator dark />
    </q-card>
  </q-page>
</template>
<router-view />

<script>
import { getauth, putauth } from 'boot/axios_request'
import { LocalStorage, Screen, throttle } from 'quasar'
import {fabChanged} from "src/store/fabchange/mutations";

export default {
  name: 'Pagezebra_cyclecount',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'cyclecount/',
      separator: 'cell',
      loading: false,
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
      bin_scan: '',
      goods_scan: ''
    }
  },
  methods: {
    datachange () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth('scanner/?bar_code=' + _this.barscan, {
        }).then(res => {
          _this.barscan = res.results[0].code
          if (res.results[0].mode === 'BINSET') {
            _this.bin_scan = res.results[0].code
            _this.goods_scan = ''
          } else if (res.results[0].mode === 'GOODS') {
            _this.goods_scan = res.results[0].code
            _this.countAdd(_this.goods_scan)
          }
        }).catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
      }
    },
    countAdd (e) {
      var _this = this
      _this.table_list.filter(function (value, index, array) {
        if (value.bin_name === _this.bin_scan && value.goods_code === e) {
          _this.table_list[index].physical_inventory += 1
        }
      })
    },
    getList () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname, {
        }).then(res => {
          _this.table_list = res.results
        }).catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
      }
    },
    reFresh () {
      var _this = this
      _this.barscan = ''
      _this.bin_scan = ''
      _this.goods_scan = ''
      _this.getList()
    },
    repeatCount (e) {
      var _this = this
      _this.table_list[e].physical_inventory = 0
    },
    ConfirmCount () {
      var _this = this
      if (LocalStorage.has('auth')) {
        putauth(_this.pathname, _this.table_list).then(res => {
          _this.table_list = []
          _this.$q.notify({
            message: 'Success Confirm Cycle Count',
            icon: 'check',
            color: 'green'
          })
        }).catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
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
    } else {
      _this.authin = '0'
    }
    _this.datachange = throttle(_this.datachange, 200)
  },
  mounted () {
    var _this = this
    _this.width = Screen.width * 1 + '' + 'px'
    _this.height = Screen.height - 50 + '' + 'px'
    _this.scroll_height = Screen.height - 175 + '' + 'px'
    _this.barscan = ''
    _this.bin_scan = ''
    _this.goods_scan = ''
    _this.getList()
  },
  computed: {
    fab: {
      get () {
        return this.$store.state.fabchange.fab
      }
    },
    barscan: {
      get () {
        console.log('scaned_cx', this.$store.state.bardata.barscan)
        return this.$store.state.bardata.barscan
      },
      set (val) {
        this.barscan = ''
        console.log('scaned_cy', val)
        this.$store.commit('bardata/barScanned', val)
      }
    }
  },
  updated () {
  },
  beforeDestroy () {
  },
  destroyed () {
  }
}
</script>
