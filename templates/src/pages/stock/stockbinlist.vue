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
             <q-td key="bin_name" :props="props">
               {{ props.row.bin_name }}
             </q-td>
             <q-td key="goods_code" :props="props">
               {{ props.row.goods_code }}
             </q-td>
             <q-td key="goods_desc" :props="props">
               {{ props.row.goods_desc }}
             </q-td>
             <q-td key="goods_qty" :props="props">
               {{ props.row.goods_qty }}
             </q-td>
             <q-td key="pick_qty" :props="props">
               {{ props.row.pick_qty }}
             </q-td>
             <q-td key="picked_qty" :props="props">
               {{ props.row.picked_qty }}
             </q-td>
             <q-td key="bin_size" :props="props">
               {{ props.row.bin_size }}
             </q-td>
             <q-td key="bin_property" :props="props">
               {{ props.row.bin_property }}
             </q-td>
             <q-td key="create_time" :props="props">
               {{ props.row.create_time }}
             </q-td>
             <q-td key="update_time" :props="props">
               {{ props.row.update_time }}
             </q-td>
             <q-td key="action" :props="props">
               <q-btn round flat push color="purple" icon="move_to_inbox" @click="BinMove(props.row)">
                 <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
                  Move goods to another Bin
                </q-tooltip>
               </q-btn>
             </q-td>
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
      <q-dialog v-model="moveForm">
       <q-card class="shadow-24">
         <q-bar class="bg-light-blue-10 text-white rounded-borders" style="height: 50px">
           <div>{{ movedata.goods_code }} From Bin {{ movedata.bin_name }}</div>
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
                    v-model.number="movedata.move_qty"
                    type="number"
                    label="Goods QTY"
                    style="margin-bottom: 5px"
                    :rules="[ val => val && val > 0 || 'Please Enter the Qty, It must > 0']"
                    @keyup.enter="MoveToBinSubmit()">
             <template v-slot:before>
               <q-select dense
                         outlined
                         square
                         use-input
                         hide-selected
                         fill-input
                         v-model="movedata.move_to_bin"
                         label="Move To Bin"
                         :options="options"
                         @filter="filterFn"
                         @keyup.enter="MoveToBinSubmit()">
                 <template v-slot:no-option>
                   <q-item>
                     <q-item-section class="text-grey">
                       No results
                     </q-item-section>
                   </q-item>
                 </template>
                 <template v-if="movedata.move_to_bin" v-slot:append>
                   <q-icon name="cancel" @click.stop="movedata.move_to_bin = ''" class="cursor-pointer" />
                 </template>
              </q-select>
             </template>
           </q-input>
         </q-card-section>
         <div style="float: right; padding: 15px 15px 15px 0">
           <q-btn color="white" text-color="black" style="margin-right: 25px" @click="MoveToBinCancel()">Cancel</q-btn>
           <q-btn color="primary" @click="MoveToBinSubmit()">Submit</q-btn>
         </div>
       </q-card>
     </q-dialog>
    </div>
</template>
    <router-view />

<script>
// import { openURL } from 'quasar'
import { getauth, postauth } from 'boot/axios_request'
import { SessionStorage } from 'quasar'

export default {
  name: 'Pagestockbinlist',
  data () {
    return {
      openid: '',
      login_name: '',
      authin: '0',
      pathname: 'stock/bin/',
      pathname_previous: '',
      pathname_next: '',
      separator: 'cell',
      loading: false,
      height: '',
      table_list: [],
      bin_size_list: [],
      bin_property_list: [],
      warehouse_list: [],
      columns: [
        { name: 'bin_name', required: true, label: 'Bin Name', align: 'left', field: 'bin_name' },
        { name: 'goods_code', label: 'Goods Code', field: 'goods_code', align: 'center' },
        { name: 'goods_desc', label: 'Goods Desc', field: 'onhand_stock', align: 'center' },
        { name: 'goods_qty', label: 'Total Qty', field: 'goods_qty', align: 'center' },
        { name: 'pick_qty', label: 'Pick Qty', field: 'pick_qty', align: 'center' },
        { name: 'picked_qty', label: 'Picked Qty', field: 'picked_qty', align: 'center' },
        { name: 'bin_size', label: 'Bin Size', field: 'bin_size', align: 'center' },
        { name: 'bin_property', label: 'Bin Property', field: 'bin_property', align: 'center' },
        { name: 'create_time', label: 'Create_time', field: 'create_time', align: 'center' },
        { name: 'update_time', label: 'Update_time', field: 'update_time', align: 'center' },
        { name: 'action', label: 'Action', align: 'right' }
      ],
      filter: '',
      pagination: {
        page: 1,
        rowsPerPage: '30'
      },
      options: [],
      moveForm: false,
      movedata: {}
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
    BinMove (e) {
      var _this = this
      _this.moveForm = true
      _this.movedata = e
    },
    MoveToBinCancel () {
      var _this = this
      _this.moveForm = false
      _this.movedata = {}
    },
    MoveToBinSubmit () {
      var _this = this
      postauth(_this.pathname + _this.movedata.id + '/', _this.movedata).then(res => {
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
          _this.MoveToBinCancel()
          _this.$q.notify({
            message: 'Bin Moving Success',
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
    filterFn (val, update, abort) {
      var _this = this
      if (val.length < 1) {
        abort()
        return
      }
      update(() => {
        const needle = val.toLowerCase()
        getauth('binset/?bin_name__icontains=' + needle).then(res => {
          var binlist = []
          res.results.forEach(detail => {
            binlist.push(detail.bin_name)
          })
          SessionStorage.set('bin_name', binlist)
          _this.options = SessionStorage.getItem('bin_name')
        }).catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
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
