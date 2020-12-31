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
             <q-btn label="New" icon="add" @click="newFormOpen()">
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
                Download 1 month data
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
             <q-td key="asn_code" :props="props">
               {{ props.row.asn_code }}
             </q-td>
             <q-td key="asn_status" :props="props">
               {{ props.row.asn_status }}
             </q-td>
             <q-td key="total_weight" :props="props">
               {{ props.row.total_weight }}
             </q-td>
             <q-td key="total_volume" :props="props">
               {{ props.row.total_volume }}
             </q-td>
             <q-td key="supplier" :props="props">
               {{ props.row.supplier }}
             </q-td>
             <q-td key="creater" :props="props">
               {{ props.row.creater }}
             </q-td>
             <q-td key="create_time" :props="props">
               {{ props.row.create_time }}
             </q-td>
             <q-td key="update_time" :props="props">
               {{ props.row.update_time }}
             </q-td>
             <q-td key="action" :props="props">
               <q-btn round flat push color="info" icon="visibility" @click="viewData(props.row)">
                 <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                  Print this ASN
                </q-tooltip>
               </q-btn>
               <q-btn round flat push color="positive" icon="img:statics/inbound/preloadstock.png" @click="preloadData(props.row.id)">
                 <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                  Confirm Delivery
                </q-tooltip>
               </q-btn>
               <q-btn round flat push color="positive" icon="img:statics/inbound/presortstock.png" @click="presortData(props.row.id)">
                 <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                  Finish Loading
                </q-tooltip>
               </q-btn>
               <q-btn round flat push color="purple" icon="img:statics/inbound/sortstock.png" @click="sortedData(props.row)">
                 <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                  Confirm Sorted
                </q-tooltip>
               </q-btn>
               <q-btn round flat push color="purple" icon="edit" @click="editData(props.row)">
                 <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                  Edit one line
                </q-tooltip>
               </q-btn>
               <q-btn round flat push color="dark" icon="delete" @click="deleteData(props.row.id)">
                 <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                  Delete one line
                </q-tooltip>
               </q-btn>
             </q-td>
             <template v-if="props.row.transportation_fee.detail !== []">
               <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                 <q-list>
                   <div v-for="(transportation_fee, index) in props.row.transportation_fee.detail" :key="index">
                    <q-item v-ripple>
                      <q-item-section>
                        <q-item-label>{{ transportation_fee.transportation_supplier }}</q-item-label>
                        <q-item-label>Estimate Cost: {{ transportation_fee.transportation_cost }}</q-item-label>
                      </q-item-section>
                    </q-item>
                  </div>
                </q-list>
               </q-tooltip>
             </template>
           </q-tr>
         </template>
      </q-table>
                 </transition>
      <template>
        <div class="q-pa-md flex flex-center">
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
           <div>{{ newFormData.asn_code }}</div>
           <q-space />
           <q-btn dense flat icon="close" v-close-popup>
             <q-tooltip>Close</q-tooltip>
           </q-btn>
         </q-bar>
         <q-card-section style="max-height: 325px; width: 400px" class="scroll">
            <q-select dense
                      outlined
                      square
                      debounce="500"
                      v-model="newFormData.supplier"
                      :options="supplier_list"
                      label="Supplier List"
                      style="margin-bottom: 5px"
                      :rules="[ val => val && val.length > 0 || 'Please Enter the Supplier']"
                      @keyup.enter="newDataSubmit()"/>
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData1.qty"
                    type="number"
                    label="Goods QTY"
                    style="margin-bottom: 5px"
                    @keyup.enter="newDataSubmit()">
             <template v-slot:before>
               <q-select dense
                         outlined
                         square
                         use-input
                         hide-selected
                         fill-input
                         v-model="goodsData1.code"
                         label="Goods Code"
                         :options="options"
                         @filter="filterFn"
                         autofocus
                         @keyup.enter="newDataSubmit()">
                 <template v-slot:no-option>
                   <q-item>
                     <q-item-section class="text-grey">
                       No results
                     </q-item-section>
                   </q-item>
                 </template>
                 <template v-if="goodsData1.code" v-slot:append>
                   <q-icon name="cancel" @click.stop="goodsData1.code = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData2.qty"
                    type="number"
                    label="Goods QTY"
                    style="margin-bottom: 5px"
                    @keyup.enter="newDataSubmit()">
             <template v-slot:before>
               <q-select dense
                         outlined
                         square
                         use-input
                         hide-selected
                         fill-input
                         v-model="goodsData2.code"
                         label="Goods Code"
                         :options="options"
                         @filter="filterFn"
                         @keyup.enter="newDataSubmit()">
                 <template v-slot:no-option>
                   <q-item>
                     <q-item-section class="text-grey">
                       No results
                     </q-item-section>
                   </q-item>
                 </template>
                 <template v-if="goodsData2.code" v-slot:append>
                   <q-icon name="cancel" @click.stop="goodsData2.code = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
         </q-card-section>
         <div style="float: right; padding: 15px 15px 15px 0">
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="newDataCancel()">Cancel</q-btn>
           <q-btn color="primary" @click="newDataSubmit()">Submit</q-btn>
         </div>
       </q-card>
     </q-dialog>
      <q-dialog v-model="editMode">
       <q-card class="shadow-24">
         <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
           <div>{{ newFormData.asn_code }}</div>
           <q-space />
           <q-btn dense flat icon="close" v-close-popup>
             <q-tooltip>Close</q-tooltip>
           </q-btn>
         </q-bar>
         <q-card-section style="max-height: 325px; width: 400px" class="scroll">
            <q-select dense
                      outlined
                      square
                      debounce="500"
                      v-model="newFormData.supplier"
                      :options="supplier_list"
                      label="Supplier List"
                      style="margin-bottom: 5px"
                      :rules="[ val => val && val.length > 0 || 'Please Enter the Supplier']"
                      @keyup.enter="editDataSubmit()"/>
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData1.qty"
                    type="number"
                    label="Goods QTY"
                    style="margin-bottom: 5px"
                    @keyup.enter="editDataSubmit()">
             <template v-slot:before>
               <q-select dense
                         outlined
                         square
                         use-input
                         hide-selected
                         fill-input
                         v-model="goodsData1.code"
                         label="Goods Code"
                         :options="options"
                         @filter="filterFn"
                         autofocus
                         @keyup.enter="editDataSubmit()">
                 <template v-slot:no-option>
                   <q-item>
                     <q-item-section class="text-grey">
                       No results
                     </q-item-section>
                   </q-item>
                 </template>
                 <template v-if="goodsData1.code" v-slot:append>
                   <q-icon name="cancel" @click.stop="goodsData1.code = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData2.qty"
                    type="number"
                    label="Goods QTY"
                    style="margin-bottom: 5px"
                    @keyup.enter="editDataSubmit()">
             <template v-slot:before>
               <q-select dense
                         outlined
                         square
                         use-input
                         hide-selected
                         fill-input
                         v-model="goodsData2.code"
                         label="Goods Code"
                         :options="options"
                         @filter="filterFn"
                         @keyup.enter="editDataSubmit()">
                 <template v-slot:no-option>
                   <q-item>
                     <q-item-section class="text-grey">
                       No results
                     </q-item-section>
                   </q-item>
                 </template>
                 <template v-if="goodsData2.code" v-slot:append>
                   <q-icon name="cancel" @click.stop="goodsData2.code = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
         </q-card-section>
         <div style="float: right; padding: 15px 15px 15px 0">
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="newDataCancel()">Cancel</q-btn>
           <q-btn color="primary" @click="editDataSubmit()">Submit</q-btn>
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
      <q-dialog v-model="preloadForm">
       <q-card class="shadow-24">
         <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
           <div>Confirm Delivery</div>
           <q-space />
           <q-btn dense flat icon="close" v-close-popup>
             <q-tooltip>Close</q-tooltip>
           </q-btn>
         </q-bar>
         <q-card-section style="max-height: 325px; width: 400px" class="scroll">
           This is an irreversible process.
         </q-card-section>
         <div style="float: right; padding: 15px 15px 15px 0">
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="preloadDataCancel()">Cancel</q-btn>
           <q-btn color="primary" @click="preloadDataSubmit()">Submit</q-btn>
         </div>
       </q-card>
     </q-dialog>
      <q-dialog v-model="presortForm">
       <q-card class="shadow-24">
         <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
           <div>Finish Loading</div>
           <q-space />
           <q-btn dense flat icon="close" v-close-popup>
             <q-tooltip>Close</q-tooltip>
           </q-btn>
         </q-bar>
         <q-card-section style="max-height: 325px; width: 400px" class="scroll">
           This is an irreversible process.
         </q-card-section>
         <div style="float: right; padding: 15px 15px 15px 0">
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="presortDataCancel()">Cancel</q-btn>
           <q-btn color="primary" @click="presortDataSubmit()">Submit</q-btn>
         </div>
       </q-card>
     </q-dialog>
      <q-dialog v-model="viewForm">
       <q-card id="printMe">
         <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
           <div>{{ viewAsn }}</div>
           <q-space />
         </q-bar>
         <q-card-section>
           <div class="text-h6">Sender: {{ supplier_detail.supplier_name }}</div>
           <div class="text-subtitle2">Address: {{ supplier_detail.supplier_city }}{{ supplier_detail.supplier_address }}</div>
           <div class="text-subtitle2">Tel: {{ supplier_detail.supplier_contact }}</div>
           <div class="text-h6">Receiver: {{ warehouse_detail.warehouse_name }}</div>
           <div class="text-subtitle2">Address: {{ warehouse_detail.warehouse_city }}{{ warehouse_detail.warehouse_address }}</div>
           <div class="text-subtitle2">Tel: {{ warehouse_detail.warehouse_contact }}</div>
         </q-card-section>
         <q-markup-table>
          <thead>
            <tr>
              <th class="text-left">Goods Code</th>
              <th class="text-right">Goods QTY</th>
              <th class="text-right">Goods Weight(Unit: KG)</th>
              <th class="text-right">Goods Volume(Unit: Cubic Metres)</th>
              <th class="text-right">Receive QTY</th>
              <th class="text-right">Comments</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(view, index) in viewprint_table" :key="index">
              <td class="text-left">{{ view.goods_code }}</td>
              <td class="text-right">{{ view.goods_qty }}</td>
              <td class="text-right">{{ view.goods_weight }}</td>
              <td class="text-right">{{ view.goods_volume }}</td>
              <td class="text-right"></td>
              <td class="text-right"></td>
            </tr>
          </tbody>
        </q-markup-table>
       </q-card>
        <div style="float: right; padding: 15px 15px 15px 0">
          <q-btn color="primary" icon="print" v-print="printObj">print</q-btn>
        </div>
     </q-dialog>
      <q-dialog v-model="sortedForm">
       <q-card class="shadow-24">
         <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
           <div>{{ newFormData.asn_code }}</div>
           <q-space />
           <q-btn dense flat icon="close" v-close-popup>
             <q-tooltip>Close</q-tooltip>
           </q-btn>
         </q-bar>
         <q-card-section style="max-height: 325px; width: 400px" class="scroll">
            <q-input dense
                     outlined
                     square
                     debounce="500"
                     disable
                     readonly
                     v-model="newFormData.supplier"
                     label="Supplier List"
                     style="margin-bottom: 5px"
            />
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData1.qty"
                    type="number"
                    autofocus
                    label="Goods Actual QTY"
                    style="margin-bottom: 5px"
                    >
             <template v-slot:before>
               <q-input dense
                        outlined
                        square
                        use-input
                        hide-selected
                        fill-input
                        disable
                        readonly
                        v-model="goodsData1.code"
                        label="Goods Code"
               >
                 <template v-slot:no-option>
                   <q-item>
                     <q-item-section class="text-grey">
                       No results
                     </q-item-section>
                   </q-item>
                 </template>
              </q-input>
             </template>
           </q-input>
           <q-input v-show="goodsData2.code !== ''"
                    dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData2.qty"
                    type="number"
                    label="Goods Actual QTY"
                    style="margin-bottom: 5px"
                    >
             <template v-slot:before>
               <q-input dense
                        outlined
                        square
                        use-input
                        hide-selected
                        fill-input
                        disable
                        readonly
                        v-model="goodsData2.code"
                        label="Goods Code"
               >
                 <template v-slot:no-option>
                   <q-item>
                     <q-item-section class="text-grey">
                       No results
                     </q-item-section>
                   </q-item>
                 </template>
              </q-input>
             </template>
           </q-input>
         </q-card-section>
         <div style="float: right; padding: 15px 15px 15px 0">
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="newDataCancel()">Cancel</q-btn>
           <q-btn color="primary" @click="sortedDataSubmit()">Submit</q-btn>
         </div>
       </q-card>
     </q-dialog>
    </div>
</template>
    <router-view />

<script>
// import { openURL } from 'quasar'
import { getauth, postauth, putauth, deleteauth, ViewPrintAuth } from 'boot/axios_request'
import { SessionStorage } from 'quasar'

export default {
  name: 'Pageasnlist',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'asn/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      viewprint_table: [],
      warehouse_detail: {},
      supplier_list: [],
      supplier_detail: {},
      columns: [
        { name: 'asn_code', required: true, label: 'ASN Code', align: 'left', field: 'asn_code' },
        { name: 'asn_status', label: 'ASN Status', field: 'asn_status', align: 'center' },
        { name: 'total_weight', label: 'Total Weight', field: 'total_weight', align: 'center' },
        { name: 'total_volume', label: 'Total Volume', field: 'total_volume', align: 'center' },
        { name: 'supplier', label: 'Supplier', field: 'supplier', align: 'center' },
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
      options: SessionStorage.getItem('goods_code'),
      newAsn: { creater: '' },
      newFormData: {
        asn_code: '',
        supplier: '',
        goods_code: [],
        goods_qty: [],
        creater: ''
      },
      goodsData1: { code: '', qty: '' },
      goodsData2: { code: '', qty: '' },
      editid: 0,
      editFormData: {},
      editMode: false,
      sortedForm: false,
      sortedid: 0,
      deleteForm: false,
      deleteid: 0,
      preloadForm: false,
      preloadid: 0,
      presortForm: false,
      presortid: 0,
      viewForm: false,
      viewAsn: '',
      viewid: 0,
      printObj: {
        id: 'printMe',
        popTitle: 'Advance Shipment Notice'
      }
    }
  },
  methods: {
    getList () {
      var _this = this
      if (_this.$q.localStorage.has('auth')) {
        getauth(_this.pathname + 'list/', {
        }).then(res => {
          _this.table_list = res.results
          _this.supplier_list = res.supplier_list
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
          _this.supplier_list = res.supplier_list
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
          _this.supplier_list = res.supplier_list
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
    newFormOpen () {
      var _this = this
      _this.newForm = true
      _this.newAsn.creater = _this.login_name
      postauth(_this.pathname + 'list/', _this.newAsn).then(res => {
        _this.newFormData.asn_code = res.asn_code
      }).catch(err => {
        _this.$q.notify({
          message: err.detail,
          icon: 'close',
          color: 'negative'
        })
      })
    },
    newDataSubmit () {
      var _this = this
      _this.newFormData.creater = _this.login_name
      if (_this.goodsData1.code !== '' && _this.goodsData1.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData1.code)
        _this.newFormData.goods_qty.push(_this.goodsData1.qty)
      }
      if (_this.goodsData2.code !== '' && _this.goodsData2.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData2.code)
        _this.newFormData.goods_qty.push(_this.goodsData2.qty)
      }
      postauth(_this.pathname + 'detail/', _this.newFormData).then(res => {
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
        asn_code: '',
        supplier: '',
        goods_code: [],
        goods_qty: [],
        creater: ''
      }
      _this.goodsDataClear()
    },
    goodsDataClear () {
      var _this = this
      _this.goodsData1 = { code: '', qty: '' }
      _this.goodsData2 = { code: '', qty: '' }
    },
    editData (e) {
      var _this = this
      _this.goodsDataClear()
      if (e.asn_status > 1) {
        _this.$q.notify({
          message: e.asn_code + ' has been deliveried , can not be edit',
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.newFormData.asn_code = e.asn_code
        _this.newFormData.supplier = e.supplier
        getauth(_this.pathname + 'detail/?asn_code=' + e.asn_code).then(res => {
          _this.editMode = true
          _this.editid = e.id
          res.results.forEach((detail, index) => {
            if (index === 0) {
              _this.goodsData1 = { code: detail.goods_code, qty: detail.goods_qty }
            } else if (index === 1) {
              _this.goodsData2 = { code: detail.goods_code, qty: detail.goods_qty }
            }
          })
        })
      }
    },
    editDataSubmit () {
      var _this = this
      _this.newFormData.creater = _this.login_name
      if (_this.goodsData1.code !== '' && _this.goodsData1.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData1.code)
        _this.newFormData.goods_qty.push(_this.goodsData1.qty)
      }
      if (_this.goodsData2.code !== '' && _this.goodsData2.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData2.code)
        _this.newFormData.goods_qty.push(_this.goodsData2.qty)
      }
      putauth(_this.pathname + 'detail/', _this.newFormData).then(res => {
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
      _this.newFormData = {
        asn_code: '',
        supplier: '',
        goods_code: [],
        goods_qty: [],
        creater: ''
      }
      _this.goodsDataClear()
    },
    deleteData (e) {
      var _this = this
      _this.deleteForm = true
      _this.deleteid = e
    },
    deleteDataSubmit () {
      var _this = this
      deleteauth(_this.pathname + 'list/' + _this.deleteid + '/').then(res => {
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
    preloadData (e) {
      var _this = this
      _this.preloadForm = true
      _this.preloadid = e
    },
    preloadDataSubmit () {
      var _this = this
      postauth(_this.pathname + 'preload/' + _this.preloadid + '/', {}).then(res => {
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
          _this.preloadDataCancel()
          _this.getList()
          _this.$q.notify({
            message: 'Success Confirm ASN Delivery',
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
    preloadDataCancel () {
      var _this = this
      _this.preloadForm = false
      _this.preloadid = 0
    },
    presortData (e) {
      var _this = this
      _this.presortForm = true
      _this.presortid = e
    },
    presortDataSubmit () {
      var _this = this
      postauth(_this.pathname + 'presort/' + _this.presortid + '/', {}).then(res => {
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
          _this.presortDataCancel()
          _this.getList()
          _this.$q.notify({
            message: 'Success Confirm ASN Delivery',
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
    presortDataCancel () {
      var _this = this
      _this.presortForm = false
      _this.presortid = 0
    },
    filterFn (val, update, abort) {
      var _this = this
      if (val.length < 1) {
        abort()
        return
      }
      update(() => {
        const needle = val.toLowerCase()
        getauth('goods/?goods_code__icontains=' + needle).then(res => {
          var goodscodelist = []
          res.results.forEach(detail => {
            goodscodelist.push(detail.goods_code)
          })
          SessionStorage.set('goods_code', goodscodelist)
          _this.options = SessionStorage.getItem('goods_code')
        }).catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
      })
    },
    sortedData (e) {
      var _this = this
      _this.goodsDataClear()
      if (e.asn_status !== 3) {
        _this.$q.notify({
          message: e.asn_code + ' Not in pre_sorted status , can not be edit',
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.newFormData.asn_code = e.asn_code
        _this.newFormData.supplier = e.supplier
        getauth(_this.pathname + 'detail/?asn_code=' + e.asn_code).then(res => {
          _this.sortedForm = true
          _this.sortedid = e.id
          res.results.forEach((detail, index) => {
            if (index === 0) {
              _this.goodsData1 = { code: detail.goods_code, qty: detail.goods_actual_qty }
            } else if (index === 1) {
              _this.goodsData2 = { code: detail.goods_code, qty: detail.goods_actual_qty }
            }
          })
        })
      }
    },
    sortedDataSubmit () {
      var _this = this
      _this.newFormData.creater = _this.login_name
      if (_this.goodsData1.code !== '' && _this.goodsData1.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData1.code)
        _this.newFormData.goods_qty.push(_this.goodsData1.qty)
      }
      if (_this.goodsData2.code !== '' && _this.goodsData2.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData2.code)
        _this.newFormData.goods_qty.push(_this.goodsData2.qty)
      }
      postauth(_this.pathname + 'sorted/' + _this.sortedid + '/', _this.newFormData).then(res => {
        console.log(res)
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
          _this.sortedDataCancel()
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
    sortedDataCancel () {
      var _this = this
      _this.sortedForm = false
      _this.sortedid = 0
      _this.newFormData = {
        asn_code: '',
        supplier: '',
        goods_code: [],
        goods_qty: [],
        creater: ''
      }
      _this.goodsDataClear()
    },
    viewData (e) {
      var _this = this
      ViewPrintAuth(_this.pathname + 'viewprint/' + e.id + '/').then(res => {
        _this.viewprint_table = res.asn_detail
        _this.warehouse_detail = res.warehouse_detail
        _this.supplier_detail = res.supplier_detail
        _this.viewAsn = e.asn_code
        _this.viewForm = true
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
    if (SessionStorage.has('goods_code')) {
    } else {
      SessionStorage.set('goods_code', [])
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
