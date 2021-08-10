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
             <q-btn :label="$t('new')" icon="add" @click="newForm = true">
               <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                 {{ $t('newtip') }}
               </q-tooltip>
             </q-btn>
             <q-btn :label="$t('refresh')" icon="refresh" @click="reFresh()">
               <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
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
             <template v-if="props.row.id === editid">
               <q-td key="goods_brand" :props="props">
                 <q-input dense
                          outlined
                          square
                          v-model="editFormData.goods_brand"
                          :label="$t('goods.view_goodslist.goods_brand')"
                          autofocus
                          :rules="[ val => val && val.length > 0 || 'Please Enter the Goods Brand']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="goods_brand" :props="props">
                 {{ props.row.goods_brand }}
               </q-td>
             </template>
             <q-td key="creater" :props="props">
               {{ props.row.creater }}
             </q-td>
             <q-td key="create_time" :props="props">
               {{ props.row.create_time }}
             </q-td>
             <q-td key="update_time" :props="props">
               {{ props.row.update_time }}
             </q-td>
             <template v-if="!editMode">
               <q-td key="action" :props="props" style="width: 100px">
                 <q-btn round flat push color="purple" icon="edit" @click="editData(props.row)">
                   <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                    {{ $t('edit') }}
                  </q-tooltip>
                 </q-btn>
                 <q-btn round flat push color="dark" icon="delete" @click="deleteData(props.row.id)">
                   <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                    {{ $t('delete') }}
                  </q-tooltip>
                 </q-btn>
               </q-td>
               </template>
             <template v-else-if="editMode">
               <template v-if="props.row.id === editid">
                 <q-td key="action" :props="props" style="width: 100px">
                 <q-btn round flat push color="secondary" icon="check" @click="editDataSubmit()">
                   <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                    {{ $t('confirmedit') }}
                  </q-tooltip>
                 </q-btn>
                 <q-btn round flat push color="red" icon="close" @click="editDataCancel()">
                   <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                    {{ $t('canceledit') }}
                  </q-tooltip>
                 </q-btn>
               </q-td>
               </template>
                <template v-else-if="props.row.id !== editid"></template>
             </template>
           </q-tr>
         </template>
        </q-table>
      </transition>
      <template>
        <div class="q-pa-md flex flex-center">
          <q-btn v-show="pathname_previous" flat push color="purple" :label="$t('previous')" icon="navigate_before" @click="getListPrevious()">
            <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
              {{ $t('previous') }}
            </q-tooltip>
          </q-btn>
          <q-btn v-show="pathname_next" flat push color="purple" :label="$t('next')" icon-right="navigate_next" @click="getListNext()">
            <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
              {{ $t('next') }}
            </q-tooltip>
          </q-btn>
          <q-btn v-show="!pathname_previous && !pathname_next" flat push color="dark" :label="$t('no_data')"></q-btn>
        </div>
      </template>
      <q-dialog v-model="newForm">
       <q-card class="shadow-24">
         <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
           <div>{{ $t('newtip') }}</div>
           <q-space />
           <q-btn dense flat icon="close" v-close-popup>
             <q-tooltip>{{ $t('index.close') }}</q-tooltip>
           </q-btn>
         </q-bar>
         <q-card-section style="max-height: 325px; width: 400px" class="scroll">
           <q-input dense
                    outlined
                    square
                    v-model="newFormData.goods_brand"
                    :label="$t('goods.view_goodslist.goods_brand')"
                    autofocus
                    :rules="[ val => val && val.length > 0 || 'Please Enter the Goods Brand']"
                    @keyup.enter="newDataSubmit()"/>
         </q-card-section>
         <div style="float: right; padding: 15px 15px 15px 0">
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="newDataCancel()">{{ $t('cancel') }}</q-btn>
           <q-btn color="primary" @click="newDataSubmit()">{{ $t('submit') }}</q-btn>
         </div>
       </q-card>
     </q-dialog>
      <q-dialog v-model="deleteForm">
       <q-card class="shadow-24">
         <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
           <div>{{ $t('delete') }}</div>
           <q-space />
           <q-btn dense flat icon="close" v-close-popup>
             <q-tooltip>{{ $t('index.close') }}</q-tooltip>
           </q-btn>
         </q-bar>
         <q-card-section style="max-height: 325px; width: 400px" class="scroll">
           {{ $t('deletetip') }}
         </q-card-section>
         <div style="float: right; padding: 15px 15px 15px 0">
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="deleteDataCancel()">{{ $t('cancel') }}</q-btn>
           <q-btn color="primary" @click="deleteDataSubmit()">{{ $t('submit') }}</q-btn>
         </div>
       </q-card>
     </q-dialog>
    </div>
</template>
    <router-view />

<script>
import { getauth, postauth, putauth, deleteauth } from 'boot/axios_request'

export default {
  name: 'Pagegoodsbrand',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'goodsbrand/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      columns: [
        { name: 'goods_brand', required: true, label: this.$t('goods.view_brand.goods_brand'), align: 'left', field: 'goods_brand' },
        { name: 'creater', label: this.$t('creater'), field: 'creater', align: 'center' },
        { name: 'create_time', label: this.$t('createtime'), field: 'create_time', align: 'center' },
        { name: 'update_time', label: this.$t('updatetime'), field: 'update_time', align: 'center' },
        { name: 'action', label: this.$t('action'), align: 'right' }
      ],
      filter: '',
      pagination: {
        page: 1,
        rowsPerPage: '30'
      },
      newForm: false,
      newFormData: {
        goods_brand: '',
        creater: ''
      },
      editid: 0,
      editFormData: {},
      editMode: false,
      deleteForm: false,
      deleteid: 0
    }
  },
  methods: {
    getList () {
      var _this = this
      if (_this.$q.localStorage.has('auth')) {
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
      if (_this.$q.localStorage.has('auth')) {
        getauth(_this.pathname + '?goods_brand__icontains=' + _this.filter, {
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
      if (_this.$q.localStorage.has('auth')) {
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
      if (_this.$q.localStorage.has('auth')) {
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
    },
    newDataSubmit () {
      var _this = this
      _this.newFormData.creater = _this.login_name
      postauth(_this.pathname, _this.newFormData).then(res => {
        _this.getList()
        _this.newDataCancel()
        _this.$q.notify({
          message: 'Success Create',
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
    },
    newDataCancel () {
      var _this = this
      _this.newForm = false
      _this.newFormData = {
        goods_brand: '',
        creater: ''
      }
    },
    editData (e) {
      var _this = this
      _this.editMode = true
      _this.editid = e.id
      _this.editFormData = {
        goods_brand: e.goods_brand,
        creater: _this.login_name
      }
    },
    editDataSubmit () {
      var _this = this
      putauth(_this.pathname + _this.editid + '/', _this.editFormData).then(res => {
        _this.editDataCancel()
        _this.getList()
        _this.$q.notify({
          message: 'Success Edit Data',
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
    },
    editDataCancel () {
      var _this = this
      _this.editMode = false
      _this.editid = 0
      _this.editFormData = {
        goods_brand: '',
        creater: ''
      }
    },
    deleteData (e) {
      var _this = this
      _this.deleteForm = true
      _this.deleteid = e
    },
    deleteDataSubmit () {
      var _this = this
      deleteauth(_this.pathname + _this.deleteid + '/').then(res => {
        _this.deleteDataCancel()
        _this.getList()
        _this.$q.notify({
          message: 'Success Edit Data',
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
    },
    deleteDataCancel () {
      var _this = this
      _this.deleteForm = false
      _this.deleteid = 0
    }
  },
  created () {
    var _this = this
    if (_this.$q.localStorage.has('openid')) {
      _this.openid = _this.$q.localStorage.getItem('openid')
    } else {
      _this.openid = ''
      _this.$q.localStorage.set('openid', '')
    }
    if (_this.$q.localStorage.has('login_name')) {
      _this.login_name = _this.$q.localStorage.getItem('login_name')
    } else {
      _this.login_name = ''
      _this.$q.localStorage.set('login_name', '')
    }
    if (_this.$q.localStorage.has('auth')) {
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
  },
  destroyed () {
  }
}
</script>
