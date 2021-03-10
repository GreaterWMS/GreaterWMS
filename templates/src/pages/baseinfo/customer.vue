<template>
    <div class="q-pa-md" style="width: 100%; margin-top: -20px">
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
             <q-btn :label="$t('download')" icon="cloud_download" @click="downloadData()">
               <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                {{ $t('downloadtip') }}
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
               <q-td key="customer_name" :props="props">
                 <q-input dense
                          outlined
                          square
                          v-model="editFormData.customer_name"
                          label="Customer Name"
                          autofocus
                          :rules="[ val => val && val.length > 0 || 'Please Enter the Customer Name']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="customer_name" :props="props">
                 {{ props.row.customer_name }}
               </q-td>
             </template>
             <template v-if="props.row.id === editid">
               <q-td key="customer_city" :props="props">
                 <q-input dense
                          outlined
                          square
                          v-model="editFormData.customer_city"
                          label="Customer City"
                          :rules="[ val => val && val.length > 0 || 'Please Enter the Customer City']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="customer_city" :props="props">
                 {{ props.row.customer_city }}
               </q-td>
             </template>
             <template v-if="props.row.id === editid">
               <q-td key="customer_address" :props="props">
                 <q-input dense
                          outlined
                          square
                          v-model="editFormData.customer_address"
                          label="Customer Address"
                          :rules="[ val => val && val.length > 0 || 'Please Enter the Customer Address']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="customer_address" :props="props">
                 {{ props.row.customer_address }}
               </q-td>
             </template>
             <template v-if="props.row.id === editid">
               <q-td key="customer_contact" :props="props">
                 <q-input dense
                          outlined
                          square
                          v-model.number="editFormData.customer_contact"
                          type="number"
                          label="Customer Contact"
                          :rules="[ val => val && val > 0 || 'Please Enter the Customer Contact']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="customer_contact" :props="props">
                 {{ props.row.customer_contact }}
               </q-td>
             </template>
             <template v-if="props.row.id === editid">
               <q-td key="customer_manager" :props="props">
                 <q-input dense
                          outlined
                          square
                          v-model="editFormData.customer_manager"
                          label="Customer Manager"
                          :rules="[ val => val && val > 0 || 'Please Enter the Customer Manager']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="customer_manager" :props="props">
                 {{ props.row.customer_manager }}
               </q-td>
             </template>
             <template v-if="props.row.id === editid">
               <q-td key="customer_level" :props="props">
                 <q-input dense
                          outlined
                          square
                          v-model.number="editFormData.customer_level"
                          type="number"
                          label="Customer Level"
                          :rules="[ val => val && val > 0 || 'Please Enter the Customer Level']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="customer_level" :props="props">
                 {{ props.row.customer_level }}
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
               <q-td key="action" :props="props">
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
                 <q-td key="action" :props="props">
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
        <div class="q-pa-lg flex flex-center">
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
                    v-model="newFormData.customer_name"
                    label="Customer Name"
                    autofocus
                    :rules="[ val => val && val.length > 0 || 'Please Enter the Customer Name']"
                    @keyup.enter="newDataSubmit()"/>
           <q-input dense
                    outlined
                    square
                    v-model="newFormData.customer_city"
                    label="Customer City"
                    :rules="[ val => val && val.length > 0 || 'Please Enter the Customer City']"
                    @keyup.enter="newDataSubmit()"/>
           <q-input dense
                    outlined
                    square
                    v-model="newFormData.customer_address"
                    label="Customer Address"
                    :rules="[ val => val && val.length > 0 || 'Please Enter the Customer Address']"
                    @keyup.enter="newDataSubmit()"/>
           <q-input dense
                    outlined
                    square
                    v-model.number="newFormData.customer_contact"
                    type="number"
                    label="Customer Contact"
                    :rules="[ val => val && val > 0 || 'Please Enter the Customer Contact']"
                    @keyup.enter="newDataSubmit()"/>
           <q-input dense
                    outlined
                    square
                    v-model="newFormData.customer_manager"
                    label="Customer Manager"
                    :rules="[ val => val && val.length > 0 || 'Please Enter the Customer Manager']"
                    @keyup.enter="newDataSubmit()"/>
           <q-input dense
                    outlined
                    square
                    v-model.number="newFormData.customer_level"
                    type="number"
                    label="Customer Level"
                    :rules="[ val => val && val > 0 || 'Please Enter the Customer Level']"
                    @keyup.enter="newDataSubmit()"/>
         </q-card-section>
         <div style="float: right; padding: 15px 15px 15px 0">
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="newDataCancel()">{{ $t('cancel') }}</q-btn>
           <q-btn color="primary" @click="newDataSubmit()">{{$t('submit')}}</q-btn>
         </div>
       </q-card>
     </q-dialog>
      <q-dialog v-model="deleteForm">
       <q-card class="shadow-24">
         <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
           <div>{{ $t('delete') }}</div>
           <q-space />
           <q-btn dense flat icon="close" v-close-popup>
             <q-tooltip>Close</q-tooltip>
           </q-btn>
         </q-bar>
         <q-card-section style="max-height: 325px; width: 400px" class="scroll">
           {{ $t('deletetip') }}
         </q-card-section>
         <div style="float: right; padding: 15px 15px 15px 0">
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="deleteDataCancel()">{{ $t('cancel') }}</q-btn>
           <q-btn color="primary" @click="deleteDataSubmit()">{{$t('submit')}}</q-btn>
         </div>
       </q-card>
     </q-dialog>
    </div>
</template>
    <router-view />

<script>
import { date, exportFile, LocalStorage } from 'quasar'
import { getauth, postauth, putauth, deleteauth, getfile } from 'boot/axios_request'

export default {
  name: 'Pagecustomer',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'customer/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      columns: [
        { name: 'customer_name', required: true, label: this.$t('baseinfo.view_customer.customer_name'), align: 'left', field: 'customer_name' },
        { name: 'customer_city', label: this.$t('baseinfo.view_customer.customer_city'), field: 'customer_city', align: 'center' },
        { name: 'customer_address', label: this.$t('baseinfo.view_customer.customer_address'), field: 'customer_address', align: 'center' },
        { name: 'customer_contact', label: this.$t('baseinfo.view_customer.customer_contact'), field: 'customer_contact', align: 'center' },
        { name: 'customer_manager', label: this.$t('baseinfo.view_customer.customer_manager'), align: 'center' },
        { name: 'customer_level', label: this.$t('baseinfo.view_customer.customer_level'), field: 'customer_level', align: 'center' },
        { name: 'creater', label: 'Creater', field: this.$t('creater'), align: 'center' },
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
        customer_name: '',
        customer_city: '',
        customer_address: '',
        customer_contact: '',
        customer_manager: '',
        customer_level: '',
        creater: ''
      },
      editid: 0,
      editFormData: {},
      editMode: false,
      deleteForm: false,
      deleteid: 0,
      sender: '',
      receiver: '',
      chat: false,
      chat_list: '',
      chat_text: '',
      chat_next: null
    }
  },
  methods: {
    getList () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname, {
        }).then(res => {
          _this.table_list = res.results
          if (res.previous) {
            var previous = res.previous.split(':')[0]
            var previouspage = res.previous.replace(previous, window.location.href.split(':')[0])
            _this.pathname_previous = previouspage
          } else {
            _this.pathname_previous = res.previous
          }
          if (res.next) {
            var next = res.next.split(':')[0]
            var nextpage = res.next.replace(next, window.location.href.split(':')[0])
            _this.pathname_next = nextpage
          } else {
            _this.pathname_next = res.next
          }
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
        getauth(_this.pathname + '?customer_name__icontains=' + _this.filter, {
        }).then(res => {
          _this.table_list = res.results
          if (res.previous) {
            var previous = res.previous.split(':')[0]
            var previouspage = res.previous.replace(previous, window.location.href.split(':')[0])
            _this.pathname_previous = previouspage
          } else {
            _this.pathname_previous = res.previous
          }
          if (res.next) {
            var next = res.next.split(':')[0]
            var nextpage = res.next.replace(next, window.location.href.split(':')[0])
            _this.pathname_next = nextpage
          } else {
            _this.pathname_next = res.next
          }
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
          if (res.previous) {
            var previous = res.previous.split(':')[0]
            var previouspage = res.previous.replace(previous, window.location.href.split(':')[0])
            _this.pathname_previous = previouspage
          } else {
            _this.pathname_previous = res.previous
          }
          if (res.next) {
            var next = res.next.split(':')[0]
            var nextpage = res.next.replace(next, window.location.href.split(':')[0])
            _this.pathname_next = nextpage
          } else {
            _this.pathname_next = res.next
          }
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
          if (res.previous) {
            var previous = res.previous.split(':')[0]
            var previouspage = res.previous.replace(previous, window.location.href.split(':')[0])
            _this.pathname_previous = previouspage
          } else {
            _this.pathname_previous = res.previous
          }
          if (res.next) {
            var next = res.next.split(':')[0]
            var nextpage = res.next.replace(next, window.location.href.split(':')[0])
            _this.pathname_next = nextpage
          } else {
            _this.pathname_next = res.next
          }
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
        if (res.status_code === 400) {
          _this.$q.notify({
            message: 'Please Enter the words',
            icon: 'close',
            color: 'negative'
          })
        } else if (res.status_code === 500) {
          _this.$q.notify({
            message: res.detail,
            icon: 'close',
            color: 'negative'
          })
        } else {
          _this.getList()
          _this.newDataCancel()
          _this.$q.notify({
            message: 'Success Create',
            icon: 'check',
            color: 'green'
          })
        }
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
        customer_name: '',
        customer_city: '',
        customer_address: '',
        customer_contact: '',
        customer_manager: '',
        customer_level: '',
        creater: ''
      }
    },
    editData (e) {
      var _this = this
      _this.editMode = true
      _this.editid = e.id
      _this.editFormData = {
        customer_name: e.customer_name,
        customer_city: e.customer_city,
        customer_address: e.customer_address,
        customer_contact: e.customer_contact,
        customer_manager: e.customer_manager,
        customer_level: e.customer_level,
        creater: _this.login_name
      }
    },
    editDataSubmit () {
      var _this = this
      putauth(_this.pathname + _this.editid + '/', _this.editFormData).then(res => {
        if (res.status_code === 400) {
          _this.$q.notify({
            message: 'Please Enter the words',
            icon: 'close',
            color: 'negative'
          })
        } else if (res.status_code === 500) {
          _this.$q.notify({
            message: res.detail,
            icon: 'close',
            color: 'negative'
          })
        } else {
          _this.editDataCancel()
          _this.getList()
          _this.$q.notify({
            message: 'Success Edit Data',
            icon: 'check',
            color: 'green'
          })
        }
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
        customer_name: '',
        customer_city: '',
        customer_address: '',
        customer_contact: '',
        customer_manager: '',
        customer_level: '',
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
        if (res.status_code === 400) {
          _this.$q.notify({
            message: 'Please Enter the words',
            icon: 'close',
            color: 'negative'
          })
        } else if (res.status_code === 500) {
          _this.$q.notify({
            message: res.detail,
            icon: 'close',
            color: 'negative'
          })
        } else {
          _this.deleteDataCancel()
          _this.getList()
          _this.$q.notify({
            message: 'Success Edit Data',
            icon: 'check',
            color: 'green'
          })
        }
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
    },
    downloadData () {
      var _this = this
      getfile(_this.pathname + 'file/?lang=' + LocalStorage.getItem('lang')).then(res => {
        var timeStamp = Date.now()
        var formattedString = date.formatDate(timeStamp, 'YYYYMMDDHHmmssSSS')
        const status = exportFile(
          _this.pathname + formattedString + '.csv',
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
    if (this.$q.platform.is.electron) {
      this.height = String(this.$q.screen.height - 290) + 'px'
    } else {
      this.height = this.$q.screen.height - 290 + '' + 'px'
    }
  },
  updated () {
  },
  destroyed () {
  }
}
</script>
