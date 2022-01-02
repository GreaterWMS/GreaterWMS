<template>
  <q-page>
    <q-input v-model="scaneddata.request_time" style="display:none"></q-input>
    <q-card v-show="!fab" :style="{ width: width,  height: height }">
      <q-card-section>
        <q-btn-group push>
          <q-btn :label="$t('refresh')" @click="reFresh()" />
          <q-btn color='purple' :label="$t('stock.view_stocklist.cyclecountresult')"  />
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
import { getauth } from 'boot/axios_request'
import { LocalStorage, Screen } from 'quasar'

export default {
  name: 'Pagezebra_cyclecount',
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
      bin_scan: '',
      goods_scan: ''
    }
  },
  methods: {
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
    barshow () {
      console.log(10, this.scaneddata)
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
  },
  mounted () {
    var _this = this
    _this.width = Screen.width * 1 + '' + 'px'
    _this.height = Screen.height - 50 + '' + 'px'
    _this.scroll_height = Screen.height - 175 + '' + 'px'
    _this.bin_scan = ''
    _this.goods_scan = ''
    _this.getList()
  },
  computed: {
    fab: {
      get () {
        console.log('7', this.$store.state.fabchange.fab)
        return this.$store.state.fabchange.fab
      }
    },
    scaneddata: {
      get () {
        console.log('8', this.$store.state.scanedsolve.scaneddata)
        return this.$store.state.scanedsolve.scaneddata
      }
    }
  },
  updated () {
    console.log(11, this.scaneddata)
  },
  beforeDestroy () {
  },
  destroyed () {
  }
}
</script>
