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
                              $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                              $q.localStorage.getItem('staff_type') !== 'StockControl'
                             "
                   :label="$t('new')" icon="add" @click="newFormOpen()">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                {{ $t('newtip') }}
              </q-tooltip>
            </q-btn>
            <q-btn :label="$t('refresh')" icon="refresh" @click="reFresh()">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                {{ $t('refreshtip') }}
              </q-tooltip>
            </q-btn>
            <q-btn v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                              $q.localStorage.getItem('staff_type') !== 'Customer' &&
                              $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                              $q.localStorage.getItem('staff_type') !== 'StockControl'
                             "
                   :label="$t('release')" icon="img:statics/outbound/orderrelease.png" @click="orderreleaseAllData()">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                {{ $t('releaseallorder') }}
              </q-tooltip>
            </q-btn>
            <q-btn :label="$t('downloaddnlist')" icon="cloud_download" @click="downloadlistData()">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                {{ $t('downloaddnlisttip') }}
              </q-tooltip>
            </q-btn>
            <q-btn :label="$t('downloaddndetail')" icon="cloud_download" @click="downloaddetailData()">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                {{ $t('downloaddndetailtip') }}
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
            <q-td key="action" :props="props" style="width: 100px">
              <q-btn v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                              $q.localStorage.getItem('staff_type') !== 'Customer' &&
                              $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                              $q.localStorage.getItem('staff_type') !== 'StockControl'
                             "
                     round flat push color="info" icon="visibility" @click="viewData(props.row)">
                <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                  {{ $t('printthisdn') }}
                </q-tooltip>
              </q-btn>
              <q-btn v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                              $q.localStorage.getItem('staff_type') !== 'Customer' &&
                              $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                              $q.localStorage.getItem('staff_type') !== 'StockControl'
                             "
                     round flat push color="positive" icon="img:statics/outbound/order.png" @click="neworderData(props.row)">
                <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                  {{ $t('confirmorder') }}
                </q-tooltip>
              </q-btn>
              <q-btn v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                              $q.localStorage.getItem('staff_type') !== 'Customer' &&
                              $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                              $q.localStorage.getItem('staff_type') !== 'StockControl'
                             "
                     round flat push color="positive" icon="img:statics/outbound/orderrelease.png" @click="orderreleaseData(props.row)">
                <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                  {{ $t('releaseorder') }}
                </q-tooltip>
              </q-btn>
              <q-btn v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                              $q.localStorage.getItem('staff_type') !== 'Customer' &&
                              $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                              $q.localStorage.getItem('staff_type') !== 'StockControl'
                             "
                     round flat push color="secondary" icon="print" @click="PrintPickingList(props.row)">
                <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                  {{ $t('print') }}
                </q-tooltip>
              </q-btn>
              <q-btn v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                              $q.localStorage.getItem('staff_type') !== 'Customer' &&
                              $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                              $q.localStorage.getItem('staff_type') !== 'StockControl'
                             "
                     round flat push color="purple" icon="img:statics/outbound/picked.png" @click="pickedData(props.row)">
                <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                  {{ $t('confirmpicked') }}
                </q-tooltip>
              </q-btn>
              <q-btn v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                              $q.localStorage.getItem('staff_type') !== 'Customer' &&
                              $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                              $q.localStorage.getItem('staff_type') !== 'StockControl'
                             "
                     round flat push color="dark" icon="rv_hookup" @click="DispatchDN(props.row)">
                <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                  {{ $t('dispatch') }}
                </q-tooltip>
              </q-btn>
              <q-btn v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                              $q.localStorage.getItem('staff_type') !== 'Customer' &&
                              $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                              $q.localStorage.getItem('staff_type') !== 'StockControl'
                             "
                     round flat push color="info" icon="img:statics/outbound/receiving.png" @click="PODData(props.row)">
                <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                  {{ $t('outbound.pod') }}
                </q-tooltip>
              </q-btn>
              <q-btn v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                              $q.localStorage.getItem('staff_type') !== 'Customer' &&
                              $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                              $q.localStorage.getItem('staff_type') !== 'StockControl'
                             "
                     round flat push color="purple" icon="edit" @click="editData(props.row)">
                <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                  {{ $t('edit') }}
                </q-tooltip>
              </q-btn>
              <q-btn v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                              $q.localStorage.getItem('staff_type') !== 'Customer' &&
                              $q.localStorage.getItem('staff_type') !== 'Inbound' &&
                              $q.localStorage.getItem('staff_type') !== 'StockControl'
                             "
                     round flat push color="dark" icon="delete" @click="deleteData(props.row)">
                <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                  {{ $t('delete') }}
                </q-tooltip>
              </q-btn>
            </q-td>
            <template v-if="props.row.transportation_fee.detail !== []">
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
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
    <q-dialog v-model="newForm">
      <q-card class="shadow-24">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <div>{{ newFormData.dn_code }}</div>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-amber text-black shadow-4">{{ $t('index.close') }}</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section style="max-height: 325px; width: 400px" class="scroll">
          <q-select dense
                    outlined
                    square
                    debounce="500"
                    v-model="newFormData.customer"
                    :options="customer_list"
                    :label="$t('baseinfo.view_customer.customer_name')"
                    style="margin-bottom: 5px"
                    :rules="[ val => val && val.length > 0 || 'Please Enter the Customer']"
                    @keyup.enter="newDataSubmit()"/>
          <q-input dense
                   outlined
                   square
                   debounce="500"
                   v-model.number="goodsData1.qty"
                   type="number"
                   :label="$t('stock.view_stocklist.goods_qty')"
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
                        :label="$t('goods.view_goodslist.goods_code')"
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
                   :label="$t('stock.view_stocklist.goods_qty')"
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
                        :label="$t('goods.view_goodslist.goods_code')"
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
                   :label="$t('stock.view_stocklist.goods_qty')"
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
                        :label="$t('goods.view_goodslist.goods_code')"
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
                   :label="$t('stock.view_stocklist.goods_qty')"
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
                        :label="$t('goods.view_goodslist.goods_code')"
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
                   :label="$t('stock.view_stocklist.goods_qty')"
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
                        :label="$t('goods.view_goodslist.goods_code')"
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
                   :label="$t('stock.view_stocklist.goods_qty')"
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
                        :label="$t('goods.view_goodslist.goods_code')"
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
                   :label="$t('stock.view_stocklist.goods_qty')"
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
                        :label="$t('goods.view_goodslist.goods_code')"
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
                   :label="$t('stock.view_stocklist.goods_qty')"
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
                        :label="$t('goods.view_goodslist.goods_code')"
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
                   :label="$t('stock.view_stocklist.goods_qty')"
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
                        :label="$t('goods.view_goodslist.goods_code')"
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
                   :label="$t('stock.view_stocklist.goods_qty')"
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
                        :label="$t('goods.view_goodslist.goods_code')"
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
                    :label="$t('baseinfo.view_customer.customer_name')"
                    style="margin-bottom: 5px"
                    :rules="[ val => val && val.length > 0 || 'Please Enter the customer']"
                    @keyup.enter="editDataSubmit()"/>
          <q-input dense
                   outlined
                   square
                   debounce="500"
                   v-model.number="goodsData1.qty"
                   type="number"
                   :label="$t('stock.view_stocklist.goods_qty')"
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
                        :label="$t('goods.view_goodslist.goods_code')"
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
                   :label="$t('stock.view_stocklist.goods_qty')"
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
                        :label="$t('goods.view_goodslist.goods_code')"
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
                   :label="$t('stock.view_stocklist.goods_qty')"
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
                        :label="$t('goods.view_goodslist.goods_code')"
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
                   :label="$t('stock.view_stocklist.goods_qty')"
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
                        :label="$t('goods.view_goodslist.goods_code')"
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
                   :label="$t('stock.view_stocklist.goods_qty')"
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
                        :label="$t('goods.view_goodslist.goods_code')"
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
                   :label="$t('stock.view_stocklist.goods_qty')"
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
                        :label="$t('goods.view_goodslist.goods_code')"
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
                   :label="$t('stock.view_stocklist.goods_qty')"
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
                        :label="$t('goods.view_goodslist.goods_code')"
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
                   :label="$t('stock.view_stocklist.goods_qty')"
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
                        :label="$t('goods.view_goodslist.goods_code')"
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
                   :label="$t('stock.view_stocklist.goods_qty')"
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
                        :label="$t('goods.view_goodslist.goods_code')"
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
                   :label="$t('stock.view_stocklist.goods_qty')"
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
                        :label="$t('goods.view_goodslist.goods_code')"
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
          <q-btn color="white" text-color="black" style="margin-right: 25px" @click="editDataCancel()">{{ $t('cancel') }}</q-btn>
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
          <q-btn color="primary" @click="neworderDataSubmit()">{{ $t('submit') }}</q-btn>
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
          <q-btn color="primary" @click="orderreleaseDataSubmit()">{{ $t('submit') }}</q-btn>
        </div>
      </q-card>
    </q-dialog>
    <q-dialog v-model="viewForm">
      <q-card id="printMe">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <div>{{ viewdn }}</div>
          <q-space />
          {{ $t('outbound.dn') }}
        </q-bar>
        <q-card-section>
          <div class="row">
            <div class="col-8">
              <div class="text-h6">Sender: {{ warehouse_detail.warehouse_name }}</div>
              <div class="text-subtitle2">Address: {{ warehouse_detail.warehouse_city }}{{ warehouse_detail.warehouse_address }}</div>
              <div class="text-subtitle2">Tel: {{ warehouse_detail.warehouse_contact }}</div>
              <div class="text-h6">Receiver: {{ customer_detail.customer_name }}</div>
              <div class="text-subtitle2">Address: {{ customer_detail.customer_city }}{{ customer_detail.customer_address }}</div>
              <div class="text-subtitle2">Tel: {{ customer_detail.customer_contact }}</div>
            </div>
            <div class="col-4">
              <img :src="bar_code" style="width: 70%; margin-left: 15%"/>
            </div>
          </div>
        </q-card-section>
        <q-markup-table>
          <thead>
          <tr>
            <th class="text-left">{{ $t('goods.view_goodslist.goods_code') }}</th>
            <th class="text-right">{{ $t('outbound.view_dn.total_weight') }}</th>
            <th class="text-right">{{ $t('outbound.view_dn.total_volume') }}</th>
            <th class="text-right">{{ $t('outbound.view_dn.intransit_qty') }}</th>
            <th class="text-right">Comments</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(view, index) in viewprint_table" :key="index">
            <td class="text-left">{{ view.goods_code }}</td>
            <td class="text-right">{{ view.goods_weight }}</td>
            <td class="text-right">{{ view.goods_volume }}</td>
            <td class="text-right">{{ view.picked_qty + view.intransit_qty }}</td>
            <td class="text-right"></td>
          </tr>
          </tbody>
        </q-markup-table>
      </q-card>
      <div style="float: right; padding: 15px 15px 15px 0">
        <q-btn color="primary" icon="print" v-print="printObj">print</q-btn>
      </div>
    </q-dialog>
    <q-dialog v-model="viewPLForm">
      <q-card id="printPL">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <div>{{ $t('print') }}</div>
          <q-space />
        </q-bar>
        <q-markup-table>
          <thead>
          <tr>
            <th class="text-left">{{ $t('outbound.view_dn.dn_code') }}</th>
            <th class="text-right">{{ $t('warehouse.view_binset.bin_name') }}</th>
            <th class="text-right">{{ $t('outbound.view_dn.goods_qty') }}</th>
            <th class="text-right">{{ $t('outbound.pickstock') }}</th>
            <th class="text-right">{{ $t('outbound.pickedstock') }}</th>
            <th class="text-right">Comments</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(view, index) in pickinglist_print_table" :key="index">
            <td class="text-left">{{ view.dn_code }}</td>
            <td class="text-right">{{ view.bin_name }}</td>
            <td class="text-right">{{ view.goods_code }}</td>
            <td class="text-right">{{ view.pick_qty }}</td>
            <td class="text-right" v-show="picklist_check === 0"></td>
            <td class="text-right" v-show="picklist_check > 0">{{ view.picked_qty }}</td>
            <td class="text-right"></td>
          </tr>
          </tbody>
        </q-markup-table>
      </q-card>
      <div style="float: right; padding: 15px 15px 15px 0">
        <q-btn color="primary" icon="print" v-print="printPL">print</q-btn>
      </div>
    </q-dialog>
    <q-dialog v-model="pickedForm">
      <q-card class="shadow-24">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <div>{{ pickFormData.dn_code }}</div>
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
                   v-model="pickFormData.customer"
                   :label="$t('baseinfo.view_customer.customer_name')"
                   style="margin-bottom: 5px"
          />
          <div v-for="(item, index) in pickFormData.goodsData" :key="index">
            <q-input dense
                     outlined
                     square
                     bottom-slots
                     type="number"
                     v-model='item.pick_qty'
                     :label="item.goods_code"
            >
              <template v-slot:append>
                {{ item.bin_name }}
              </template>
            </q-input>
          </div>
        </q-card-section>
        <div style="float: right; padding: 15px 15px 15px 0">
          <q-btn color="white" text-color="black" style="margin-right: 25px" @click="pickedDataCancel()">{{ $t('cancel') }}</q-btn>
          <q-btn color="primary" @click="pickedDataSubmit()">{{ $t('submit') }}</q-btn>
        </div>
      </q-card>
    </q-dialog>
    <q-dialog v-model="dispatchForm">
      <q-card class="shadow-24">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <div>{{ dispatchFormData.dn_code }}</div>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip>{{ $t('index.close') }}</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section style="max-height: 325px; width: 400px" class="scroll">
          <q-select dense
                    outlined
                    square
                    use-input
                    hide-selected
                    fill-input
                    v-model="dispatchFormData.driver"
                    :label="$t('driver.view_driver.driver_name')"
                    :options="driver_options"
                    @filter="filterFnDispatch"
                    autofocus
                    @keyup.enter="dispatchDataSubmit()">
            <template v-slot:no-option>
              <q-item>
                <q-item-section class="text-grey">
                  No results
                </q-item-section>
              </q-item>
            </template>
            <template v-if="dispatchFormData.driver" v-slot:append>
              <q-icon name="cancel" @click.stop="dispatchFormData.driver = ''" class="cursor-pointer" />
            </template>
          </q-select>
        </q-card-section>
        <div style="float: right; padding: 15px 15px 15px 0">
          <q-btn color="white" text-color="black" style="margin-right: 25px" @click="dispatchDataCancel()">{{ $t('cancel') }}</q-btn>
          <q-btn color="primary" @click="dispatchDataSubmit()">{{ $t('submit') }}</q-btn>
        </div>
      </q-card>
    </q-dialog>
    <q-dialog v-model="podForm">
      <q-card class="shadow-24">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <div>{{ $t('outbound.dn') }}: {{ podFormData.dn_code }}</div>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip>{{ $t('index.close') }}</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section style="max-height: 325px; width: 400px" class="scroll">
          {{ $t('baseinfo.customer') }}: {{ podFormData.customer }}
          <div v-for="(item, index) in podFormData.goodsData" :key="index">
            <q-input dense
                     outlined
                     square
                     debounce="500"
                     v-model.number="item.intransit_qty"
                     type="number"
                     :label="$t('outbound.view_dn.delivery_actual_qty')"
                     style="margin-bottom: 5px"
            >
              <template v-slot:after>
                <q-input dense
                         outlined
                         square
                         debounce="500"
                         v-model.number="item.delivery_damage_qty"
                         type="number"
                         :label="$t('outbound.view_dn.delivery_damage_qty')"
                >
                </q-input>
              </template>
            </q-input>
          </div>
        </q-card-section>
        <div style="float: right; padding: 15px 15px 15px 0">
          <q-btn color="white" text-color="black" style="margin-right: 25px" @click="PODDataCancel()">{{ $t('cancel') }}</q-btn>
          <q-btn color="primary" @click="PODDataSubmit()">{{ $t('submit') }}</q-btn>
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
      bar_code: '',
      pickinglist_print_table: [],
      pickinglist_check: 0,
      warehouse_detail: {},
      customer_list: [],
      driver_list: [],
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
      driver_options: LocalStorage.getItem('driver_name_list'),
      newdn: { creater: '' },
      newFormData: {
        dn_code: '',
        customer: '',
        goods_code: [],
        goods_qty: [],
        creater: ''
      },
      pickFormData: {
        dn_code: '',
        customer: '',
        goodsData: [],
        creater: ''
      },
      goodsData1: { bin: '', code: '', qty: '' },
      goodsData2: { bin: '', code: '', qty: '' },
      goodsData3: { bin: '', code: '', qty: '' },
      goodsData4: { bin: '', code: '', qty: '' },
      goodsData5: { bin: '', code: '', qty: '' },
      goodsData6: { bin: '', code: '', qty: '' },
      goodsData7: { bin: '', code: '', qty: '' },
      goodsData8: { bin: '', code: '', qty: '' },
      goodsData9: { bin: '', code: '', qty: '' },
      goodsData10: { bin: '', code: '', qty: '' },
      editid: 0,
      editFormData: {},
      editMode: false,
      pickedForm: false,
      pickedid: 0,
      deleteForm: false,
      deleteid: 0,
      neworderForm: false,
      neworderid: 0,
      orderreleaseForm: false,
      orderreleaseid: 0,
      viewForm: false,
      viewPLForm: false,
      viewdn: '',
      viewid: 0,
      dispatchid: 0,
      dispatchForm: false,
      dispatchFormData: {
        dn_code: '',
        driver: ''
      },
      podid: 0,
      podForm: false,
      podFormData: {
        dn_code: '',
        customer: '',
        goodsData: []
      },
      printObj: {
        id: 'printMe',
        popTitle: 'Advance Shipment Notice'
      },
      printPL: {
        id: 'printPL',
        popTitle: 'Picking List'
      }
    }
  },
  methods: {
    getList () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname + 'list/', {
        }).then(res => {
          _this.table_list = []
          res.results.forEach((item) => {
            if (item.dn_status === 1) {
              item.dn_status = _this.$t('outbound.freshorder')
            } else if (item.dn_status === 2) {
              item.dn_status = _this.$t('outbound.neworder')
            } else if (item.dn_status === 3) {
              item.dn_status = _this.$t('outbound.pickstock')
            } else if (item.dn_status === 4) {
              item.dn_status = _this.$t('outbound.pickedstock')
            } else if (item.dn_status === 5) {
              item.dn_status = _this.$t('outbound.shippedstock')
            } else if (item.dn_status === 6) {
              item.dn_status = _this.$t('outbound.received')
            } else {
              item.dn_status = 'N/A'
            }
            _this.table_list.push(item)
          })
          res.results.forEach((item) => {
            if (item.asn_status === 1) {
              item.asn_status = _this.$t()
            }
          })
          _this.customer_list = res.customer_list
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
        getauth(_this.pathname + 'list/?dn_code__icontains=' + _this.filter, {
        }).then(res => {
          _this.table_list = []
          res.results.forEach((item) => {
            if (item.dn_status === 1) {
              item.dn_status = _this.$t('outbound.freshorder')
            } else if (item.dn_status === 2) {
              item.dn_status = _this.$t('outbound.neworder')
            } else if (item.dn_status === 3) {
              item.dn_status = _this.$t('outbound.pickstock')
            } else if (item.dn_status === 4) {
              item.dn_status = _this.$t('outbound.pickedstock')
            } else if (item.dn_status === 5) {
              item.dn_status = _this.$t('outbound.shippedstock')
            } else if (item.dn_status === 6) {
              item.dn_status = _this.$t('outbound.received')
            } else {
              item.dn_status = 'N/A'
            }
            _this.table_list.push(item)
          })
          _this.customer_list = res.customer_list
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
          _this.table_list = []
          res.results.forEach((item) => {
            if (item.dn_status === 1) {
              item.dn_status = _this.$t('outbound.freshorder')
            } else if (item.dn_status === 2) {
              item.dn_status = _this.$t('outbound.neworder')
            } else if (item.dn_status === 3) {
              item.dn_status = _this.$t('outbound.pickstock')
            } else if (item.dn_status === 4) {
              item.dn_status = _this.$t('outbound.pickedstock')
            } else if (item.dn_status === 5) {
              item.dn_status = _this.$t('outbound.shippedstock')
            } else if (item.dn_status === 6) {
              item.dn_status = _this.$t('outbound.received')
            } else {
              item.dn_status = 'N/A'
            }
            _this.table_list.push(item)
          })
          _this.customer_list = res.customer_list
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
          _this.table_list = []
          res.results.forEach((item) => {
            if (item.dn_status === 1) {
              item.dn_status = _this.$t('outbound.freshorder')
            } else if (item.dn_status === 2) {
              item.dn_status = _this.$t('outbound.neworder')
            } else if (item.dn_status === 3) {
              item.dn_status = _this.$t('outbound.pickstock')
            } else if (item.dn_status === 4) {
              item.dn_status = _this.$t('outbound.pickedstock')
            } else if (item.dn_status === 5) {
              item.dn_status = _this.$t('outbound.shippedstock')
            } else if (item.dn_status === 6) {
              item.dn_status = _this.$t('outbound.received')
            } else {
              item.dn_status = 'N/A'
            }
            _this.table_list.push(item)
          })
          _this.customer_list = res.customer_list
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
      _this.table_list = []
      _this.getList()
    },
    newFormOpen () {
      var _this = this
      _this.newForm = true
      _this.newdn.creater = _this.login_name
      postauth(_this.pathname + 'list/', _this.newdn).then(res => {
        if (!res.detail) {
          _this.newFormData.dn_code = res.dn_code
        }
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
        _this.newFormData.goods_code[0] = _this.goodsData1.code
        _this.newFormData.goods_qty[0] = _this.goodsData1.qty
      }
      if (_this.goodsData2.code !== '' && _this.goodsData2.qty !== '') {
        _this.newFormData.goods_code[1] = _this.goodsData2.code
        _this.newFormData.goods_qty[1] = _this.goodsData2.qty
      }
      if (_this.goodsData3.code !== '' && _this.goodsData3.qty !== '') {
        _this.newFormData.goods_code[2] = _this.goodsData3.code
        _this.newFormData.goods_qty[2] = _this.goodsData3.qty
      }
      if (_this.goodsData4.code !== '' && _this.goodsData4.qty !== '') {
        _this.newFormData.goods_code[3] = _this.goodsData4.code
        _this.newFormData.goods_qty[3] = _this.goodsData4.qty
      }
      if (_this.goodsData5.code !== '' && _this.goodsData5.qty !== '') {
        _this.newFormData.goods_code[4] = _this.goodsData5.code
        _this.newFormData.goods_qty[4] = _this.goodsData5.qty
      }
      if (_this.goodsData6.code !== '' && _this.goodsData6.qty !== '') {
        _this.newFormData.goods_code[5] = _this.goodsData6.code
        _this.newFormData.goods_qty[5] = _this.goodsData6.qty
      }
      if (_this.goodsData7.code !== '' && _this.goodsData7.qty !== '') {
        _this.newFormData.goods_code[6] = _this.goodsData7.code
        _this.newFormData.goods_qty[6] = _this.goodsData7.qty
      }
      if (_this.goodsData8.code !== '' && _this.goodsData8.qty !== '') {
        _this.newFormData.goods_code[7] = _this.goodsData8.code
        _this.newFormData.goods_qty[7] = _this.goodsData8.qty
      }
      if (_this.goodsData9.code !== '' && _this.goodsData9.qty !== '') {
        _this.newFormData.goods_code[8] = _this.goodsData9.code
        _this.newFormData.goods_qty[8] = _this.goodsData9.qty
      }
      if (_this.goodsData10.code !== '' && _this.goodsData10.qty !== '') {
        _this.newFormData.goods_code[9] = _this.goodsData10.code
        _this.newFormData.goods_qty[9] = _this.goodsData10.qty
      }
      postauth(_this.pathname + 'detail/', _this.newFormData).then(res => {
        _this.table_list = []
        _this.getList()
        _this.newDataCancel()
        if (!res.detail) {
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
      _this.goodsData1 = { bin: '', code: '', qty: '' }
      _this.goodsData2 = { bin: '', code: '', qty: '' }
      _this.goodsData3 = { bin: '', code: '', qty: '' }
      _this.goodsData4 = { bin: '', code: '', qty: '' }
      _this.goodsData5 = { bin: '', code: '', qty: '' }
      _this.goodsData6 = { bin: '', code: '', qty: '' }
      _this.goodsData7 = { bin: '', code: '', qty: '' }
      _this.goodsData8 = { bin: '', code: '', qty: '' }
      _this.goodsData9 = { bin: '', code: '', qty: '' }
      _this.goodsData10 = { bin: '', code: '', qty: '' }
    },
    editData (e) {
      var _this = this
      _this.goodsDataClear()
      if (e.dn_status !== _this.$t('outbound.freshorder')) {
        _this.$q.notify({
          message: e.dn_code + ' DN Status Not ' + _this.$t('outbound.freshorder'),
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
        _this.newFormData.goods_code[0] = _this.goodsData1.code
        _this.newFormData.goods_qty[0] = _this.goodsData1.qty
      }
      if (_this.goodsData2.code !== '' && _this.goodsData2.qty !== '') {
        _this.newFormData.goods_code[1] = _this.goodsData2.code
        _this.newFormData.goods_qty[1] = _this.goodsData2.qty
      }
      if (_this.goodsData3.code !== '' && _this.goodsData3.qty !== '') {
        _this.newFormData.goods_code[2] = _this.goodsData3.code
        _this.newFormData.goods_qty[2] = _this.goodsData3.qty
      }
      if (_this.goodsData4.code !== '' && _this.goodsData4.qty !== '') {
        _this.newFormData.goods_code[3] = _this.goodsData4.code
        _this.newFormData.goods_qty[3] = _this.goodsData4.qty
      }
      if (_this.goodsData5.code !== '' && _this.goodsData5.qty !== '') {
        _this.newFormData.goods_code[4] = _this.goodsData5.code
        _this.newFormData.goods_qty[4] = _this.goodsData5.qty
      }
      if (_this.goodsData6.code !== '' && _this.goodsData6.qty !== '') {
        _this.newFormData.goods_code[5] = _this.goodsData6.code
        _this.newFormData.goods_qty[5] = _this.goodsData6.qty
      }
      if (_this.goodsData7.code !== '' && _this.goodsData7.qty !== '') {
        _this.newFormData.goods_code[6] = _this.goodsData7.code
        _this.newFormData.goods_qty[6] = _this.goodsData7.qty
      }
      if (_this.goodsData8.code !== '' && _this.goodsData8.qty !== '') {
        _this.newFormData.goods_code[7] = _this.goodsData8.code
        _this.newFormData.goods_qty[7] = _this.goodsData8.qty
      }
      if (_this.goodsData9.code !== '' && _this.goodsData9.qty !== '') {
        _this.newFormData.goods_code[8] = _this.goodsData9.code
        _this.newFormData.goods_qty[8] = _this.goodsData9.qty
      }
      if (_this.goodsData10.code !== '' && _this.goodsData10.qty !== '') {
        _this.newFormData.goods_code[9] = _this.goodsData10.code
        _this.newFormData.goods_qty[9] = _this.goodsData10.qty
      }
      putauth(_this.pathname + 'detail/', _this.newFormData).then(res => {
        _this.table_list = []
        _this.editDataCancel()
        _this.getList()
        if (!res.detail) {
          _this.$q.notify({
            message: 'Success Edit DN',
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
      if (e.dn_status !== _this.$t('outbound.freshorder')) {
        _this.$q.notify({
          message: e.dn_code + ' DN Status Is Not ' + _this.$t('outbound.freshorder'),
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.deleteForm = true
        _this.deleteid = e.id
      }
    },
    deleteDataSubmit () {
      var _this = this
      deleteauth(_this.pathname + 'list/' + _this.deleteid + '/').then(res => {
        _this.table_list = []
        _this.deleteDataCancel()
        _this.getList()
        if (!res.detail) {
          _this.$q.notify({
            message: 'Success Delete DN',
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
      if (e.dn_status !== _this.$t('outbound.freshorder')) {
        _this.$q.notify({
          message: e.dn_code + ' DN Status Is Not ' + _this.$t('outbound.freshorder'),
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.neworderForm = true
        _this.neworderid = e.id
      }
    },
    neworderDataSubmit () {
      var _this = this
      postauth(_this.pathname + 'neworder/' + _this.neworderid + '/', {}).then(res => {
        _this.table_list = []
        _this.neworderDataCancel()
        _this.getList()
        if (!res.detail) {
          _this.$q.notify({
            message: 'Success Confirm DN Delivery',
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
      if (e.dn_status !== _this.$t('outbound.neworder')) {
        _this.$q.notify({
          message: e.dn_code + ' DN Status Is Not ' + _this.$t('outbound.neworder'),
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.orderreleaseForm = true
        _this.orderreleaseid = e.id
      }
    },
    orderreleaseAllData () {
      var _this = this
      postauth(_this.pathname + 'orderrelease/', {}).then(res => {
        _this.table_list = []
        _this.getList()
        if (!res.detail) {
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
        _this.table_list = []
        _this.orderreleaseDataCancel()
        _this.getList()
        if (!res.detail) {
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
          const goodscodelist = []
          for (let i = 0; i < res.results.length; i++) {
            goodscodelist.push(res.results[i].goods_code)
          }
          LocalStorage.set('goods_code_list', goodscodelist)
          _this.options = LocalStorage.getItem('goods_code_list')
          _this.$forceUpdate()
        }).catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
      })
    },
    PrintPickingList (e) {
      var _this = this
      getauth(_this.pathname + 'pickinglist/' + e.id + '/').then(res => {
        _this.pickinglist_print_table = []
        _this.picklist_check = 0
        res.forEach((item) => {
          if (item.picked_qty > 0) {
            _this.picklist_check += 1
          } else {}
        })
        _this.pickinglist_print_table = res
        _this.viewPLForm = true
      }).catch(err => {
        _this.$q.notify({
          message: err.detail,
          icon: 'close',
          color: 'negative'
        })
      })
    },
    pickedData (e) {
      var _this = this
      if (e.dn_status !== _this.$t('outbound.pickstock')) {
        _this.$q.notify({
          message: e.dn_code + ' DN Status Is Not ' + _this.$t('outbound.pickstock'),
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.pickFormData.dn_code = e.dn_code
        _this.pickFormData.customer = e.customer
        getauth(_this.pathname + 'pickinglist/' + e.id + '/').then(res => {
          _this.pickedForm = true
          _this.pickedid = e.id
          _this.pickFormData.goodsData = res
        })
      }
    },
    pickedDataSubmit () {
      var _this = this
      _this.pickFormData.creater = _this.login_name
      postauth(_this.pathname + 'picked/' + _this.pickedid + '/', _this.pickFormData).then(res => {
        _this.table_list = []
        _this.pickedDataCancel()
        _this.getList()
        if (!res.detail) {
          _this.$q.notify({
            message: 'Success Confirm Picking List',
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
    pickedDataCancel () {
      var _this = this
      _this.pickedForm = false
      _this.pickedid = 0
      _this.pickFormData = {
        dn_code: '',
        customer: '',
        goodsData: [],
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
        var QRCode = require('qrcode')
        QRCode.toDataURL(e.dn_code, [{
          errorCorrectionLevel: 'H',
          mode: 'byte',
          version: '2',
          type: 'image/jpeg'
        }]
        ).then(url => {
          _this.bar_code = url
        }).catch(err => {
          console.error(err)
        })
        _this.viewForm = true
      })
    },
    filterFnDispatch (val, update, abort) {
      var _this = this
      if (val.length < 1) {
        abort()
        return
      }
      update(() => {
        const needle = val.toLowerCase()
        getauth('driver/?driver_name__icontains=' + needle).then(res => {
          const drivernamelist = []
          for (let i = 0; i < res.results.length; i++) {
            drivernamelist.push(res.results[i].driver_name)
          }
          LocalStorage.set('driver_name_list', drivernamelist)
          _this.driver_options = LocalStorage.getItem('driver_name_list')
          _this.$forceUpdate()
        }).catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
      })
    },
    DispatchDN (e) {
      var _this = this
      if (e.dn_status !== _this.$t('outbound.pickedstock')) {
        _this.$q.notify({
          message: e.dn_code + ' DN Status Is Not ' + _this.$t('outbound.pickedstock'),
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.dispatchFormData.dn_code = e.dn_code
        _this.dispatchid = e.id
        _this.dispatchForm = true
      }
    },
    dispatchDataCancel () {
      var _this = this
      _this.dispatchFormData = { dn_code: '', driver: '' }
      _this.dispatchForm = false
    },
    dispatchDataSubmit () {
      var _this = this
      postauth(_this.pathname + 'dispatch/' + _this.dispatchid + '/', _this.dispatchFormData).then(res => {
        _this.table_list = []
        _this.dispatchDataCancel()
        _this.getList()
        if (!res.detail) {
          _this.$q.notify({
            message: 'Success Dispatch',
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
    PODData (e) {
      var _this = this
      if (e.dn_status !== _this.$t('outbound.shippedstock')) {
        _this.$q.notify({
          message: e.dn_code + ' DN Status Is Not ' + _this.$t('outbound.shippedstock'),
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.podFormData.dn_code = e.dn_code
        _this.podFormData.customer = e.customer
        getauth(_this.pathname + 'detail/?dn_code=' + e.dn_code).then(res => {
          _this.podForm = true
          _this.podid = e.id
          _this.podFormData.goodsData = res.results
        })
      }
    },
    PODDataCancel () {
      var _this = this
      _this.podForm = false
      _this.podid = 0
      _this.podFormData = {
        dn_code: '',
        customer: '',
        goodsData: []
      }
    },
    PODDataSubmit () {
      var _this = this
      postauth(_this.pathname + 'pod/' + _this.podid + '/', _this.podFormData).then(res => {
        _this.table_list = []
        _this.PODDataCancel()
        _this.getList()
        if (!res.detail) {
          _this.$q.notify({
            message: 'Success Dispatch',
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
      _this.table_list = []
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
