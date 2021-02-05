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
             <q-btn :label="$t('new')" icon="add" @click="newFormOpen()">
               <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                 {{ $t('newtip') }}
               </q-tooltip>
             </q-btn>
             <q-btn :label="$t('refresh')" icon="refresh" @click="reFresh()">
               <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                 {{ $t('refreshtip') }}
               </q-tooltip>
             </q-btn>
             <q-btn :label="$t('release')" icon="img:statics/outbound/orderrelease.png" @click="orderreleaseAllData()">
               <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                 {{ $t('releaseallorder') }}
               </q-tooltip>
             </q-btn>
             <q-btn :label="$t('downloaddnlist')" icon="cloud_download" @click="downloadlistData()">
               <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                {{ $t('downloaddnlisttip') }}
               </q-tooltip>
             </q-btn>
             <q-btn :label="$t('downloaddndetail')" icon="cloud_download" @click="downloaddetailData()">
               <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                 {{ $t('downloaddndetailtip') }}
               </q-tooltip>
             </q-btn>
           </q-btn-group>
           <q-space />
           <q-input v-show="$q.platform.is.desktop" outlined rounded dense debounce="300" color="primary" v-model="filter" :placeholder="$t('search')">
             <template v-slot:append>
               <q-icon name="search" />
             </template>
           </q-input>
         </template>
         <template v-slot:body="props">
           <q-tr :props="props">
             <q-td key="dn_code" :props="props">
               {{ props.row.dn_code }}
             </q-td>
             <q-td key="dn_status" :props="props">
               {{ props.row.dn_status }}
             </q-td>
             <q-td key="total_weight" :props="props">
               {{ props.row.total_weight }}
             </q-td>
             <q-td key="total_volume" :props="props">
               {{ props.row.total_volume }}
             </q-td>
             <q-td key="customer" :props="props">
               {{ props.row.customer }}
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
                   {{ $t('printthisdn') }}
                </q-tooltip>
               </q-btn>
               <q-btn round flat push color="positive" icon="img:statics/outbound/order.png" @click="neworderData(props.row.id)">
                 <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                   {{ $t('confirmorder') }}
                </q-tooltip>
               </q-btn>
               <q-btn round flat push color="positive" icon="img:statics/outbound/orderrelease.png" @click="orderreleaseData(props.row.id)">
                 <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                   {{ $t('releaseorder') }}
                </q-tooltip>
               </q-btn>
               <q-btn round flat push color="purple" icon="img:statics/outbound/picked.png" @click="sortedData(props.row)">
                 <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                   {{ $t('confirmpicked') }}
                </q-tooltip>
               </q-btn>
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
             <template v-if="props.row.transportation_fee.detail !== []">
               <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                 <q-list>
                   <div v-for="(transportation_fee, index) in props.row.transportation_fee.detail" :key="index">
                    <q-item v-ripple>
                      <q-item-section>
                        <q-item-label>{{ transportation_fee.transportation_supplier }}</q-item-label>
                        <q-item-label>{{ $t('estimate') }}: {{ transportation_fee.transportation_cost }}</q-item-label>
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
           <div>{{ newFormData.dn_code }}</div>
           <q-space />
           <q-btn dense flat icon="close" v-close-popup>
             <q-tooltip>{{ $t('index.close') }}</q-tooltip>
           </q-btn>
         </q-bar>
         <q-card-section style="max-height: 325px; width: 400px" class="scroll">
            <q-select dense
                      outlined
                      square
                      debounce="500"
                      v-model="newFormData.customer"
                      :options="customer_list"
                      label="Customer List"
                      style="margin-bottom: 5px"
                      :rules="[ val => val && val.length > 0 || 'Please Enter the Customer']"
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
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="newDataCancel()">{{ $t('cancel') }}</q-btn>
           <q-btn color="primary" @click="newDataSubmit()">Submit</q-btn>
         </div>
       </q-card>
     </q-dialog>
      <q-dialog v-model="editMode">
       <q-card class="shadow-24">
         <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
           <div>{{ newFormData.dn_code }}</div>
           <q-space />
           <q-btn dense flat icon="close" v-close-popup>
             <q-tooltip>{{ $t('index.close') }}</q-tooltip>
           </q-btn>
         </q-bar>
         <q-card-section style="max-height: 325px; width: 400px" class="scroll">
            <q-select dense
                      outlined
                      square
                      debounce="500"
                      v-model="newFormData.customer"
                      :options="customer_list"
                      label="customer List"
                      style="margin-bottom: 5px"
                      :rules="[ val => val && val.length > 0 || 'Please Enter the customer']"
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
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="newDataCancel()">{{ $t('cancel') }}</q-btn>
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
             <q-tooltip>{{ $t('index.close') }}</q-tooltip>
           </q-btn>
         </q-bar>
         <q-card-section style="max-height: 325px; width: 400px" class="scroll">
           {{ $t('deletetip') }}
         </q-card-section>
         <div style="float: right; padding: 15px 15px 15px 0">
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="deleteDataCancel()">{{ $t('cancel') }}</q-btn>
           <q-btn color="primary" @click="deleteDataSubmit()">Submit</q-btn>
         </div>
       </q-card>
     </q-dialog>
      <q-dialog v-model="neworderForm">
       <q-card class="shadow-24">
         <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
           <div>{{ $t('confirmorder') }}</div>
           <q-space />
           <q-btn dense flat icon="close" v-close-popup>
             <q-tooltip>{{ $t('index.close') }}</q-tooltip>
           </q-btn>
         </q-bar>
         <q-card-section style="max-height: 325px; width: 400px" class="scroll">
           {{ $t('deletetip') }}
         </q-card-section>
         <div style="float: right; padding: 15px 15px 15px 0">
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="neworderDataCancel()">{{ $t('cancel') }}</q-btn>
           <q-btn color="primary" @click="neworderDataSubmit()">Submit</q-btn>
         </div>
       </q-card>
     </q-dialog>
      <q-dialog v-model="orderreleaseForm">
       <q-card class="shadow-24">
         <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
           <div>{{ $t('releaseorder') }}</div>
           <q-space />
           <q-btn dense flat icon="close" v-close-popup>
             <q-tooltip>{{ $t('index.close') }}</q-tooltip>
           </q-btn>
         </q-bar>
         <q-card-section style="max-height: 325px; width: 400px" class="scroll">
           {{ $t('deletetip') }}
         </q-card-section>
         <div style="float: right; padding: 15px 15px 15px 0">
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="orderreleaseDataCancel()">{{ $t('cancel') }}</q-btn>
           <q-btn color="primary" @click="orderreleaseDataSubmit()">Submit</q-btn>
         </div>
       </q-card>
     </q-dialog>
      <q-dialog v-model="viewForm">
       <q-card id="printMe">
         <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
           <div>{{ viewdn }}</div>
           <q-space />
         </q-bar>
         <q-card-section>
           <div class="text-h6">Sender: {{ warehouse_detail.warehouse_name }}</div>
           <div class="text-subtitle2">Address: {{ warehouse_detail.warehouse_city }}{{ warehouse_detail.warehouse_address }}</div>
           <div class="text-subtitle2">Tel: {{ warehouse_detail.warehouse_contact }}</div>
           <div class="text-h6">Receiver: {{ customer_detail.customer_name }}</div>
           <div class="text-subtitle2">Address: {{ customer_detail.customer_city }}{{ customer_detail.customer_address }}</div>
           <div class="text-subtitle2">Tel: {{ customer_detail.customer_contact }}</div>
         </q-card-section>
         <q-markup-table>
          <thead>
            <tr>
              <th class="text-left">Goods Code</th>
              <th class="text-right">Goods Weight(Unit: KG)</th>
              <th class="text-right">Goods Volume(Unit: Cubic Metres)</th>
              <th class="text-right">Shipping QTY</th>
              <th class="text-right">Comments</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(view, index) in viewprint_table" :key="index">
              <td class="text-left">{{ view.goods_code }}</td>
              <td class="text-right">{{ view.goods_weight }}</td>
              <td class="text-right">{{ view.goods_volume }}</td>
              <td class="text-right">{{ view.goods_qty }}</td>
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
           <div>{{ newFormData.dn_code }}</div>
           <q-space />
           <q-btn dense flat icon="close" v-close-popup>
             <q-tooltip>{{ $t('index.close') }}</q-tooltip>
           </q-btn>
         </q-bar>
         <q-card-section style="max-height: 325px; width: 400px" class="scroll">
            <q-input dense
                     outlined
                     square
                     debounce="500"
                     disable
                     readonly
                     v-model="newFormData.customer"
                     label="Customer List"
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
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="newDataCancel()">{{ $t('cancel') }}</q-btn>
           <q-btn color="primary" @click="sortedDataSubmit()">Submit</q-btn>
         </div>
       </q-card>
     </q-dialog>
    </div>
</template>
    <router-view />

<script>
import { getauth, postauth, putauth, deleteauth, ViewPrintAuth, getfile } from 'boot/axios_request'
import { date, exportFile, LocalStorage } from 'quasar'

export default {
  name: 'Pagednlist',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'dn/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      viewprint_table: [],
      warehouse_detail: {},
      customer_list: [],
      customer_detail: {},
      columns: [
        { name: 'dn_code', required: true, label: this.$t('outbound.view_dn.dn_code'), align: 'left', field: 'dn_code' },
        { name: 'dn_status', label: this.$t('outbound.view_dn.dn_status'), field: 'dn_status', align: 'center' },
        { name: 'total_weight', label: this.$t('outbound.view_dn.total_weight'), field: 'total_weight', align: 'center' },
        { name: 'total_volume', label: this.$t('outbound.view_dn.total_volume'), field: 'total_volume', align: 'center' },
        { name: 'customer', label: this.$t('outbound.view_dn.customer'), field: 'customer', align: 'center' },
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
      options: LocalStorage.getItem('goods_code_list'),
      newdn: { creater: '' },
      newFormData: {
        dn_code: '',
        customer: '',
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
      neworderForm: false,
      neworderid: 0,
      orderreleaseForm: false,
      orderreleaseid: 0,
      viewForm: false,
      viewdn: '',
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
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname + 'list/', {
        }).then(res => {
          _this.table_list = res.results
          _this.customer_list = res.customer_list
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
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname_previous, {
        }).then(res => {
          _this.table_list = res.results
          _this.customer_list = res.customer_list
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
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname_next, {
        }).then(res => {
          _this.table_list = res.results
          _this.customer_list = res.customer_list
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
      _this.newdn.creater = _this.login_name
      postauth(_this.pathname + 'list/', _this.newdn).then(res => {
        _this.newFormData.dn_code = res.dn_code
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
        dn_code: '',
        customer: '',
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
      if (e.dn_status > 1) {
        _this.$q.notify({
          message: e.dn_code + ' has been deliveried , can not be edit',
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.newFormData.dn_code = e.dn_code
        _this.newFormData.customer = e.customer
        getauth(_this.pathname + 'detail/?dn_code=' + e.dn_code).then(res => {
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
        dn_code: '',
        customer: '',
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
    neworderData (e) {
      var _this = this
      _this.neworderForm = true
      _this.neworderid = e
    },
    neworderDataSubmit () {
      var _this = this
      postauth(_this.pathname + 'neworder/' + _this.neworderid + '/', {}).then(res => {
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
          _this.neworderDataCancel()
          _this.getList()
          _this.$q.notify({
            message: 'Success Confirm dn Delivery',
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
    neworderDataCancel () {
      var _this = this
      _this.neworderForm = false
      _this.neworderid = 0
    },
    orderreleaseData (e) {
      var _this = this
      _this.orderreleaseForm = true
      _this.orderreleaseid = e
    },
    orderreleaseAllData () {
      var _this = this
      postauth(_this.pathname + 'orderrelease/', {}).then(res => {
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
          _this.$q.notify({
            message: 'Success Release All Order',
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
    orderreleaseDataSubmit () {
      var _this = this
      putauth(_this.pathname + 'orderrelease/' + _this.orderreleaseid + '/', {}).then(res => {
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
          _this.orderreleaseDataCancel()
          _this.getList()
          _this.$q.notify({
            message: 'Success Release DN Code',
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
    orderreleaseDataCancel () {
      var _this = this
      _this.orderreleaseForm = false
      _this.orderreleaseid = 0
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
          LocalStorage.set('goods_code_list', goodscodelist)
          _this.options = LocalStorage.getItem('goods_code_list')
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
      if (e.dn_status !== 3) {
        _this.$q.notify({
          message: e.dn_code + ' Not in pre_sorted status , can not be edit',
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.newFormData.dn_code = e.dn_code
        _this.newFormData.customer = e.customer
        getauth(_this.pathname + 'detail/?dn_code=' + e.dn_code).then(res => {
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
        dn_code: '',
        customer: '',
        goods_code: [],
        goods_qty: [],
        creater: ''
      }
      _this.goodsDataClear()
    },
    viewData (e) {
      var _this = this
      ViewPrintAuth(_this.pathname + 'viewprint/' + e.id + '/').then(res => {
        _this.viewprint_table = res.dn_detail
        _this.warehouse_detail = res.warehouse_detail
        _this.customer_detail = res.customer_detail
        _this.viewdn = e.dn_code
        _this.viewForm = true
      })
    },
    downloadlistData () {
      var _this = this
      getfile(_this.pathname + 'filelist/?lang=' + LocalStorage.getItem('lang')).then(res => {
        var timeStamp = Date.now()
        var formattedString = date.formatDate(timeStamp, 'YYYYMMDDHHmmssSSS')
        const status = exportFile(
          _this.pathname + 'list' + formattedString + '.csv',
          res.data,
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
    },
    downloaddetailData () {
      var _this = this
      getfile(_this.pathname + 'filedetail/?lang=' + LocalStorage.getItem('lang')).then(res => {
        var timeStamp = Date.now()
        var formattedString = date.formatDate(timeStamp, 'YYYYMMDDHHmmssSSS')
        const status = exportFile(
          _this.pathname + 'detail' + formattedString + '.csv',
          res.data,
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
    if (LocalStorage.has('goods_code_list')) {
    } else {
      LocalStorage.set('goods_code_list', [])
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
