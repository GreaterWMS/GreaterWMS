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
             <q-btn v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                            $q.localStorage.getItem('staff_type') !== 'Customer' &&
                            $q.localStorage.getItem('staff_type') !== 'Outbound' &&
                            $q.localStorage.getItem('staff_type') !== 'StockControl'
                           "
                    :label="$t('new')" icon="add" @click="newFormOpen()">
               <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                 {{ $t('newtip') }}
               </q-tooltip>
             </q-btn>
             <q-btn v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                            $q.localStorage.getItem('staff_type') !== 'Customer'
                           "
                    :label="$t('refresh')" icon="refresh" @click="reFresh()">
               <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                 {{ $t('refreshtip') }}
               </q-tooltip>
             </q-btn>
             <q-btn :label="$t('downloadasnlist')" icon="cloud_download" @click="downloadlistData()">
               <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                {{ $t('downloadasnlisttip') }}
               </q-tooltip>
             </q-btn>
             <q-btn :label="$t('downloadasnlist')" icon="cloud_download" @click="downloaddetailData()">
               <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                 {{ $t('downloadasndetailtip') }}
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
             <q-td key="action" :props="props" style="width: 100px">
               <q-btn v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                              $q.localStorage.getItem('staff_type') !== 'Customer' &&
                              $q.localStorage.getItem('staff_type') !== 'Outbound' &&
                              $q.localStorage.getItem('staff_type') !== 'StockControl'
                             "
                      round flat push color="info" icon="visibility" @click="viewData(props.row)">
                 <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                  {{ $t('printthisasn') }}
                </q-tooltip>
               </q-btn>
               <q-btn v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                              $q.localStorage.getItem('staff_type') !== 'Customer' &&
                              $q.localStorage.getItem('staff_type') !== 'Outbound' &&
                              $q.localStorage.getItem('staff_type') !== 'StockControl'
                             "
                      round flat push color="positive" icon="img:statics/inbound/preloadstock.png" @click="preloadData(props.row.id)">
                 <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                  {{ $t('confirmdelivery') }}
                </q-tooltip>
               </q-btn>
               <q-btn v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                              $q.localStorage.getItem('staff_type') !== 'Customer' &&
                              $q.localStorage.getItem('staff_type') !== 'Outbound' &&
                              $q.localStorage.getItem('staff_type') !== 'StockControl'
                             "
                      round flat push color="positive" icon="img:statics/inbound/presortstock.png" @click="presortData(props.row.id)">
                 <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                  {{ $t('finishloading') }}
                </q-tooltip>
               </q-btn>
               <q-btn v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                              $q.localStorage.getItem('staff_type') !== 'Customer' &&
                              $q.localStorage.getItem('staff_type') !== 'Outbound' &&
                              $q.localStorage.getItem('staff_type') !== 'StockControl'
                             "
                      round flat push color="purple" icon="img:statics/inbound/sortstock.png" @click="sortedData(props.row)">
                 <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                  {{ $t('confirmsorted') }}
                </q-tooltip>
               </q-btn>
               <q-btn v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                              $q.localStorage.getItem('staff_type') !== 'Customer' &&
                              $q.localStorage.getItem('staff_type') !== 'Outbound' &&
                              $q.localStorage.getItem('staff_type') !== 'StockControl'
                             "
                      round flat push color="purple" icon="edit" @click="editData(props.row)">
                 <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                  {{ $t('edit') }}
                </q-tooltip>
               </q-btn>
               <q-btn v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                              $q.localStorage.getItem('staff_type') !== 'Customer' &&
                              $q.localStorage.getItem('staff_type') !== 'Outbound' &&
                              $q.localStorage.getItem('staff_type') !== 'StockControl'
                             "
                      round flat push color="dark" icon="delete" @click="deleteData(props.row.id)">
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
          <q-btn v-show="!pathname_previous && !pathname_next" flat push color="dark" :label="$t('no_data')"></q-btn>
        </div>
      </template>
      <q-dialog v-model="newForm">
       <q-card class="shadow-24">
         <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
           <div>{{ newFormData.asn_code }}</div>
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
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData3.qty"
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
                         v-model="goodsData3.code"
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
                 <template v-if="goodsData3.code" v-slot:append>
                   <q-icon name="cancel" @click.stop="goodsData3.code = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData4.qty"
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
                         v-model="goodsData4.code"
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
                 <template v-if="goodsData4.code" v-slot:append>
                   <q-icon name="cancel" @click.stop="goodsData4.code = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData5.qty"
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
                         v-model="goodsData5.code"
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
                 <template v-if="goodsData5.code" v-slot:append>
                   <q-icon name="cancel" @click.stop="goodsData5.code = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData6.qty"
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
                         v-model="goodsData6.code"
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
                 <template v-if="goodsData6.code" v-slot:append>
                   <q-icon name="cancel" @click.stop="goodsData6.code = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData7.qty"
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
                         v-model="goodsData7.code"
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
                 <template v-if="goodsData7.code" v-slot:append>
                   <q-icon name="cancel" @click.stop="goodsData7.code = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData8.qty"
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
                         v-model="goodsData8.code"
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
                 <template v-if="goodsData8.code" v-slot:append>
                   <q-icon name="cancel" @click.stop="goodsData8.code = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData9.qty"
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
                         v-model="goodsData9.code"
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
                 <template v-if="goodsData9.code" v-slot:append>
                   <q-icon name="cancel" @click.stop="goodsData9.code = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData10.qty"
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
                         v-model="goodsData10.code"
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
                 <template v-if="goodsData10.code" v-slot:append>
                   <q-icon name="cancel" @click.stop="goodsData10.code = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
         </q-card-section>
         <div style="float: right; padding: 15px 15px 15px 0">
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="newDataCancel()">{{ $t('cancel') }}</q-btn>
           <q-btn color="primary" @click="newDataSubmit()">{{ $t('submit') }}</q-btn>
         </div>
       </q-card>
     </q-dialog>
      <q-dialog v-model="editMode">
       <q-card class="shadow-24">
         <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
           <div>{{ newFormData.asn_code }}</div>
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
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData3.qty"
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
                         v-model="goodsData3.code"
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
                 <template v-if="goodsData3.code" v-slot:append>
                   <q-icon name="cancel" @click.stop="goodsData3.code = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData4.qty"
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
                         v-model="goodsData4.code"
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
                 <template v-if="goodsData4.code" v-slot:append>
                   <q-icon name="cancel" @click.stop="goodsData4.code = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData5.qty"
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
                         v-model="goodsData5.code"
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
                 <template v-if="goodsData5.code" v-slot:append>
                   <q-icon name="cancel" @click.stop="goodsData5.code = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData6.qty"
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
                         v-model="goodsData6.code"
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
                 <template v-if="goodsData6.code" v-slot:append>
                   <q-icon name="cancel" @click.stop="goodsData6.code = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData7.qty"
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
                         v-model="goodsData7.code"
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
                 <template v-if="goodsData7.code" v-slot:append>
                   <q-icon name="cancel" @click.stop="goodsData7.code = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData8.qty"
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
                         v-model="goodsData8.code"
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
                 <template v-if="goodsData8.code" v-slot:append>
                   <q-icon name="cancel" @click.stop="goodsData8.code = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData9.qty"
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
                         v-model="goodsData9.code"
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
                 <template v-if="goodsData9.code" v-slot:append>
                   <q-icon name="cancel" @click.stop="goodsData9.code = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
           <q-input dense
                    outlined
                    square
                    debounce="500"
                    v-model.number="goodsData10.qty"
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
                         v-model="goodsData10.code"
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
                 <template v-if="goodsData10.code" v-slot:append>
                   <q-icon name="cancel" @click.stop="goodsData10.code = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
         </q-card-section>
         <div style="float: right; padding: 15px 15px 15px 0">
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="newDataCancel()">{{ $t('cancel') }}</q-btn>
           <q-btn color="primary" @click="editDataSubmit()">{{ $t('submit') }}</q-btn>
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
      <q-dialog v-model="preloadForm">
       <q-card class="shadow-24">
         <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
           <div>{{ $t('confirmdelivery') }}</div>
           <q-space />
           <q-btn dense flat icon="close" v-close-popup>
             <q-tooltip>{{ $t('index.close') }}</q-tooltip>
           </q-btn>
         </q-bar>
         <q-card-section style="max-height: 325px; width: 400px" class="scroll">
           {{ $t('deletetip') }}
         </q-card-section>
         <div style="float: right; padding: 15px 15px 15px 0">
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="preloadDataCancel()">{{ $t('cancel') }}</q-btn>
           <q-btn color="primary" @click="preloadDataSubmit()">{{ $t('submit') }}</q-btn>
         </div>
       </q-card>
     </q-dialog>
      <q-dialog v-model="presortForm">
       <q-card class="shadow-24">
         <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
           <div>{{ $t('finishloading') }}</div>
           <q-space />
           <q-btn dense flat icon="close" v-close-popup>
             <q-tooltip>{{ $t('index.close') }}</q-tooltip>
           </q-btn>
         </q-bar>
         <q-card-section style="max-height: 325px; width: 400px" class="scroll">
           {{ $t('deletetip') }}
         </q-card-section>
         <div style="float: right; padding: 15px 15px 15px 0">
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="presortDataCancel()">{{ $t('cancel') }}</q-btn>
           <q-btn color="primary" @click="presortDataSubmit()">{{ $t('submit') }}</q-btn>
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
           <div>{{ sorted_list.asn_code }}</div>
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
                     v-model="sorted_list.supplier"
                     label="Supplier List"
                     style="margin-bottom: 5px"
            />
           <div v-for="(item, index) in sorted_list.goodsData" :key="index">
             <q-input dense
                      outlined
                      square
                      bottom-slots
                      type="number"
                      v-model='item.goods_actual_qty'
                      label="Goods Actual Qty"
             >
               <template v-slot:append>
                 {{ item.goods_code }}
               </template>
            </q-input>
           </div>
         </q-card-section>
         <div style="float: right; padding: 15px 15px 15px 0">
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="sortedDataCancel()">{{ $t('cancel') }}</q-btn>
           <q-btn color="primary" @click="sortedDataSubmit()">{{ $t('submit') }}</q-btn>
         </div>
       </q-card>
     </q-dialog>
    </div>
</template>
    <router-view />

<script>
import { getauth, postauth, putauth, deleteauth, ViewPrintAuth, getfile } from 'boot/axios_request'
import { date, exportFile, SessionStorage, LocalStorage } from 'quasar'

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
        { name: 'asn_code', required: true, label: this.$t('inbound.view_asn.asn_code'), align: 'left', field: 'asn_code' },
        { name: 'asn_status', label: this.$t('inbound.view_asn.asn_status'), field: 'asn_status', align: 'center' },
        { name: 'total_weight', label: this.$t('inbound.view_asn.total_weight'), field: 'total_weight', align: 'center' },
        { name: 'total_volume', label: this.$t('inbound.view_asn.total_volume'), field: 'total_volume', align: 'center' },
        { name: 'supplier', label: this.$t('baseinfo.view_supplier.supplier_name'), field: 'supplier', align: 'center' },
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
      goodsData3: { code: '', qty: '' },
      goodsData4: { code: '', qty: '' },
      goodsData5: { code: '', qty: '' },
      goodsData6: { code: '', qty: '' },
      goodsData7: { code: '', qty: '' },
      goodsData8: { code: '', qty: '' },
      goodsData9: { code: '', qty: '' },
      goodsData10: { code: '', qty: '' },
      editid: 0,
      editFormData: {},
      editMode: false,
      sortedForm: false,
      sortedid: 0,
      sorted_list: {
        asn_code: '',
        supplier: '',
        goodsData: [],
        creater: ''
      },
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
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname + 'list/', {
        }).then(res => {
          _this.table_list = res.results
          _this.supplier_list = res.supplier_list
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
        getauth(_this.pathname + 'list/?asn_code__icontains=' + _this.filter, {
        }).then(res => {
          _this.table_list = res.results
          _this.supplier_list = res.supplier_list
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
          _this.supplier_list = res.supplier_list
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
          _this.supplier_list = res.supplier_list
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
      if (_this.goodsData3.code !== '' && _this.goodsData3.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData3.code)
        _this.newFormData.goods_qty.push(_this.goodsData3.qty)
      }
      if (_this.goodsData4.code !== '' && _this.goodsData4.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData4.code)
        _this.newFormData.goods_qty.push(_this.goodsData4.qty)
      }
      if (_this.goodsData5.code !== '' && _this.goodsData5.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData5.code)
        _this.newFormData.goods_qty.push(_this.goodsData5.qty)
      }
      if (_this.goodsData6.code !== '' && _this.goodsData6.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData6.code)
        _this.newFormData.goods_qty.push(_this.goodsData6.qty)
      }
      if (_this.goodsData7.code !== '' && _this.goodsData7.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData7.code)
        _this.newFormData.goods_qty.push(_this.goodsData7.qty)
      }
      if (_this.goodsData8.code !== '' && _this.goodsData8.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData8.code)
        _this.newFormData.goods_qty.push(_this.goodsData8.qty)
      }
      if (_this.goodsData9.code !== '' && _this.goodsData9.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData9.code)
        _this.newFormData.goods_qty.push(_this.goodsData9.qty)
      }
      if (_this.goodsData10.code !== '' && _this.goodsData10.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData10.code)
        _this.newFormData.goods_qty.push(_this.goodsData10.qty)
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
      _this.goodsData3 = { code: '', qty: '' }
      _this.goodsData4 = { code: '', qty: '' }
      _this.goodsData5 = { code: '', qty: '' }
      _this.goodsData6 = { code: '', qty: '' }
      _this.goodsData7 = { code: '', qty: '' }
      _this.goodsData8 = { code: '', qty: '' }
      _this.goodsData9 = { code: '', qty: '' }
      _this.goodsData10 = { code: '', qty: '' }
    },
    editData (e) {
      var _this = this
      _this.goodsDataClear()
      if (e.asn_status !== 1) {
        _this.$q.notify({
          message: e.asn_code + 'Status Is Not 1',
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
            } else if (index === 2) {
              _this.goodsData3 = { code: detail.goods_code, qty: detail.goods_qty }
            } else if (index === 3) {
              _this.goodsData4 = { code: detail.goods_code, qty: detail.goods_qty }
            } else if (index === 4) {
              _this.goodsData5 = { code: detail.goods_code, qty: detail.goods_qty }
            } else if (index === 5) {
              _this.goodsData6 = { code: detail.goods_code, qty: detail.goods_qty }
            } else if (index === 6) {
              _this.goodsData7 = { code: detail.goods_code, qty: detail.goods_qty }
            } else if (index === 7) {
              _this.goodsData8 = { code: detail.goods_code, qty: detail.goods_qty }
            } else if (index === 8) {
              _this.goodsData9 = { code: detail.goods_code, qty: detail.goods_qty }
            } else if (index === 9) {
              _this.goodsData10 = { code: detail.goods_code, qty: detail.goods_qty }
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
      if (_this.goodsData3.code !== '' && _this.goodsData3.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData3.code)
        _this.newFormData.goods_qty.push(_this.goodsData3.qty)
      }
      if (_this.goodsData4.code !== '' && _this.goodsData4.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData4.code)
        _this.newFormData.goods_qty.push(_this.goodsData4.qty)
      }
      if (_this.goodsData5.code !== '' && _this.goodsData5.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData5.code)
        _this.newFormData.goods_qty.push(_this.goodsData5.qty)
      }
      if (_this.goodsData6.code !== '' && _this.goodsData6.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData6.code)
        _this.newFormData.goods_qty.push(_this.goodsData6.qty)
      }
      if (_this.goodsData7.code !== '' && _this.goodsData7.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData7.code)
        _this.newFormData.goods_qty.push(_this.goodsData7.qty)
      }
      if (_this.goodsData8.code !== '' && _this.goodsData8.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData8.code)
        _this.newFormData.goods_qty.push(_this.goodsData8.qty)
      }
      if (_this.goodsData9.code !== '' && _this.goodsData9.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData9.code)
        _this.newFormData.goods_qty.push(_this.goodsData9.qty)
      }
      if (_this.goodsData10.code !== '' && _this.goodsData10.qty !== '') {
        _this.newFormData.goods_code.push(_this.goodsData10.code)
        _this.newFormData.goods_qty.push(_this.goodsData10.qty)
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
          message: e.asn_code + 'Status Is Not 3',
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.sorted_list.asn_code = e.asn_code
        _this.sorted_list.supplier = e.supplier
        getauth(_this.pathname + 'detail/?asn_code=' + e.asn_code).then(res => {
          _this.sortedForm = true
          _this.sortedid = e.id
          _this.sorted_list.goodsData = res.results
        })
      }
    },
    sortedDataSubmit () {
      var _this = this
      _this.sorted_list.creater = _this.login_name
      postauth(_this.pathname + 'sorted/' + _this.sortedid + '/', _this.sorted_list).then(res => {
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
      _this.sorted_list = {
        asn_code: '',
        supplier: '',
        goodsData: [],
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
    },
    downloadlistData () {
      var _this = this
      getfile(_this.pathname + 'filelist/?lang=' + LocalStorage.getItem('lang')).then(res => {
        var timeStamp = Date.now()
        var formattedString = date.formatDate(timeStamp, 'YYYYMMDDHHmmssSSS')
        const status = exportFile(
          _this.pathname + 'list' + formattedString + '.csv',
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
    },
    downloaddetailData () {
      var _this = this
      getfile(_this.pathname + 'filedetail/?lang=' + LocalStorage.getItem('lang')).then(res => {
        var timeStamp = Date.now()
        var formattedString = date.formatDate(timeStamp, 'YYYYMMDDHHmmssSSS')
        const status = exportFile(
          _this.pathname + 'detail' + formattedString + '.csv',
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
    if (SessionStorage.has('goods_code')) {
    } else {
      SessionStorage.set('goods_code', [])
    }
  },
  mounted () {
    var _this = this
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
