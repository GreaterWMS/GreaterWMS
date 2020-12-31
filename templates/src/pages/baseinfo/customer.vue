<template>
    <div class="q-pa-md" style="width: 100%; margin-top: -20px">
      <transition appear enter-active-class="animated fadeIn">
      <q-table
        class="my-sticky-header-table shadow-24"
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
             <q-btn label="New" icon="add" @click="newForm = true">
               <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                 New one data
               </q-tooltip>
             </q-btn>
             <q-btn label="refresh" icon="refresh" @click="reFresh()">
               <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                 Refresh data
               </q-tooltip>
             </q-btn>
             <q-btn label="Download" icon="cloud_download" @click="downloadData()">
               <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                Download All data
               </q-tooltip>
             </q-btn>
           </q-btn-group>
           <q-space />
           <q-input outlined rounded dense debounce="300" color="primary" v-model="filter" placeholder="Search word">
             <template v-slot:append>
               <q-icon name="search" />
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
                          label="Customer_name"
                          autofocus
                          :rules="[ val => val && val.length > 0 || 'Please Enter the customer_name']"
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
                          label="Customer_city"
                          :rules="[ val => val && val.length > 0 || 'Please Enter the customer_city']"
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
                          label="Customer_address"
                          :rules="[ val => val && val.length > 0 || 'Please Enter the customer_address']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="customer_address" :props="props">
                 {{ props.row.customer_address }}
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="customer_contact" :props="props">
                 {{ props.row.customer_contact }}
               </q-td>
             </template>
             <template v-if="props.row.id === editid">
               <q-td key="customer_contact" :props="props">
                 <q-input dense
                          outlined
                          square
                          v-model.number="editFormData.customer_contact"
                          type="number"
                          label="Customer_contact"
                          :rules="[ val => val && val > 0 || 'Please Enter the customer_contact']"
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
                          label="Customer_manager"
                          :rules="[ val => val && val > 0 || 'Please Enter the customer_manager']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="customer_manager" :props="props">
                 {{ props.row.customer_manager }}
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
                 <q-btn round flat push color="secondary" icon="edit" @click="editData(props.row)">
                   <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                    Edit one line
                  </q-tooltip>
                 </q-btn>
                 <q-btn round flat push color="red" icon="delete" @click="deleteData(props.row.id)">
                   <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                    Delete one line
                  </q-tooltip>
                 </q-btn>
               </q-td>
               </template>
             <template v-else-if="editMode">
               <template v-if="props.row.id === editid">
                 <q-td key="action" :props="props">
                 <q-btn round flat push color="secondary" icon="check" @click="editDataSubmit()">
                   <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                    Confirm edit data
                  </q-tooltip>
                 </q-btn>
                 <q-btn round flat push color="red" icon="close" @click="editDataCancel()">
                   <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                    Cancel edit data
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
          <q-btn v-show="pathname_previous" flat push color="purple" label="Previous" icon="navigate_before" @click="getListPrevious()">
            <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
              Previous
            </q-tooltip>
          </q-btn>
          <q-btn v-show="pathname_next" flat push color="purple" label="Next" icon-right="navigate_next" @click="getListNext()">
            <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
              Next
            </q-tooltip>
          </q-btn>
        </div>
      </template>
      <q-dialog v-model="newForm">
       <q-card class="shadow-24">
         <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
           <div>New one data</div>
           <q-space />
           <q-btn dense flat icon="close" v-close-popup>
             <q-tooltip>Close</q-tooltip>
           </q-btn>
         </q-bar>
         <q-card-section style="max-height: 325px; width: 400px" class="scroll">
           <q-input dense
                    outlined
                    square
                    v-model="newFormData.customer_name"
                    label="Customer_name"
                    autofocus
                    :rules="[ val => val && val.length > 0 || 'Please Enter the customer_name']"
                    @keyup.enter="newDataSubmit()"/>
           <q-input dense
                    outlined
                    square
                    v-model="newFormData.customer_city"
                    label="Customer_city"
                    :rules="[ val => val && val.length > 0 || 'Please Enter the customer_city']"
                    @keyup.enter="newDataSubmit()"/>
           <q-input dense
                    outlined
                    square
                    v-model="newFormData.customer_address"
                    label="Customer_address"
                    :rules="[ val => val && val.length > 0 || 'Please Enter the customer_address']"
                    @keyup.enter="newDataSubmit()"/>
           <q-input dense
                    outlined
                    square
                    v-model.number="newFormData.customer_contact"
                    type="number"
                    label="Customer_contact"
                    :rules="[ val => val && val > 0 || 'Please Enter the customer_contact']"
                    @keyup.enter="newDataSubmit()"/>
           <q-input dense
                    outlined
                    square
                    v-model="newFormData.customer_manager"
                    label="Customer_manager"
                    :rules="[ val => val && val.length > 0 || 'Please Enter the customer_manager']"
                    @keyup.enter="newDataSubmit()"/>
         </q-card-section>
         <div style="float: right; padding: 15px 15px 15px 0">
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="newDataCancel()">Cancel</q-btn>
           <q-btn color="primary" @click="newDataSubmit()">Submit</q-btn>
         </div>
       </q-card>
     </q-dialog>
      <q-dialog v-model="deleteForm">
       <q-card class="shadow-24">
         <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
           <div>Delete one data</div>
           <q-space />
           <q-btn dense flat icon="close" v-close-popup>
             <q-tooltip>Close</q-tooltip>
           </q-btn>
         </q-bar>
         <q-card-section style="max-height: 325px; width: 400px" class="scroll">
           This is an irreversible process.
         </q-card-section>
         <div style="float: right; padding: 15px 15px 15px 0">
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="deleteDataCancel()">Cancel</q-btn>
           <q-btn color="primary" @click="deleteDataSubmit()">Submit</q-btn>
         </div>
       </q-card>
     </q-dialog>
    </div>
</template>
    <router-view />

<script>
import { date } from 'quasar'
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
        { name: 'customer_name', required: true, label: 'Customer_name', align: 'left', field: 'customer_name' },
        { name: 'customer_city', label: 'Customer_city', field: 'customer_city', align: 'center' },
        { name: 'customer_address', label: 'Customer_address', field: 'customer_address', align: 'center' },
        { name: 'customer_contact', label: 'Customer_contact', field: 'customer_contact', align: 'center' },
        { name: 'customer_manager', label: 'Customer_manager', field: 'customer_manager', align: 'center' },
        { name: 'creater', label: 'Creater', field: 'creater', align: 'center' },
        { name: 'create_time', label: 'Create_time', field: 'create_time', align: 'center' },
        { name: 'update_time', label: 'Update_time', field: 'update_time', align: 'center' },
        { name: 'action', label: 'Action', align: 'right' }
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
      if (_this.$q.localStorage.has('auth')) {
        getauth(_this.pathname, {
        }).then(res => {
          _this.table_list = res.results
          if (res.previous) {
            var previous = res.previous.split(':')[0]
            res.previous.replace(previous, window.location.href.split(':')[0])
            _this.pathname_previous = res.previous
          } else {
            _this.pathname_previous = res.previous
          }
          if (res.next) {
            var next = res.next.split(':')[0]
            res.next.replace(next, window.location.href.split(':')[0])
            _this.pathname_next = res.next
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
      if (_this.$q.localStorage.has('auth')) {
        getauth(_this.pathname_previous, {
        }).then(res => {
          _this.table_list = res.results
          if (res.previous) {
            var previous = res.previous.split(':')[0]
            res.previous.replace(previous, window.location.href.split(':')[0])
            _this.pathname_previous = res.previous
          } else {
            _this.pathname_previous = res.previous
          }
          if (res.next) {
            var next = res.next.split(':')[0]
            res.next.replace(next, window.location.href.split(':')[0])
            _this.pathname_next = res.next
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
      if (_this.$q.localStorage.has('auth')) {
        getauth(_this.pathname_next, {
        }).then(res => {
          _this.table_list = res.results
          if (res.previous) {
            var previous = res.previous.split(':')[0]
            res.previous.replace(previous, window.location.href.split(':')[0])
            _this.pathname_previous = res.previous
          } else {
            _this.pathname_previous = res.previous
          }
          if (res.next) {
            var next = res.next.split(':')[0]
            res.next.replace(next, window.location.href.split(':')[0])
            _this.pathname_next = res.next
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
      getfile(_this.pathname + 'file/').then(res => {
        var blob = new Blob([res.data], { type: res.headers['content-type'] })
        var downloadElement = document.createElement('a')
        var href = window.URL.createObjectURL(blob)
        downloadElement.href = href
        var timeStamp = Date.now()
        var formattedString = date.formatDate(timeStamp, 'X')
        downloadElement.download = 'customerlist' + formattedString + '.csv'
        document.body.appendChild(downloadElement)
        downloadElement.click()
        document.body.removeChild(downloadElement)
        window.URL.revokeObjectURL(href)
      })
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
