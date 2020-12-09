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
             <template v-if="props.row.id === editid">
               <q-td key="goods_code" :props="props">
                 <q-input dense
                          outlined
                          square
                          v-model="editFormData.goods_code"
                          label="Goods Code"
                          autofocus
                          :rules="[ val => val && val.length > 0 || 'Please Enter the goods code']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="goods_code" :props="props">
                 {{ props.row.goods_code }}
               </q-td>
             </template>
             <template v-if="props.row.id === editid">
               <q-td key="goods_desc" :props="props">
                 <q-input dense
                          outlined
                          square
                          v-model="editFormData.goods_desc"
                          label="Goods Description"
                          :rules="[ val => val && val.length > 0 || 'Please Enter the goods description']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="goods_desc" :props="props">
                 {{ props.row.goods_desc }}
               </q-td>
             </template>
             <template v-if="props.row.id === editid">
               <q-td key="goods_supplier" :props="props">
                 <q-select dense
                           outlined
                           square
                           v-model="editFormData.goods_supplier"
                           :options="supplier_list"
                           transition-show="scale"
                           transition-hide="scale"
                           label="Supplier"
                           :rules="[ val => val && val.length > 0 || 'Please Enter the supplier']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="goods_supplier" :props="props">
                 {{ props.row.goods_supplier }}
               </q-td>
             </template>
             <template v-if="props.row.id === editid">
               <q-td key="goods_weight" :props="props">
                 <q-input dense
                          outlined
                          square
                          v-model.number="editFormData.goods_weight"
                          type="number"
                          label="Goods Weight(Unit:g)"
                          :rules="[ val => val && val > 0 || 'goods width must greater than 0']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="goods_weight" :props="props">
                 {{ props.row.goods_weight }}
               </q-td>
             </template>
             <template v-if="props.row.id === editid">
               <q-td key="goods_w" :props="props">
                 <q-input dense
                          outlined
                          square
                          v-model.number="editFormData.goods_w"
                          type="number"
                          label="Goods Width(Unit:mm)"
                          :rules="[ val => val && val > 0 || 'goods width must greater than 0']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="goods_w" :props="props">
                 {{ props.row.goods_w }}
               </q-td>
             </template>
             <template v-if="props.row.id === editid">
               <q-td key="goods_d" :props="props">
                 <q-input dense
                          outlined
                          square
                          v-model.number="editFormData.goods_d"
                          type="number"
                          label="Goods depth(Unit:mm)"
                          :rules="[ val => val && val > 0 || 'goods depthh must greater than 0']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="goods_d" :props="props">
                 {{ props.row.goods_d }}
               </q-td>
             </template>
             <template v-if="props.row.id === editid">
               <q-td key="goods_h" :props="props">
                 <q-input dense
                          outlined
                          square
                          v-model.number="editFormData.goods_h"
                          type="number"
                          label="Goods Height(Unit:mm)"
                          :rules="[ val => val && val > 0 || 'goods height must greater than 0']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="goods_h" :props="props">
                 {{ props.row.goods_h }}
               </q-td>
             </template>
             <q-td key="unit_volume" :props="props">
               {{ props.row.unit_volume }}
             </q-td>
             <template v-if="props.row.id === editid">
               <q-td key="goods_unit" :props="props">
                 <q-select dense
                           outlined
                           square
                           v-model="editFormData.goods_unit"
                           :options="goods_unit_list"
                           transition-show="scale"
                           transition-hide="scale"
                           label="Goods Unit"
                           :rules="[ val => val && val.length > 0 || 'Please Enter the goods unit']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="goods_unit" :props="props">
                 {{ props.row.goods_unit }}
               </q-td>
             </template>
             <template v-if="props.row.id === editid">
               <q-td key="goods_class" :props="props">
                 <q-select dense
                           outlined
                           square
                           v-model="editFormData.goods_class"
                           :options="goods_class_list"
                           transition-show="scale"
                           transition-hide="scale"
                           label="Goods Class"
                           :rules="[ val => val && val.length > 0 || 'Please Enter the goods class']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="goods_class" :props="props">
                 {{ props.row.goods_class }}
               </q-td>
             </template>
             <template v-if="props.row.id === editid">
               <q-td key="goods_brand" :props="props">
                 <q-select dense
                           outlined
                           square
                           v-model="editFormData.goods_brand"
                           :options="goods_brand_list"
                           transition-show="scale"
                           transition-hide="scale"
                           label="Goods Brand"
                           :rules="[ val => val && val.length > 0 || 'Please Enter the goods brand']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="goods_brand" :props="props">
                 {{ props.row.goods_brand }}
               </q-td>
             </template>
             <template v-if="props.row.id === editid">
               <q-td key="goods_color" :props="props">
                 <q-select dense
                           outlined
                           square
                           v-model="editFormData.goods_color"
                           :options="goods_color_list"
                           transition-show="scale"
                           transition-hide="scale"
                           label="Goods Color"
                           :rules="[ val => val && val.length > 0 || 'Please Enter the goods color']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="goods_color" :props="props">
                 {{ props.row.goods_color }}
               </q-td>
             </template>
             <template v-if="props.row.id === editid">
               <q-td key="goods_shape" :props="props">
                 <q-select dense
                           outlined
                           square
                           v-model="editFormData.goods_shape"
                           :options="goods_shape_list"
                           transition-show="scale"
                           transition-hide="scale"
                           label="Goods Shape"
                           :rules="[ val => val && val.length > 0 || 'Please Enter the goods shape']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="goods_shape" :props="props">
                 {{ props.row.goods_shape }}
               </q-td>
             </template>
             <template v-if="props.row.id === editid">
               <q-td key="goods_specs" :props="props">
                 <q-select dense
                           outlined
                           square
                           v-model="editFormData.goods_specs"
                           :options="goods_specs_list"
                           transition-show="scale"
                           transition-hide="scale"
                           label="Goods Specs"
                           :rules="[ val => val && val.length > 0 || 'Please Enter the goods specs']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="goods_specs" :props="props">
                 {{ props.row.goods_specs }}
               </q-td>
             </template>
             <template v-if="props.row.id === editid">
               <q-td key="goods_origin" :props="props">
                 <q-select dense
                           outlined
                           square
                           v-model="editFormData.goods_origin"
                           :options="goods_origin_list"
                           transition-show="scale"
                           transition-hide="scale"
                           label="Goods Origin"
                           :rules="[ val => val && val.length > 0 || 'Please Enter the goods origin']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="goods_origin" :props="props">
                 {{ props.row.goods_origin }}
               </q-td>
             </template>
             <template v-if="props.row.id === editid">
               <q-td key="goods_cost" :props="props">
                 <q-input dense
                          outlined
                          square
                          v-model.number="editFormData.goods_cost"
                          type="number"
                          label="Goods Cost"
                          :rules="[ val => val || 'Please Enter the Goods Cost']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="goods_cost" :props="props">
                 {{ props.row.goods_cost }}
               </q-td>
             </template>
             <template v-if="props.row.id === editid">
               <q-td key="goods_price" :props="props">
                 <q-input dense
                          outlined
                          square
                          v-model.number="editFormData.goods_price"
                          type="number"
                          label="Goods Price"
                          :rules="[ val => val || 'Please Enter the Goods Price']"
                 />
               </q-td>
             </template>
             <template v-else-if="props.row.id !== editid">
               <q-td key="goods_price" :props="props">
                 {{ props.row.goods_price }}
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
                    v-model="newFormData.goods_code"
                    label="Goods Code"
                    autofocus
                    :rules="[ val => val && val.length > 0 || 'Please Enter the goods code']"
                    @keyup.enter="newDataSubmit()"/>
           <q-input dense
                    outlined
                    square
                    v-model="newFormData.goods_desc"
                    label="Goods Description"
                    :rules="[ val => val && val.length > 0 || 'Please Enter the goods description']"
                    @keyup.enter="newDataSubmit()"/>
           <q-select dense
                     outlined
                     square
                     v-model="newFormData.goods_supplier"
                     :options="supplier_list"
                     transition-show="scale"
                     transition-hide="scale"
                     label="Supplier"
                     :rules="[ val => val && val.length > 0 || 'Please Enter the supplier']"
                     @keyup.enter="newDataSubmit()"/>
           <q-input dense
                    outlined
                    square
                    v-model.number="newFormData.goods_weight"
                    type="number"
                    label="Goods Weight"
                    :rules="[ val => val && val > 0 || 'goods width must greater than 0']"
                    @keyup.enter="newDataSubmit()"/>
           <q-input dense
                    outlined
                    square
                    v-model.number="newFormData.goods_w"
                    type="number"
                    label="Goods Width(Unit:mm)"
                    :rules="[ val => val && val > 0 || 'goods width must greater than 0']"
                    @keyup.enter="newDataSubmit()"/>
           <q-input dense
                    outlined
                    square
                    v-model.number="newFormData.goods_d"
                    type="number"
                    label="Goods Depth(Unit:mm)"
                    :rules="[ val => val && val > 0 || 'goods depthh must greater than 0']"
                    @keyup.enter="newDataSubmit()"/>
           <q-input dense
                    outlined
                    square
                    v-model.number="newFormData.goods_h"
                    type="number"
                    label="Goods Height(Unit:mm)"
                    :rules="[ val => val && val > 0 || 'goods height must greater than 0']"
                    @keyup.enter="newDataSubmit()"/>
           <q-select dense
                     outlined
                     square
                     v-model="newFormData.goods_unit"
                     :options="goods_unit_list"
                     transition-show="scale"
                     transition-hide="scale"
                     label="Goods Unit"
                     :rules="[ val => val && val.length > 0 || 'Please Enter the goods unit']"
                     @keyup.enter="newDataSubmit()"/>
           <q-select dense
                     outlined
                     square
                     v-model="newFormData.goods_class"
                     :options="goods_class_list"
                     transition-show="scale"
                     transition-hide="scale"
                     label="Goods Class"
                     :rules="[ val => val && val.length > 0 || 'Please Enter the goods class']"
                     @keyup.enter="newDataSubmit()"/>
           <q-select dense
                     outlined
                     square
                     v-model="newFormData.goods_brand"
                     :options="goods_brand_list"
                     transition-show="scale"
                     transition-hide="scale"
                     label="Goods Brand"
                     :rules="[ val => val && val.length > 0 || 'Please Enter the goods brand']"
                     @keyup.enter="newDataSubmit()"/>
           <q-select dense
                     outlined
                     square
                     v-model="newFormData.goods_color"
                     :options="goods_color_list"
                     transition-show="scale"
                     transition-hide="scale"
                     label="Goods Color"
                     :rules="[ val => val && val.length > 0 || 'Please Enter the goods color']"
                     @keyup.enter="newDataSubmit()"/>
           <q-select dense
                     outlined
                     square
                     v-model="newFormData.goods_shape"
                     :options="goods_shape_list"
                     transition-show="scale"
                     transition-hide="scale"
                     label="Goods Shape"
                     :rules="[ val => val && val.length > 0 || 'Please Enter the goods shape']"
                     @keyup.enter="newDataSubmit()"/>
           <q-select dense
                     outlined
                     square
                     v-model="newFormData.goods_specs"
                     :options="goods_specs_list"
                     transition-show="scale"
                     transition-hide="scale"
                     label="Goods Specs"
                     :rules="[ val => val && val.length > 0 || 'Please Enter the goods specs']"
                     @keyup.enter="newDataSubmit()"/>
           <q-select dense
                     outlined
                     square
                     v-model="newFormData.goods_origin"
                     :options="goods_origin_list"
                     transition-show="scale"
                     transition-hide="scale"
                     label="Goods Origin"
                     :rules="[ val => val && val.length > 0 || 'Please Enter the goods origin']"
                     @keyup.enter="newDataSubmit()"/>
           <q-input dense
                    outlined
                    square
                    v-model.number="newFormData.goods_cost"
                    type="number"
                    label="Goods Cost"
                    :rules="[ val => val || 'Please Enter the goods cost']"
                    @keyup.enter="newDataSubmit()"/>
           <q-input dense
                    outlined
                    square
                    v-model.number="newFormData.goods_price"
                    type="number"
                    label="Goods Price"
                    :rules="[ val => val || 'Please Enter the goods price']"
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
// import { openURL } from 'quasar'
import { getauth, postauth, putauth, deleteauth } from 'boot/axios_request'

export default {
  name: 'Pagegoods',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'goods/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      goods_unit_list: [],
      goods_class_list: [],
      goods_brand_list: [],
      goods_color_list: [],
      goods_shape_list: [],
      goods_specs_list: [],
      goods_origin_list: [],
      supplier_list: [],
      columns: [
        { name: 'goods_code', required: true, label: 'Goods Code', align: 'left', field: 'goods_code' },
        { name: 'goods_desc', label: 'Goods Desc', field: 'goods_desc', align: 'center' },
        { name: 'goods_supplier', label: 'Goods Supplier', field: 'goods_supplier', align: 'center' },
        { name: 'goods_weight', label: 'Goods Weight', field: 'goods_weight', align: 'center' },
        { name: 'goods_w', label: 'Goods Width(Unit:mm)', field: 'goods_w', align: 'center' },
        { name: 'goods_d', label: 'Goods Depth(Unit:mm)', field: 'goods_d', align: 'center' },
        { name: 'goods_h', label: 'Goods Height(Unit:mm)', field: 'goods_h', align: 'center' },
        { name: 'unit_volume', label: 'Unit Volume', field: 'unit_volume', align: 'center' },
        { name: 'goods_unit', label: 'Goods Unit', field: 'goods_unit', align: 'center' },
        { name: 'goods_class', label: 'Goods Class', field: 'goods_class', align: 'center' },
        { name: 'goods_brand', label: 'Goods Brand', field: 'goods_brand', align: 'center' },
        { name: 'goods_color', label: 'Goods Color', field: 'goods_color', align: 'center' },
        { name: 'goods_shape', label: 'Goods Shape', field: 'goods_shape', align: 'center' },
        { name: 'goods_specs', label: 'Goods Specs', field: 'goods_specs', align: 'center' },
        { name: 'goods_origin', label: 'Goods Origin', field: 'goods_origin', align: 'center' },
        { name: 'goods_cost', label: 'Goods Cost', field: 'goods_cost', align: 'center' },
        { name: 'goods_price', label: 'Goods Price', field: 'goods_price', align: 'center' },
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
        goods_code: '',
        goods_desc: '',
        goods_supplier: '',
        goods_weight: '',
        goods_w: '',
        goods_d: '',
        goods_h: '',
        goods_unit: '',
        goods_class: '',
        goods_brand: '',
        goods_color: '',
        goods_shape: '',
        goods_specs: '',
        goods_origin: '',
        goods_cost: '',
        goods_price: '',
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
          _this.goods_unit_list = res.goods_unit_list
          _this.goods_class_list = res.goods_class_list
          _this.goods_brand_list = res.goods_brand_list
          _this.goods_color_list = res.goods_color_list
          _this.goods_shape_list = res.goods_shape_list
          _this.goods_specs_list = res.goods_specs_list
          _this.goods_origin_list = res.goods_origin_list
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
          _this.goods_unit_list = res.goods_unit_list
          _this.goods_class_list = res.goods_class_list
          _this.goods_brand_list = res.goods_brand_list
          _this.goods_color_list = res.goods_color_list
          _this.goods_shape_list = res.goods_shape_list
          _this.goods_specs_list = res.goods_specs_list
          _this.goods_origin_list = res.goods_origin_list
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
          _this.goods_unit_list = res.goods_unit_list
          _this.goods_class_list = res.goods_class_list
          _this.goods_brand_list = res.goods_brand_list
          _this.goods_color_list = res.goods_color_list
          _this.goods_shape_list = res.goods_shape_list
          _this.goods_specs_list = res.goods_specs_list
          _this.goods_origin_list = res.goods_origin_list
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
    newDataSubmit () {
      var _this = this
      _this.newFormData.creater = _this.login_name
      postauth(_this.pathname, _this.newFormData).then(res => {
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
        goods_code: '',
        goods_desc: '',
        goods_supplier: '',
        goods_weight: '',
        goods_w: '',
        goods_d: '',
        goods_h: '',
        goods_unit: '',
        goods_class: '',
        goods_brand: '',
        goods_color: '',
        goods_shape: '',
        goods_specs: '',
        goods_origin: '',
        goods_cost: '',
        goods_price: '',
        creater: ''
      }
    },
    editData (e) {
      var _this = this
      _this.editMode = true
      _this.editid = e.id
      _this.editFormData = {
        goods_code: e.goods_code,
        goods_desc: e.goods_desc,
        goods_supplier: e.goods_supplier,
        goods_weight: e.goods_weight,
        goods_w: e.goods_w,
        goods_d: e.goods_d,
        goods_h: e.goods_h,
        goods_unit: e.goods_unit,
        goods_class: e.goods_class,
        goods_brand: e.goods_brand,
        goods_color: e.goods_color,
        goods_shape: e.goods_shape,
        goods_specs: e.goods_specs,
        goods_origin: e.goods_origin,
        goods_cost: e.goods_cost,
        goods_price: e.goods_price,
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
        goods_code: '',
        goods_desc: '',
        goods_supplier: '',
        goods_weight: '',
        goods_w: '',
        goods_d: '',
        goods_h: '',
        goods_unit: '',
        goods_class: '',
        goods_brand: '',
        goods_color: '',
        goods_shape: '',
        goods_specs: '',
        goods_origin: '',
        goods_cost: '',
        goods_price: '',
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
