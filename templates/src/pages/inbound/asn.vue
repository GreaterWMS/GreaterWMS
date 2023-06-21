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
            <q-btn
              :label="$t('new')"
              icon="add"
              @click="newFormOpen()"
            >
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('newtip') }}</q-tooltip>
            </q-btn>
            <q-btn
              v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' && $q.localStorage.getItem('staff_type') !== 'Customer'"
              :label="$t('refresh')"
              icon="refresh"
              @click="reFresh()"
            >
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('refreshtip') }}</q-tooltip>
            </q-btn>
          </q-btn-group>
          <q-space />
          <q-input outlined rounded dense debounce="300" color="primary" v-model="filter" :placeholder="$t('search')" @input="getSearchList()" @keyup.enter="getSearchList()">
            <template v-slot:append>
              <q-icon name="search" @click="getSearchList()" />
            </template>
          </q-input>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td key="asn_code" :props="props">{{ props.row.asn_code }}</q-td>
            <q-td key="asn_status" :props="props">{{ props.row.asn_status }}</q-td>
            <q-td key="total_weight" :props="props">{{ props.row.total_weight.toFixed(4) }}</q-td>
            <q-td key="total_volume" :props="props">{{ props.row.total_volume.toFixed(4) }}</q-td>
            <q-td key="supplier" :props="props">{{ props.row.supplier }}</q-td>
            <q-td key="creater" :props="props">{{ props.row.creater }}</q-td>
            <q-td key="create_time" :props="props">{{ props.row.create_time }}</q-td>
            <q-td key="update_time" :props="props">{{ props.row.update_time }}</q-td>
            <q-td key="action" :props="props" style="width: 100px">
              <q-btn
                round
                flat
                push
                color="info"
                icon="visibility"
                @click="viewData(props.row)"
              >
                <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('printthisasn') }}</q-tooltip>
              </q-btn>
              <q-btn
                round
                flat
                push
                color="positive"
                icon="img:statics/inbound/preloadstock.png"
                @click="preloadData(props.row)"
              >
                <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('confirmdelivery') }}</q-tooltip>
              </q-btn>
              <q-btn
                round
                flat
                push
                color="positive"
                icon="img:statics/inbound/presortstock.png"
                @click="presortData(props.row)"
              >
                <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('finishloading') }}</q-tooltip>
              </q-btn>
              <q-btn
                round
                flat
                push
                color="purple"
                icon="img:statics/inbound/sortstock.png"
                @click="sortedData(props.row)"
              >
                <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('confirmsorted') }}</q-tooltip>
              </q-btn>
              <q-btn
                round
                flat
                push
                color="purple"
                icon="edit"
                @click="editData(props.row)"
              >
                <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('edit') }}</q-tooltip>
              </q-btn>
              <q-btn
                round
                flat
                push
                color="dark"
                icon="delete"
                @click="deleteData(props.row)"
              >
                <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('delete') }}</q-tooltip>
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
        <div v-show="max !== 0" class="q-pa-lg flex flex-center">
           <div>{{ total }} </div>
          <q-pagination
            v-model="current"
            color="black"
            :max="max"
            :max-pages="6"
            boundary-links
            @click="getList()"
          />
          <div>
            <input
              v-model="paginationIpt"
              @blur="changePageEnter"
              @keyup.enter="changePageEnter"
              style="width: 60px; text-align: center"
            />
          </div>
        </div>
        <div v-show="max === 0" class="q-pa-lg flex flex-center">
          <q-btn flat push color="dark" :label="$t('no_data')"></q-btn>
        </div>
    </template>
    <q-dialog v-model="newForm">
      <q-card class="shadow-24">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <div>{{ newFormData.asn_code }}</div>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-amber text-black shadow-4">{{ $t('index.close') }}</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section style="max-height: 325px; width: 400px" class="scroll">
          <q-select
            filled
            use-input
            fill-input
            hide-selected
            input-debounce="0"
            dense
            outlined
            square
            v-model="newFormData.supplier"
            :options="supplier_list"
            @filter="filterFnS"
            @input-value="setModel"
            :label="$t('baseinfo.view_supplier.supplier_name')"
            style="margin-bottom: 5px"
            :rules="[val => (val && val.length > 0) || error1]"
            @keyup.enter="isEdit ? editDataSubmit() : newDataSubmit()"
          >
            <template v-slot:Sno-option>
              <q-item>
                <q-item-section class="text-grey">
                  No Result
                </q-item-section>
              </q-item>
            </template>
          </q-select>
          <q-input
            dense
            outlined
            square
            debounce="500"
            v-model.number="goodsData1.qty"
            type="number"
            :label="$t('stock.view_stocklist.goods_qty')"
            style="margin-bottom: 5px"
            @keyup.enter="isEdit ? editDataSubmit() : newDataSubmit()"
          >
            <template v-slot:before>
              <q-select
                ref="one"
                dense
                outlined
                square
                use-input
                hide-selected
                fill-input
                v-model="goodsData1.code"
                :label="$t('goods.view_goodslist.goods_code')"
                :options="options"
                @focus="getFocus(1)"
                @input-value="setOptions"
                @filter="filterFn"
                autofocus
                @keyup.enter="isEdit ? editDataSubmit() : newDataSubmit()"
              >
                <template v-slot:no-option>
                  <q-item><q-item-section class="text-grey">No results</q-item-section></q-item>
                </template>
                <template v-if="goodsData1.code" v-slot:append>
                  <q-icon name="cancel" @click.stop="goodsData1.code = ''" class="cursor-pointer" />
                </template>
              </q-select>
            </template>
          </q-input>
          <q-input
            dense
            outlined
            square
            debounce="500"
            v-model.number="goodsData2.qty"
            type="number"
            :label="$t('stock.view_stocklist.goods_qty')"
            style="margin-bottom: 5px"
            @keyup.enter="isEdit ? editDataSubmit() : newDataSubmit()"
          >
            <template v-slot:before>
              <q-select
                dense
                outlined
                square
                use-input
                hide-selected
                fill-input
                v-model="goodsData2.code"
                :label="$t('goods.view_goodslist.goods_code')"
                :options="options"
                @focus="getFocus(2)"
                @input-value="setOptions"
                @filter="filterFn"
                @keyup.enter="isEdit ? editDataSubmit() : newDataSubmit()"
              >
                <template v-slot:no-option>
                  <q-item><q-item-section class="text-grey">No results</q-item-section></q-item>
                </template>
                <template v-if="goodsData2.code" v-slot:append>
                  <q-icon name="cancel" @click.stop="goodsData2.code = ''" class="cursor-pointer" />
                </template>
              </q-select>
            </template>
          </q-input>
          <q-input
            dense
            outlined
            square
            debounce="500"
            v-model.number="goodsData3.qty"
            type="number"
            :label="$t('stock.view_stocklist.goods_qty')"
            style="margin-bottom: 5px"
            @keyup.enter="isEdit ? editDataSubmit() : newDataSubmit()"
          >
            <template v-slot:before>
              <q-select
                dense
                outlined
                square
                use-input
                hide-selected
                fill-input
                v-model="goodsData3.code"
                :label="$t('goods.view_goodslist.goods_code')"
                :options="options"
                @focus="getFocus(3)"
                @input-value="setOptions"
                @filter="filterFn"
                @keyup.enter="isEdit ? editDataSubmit() : newDataSubmit()"
              >
                <template v-slot:no-option>
                  <q-item><q-item-section class="text-grey">No results</q-item-section></q-item>
                </template>
                <template v-if="goodsData3.code" v-slot:append>
                  <q-icon name="cancel" @click.stop="goodsData3.code = ''" class="cursor-pointer" />
                </template>
              </q-select>
            </template>
          </q-input>
          <q-input
            dense
            outlined
            square
            debounce="500"
            v-model.number="goodsData4.qty"
            type="number"
            :label="$t('stock.view_stocklist.goods_qty')"
            style="margin-bottom: 5px"
            @keyup.enter="isEdit ? editDataSubmit() : newDataSubmit()"
          >
            <template v-slot:before>
              <q-select
                dense
                outlined
                square
                use-input
                hide-selected
                fill-input
                v-model="goodsData4.code"
                :label="$t('goods.view_goodslist.goods_code')"
                :options="options"
                @focus="getFocus(4)"
                @input-value="setOptions"
                @filter="filterFn"
                @keyup.enter="isEdit ? editDataSubmit() : newDataSubmit()"
              >
                <template v-slot:no-option>
                  <q-item><q-item-section class="text-grey">No results</q-item-section></q-item>
                </template>
                <template v-if="goodsData4.code" v-slot:append>
                  <q-icon name="cancel" @click.stop="goodsData4.code = ''" class="cursor-pointer" />
                </template>
              </q-select>
            </template>
          </q-input>
          <q-input
            dense
            outlined
            square
            debounce="500"
            v-model.number="goodsData5.qty"
            type="number"
            :label="$t('stock.view_stocklist.goods_qty')"
            style="margin-bottom: 5px"
            @keyup.enter="isEdit ? editDataSubmit() : newDataSubmit()"
          >
            <template v-slot:before>
              <q-select
                dense
                outlined
                square
                use-input
                hide-selected
                fill-input
                v-model="goodsData5.code"
                :label="$t('goods.view_goodslist.goods_code')"
                :options="options"
                @focus="getFocus(5)"
                @input-value="setOptions"
                @filter="filterFn"
                @keyup.enter="isEdit ? editDataSubmit() : newDataSubmit()"
              >
                <template v-slot:no-option>
                  <q-item><q-item-section class="text-grey">No results</q-item-section></q-item>
                </template>
                <template v-if="goodsData5.code" v-slot:append>
                  <q-icon name="cancel" @click.stop="goodsData5.code = ''" class="cursor-pointer" />
                </template>
              </q-select>
            </template>
          </q-input>
          <q-input
            dense
            outlined
            square
            debounce="500"
            v-model.number="goodsData6.qty"
            type="number"
            :label="$t('stock.view_stocklist.goods_qty')"
            style="margin-bottom: 5px"
            @keyup.enter="isEdit ? editDataSubmit() : newDataSubmit()"
          >
            <template v-slot:before>
              <q-select
                dense
                outlined
                square
                use-input
                hide-selected
                fill-input
                v-model="goodsData6.code"
                :label="$t('goods.view_goodslist.goods_code')"
                :options="options"
                @focus="getFocus(6)"
                @input-value="setOptions"
                @filter="filterFn"
                @keyup.enter="isEdit ? editDataSubmit() : newDataSubmit()"
              >
                <template v-slot:no-option>
                  <q-item><q-item-section class="text-grey">No results</q-item-section></q-item>
                </template>
                <template v-if="goodsData6.code" v-slot:append>
                  <q-icon name="cancel" @click.stop="goodsData6.code = ''" class="cursor-pointer" />
                </template>
              </q-select>
            </template>
          </q-input>
          <q-input
            dense
            outlined
            square
            debounce="500"
            v-model.number="goodsData7.qty"
            type="number"
            :label="$t('stock.view_stocklist.goods_qty')"
            style="margin-bottom: 5px"
            @keyup.enter="isEdit ? editDataSubmit() : newDataSubmit()"
          >
            <template v-slot:before>
              <q-select
                dense
                outlined
                square
                use-input
                hide-selected
                fill-input
                v-model="goodsData7.code"
                :label="$t('goods.view_goodslist.goods_code')"
                :options="options"
                @focus="getFocus(7)"
                @input-value="setOptions"
                @filter="filterFn"
                @keyup.enter="isEdit ? editDataSubmit() : newDataSubmit()"
              >
                <template v-slot:no-option>
                  <q-item><q-item-section class="text-grey">No results</q-item-section></q-item>
                </template>
                <template v-if="goodsData7.code" v-slot:append>
                  <q-icon name="cancel" @click.stop="goodsData7.code = ''" class="cursor-pointer" />
                </template>
              </q-select>
            </template>
          </q-input>
          <q-input
            dense
            outlined
            square
            debounce="500"
            v-model.number="goodsData8.qty"
            type="number"
            :label="$t('stock.view_stocklist.goods_qty')"
            style="margin-bottom: 5px"
            @keyup.enter="isEdit ? editDataSubmit() : newDataSubmit()"
          >
            <template v-slot:before>
              <q-select
                dense
                outlined
                square
                use-input
                hide-selected
                fill-input
                v-model="goodsData8.code"
                :label="$t('goods.view_goodslist.goods_code')"
                :options="options"
                @focus="getFocus(8)"
                @input-value="setOptions"
                @filter="filterFn"
                @keyup.enter="isEdit ? editDataSubmit() : newDataSubmit()"
              >
                <template v-slot:no-option>
                  <q-item><q-item-section class="text-grey">No results</q-item-section></q-item>
                </template>
                <template v-if="goodsData8.code" v-slot:append>
                  <q-icon name="cancel" @click.stop="goodsData8.code = ''" class="cursor-pointer" />
                </template>
              </q-select>
            </template>
          </q-input>
          <q-input
            dense
            outlined
            square
            debounce="500"
            v-model.number="goodsData9.qty"
            type="number"
            :label="$t('stock.view_stocklist.goods_qty')"
            style="margin-bottom: 5px"
            @keyup.enter="isEdit ? editDataSubmit() : newDataSubmit()"
          >
            <template v-slot:before>
              <q-select
                dense
                outlined
                square
                use-input
                hide-selected
                fill-input
                v-model="goodsData9.code"
                :label="$t('goods.view_goodslist.goods_code')"
                :options="options"
                @focus="getFocus(9)"
                @input-value="setOptions"
                @filter="filterFn"
                @keyup.enter="isEdit ? editDataSubmit() : newDataSubmit()"
              >
                <template v-slot:no-option>
                  <q-item><q-item-section class="text-grey">No results</q-item-section></q-item>
                </template>
                <template v-if="goodsData9.code" v-slot:append>
                  <q-icon name="cancel" @click.stop="goodsData9.code = ''" class="cursor-pointer" />
                </template>
              </q-select>
            </template>
          </q-input>
          <q-input
            dense
            outlined
            square
            debounce="500"
            v-model.number="goodsData10.qty"
            type="number"
            :label="$t('stock.view_stocklist.goods_qty')"
            style="margin-bottom: 5px"
            @keyup.enter="isEdit ? editDataSubmit() : newDataSubmit()"
          >
            <template v-slot:before>
              <q-select
                dense
                outlined
                square
                use-input
                hide-selected
                fill-input
                v-model="goodsData10.code"
                :label="$t('goods.view_goodslist.goods_code')"
                :options="options"
                @focus="getFocus(10)"
                @input-value="setOptions"
                @filter="filterFn"
                @keyup.enter="isEdit ? editDataSubmit() : newDataSubmit()"
              >
                <template v-slot:no-option>
                  <q-item><q-item-section class="text-grey">No results</q-item-section></q-item>
                </template>
                <template v-if="goodsData10.code" v-slot:append>
                  <q-icon name="cancel" @click.stop="goodsData10.code = ''" class="cursor-pointer" />
                </template>
              </q-select>
            </template>
          </q-input>
        </q-card-section>
        <div style="float: right; padding: 15px 15px 15px 0">
          <q-btn color="white" text-color="black" style="margin-right: 25px" @click="isEdit ? editDataCancel() : newDataCancel()">{{ $t('cancel') }}</q-btn>
          <q-btn color="primary" @click="isEdit ? editDataSubmit() : newDataSubmit()">{{ $t('submit') }}</q-btn>
        </div>
      </q-card>
    </q-dialog>
    <q-dialog v-model="deleteForm">
      <q-card class="shadow-24">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <div>{{ $t('delete') }}</div>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-amber text-black shadow-4">{{ $t('index.close') }}</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section style="max-height: 325px; width: 400px" class="scroll">{{ $t('deletetip') }}</q-card-section>
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
            <q-tooltip content-class="bg-amber text-black shadow-4">{{ $t('index.close') }}</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section style="max-height: 325px; width: 400px" class="scroll">{{ $t('deletetip') }}</q-card-section>
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
            <q-tooltip content-class="bg-amber text-black shadow-4">{{ $t('index.close') }}</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section style="max-height: 325px; width: 400px" class="scroll">{{ $t('deletetip') }}</q-card-section>
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
          {{ $t('inbound.asn') }}
        </q-bar>
        <q-card-section>
          <div class="row">
            <div class="col-8">
              <div class="text-h6">Sender: {{ supplier_detail.supplier_name }}</div>
              <div class="text-subtitle2">Address: {{ supplier_detail.supplier_city }}{{ supplier_detail.supplier_address }}</div>
              <div class="text-subtitle2">Tel: {{ supplier_detail.supplier_contact }}</div>
              <div class="text-h6">Receiver: {{ warehouse_detail.warehouse_name }}</div>
              <div class="text-subtitle2">Address: {{ warehouse_detail.warehouse_city }}{{ warehouse_detail.warehouse_address }}</div>
              <div class="text-subtitle2">Tel: {{ warehouse_detail.warehouse_contact }}</div>
            </div>
            <div class="col-4"><img :src="bar_code" style="width: 70%; margin-left: 15%" /></div>
          </div>
        </q-card-section>
        <q-markup-table>
          <thead>
            <tr>
              <th class="text-left">{{ $t('goods.view_goodslist.goods_code') }}</th>
              <th class="text-right">{{ $t('stock.view_stocklist.goods_qty') }}</th>
              <th class="text-right">{{ $t('inbound.view_asn.total_weight') }}</th>
              <th class="text-right">{{ $t('inbound.view_asn.total_volume') }}</th>
              <th class="text-right">{{ $t('inbound.view_asn.goods_actual_qty') }}</th>
              <th class="text-right">Comments</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(view, index) in viewprint_table" :key="index">
              <td class="text-left">{{ view.goods_code }}</td>
              <td class="text-right">{{ view.goods_qty }}</td>
              <td class="text-right">{{ view.goods_weight }}</td>
              <td class="text-right">{{ view.goods_volume }}</td>
              <td class="text-right">{{ view.goods_actual_qty }}</td>
              <td class="text-right"></td>
            </tr>
          </tbody>
        </q-markup-table>
      </q-card>
      <div style="float: right; padding: 15px 15px 15px 0"><q-btn color="primary" icon="print" v-print="printObj">print</q-btn></div>
    </q-dialog>
    <q-dialog v-model="sortedForm">
      <q-card class="shadow-24">
        <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
          <div>{{ sorted_list.asn_code }}</div>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-amber text-black shadow-4">{{ $t('index.close') }}</q-tooltip>
          </q-btn>
        </q-bar>
        <q-card-section style="max-height: 325px; width: 400px" class="scroll">
          <q-input
            dense
            outlined
            square
            debounce="500"
            disable
            readonly
            v-model="sorted_list.supplier"
            :label="$t('baseinfo.view_supplier.supplier_name')"
            style="margin-bottom: 5px"
          />
          <div v-for="(item, index) in sorted_list.goodsData" :key="index">
            <q-input dense outlined square bottom-slots type="number" v-model="item.goods_actual_qty" :label="$t('inbound.view_asn.goods_actual_qty')">
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
import { getauth, postauth, putauth, deleteauth, ViewPrintAuth } from 'boot/axios_request'
import { SessionStorage, LocalStorage } from 'quasar'

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
      bar_code: '',
      warehouse_detail: {},
      supplier_list: [],
      supplier_list1: [],
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
      options1: [],
      isEdit: false,
      listNumber: '',
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
        popTitle: this.$t('inbound.asn')
      },
      devi: window.device,
      error1: this.$t('baseinfo.view_supplier.error1'),
      goodsListData: [],
      current: 1,
      max: 0,
      total: 0,
      paginationIpt: 1
    }
  },
  methods: {
    getList () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname + 'list/' + '?page=' + '' + _this.current, {})
          .then(res => {
            _this.table_list = []
            _this.total = res.count
            if (res.count === 0) {
              _this.max = 0
            } else {
              if (Math.ceil(res.count / 30) === 1) {
                _this.max = 0
              } else {
                _this.max = Math.ceil(res.count / 30)
              }
            }
            res.results.forEach(item => {
              if (item.asn_status === 1) {
                item.asn_status = _this.$t('inbound.predeliverystock')
              } else if (item.asn_status === 2) {
                item.asn_status = _this.$t('inbound.preloadstock')
              } else if (item.asn_status === 3) {
                item.asn_status = _this.$t('inbound.presortstock')
              } else if (item.asn_status === 4) {
                item.asn_status = _this.$t('inbound.sortstock')
              } else if (item.asn_status === 5) {
                item.asn_status = _this.$t('inbound.asndone')
              } else {
                item.asn_status = 'N/A'
              }
              _this.table_list.push(item)
            })
            _this.supplier_list = res.supplier_list
            _this.supplier_list1 = res.supplier_list
            _this.pathname_previous = res.previous
            _this.pathname_next = res.next
            _this.goodsListData = res.results
          })
          .catch(err => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            })
          })
      }
    },
    changePageEnter(e) {
      if (Number(this.paginationIpt) < 1) {
        this.current = 1;
        this.paginationIpt = 1;
      } else if (Number(this.paginationIpt) > this.max) {
        this.current = this.max;
        this.paginationIpt = this.max;
      } else {
        this.current = Number(this.paginationIpt);
      }
      this.getList();
    },
    getSearchList () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname + 'list/?asn_code__icontains=' + _this.filter + '&page=' + '' + _this.current, {})
          .then(res => {
            _this.table_list = []
            _this.total = res.count
            if (res.count === 0) {
              _this.max = 0
            } else {
              if (Math.ceil(res.count / 30) === 1) {
                _this.max = 0
              } else {
                _this.max = Math.ceil(res.count / 30)
              }
            }
            res.results.forEach(item => {
              if (item.asn_status === 1) {
                item.asn_status = _this.$t('inbound.predeliverystock')
              } else if (item.asn_status === 2) {
                item.asn_status = _this.$t('inbound.preloadstock')
              } else if (item.asn_status === 3) {
                item.asn_status = _this.$t('inbound.presortstock')
              } else if (item.asn_status === 4) {
                item.asn_status = _this.$t('inbound.sortstock')
              } else if (item.asn_status === 5) {
                item.asn_status = _this.$t('inbound.asndone')
              } else {
                item.asn_status = 'N/A'
              }
              _this.table_list.push(item)
            })
            _this.supplier_list = res.supplier_list
            _this.supplier_list1 = res.supplier_list
            _this.pathname_previous = res.previous
            _this.pathname_next = res.next
          })
          .catch(err => {
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
        getauth(_this.pathname_previous, {})
          .then(res => {
            _this.table_list = []
            res.results.forEach(item => {
              if (item.asn_status === 1) {
                item.asn_status = _this.$t('inbound.predeliverystock')
              } else if (item.asn_status === 2) {
                item.asn_status = _this.$t('inbound.preloadstock')
              } else if (item.asn_status === 3) {
                item.asn_status = _this.$t('inbound.presortstock')
              } else if (item.asn_status === 4) {
                item.asn_status = _this.$t('inbound.sortstock')
              } else if (item.asn_status === 5) {
                item.asn_status = _this.$t('inbound.asndone')
              } else {
                item.asn_status = 'N/A'
              }
              _this.table_list.push(item)
            })
            _this.supplier_list = res.supplier_list
            _this.supplier_list1 = res.supplier_list
            _this.pathname_previous = res.previous
            _this.pathname_next = res.next
          })
          .catch(err => {
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
        getauth(_this.pathname_next, {})
          .then(res => {
            _this.table_list = []
            res.results.forEach(item => {
              if (item.asn_status === 1) {
                item.asn_status = _this.$t('inbound.predeliverystock')
              } else if (item.asn_status === 2) {
                item.asn_status = _this.$t('inbound.preloadstock')
              } else if (item.asn_status === 3) {
                item.asn_status = _this.$t('inbound.presortstock')
              } else if (item.asn_status === 4) {
                item.asn_status = _this.$t('inbound.sortstock')
              } else if (item.asn_status === 5) {
                item.asn_status = _this.$t('inbound.asndone')
              } else {
                item.asn_status = 'N/A'
              }
              _this.table_list.push(item)
            })
            _this.supplier_list = res.supplier_list
            _this.supplier_list1 = res.supplier_list
            _this.pathname_previous = res.previous
            _this.pathname_next = res.next
          })
          .catch(err => {
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
      _this.isEdit = false
      _this.goodsDataClear()
      _this.newForm = true
      _this.newAsn.creater = _this.login_name
      postauth(_this.pathname + 'list/', _this.newAsn)
        .then(res => {
          if (!res.detail) {
            _this.newFormData.asn_code = res.asn_code
          }
        })
        .catch(err => {
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
      let cancelRequest = false
      if (_this.newFormData.supplier !== '') {
        _this.newFormData.goods_code = []
        _this.newFormData.goods_qty = []
        let goodsDataCheck = 0
        for (let i = 0; i < 10; i++) {
          const goodsData = `goodsData${i + 1}`
          if (_this[goodsData].code !== '' && _this[goodsData].qty !== '') {
            if (_this[goodsData].qty < 1) {
              cancelRequest = true
              _this.$q.notify({
                message: 'Total Quantity Must Be > 0',
                icon: 'close',
                color: 'negative'
              })
            } else {
              _this.newFormData.goods_code.push(_this[goodsData].code)
              _this.newFormData.goods_qty.push(_this[goodsData].qty)
            }
            goodsDataCheck += 1
          }
        }
        if (goodsDataCheck === 0) {
          cancelRequest = true
          _this.$q.notify({
            message: 'Please Enter The Goods & Qty',
            icon: 'close',
            color: 'negative'
          })
        }
      } else {
        cancelRequest = true
        _this.$q.notify({
          message: 'Please Enter The Supplier',
          icon: 'close',
          color: 'negative'
        })
      }
      if (!cancelRequest) {
        postauth(_this.pathname + 'detail/', _this.newFormData)
          .then(res => {
            _this.table_list = []
            _this.getList()
            _this.newDataCancel()
            if (res.detail === 'success') {
              _this.$q.notify({
                message: 'Success Create',
                icon: 'check',
                color: 'green'
              })
            }
          })
          .catch(err => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            })
          })
      }
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
      for (let i = 1; i <= 10; i++) {
        _this[`goodsData${i}`] = { code: '', qty: '' }
      }
    },
    editData (e) {
      var _this = this
      _this.isEdit = true
      _this.goodsDataClear()
      if (e.asn_status !== _this.$t('inbound.predeliverystock')) {
        _this.$q.notify({
          message: e.asn_code + ' ASN Status Is Not ' + _this.$t('inbound.predeliverystock'),
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.newFormData.asn_code = e.asn_code
        _this.newFormData.supplier = e.supplier
        getauth(_this.pathname + 'detail/?asn_code=' + e.asn_code).then(res => {
          _this.newForm = true
          _this.editid = e.id
          res.results.forEach((detail, index) => {
            _this[`goodsData${index + 1}`] = { code: detail.goods_code, qty: detail.goods_qty }
          })
        })
      }
    },
    editDataSubmit () {
      var _this = this
      _this.newFormData.creater = _this.login_name
      let cancelRequest = false
      if (_this.newFormData.supplier !== '') {
        _this.newFormData.goods_code = []
        _this.newFormData.goods_qty = []
        let goodsDataCheck = 0
        for (let i = 0; i < 10; i++) {
          const goodsData = `goodsData${i + 1}`
          if (_this[goodsData].code !== '' && _this[goodsData].qty !== '') {
            if (_this[goodsData].qty < 1) {
              cancelRequest = true
              _this.$q.notify({
                message: 'Total Quantity Must Be > 0',
                icon: 'close',
                color: 'negative'
              })
            } else {
              _this.newFormData.goods_code.push(_this[goodsData].code)
              _this.newFormData.goods_qty.push(_this[goodsData].qty)
            }
            goodsDataCheck += 1
          }
        }
        if (goodsDataCheck === 0) {
          cancelRequest = true
          _this.$q.notify({
            message: 'Please Enter The Goods & Qty',
            icon: 'close',
            color: 'negative'
          })
        }
      } else {
        cancelRequest = true
        _this.$q.notify({
          message: 'Please Enter The Supplier',
          icon: 'close',
          color: 'negative'
        })
      }
      if (!cancelRequest) {
        putauth(_this.pathname + 'detail/', _this.newFormData)
          .then(res => {
            _this.table_list = []
            _this.editDataCancel()
            _this.getList()
            if (res.detail === 'success') {
              _this.$q.notify({
                message: 'Success Edit Data',
                icon: 'check',
                color: 'green'
              })
            }
          })
          .catch(err => {
            _this.$q.notify({
              message: err.detail,
              icon: 'close',
              color: 'negative'
            })
          })
      }
    },
    editDataCancel () {
      var _this = this
      _this.newForm = false
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
      if (e.asn_status !== _this.$t('inbound.predeliverystock')) {
        _this.$q.notify({
          message: e.asn_code + ' ASN Status Is Not ' + _this.$t('inbound.predeliverystock'),
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
      deleteauth(_this.pathname + 'list/' + _this.deleteid + '/')
        .then(res => {
          _this.table_list = []
          _this.deleteDataCancel()
          _this.getList()
          if (!res.data) {
            _this.$q.notify({
              message: 'Success Delete Data',
              icon: 'check',
              color: 'green'
            })
          }
        })
        .catch(err => {
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
      if (e.asn_status !== _this.$t('inbound.predeliverystock')) {
        _this.$q.notify({
          message: e.asn_code + ' ASN Status Is Not ' + _this.$t('inbound.predeliverystock'),
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.preloadForm = true
        _this.preloadid = e.id
      }
    },
    preloadDataSubmit () {
      var _this = this
      postauth(_this.pathname + 'preload/' + _this.preloadid + '/', {})
        .then(res => {
          _this.table_list = []
          _this.preloadDataCancel()
          _this.getList()
          if (!res.detail) {
            _this.$q.notify({
              message: 'Success Confirm ASN Delivery',
              icon: 'check',
              color: 'green'
            })
          }
        })
        .catch(err => {
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
      if (e.asn_status !== _this.$t('inbound.preloadstock')) {
        _this.$q.notify({
          message: e.asn_code + ' ASN Status Is Not ' + _this.$t('inbound.preloadstock'),
          icon: 'close',
          color: 'negative'
        })
      } else {
        _this.presortForm = true
        _this.presortid = e.id
      }
    },
    presortDataSubmit () {
      var _this = this
      postauth(_this.pathname + 'presort/' + _this.presortid + '/', {})
        .then(res => {
          _this.table_list = []
          _this.presortDataCancel()
          _this.getList()
          if (!res.detail) {
            _this.$q.notify({
              message: 'Success Load ASN',
              icon: 'check',
              color: 'green'
            })
          }
        })
        .catch(err => {
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
    getFocus (number) {
      this.listNumber = number
    },
    setOptions (val) {
      const _this = this
      if (!val) {
        this[`goodsData${this.listNumber}`].code = ''
      }
      const needle = val.toLowerCase()
      getauth('goods/?goods_code__icontains=' + needle).then(res => {
        const goodscodelist = []
        for (let i = 0; i < res.results.length; i++) {
          goodscodelist.push(res.results[i].goods_code)
          if (this.listNumber) {
            if (res.results[i].goods_code === val) {
              this[`goodsData${this.listNumber}`].code = val
            }
          }
        }
        _this.options1 = goodscodelist
      })
    },
    filterFn (val, update, abort) {
      if (val.length < 1) {
        abort()
        return
      }
      update(() => {
        this.options = this.options1
      })
    },
    setModel (val) {
      const _this = this
      _this.newFormData.supplier = val
    },
    filterFnS (val, update, abort) {
      var _this = this
      update(() => {
        const needle = val.toLocaleLowerCase()
        const data_filter = _this.supplier_list1
        _this.supplier_list = data_filter.filter(v => v.toLocaleLowerCase().indexOf(needle) > -1)
      })
    },
    sortedData (e) {
      var _this = this
      _this.goodsDataClear()
      if (e.asn_status !== _this.$t('inbound.presortstock')) {
        _this.$q.notify({
          message: e.asn_code + ' ASN Status Is Not ' + _this.$t('inbound.presortstock'),
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
      postauth(_this.pathname + 'sorted/' + _this.sortedid + '/', _this.sorted_list)
        .then(res => {
          _this.table_list = []
          _this.sortedDataCancel()
          _this.getList()
          if (!res.data) {
            _this.$q.notify({
              message: 'Success Sorted ASN',
              icon: 'check',
              color: 'green'
            })
          }
        })
        .catch(err => {
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
        var QRCode = require('qrcode')
        QRCode.toDataURL(e.bar_code, [
          {
            errorCorrectionLevel: 'H',
            mode: 'byte',
            version: '2',
            type: 'image/jpeg'
          }
        ])
          .then(url => {
            _this.bar_code = url
          })
          .catch(err => {
            console.error(err)
          })
        _this.viewForm = true
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
    if (SessionStorage.has('goods_code')) {
    } else {
      SessionStorage.set('goods_code', [])
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
  updated () {},
  destroyed () {}
}
</script>
