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
              <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('newtip') }}</q-tooltip>
            </q-btn>
            <q-btn :label="$t('refresh')" icon="refresh" @click="reFresh()">
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
            <template v-if="props.row.id === editid">
              <q-td key="goods_code" :props="props">
                <q-input
                  dense
                  outlined
                  square
                  v-model="editFormData.goods_code"
                  :label="$t('goods.view_goodslist.goods_code')"
                  autofocus
                  :rules="[val => (val && val.length > 0) || error1]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_code" :props="props">{{ props.row.goods_code }}</q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_desc" :props="props">
                <q-input
                  dense
                  outlined
                  square
                  v-model="editFormData.goods_desc"
                  :label="$t('goods.view_goodslist.goods_desc')"
                  :rules="[val => (val && val.length > 0) || error2]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_desc" :props="props">{{ props.row.goods_desc }}</q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_supplier" :props="props">
                <q-select
                  dense
                  outlined
                  square
                  v-model="editFormData.goods_supplier"
                  :options="supplier_list"
                  transition-show="scale"
                  transition-hide="scale"
                  :label="$t('goods.view_goodslist.goods_supplier')"
                  :rules="[val => (val && val.length > 0) || error3]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_supplier" :props="props">{{ props.row.goods_supplier }}</q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_weight" :props="props">
                <q-input
                  dense
                  outlined
                  square
                  v-model.number="editFormData.goods_weight"
                  type="number"
                  :label="$t('goods.view_goodslist.goods_weight')"
                  :rules="[val => (val && val > 0) || error4]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_weight" :props="props">{{ props.row.goods_weight }}</q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_w" :props="props">
                <q-input
                  dense
                  outlined
                  square
                  v-model.number="editFormData.goods_w"
                  type="number"
                  :label="$t('goods.view_goodslist.goods_w')"
                  :rules="[val => (val && val > 0) || error5]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_w" :props="props">{{ props.row.goods_w }}</q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_d" :props="props">
                <q-input
                  dense
                  outlined
                  square
                  v-model.number="editFormData.goods_d"
                  type="number"
                  :label="$t('goods.view_goodslist.goods_d')"
                  :rules="[val => (val && val > 0) || error6]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_d" :props="props">{{ props.row.goods_d }}</q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_h" :props="props">
                <q-input
                  dense
                  outlined
                  square
                  v-model.number="editFormData.goods_h"
                  type="number"
                  :label="$t('goods.view_goodslist.goods_h')"
                  :rules="[val => (val && val > 0) || error7]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_h" :props="props">{{ props.row.goods_h }}</q-td>
            </template>
            <q-td key="unit_volume" :props="props">{{ props.row.unit_volume }}</q-td>
            <template v-if="props.row.id === editid">
              <q-td key="goods_unit" :props="props">
                <q-select
                  dense
                  outlined
                  square
                  v-model="editFormData.goods_unit"
                  :options="goods_unit_list"
                  transition-show="scale"
                  transition-hide="scale"
                  :label="$t('goods.view_goodslist.goods_unit')"
                  :rules="[val => (val && val.length > 0) || error8]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_unit" :props="props">{{ props.row.goods_unit }}</q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_class" :props="props">
                <q-select
                  dense
                  outlined
                  square
                  v-model="editFormData.goods_class"
                  :options="goods_class_list"
                  transition-show="scale"
                  transition-hide="scale"
                  :label="$t('goods.view_goodslist.goods_class')"
                  :rules="[val => (val && val.length > 0) || error9]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_class" :props="props">{{ props.row.goods_class }}</q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_brand" :props="props">
                <q-select
                  dense
                  outlined
                  square
                  v-model="editFormData.goods_brand"
                  :options="goods_brand_list"
                  transition-show="scale"
                  transition-hide="scale"
                  :label="$t('goods.view_goodslist.goods_brand')"
                  :rules="[val => (val && val.length > 0) || error10]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_brand" :props="props">{{ props.row.goods_brand }}</q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_color" :props="props">
                <q-select
                  dense
                  outlined
                  square
                  v-model="editFormData.goods_color"
                  :options="goods_color_list"
                  transition-show="scale"
                  transition-hide="scale"
                  :label="$t('goods.view_goodslist.goods_color')"
                  :rules="[val => (val && val.length > 0) || error11]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_color" :props="props">{{ props.row.goods_color }}</q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_shape" :props="props">
                <q-select
                  dense
                  outlined
                  square
                  v-model="editFormData.goods_shape"
                  :options="goods_shape_list"
                  transition-show="scale"
                  transition-hide="scale"
                  :label="$t('goods.view_goodslist.goods_shape')"
                  :rules="[val => (val && val.length > 0) || error12]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_shape" :props="props">{{ props.row.goods_shape }}</q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_specs" :props="props">
                <q-select
                  dense
                  outlined
                  square
                  v-model="editFormData.goods_specs"
                  :options="goods_specs_list"
                  transition-show="scale"
                  transition-hide="scale"
                  :label="$t('goods.view_goodslist.goods_specs')"
                  :rules="[val => (val && val.length > 0) || error13]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_specs" :props="props">{{ props.row.goods_specs }}</q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_origin" :props="props">
                <q-select
                  dense
                  outlined
                  square
                  v-model="editFormData.goods_origin"
                  :options="goods_origin_list"
                  transition-show="scale"
                  transition-hide="scale"
                  :label="$t('goods.view_goodslist.goods_origin')"
                  :rules="[val => (val && val.length > 0) || error14]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_origin" :props="props">{{ props.row.goods_origin }}</q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_cost" :props="props">
                <q-input
                  dense
                  outlined
                  square
                  v-model.number="editFormData.goods_cost"
                  type="number"
                  :label="$t('goods.view_goodslist.goods_cost')"
                  :rules="[val => (val && val > 0) || error15]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_cost" :props="props">{{ props.row.goods_cost }}</q-td>
            </template>
            <template v-if="props.row.id === editid">
              <q-td key="goods_price" :props="props">
                <q-input
                  dense
                  outlined
                  square
                  v-model.number="editFormData.goods_price"
                  type="number"
                  :label="$t('goods.view_goodslist.goods_price')"
                  :rules="[val => (val && val > 0) || error16]"
                />
              </q-td>
            </template>
            <template v-else-if="props.row.id !== editid">
              <q-td key="goods_price" :props="props">{{ props.row.goods_price }}</q-td>
            </template>
            <q-td key="creater" :props="props">{{ props.row.creater }}</q-td>
            <q-td key="create_time" :props="props">{{ props.row.create_time }}</q-td>
            <q-td key="update_time" :props="props">{{ props.row.update_time }}</q-td>
            <template v-if="!editMode">
              <q-td key="action" :props="props" style="width: 100px">
                <q-btn
                  round
                  flat
                  push
                  color="info"
                  icon="print"
                  @click="viewData(props.row)"
                >
                  <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                    {{ $t('goods.view_goodslist.print_goods_label') }}
                  </q-tooltip>
                </q-btn>
                <q-btn round flat push color="purple" icon="edit" @click="editData(props.row)">
                  <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('edit') }}</q-tooltip>
                </q-btn>
                <q-btn round flat push color="dark" icon="delete" @click="deleteData(props.row.id)">
                  <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('delete') }}</q-tooltip>
                </q-btn>
              </q-td>
            </template>
            <template v-else-if="editMode">
              <template v-if="props.row.id === editid">
                <q-td key="action" :props="props" style="width: 100px">
                  <q-btn round flat push color="secondary" icon="check" @click="editDataSubmit()">
                    <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('confirmedit') }}</q-tooltip>
                  </q-btn>
                  <q-btn round flat push color="red" icon="close" @click="editDataCancel()">
                    <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">{{ $t('canceledit') }}</q-tooltip>
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
          <div>{{ $t('newtip') }}</div>
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
            v-model="newFormData.goods_code"
            :label="$t('goods.view_goodslist.goods_code')"
            autofocus
            :rules="[val => (val && val.length > 0) || error1]"
            @keyup.enter="newDataSubmit()"
          />
          <q-input
            dense
            outlined
            square
            v-model="newFormData.goods_desc"
            :label="$t('goods.view_goodslist.goods_desc')"
            :rules="[val => (val && val.length > 0) || error2]"
            @keyup.enter="newDataSubmit()"
          />
          <q-select
            dense
            outlined
            square
            v-model="newFormData.goods_supplier"
            :options="supplier_list"
            transition-show="scale"
            transition-hide="scale"
            :label="$t('goods.view_goodslist.goods_supplier')"
            :rules="[val => (val && val.length > 0) || error3]"
            @keyup.enter="newDataSubmit()"
          />
          <q-input
            dense
            outlined
            square
            v-model.number="newFormData.goods_weight"
            type="number"
            :label="$t('goods.view_goodslist.goods_weight')"
            :rules="[val => (val && val > 0) || error4]"
            @keyup.enter="newDataSubmit()"
          />
          <q-input
            dense
            outlined
            square
            v-model.number="newFormData.goods_w"
            type="number"
            :label="$t('goods.view_goodslist.goods_w')"
            :rules="[val => (val && val > 0) || error5]"
            @keyup.enter="newDataSubmit()"
          />
          <q-input
            dense
            outlined
            square
            v-model.number="newFormData.goods_d"
            type="number"
            :label="$t('goods.view_goodslist.goods_d')"
            :rules="[val => (val && val > 0) || error6]"
            @keyup.enter="newDataSubmit()"
          />
          <q-input
            dense
            outlined
            square
            v-model.number="newFormData.goods_h"
            type="number"
            :label="$t('goods.view_goodslist.goods_h')"
            :rules="[val => (val && val > 0) || error7]"
            @keyup.enter="newDataSubmit()"
          />
          <q-select
            dense
            outlined
            square
            v-model="newFormData.goods_unit"
            :options="goods_unit_list"
            transition-show="scale"
            transition-hide="scale"
            :label="$t('goods.view_goodslist.goods_unit')"
            :rules="[val => (val && val.length > 0) || error8]"
            @keyup.enter="newDataSubmit()"
          />
          <q-select
            dense
            outlined
            square
            v-model="newFormData.goods_class"
            :options="goods_class_list"
            transition-show="scale"
            transition-hide="scale"
            :label="$t('goods.view_goodslist.goods_class')"
            :rules="[val => (val && val.length > 0) || error9]"
            @keyup.enter="newDataSubmit()"
          />
          <q-select
            dense
            outlined
            square
            v-model="newFormData.goods_brand"
            :options="goods_brand_list"
            transition-show="scale"
            transition-hide="scale"
            :label="$t('goods.view_goodslist.goods_brand')"
            :rules="[val => (val && val.length > 0) || error10]"
            @keyup.enter="newDataSubmit()"
          />
          <q-select
            dense
            outlined
            square
            v-model="newFormData.goods_color"
            :options="goods_color_list"
            transition-show="scale"
            transition-hide="scale"
            :label="$t('goods.view_goodslist.goods_color')"
            :rules="[val => (val && val.length > 0) || error11]"
            @keyup.enter="newDataSubmit()"
          />
          <q-select
            dense
            outlined
            square
            v-model="newFormData.goods_shape"
            :options="goods_shape_list"
            transition-show="scale"
            transition-hide="scale"
            :label="$t('goods.view_goodslist.goods_shape')"
            :rules="[val => (val && val.length > 0) || error12]"
            @keyup.enter="newDataSubmit()"
          />
          <q-select
            dense
            outlined
            square
            v-model="newFormData.goods_specs"
            :options="goods_specs_list"
            transition-show="scale"
            transition-hide="scale"
            :label="$t('goods.view_goodslist.goods_specs')"
            :rules="[val => (val && val.length > 0) || error13]"
            @keyup.enter="newDataSubmit()"
          />
          <q-select
            dense
            outlined
            square
            v-model="newFormData.goods_origin"
            :options="goods_origin_list"
            transition-show="scale"
            transition-hide="scale"
            :label="$t('goods.view_goodslist.goods_origin')"
            :rules="[val => (val && val.length > 0) || error14]"
            @keyup.enter="newDataSubmit()"
          />
          <q-input
            dense
            outlined
            square
            v-model.number="newFormData.goods_cost"
            type="number"
            :label="$t('goods.view_goodslist.goods_cost')"
            :rules="[val => (val && val > 0) || error15]"
            @keyup.enter="newDataSubmit()"
          />
          <q-input
            dense
            outlined
            square
            v-model.number="newFormData.goods_price"
            type="number"
            :label="$t('goods.view_goodslist.goods_price')"
            :rules="[val => (val && val > 0) || error16]"
            @keyup.enter="newDataSubmit()"
          />
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
        <q-card-section style="max-height: 325px; width: 400px" class="scroll">{{ $t('deletetip') }}</q-card-section>
        <div style="float: right; padding: 15px 15px 15px 0">
          <q-btn color="white" text-color="black" style="margin-right: 25px" @click="deleteDataCancel()">{{ $t('cancel') }}</q-btn>
          <q-btn color="primary" @click="deleteDataSubmit()">{{ $t('submit') }}</q-btn>
        </div>
      </q-card>
    </q-dialog>
    <q-dialog v-model="viewForm">
      <div id="printMe" style="width: 400px;height:280px;background-color: white">
        <q-card-section>
          <div class="row" style="height: 50px">
            <div class="col-3"><img src="statics/goods/logo.png" style="width: 60px;height: 50px;margin-top: 5px;margin-left: 5px" /></div>
            <div class="col-9" style="height: 50px;float: contour;margin-top: 10px">
              <p style="font-size: 20px;font-weight: 550">{{ $t('goods.view_goodslist.goods_code') + ':' + goods_code }}</p>
            </div>
          </div>
          <hr />
          <div class="row">
            <div class="col-8" style="margin-top: 30px;padding-left: 3%">
              <p style="font-size: 20px;font-weight: 550">{{ $t('goods.view_goodslist.goods_name') + ':' }}</p>
              <p style="font-size: 20px;font-weight: 550">{{ goods_desc }}</p>
            </div>
            <div class="col-4" style="margin-top: 25px;"><img :src="bar_code" style="width: 70%;margin-left: 23px" /></div>
          </div>
        </q-card-section>
      </div>
      <div style="float: right; padding: 15px 15px 15px 0"><q-btn color="primary" icon="print" v-print="printObj">print</q-btn></div>
    </q-dialog>
  </div>
</template>
<router-view />

<script>
import { getauth, postauth, putauth, deleteauth } from 'boot/axios_request'
import { LocalStorage } from 'quasar'

export default {
  name: 'Pagegoodslist',
  data () {
    return {
      goods_code: '',
      goods_desc: '',
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'goods/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      viewForm: false,
      printObj: {
        id: 'printMe',
        popTitle: this.$t('inbound.asn')
      },
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
        { name: 'goods_code', required: true, label: this.$t('goods.view_goodslist.goods_code'), align: 'left', field: 'goods_code' },
        { name: 'goods_desc', label: this.$t('goods.view_goodslist.goods_desc'), field: 'goods_desc', align: 'center' },
        { name: 'goods_supplier', label: this.$t('goods.view_goodslist.goods_supplier'), field: 'goods_supplier', align: 'center' },
        { name: 'goods_weight', label: this.$t('goods.view_goodslist.goods_weight'), field: 'goods_weight', align: 'center' },
        { name: 'goods_w', label: this.$t('goods.view_goodslist.goods_w'), field: 'goods_w', align: 'center' },
        { name: 'goods_d', label: this.$t('goods.view_goodslist.goods_d'), field: 'goods_d', align: 'center' },
        { name: 'goods_h', label: this.$t('goods.view_goodslist.goods_h'), field: 'goods_h', align: 'center' },
        { name: 'unit_volume', label: this.$t('goods.view_goodslist.unit_volume'), field: 'unit_volume', align: 'center' },
        { name: 'goods_unit', label: this.$t('goods.view_goodslist.goods_unit'), field: 'goods_unit', align: 'center' },
        { name: 'goods_class', label: this.$t('goods.view_goodslist.goods_class'), field: 'goods_class', align: 'center' },
        { name: 'goods_brand', label: this.$t('goods.view_goodslist.goods_brand'), field: 'goods_brand', align: 'center' },
        { name: 'goods_color', label: this.$t('goods.view_goodslist.goods_color'), field: 'goods_color', align: 'center' },
        { name: 'goods_shape', label: this.$t('goods.view_goodslist.goods_shape'), field: 'goods_shape', align: 'center' },
        { name: 'goods_specs', label: this.$t('goods.view_goodslist.goods_specs'), field: 'goods_specs', align: 'center' },
        { name: 'goods_origin', label: this.$t('goods.view_goodslist.goods_origin'), field: 'goods_origin', align: 'center' },
        { name: 'goods_cost', label: this.$t('goods.view_goodslist.goods_cost'), field: 'goods_cost', align: 'center' },
        { name: 'goods_price', label: this.$t('goods.view_goodslist.goods_price'), field: 'goods_price', align: 'center' },
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
      bar_code: '',
      error1: this.$t('goods.view_goodslist.error1'),
      error2: this.$t('goods.view_goodslist.error2'),
      error3: this.$t('goods.view_goodslist.error3'),
      error4: this.$t('goods.view_goodslist.error4'),
      error5: this.$t('goods.view_goodslist.error5'),
      error6: this.$t('goods.view_goodslist.error6'),
      error7: this.$t('goods.view_goodslist.error7'),
      error8: this.$t('goods.view_unit.error1'),
      error9: this.$t('goods.view_class.error1'),
      error10: this.$t('goods.view_brand.error1'),
      error11: this.$t('goods.view_color.error1'),
      error12: this.$t('goods.view_shape.error1'),
      error13: this.$t('goods.view_specs.error1'),
      error14: this.$t('goods.view_origin.error1'),
      error15: this.$t('goods.view_goodslist.error8'),
      error16: this.$t('goods.view_goodslist.error9'),
      current: 1,
      max: 0,
      total: 0,
      paginationIpt: 1
    }
  },
  methods: {
    getList () {
      var _this = this
      getauth(_this.pathname + '?page=' + '' + _this.current, {})
        .then(res => {
          _this.table_list = res.results
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
          _this.goods_unit_list = res.goods_unit_list
          _this.goods_class_list = res.goods_class_list
          _this.goods_brand_list = res.goods_brand_list
          _this.goods_color_list = res.goods_color_list
          _this.goods_shape_list = res.goods_shape_list
          _this.goods_specs_list = res.goods_specs_list
          _this.goods_origin_list = res.goods_origin_list
          _this.supplier_list = res.supplier_list
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
    },
    changePageEnter (e) {
      if (Number(this.paginationIpt) < 1) {
        this.current = 1
        this.paginationIpt = 1
      } else if (Number(this.paginationIpt) > this.max) {
        this.current = this.max
        this.paginationIpt = this.max
      } else {
        this.current = Number(this.paginationIpt)
      }
      this.getList()
    },
    getSearchList () {
      var _this = this
      if (LocalStorage.has('auth')) {
        _this.current = 1
        _this.paginationIpt = 1
        getauth(_this.pathname + '?goods_desc__icontains=' + _this.filter + '&page=' + '' + _this.current, {})
          .then(res => {
            _this.table_list = res.results
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
            _this.goods_unit_list = res.goods_unit_list
            _this.goods_class_list = res.goods_class_list
            _this.goods_brand_list = res.goods_brand_list
            _this.goods_color_list = res.goods_color_list
            _this.goods_shape_list = res.goods_shape_list
            _this.goods_specs_list = res.goods_specs_list
            _this.goods_origin_list = res.goods_origin_list
            _this.supplier_list = res.supplier_list
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
      }
    },
    getListPrevious () {
      var _this = this
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname_previous, {})
          .then(res => {
            _this.table_list = res.results
            _this.goods_unit_list = res.goods_unit_list
            _this.goods_class_list = res.goods_class_list
            _this.goods_brand_list = res.goods_brand_list
            _this.goods_color_list = res.goods_color_list
            _this.goods_shape_list = res.goods_shape_list
            _this.goods_specs_list = res.goods_specs_list
            _this.goods_origin_list = res.goods_origin_list
            _this.supplier_list = res.supplier_list
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
            _this.table_list = res.results
            _this.goods_unit_list = res.goods_unit_list
            _this.goods_class_list = res.goods_class_list
            _this.goods_brand_list = res.goods_brand_list
            _this.goods_color_list = res.goods_color_list
            _this.goods_shape_list = res.goods_shape_list
            _this.goods_specs_list = res.goods_specs_list
            _this.goods_origin_list = res.goods_origin_list
            _this.supplier_list = res.supplier_list
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
      }
    },
    reFresh () {
      var _this = this
      _this.getList()
    },
    newDataSubmit () {
      var _this = this
      var goodscodes = []
      _this.table_list.forEach(i => {
        goodscodes.push(i.goods_code)
      })
      if (goodscodes.indexOf(_this.newFormData.goods_code) === -1 && _this.newFormData.goods_code.length !== 0) {
        _this.newFormData.creater = _this.login_name
        postauth(_this.pathname, _this.newFormData)
          .then(res => {
            _this.getList()
            _this.newDataCancel()
            if (res.status_code != 500) {
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
      } else if (goodscodes.indexOf(_this.newFormData.goods_code) !== -1) {
        _this.$q.notify({
          message: _this.$t('notice.goodserror.goods_listerror'),
          icon: 'close',
          color: 'negative'
        })
      } else if (_this.newFormData.goods_code.length === 0) {
        _this.$q.notify({
          message: _this.$t('goods.view_goodslist.error1'),
          icon: 'close',
          color: 'negative'
        })
      }
      goodscodes = []
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
        creater: _this.login_name,
        bar_code: e.bar_code
      }
    },
    editDataSubmit () {
      var _this = this
      putauth(_this.pathname + _this.editid + '/', _this.editFormData)
        .then(res => {
          _this.editDataCancel()
          _this.getList()
          if (res.status_code != 500) {
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
      deleteauth(_this.pathname + _this.deleteid + '/')
        .then(res => {
          _this.deleteDataCancel()
          _this.getList()
          _this.$q.notify({
            message: 'Success Edit Data',
            icon: 'check',
            color: 'green'
          })
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
    viewData (e) {
      var _this = this
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
          _this.goods_code = e.goods_code
          _this.goods_desc = e.goods_desc
          _this.bar_code = url
        })
        .catch(err => {
          console.error(err)
        })
      _this.viewForm = true
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
  updated () {},
  destroyed () {}
}
</script>
