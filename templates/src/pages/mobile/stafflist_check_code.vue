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
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                {{ $t('refreshtip') }}
              </q-tooltip>
            </q-btn>
          </q-btn-group>
          <q-space />
          <q-input outlined rounded dense debounce="300" color="primary" v-model="filter" :placeholder="$t('search')" @blur="getSearchList()" @keyup.enter="getSearchList()">
            <template v-slot:append>
              <q-icon name="search" @click="getSearchList()"/>
            </template>
          </q-input>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td key="staff_name" :props="props">
              {{ props.row.staff_name }}
            </q-td>
            <q-td key="staff_type" :props="props">
              {{ props.row.staff_type }}
            </q-td>
            <q-td key="check_code" :props="props">
              {{ props.row.check_code }}
            </q-td>
            <q-td key="create_time" :props="props">
              {{ props.row.create_time }}
            </q-td>
            <q-td key="update_time" :props="props">
              {{ props.row.update_time }}
            </q-td>
          </q-tr>
        </template>
      </q-table>
    </transition>
    <template>
      <div class="q-pa-lg flex flex-center">
        <q-btn v-show="pathname_previous" flat push color="purple" :label="$t('previous')" icon="navigate_before" @click="getListPrevious()">
          <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
            {{ $t('previous') }}
          </q-tooltip>
        </q-btn>
        <q-btn v-show="pathname_next" flat push color="purple" :label="$t('next')" icon-right="navigate_next" @click="getListNext()">
          <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
            {{ $t('next') }}
          </q-tooltip>
        </q-btn>
        <q-btn v-show="!pathname_previous && !pathname_next" flat push color="dark" :label="$t('no_data')"></q-btn>
      </div>
    </template>
  </div>
</template>
<router-view />

<script>
import { getauth } from 'boot/axios_request'
import { LocalStorage } from 'quasar'

export default {
  name: 'Pagestafflistcheckcode',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'staff/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      staff_type_list: ['Manager', 'Inbound', 'Outbound', 'Supervisor', 'StockControl', 'Customer', 'Supplier'],
      columns: [
        { name: 'staff_name', required: true, label: this.$t('staff.view_staff.staff_name'), align: 'left', field: 'staff_name' },
        { name: 'staff_type', label: this.$t('staff.view_staff.staff_type'), field: 'staff_type', align: 'center' },
        { name: 'check_code', label: this.$t('staff.check_code'), field: 'check_code', align: 'center' },
        { name: 'create_time', label: this.$t('createtime'), field: 'create_time', align: 'center' },
        { name: 'update_time', label: this.$t('updatetime'), field: 'update_time', align: 'center' }
      ],
      filter: '',
      pagination: {
        page: 1,
        rowsPerPage: '30'
      }
    }
  },
  methods: {
    getList () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname, {
        }).then(res => {
          _this.table_list = res.results
          _this.pathname_previous = res.previous
          _this.pathname_next = res.next
        }).catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
      } else {
      }
    },
    getSearchList () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname + '?staff_name__icontains=' + _this.filter, {
        }).then(res => {
          _this.table_list = res.results
          _this.pathname_previous = res.previous
          _this.pathname_next = res.next
        }).catch(err => {
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
        getauth(_this.pathname_previous, {
        }).then(res => {
          _this.table_list = res.results
          _this.pathname_previous = res.previous
          _this.pathname_next = res.next
        }).catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
      } else {
      }
    },
    getListNext () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname_next, {
        }).then(res => {
          _this.table_list = res.results
          _this.pathname_previous = res.previous
          _this.pathname_next = res.next
        }).catch(err => {
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
  updated () {
    if (document.getElementById('chat_scroll')) {
      document.getElementById('chat_scroll').scrollTop = document.getElementById('chat_scroll').scrollHeight
    } else {
    }
  },
  destroyed () {
  }
}
</script>
