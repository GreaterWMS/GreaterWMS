<template>
    <q-page>

    <template>
    <div class="q-pa-md" style="width: 100%">
      <q-table
        title="Treats"
        dense
        :data="data"
        :columns="columns"
        row-key="name"
        :separator="separator"
        :loading="loading"
        :pagination.sync="pagination"
        no-data-label="没有找到任何数据"
        no-results-label="没有找到您想要的数据"
        :table-style="{ height: height }"
      >
         <template v-slot:top>
           <q-btn-group push>
      <q-btn unelevated label="刷新" icon="refresh" @click="openidCheck()">
        <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">
          刷新现在页面
        </q-tooltip>
      </q-btn>
<!--       <q-btn unelevated label="上传" icon="cloud_upload" @click="onRefresh">-->
<!--         <q-tooltip content-class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">-->
<!--          批量上传-->
<!--        </q-tooltip>-->
<!--       </q-btn>-->
    </q-btn-group>
             <q-space />
        <q-input outlined rounded dense debounce="300" color="primary"
                 v-model="searchword" placeholder="请输入商品编码进行搜索" @keyup.enter="getList()">
          <template v-slot:append>
            <q-icon name="search" @click="getList()"/>
          </template>
        </q-input>
      </template>
        <template v-slot:no-data="{ icon, message, filter }">
        <div class="full-width row flex-center text-accent q-gutter-sm">
          <q-icon size="2em" name="sentiment_dissatisfied" />
          <span>
            没有找到任何数据... {{ message }}
          </span>
          <q-icon size="2em" :name="filter ? 'filter_b_and_w' : icon" />
        </div>
      </template>
              <template v-slot:body="props">
        <q-tr :props="props">
          <q-td key="goods_code" :props="props">{{ props.row.goods_code }}</q-td>
          <q-td key="forcast_day" :props="props">{{ props.row.forcast_day }}</q-td>
          <q-td key="forcast_shipping" :props="props">{{ props.row.forcast_shipping }}</q-td>
          <q-td key="forcast_on_hand" :props="props">{{ props.row.forcast_on_hand }}</q-td>
                    <q-td key="plan_order_qty" :props="props">
            {{ props.row.plan_order_qty }}
            <q-popup-edit v-model="props.row.plan_order_qty" key="forcast_on_hand" title="模拟下单" buttons persistent
                          @save="inde(props.row.plan_order_qty, props.rowIndex)"
                          @before-show="indedata()">
              <q-input type="number" v-model="props.row.plan_order_qty" dense autofocus hint="点击下方设置，模拟下单" />
            </q-popup-edit>
          </q-td>
          <q-td key="oos" :props="props">{{ props.row.oos }}</q-td>
        </q-tr>
      </template>
      </q-table>
<q-btn label="点击模拟下单，输入模拟下单数量" size="md" align="left" flat icon="warning"/>
  </div>
</template>
    <router-view />
  </q-page>
</template>

<script>
import { post } from 'boot/axios'

export default {
  name: 'simorder',
  data () {
    return {
      separator: 'vertical',
      loading: false,
      searchword: '',
      height: '',
      columns: [
        { name: 'goods_code', label: '商品编码', align: 'left', field: 'goods_code' },
        { name: 'forcast_day', label: '预测日期', field: 'forcast_day' },
        { name: 'forcast_shipping', label: '预测发货数量', field: 'forcast_shipping' },
        { name: 'forcast_on_hand', label: '预测剩余库存', field: 'forcast_on_hand' },
        { name: 'plan_order_qty', label: '模拟下单数量', field: 'plan_order_qty' },
        { name: 'oos', label: '断货提示', field: 'oos' }
      ],
      data: [
      ],
      pagination: {
        sortBy: 'forcast_day',
        descending: false,
        page: 1,
        rowsPerPage: 50
      },
      onhand: '',
      leadtime: ''
    }
  },
  methods: {
    openidCheck () {
      if (this.$q.localStorage.has('openid')) {
        this.getList()
      } else {}
    },
    getList () {
      var openid = this.$q.localStorage.getItem('openid')
      post('simorder/', { openid: openid }, { data: this.searchword }).then(response => {
        if (response.data.code === '200') {
          this.onhand = response.data.forcast_on_hand
          this.leadtime = response.data.lead_time
          this.$q.localStorage.set('simorder', response.data.data)
          var simdata = this.$q.localStorage.getItem('simorder')
          var avg1data = []
          var avg2data = []
          var avg3data = []
          var avg4data = []
          var avg5data = []
          var avg6data = []
          var avg7data = []
          for (var i = 0; i < 89; i++) {
            var avg1 = i % 7
            if (avg1 === 0) {
              avg7data.push(simdata[i].forcast_shipping)
            } else if (avg1 === 1) {
              avg1data.push(simdata[i].forcast_shipping)
            } else if (avg1 === 2) {
              avg2data.push(simdata[i].forcast_shipping)
            } else if (avg1 === 3) {
              avg3data.push(simdata[i].forcast_shipping)
            } else if (avg1 === 4) {
              avg4data.push(simdata[i].forcast_shipping)
            } else if (avg1 === 5) {
              avg5data.push(simdata[i].forcast_shipping)
            } else if (avg1 === 6) {
              avg6data.push(simdata[i].forcast_shipping)
            } else {}
          }
          var sum1 = 0
          var sum2 = 0
          var sum3 = 0
          var sum4 = 0
          var sum5 = 0
          var sum6 = 0
          var sum7 = 0
          for (var j = 0; j < avg1data.length; j++) {
            sum1 += avg1data[j]
          }
          var avgdetail1 = sum1 / avg1data.length
          for (var k = 0; k < avg2data.length; k++) {
            sum2 += avg2data[k]
          }
          var avgdetail2 = sum2 / avg2data.length
          for (var v = 0; v < avg3data.length; v++) {
            sum3 += avg3data[v]
          }
          var avgdetail3 = sum3 / avg3data.length
          for (var x = 0; x < avg4data.length; x++) {
            sum4 += avg4data[x]
          }
          var avgdetail4 = sum4 / avg4data.length
          for (var y = 0; y < avg5data.length; y++) {
            sum5 += avg5data[y]
          }
          var avgdetail5 = sum5 / avg5data.length
          for (var z = 0; z < avg6data.length; z++) {
            sum6 += avg6data[z]
          }
          var avgdetail6 = sum6 / avg6data.length
          for (var n = 0; n < avg7data.length; n++) {
            sum7 += avg7data[n]
          }
          var avgdetail7 = sum7 / avg7data.length
          for (var m = 0; m < 90; m++) {
            if ((m + 90) % 7 === 6) {
              simdata[m + 90].forcast_shipping = parseInt(avgdetail1)
              simdata[m + 90].forcast_on_hand = this.onhand - parseInt(avgdetail1)
              this.onhand = this.onhand - parseInt(avgdetail1)
              if (this.onhand <= 0) {
                simdata[m + 90].oos = '已经断货'
              }
            } else if ((m + 90) % 7 === 0) {
              simdata[m + 90].forcast_shipping = parseInt(avgdetail2)
              simdata[m + 90].forcast_on_hand = this.onhand - parseInt(avgdetail2)
              this.onhand = this.onhand - parseInt(avgdetail2)
              if (this.onhand <= 0) {
                simdata[m + 90].oos = '已经断货'
              }
            } else if ((m + 90) % 7 === 1) {
              simdata[m + 90].forcast_shipping = parseInt(avgdetail3)
              simdata[m + 90].forcast_on_hand = this.onhand - parseInt(avgdetail3)
              this.onhand = this.onhand - parseInt(avgdetail3)
              if (this.onhand <= 0) {
                simdata[m + 90].oos = '已经断货'
              }
            } else if ((m + 90) % 7 === 2) {
              simdata[m + 90].forcast_shipping = parseInt(avgdetail4)
              simdata[m + 90].forcast_on_hand = this.onhand - parseInt(avgdetail4)
              this.onhand = this.onhand - parseInt(avgdetail4)
              if (this.onhand <= 0) {
                simdata[m + 90].oos = '已经断货'
              }
            } else if ((m + 90) % 7 === 3) {
              simdata[m + 90].forcast_shipping = parseInt(avgdetail5)
              simdata[m + 90].forcast_on_hand = this.onhand - parseInt(avgdetail5)
              this.onhand = this.onhand - parseInt(avgdetail5)
              if (this.onhand <= 0) {
                simdata[m + 90].oos = '已经断货'
              }
            } else if ((m + 90) % 7 === 4) {
              simdata[m + 90].forcast_shipping = parseInt(avgdetail6)
              simdata[m + 90].forcast_on_hand = this.onhand - parseInt(avgdetail6)
              this.onhand = this.onhand - parseInt(avgdetail6)
              if (this.onhand <= 0) {
                simdata[m + 90].oos = '已经断货'
              }
            } else if ((m + 90) % 7 === 5) {
              simdata[m + 90].forcast_shipping = parseInt(avgdetail7)
              simdata[m + 90].forcast_on_hand = this.onhand - parseInt(avgdetail7)
              this.onhand = this.onhand - parseInt(avgdetail7)
              if (this.onhand <= 0) {
                simdata[m + 90].oos = '已经断货'
              }
            } else {
            }
          }
          simdata.splice(0, 90)
          this.data = simdata
        } else {
          this.$q.notify({
            message: response.data.msg,
            icon: 'close',
            color: 'negative',
            position: 'right',
            timeout: 1500
          })
        }
      }).catch(error => { console.log(error) })
    },
    indedata () {
      this.$q.localStorage.set('indedata', this.data)
    },
    inde (e, i) {
      var indedata = this.$q.localStorage.getItem('indedata')
      if (e === '') {
        this.data[i].plan_order_qty = 0
        this.data.forEach((response, index) => {
          if (index >= i + this.leadtime) {
            var plandatachange = 0 - parseInt(indedata[i].plan_order_qty)
            var resultOH = parseInt(this.data[index].forcast_on_hand) + plandatachange
            this.data[index].forcast_on_hand = resultOH
            if (this.data[index].forcast_on_hand >= 0) {
              this.data[index].oos = ''
            } else if (this.data[index].forcast_on_hand < 0) {
              this.data[index].oos = '已经断货'
            }
          }
        })
      } else {
        this.data[i].plan_order_qty = parseInt(e)
        this.data.forEach((response, index) => {
          if (index >= i + this.leadtime) {
            var plandatachange = parseInt(e) - parseInt(indedata[i].plan_order_qty)
            var resultOH = parseInt(this.data[index].forcast_on_hand) + plandatachange
            this.data[index].forcast_on_hand = resultOH
            if (this.data[index].forcast_on_hand >= 0) {
              this.data[index].oos = ''
            } else if (this.data[index].forcast_on_hand < 0) {
              this.data[index].oos = '已经断货'
            }
          }
        })
      }
    }
  },
  created () {
    this.openid = this.$q.localStorage.getItem('openid')
  },
  mounted () {
    if (this.$q.platform.is.electron) {
      this.height = String(this.$q.screen.height - 230) + 'px'
    } else {
      this.height = this.$q.screen.height - 230 + '' + 'px'
    }
  },
  updated () {
  }
}
</script>
