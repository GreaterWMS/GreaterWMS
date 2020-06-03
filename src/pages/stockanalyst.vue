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
        :filter="filter"
        :pagination.sync="pagination"
        no-data-label="没有找到任何数据"
        no-results-label="没有找到您想要的数据"
        :table-style="{ height: height }"
      >
         <template v-slot:top>
           <q-btn-group push>
      <q-btn unelevated label="刷新" icon="refresh" @click="getList()">
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
        <q-input outlined rounded dense debounce="300" color="primary" v-model="filter" placeholder="关键字搜索">
          <template v-slot:append>
            <q-icon name="search" />
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
      </q-table>

  </div>
</template>
    <router-view />
  </q-page>
</template>

<script>
import { post } from 'boot/axios'

export default {
  name: 'stockanalyst',
  data () {
    return {
      separator: 'vertical',
      loading: false,
      filter: '',
      height: '',
      columns: [
        { name: 'goods_code', label: '商品编码', align: 'left', field: 'goods_code' },
        { name: 'shipping_data1', label: '前30天总消耗量', field: 'shipping_data1' },
        { name: 'shipping_data2', label: '前60天总消耗量', field: 'shipping_data2' },
        { name: 'shipping_data3', label: '前90天总消耗量', field: 'shipping_data3' },
        { name: 'plan_date4', label: '预计现有库存可支持天数', field: 'plan_date4', sortable: true },
        { name: 'plan_date1', label: '按30天消耗量预测断货日期', field: 'plan_date1', sortable: true },
        { name: 'plan_date2', label: '按60天消耗量预测断货日期', field: 'plan_date2', sortable: true },
        { name: 'plan_date3', label: '按90天消耗量预测断货日期', field: 'plan_date3', sortable: true },
        { name: 'oos_lv', label: '库存情况', field: 'oos_lv', sortable: true }
      ],
      data: [
      ],
      pagination: {
        sortBy: 'goods_code',
        descending: false,
        page: 1,
        rowsPerPage: 50
      }
    }
  },
  methods: {
    getList () {
      var openid = this.$q.localStorage.getItem('openid')
      post('stockanalyst/', { openid: openid }, { data: '' }).then(response => {
        if (response.data.code === '200') {
          this.data = response.data.data
        } else {
          this.$q.notify({
            message: response.data.msg,
            icon: 'close',
            color: 'negative',
            position: 'right',
            timeout: 1500
          })
        }
        this.data = response.data.data
      }).catch(error => { console.log(error) })
    }
  },
  created () {
    this.openid = this.$q.localStorage.getItem('openid')
  },
  mounted () {
    if (this.$q.localStorage.has('openid')) {
      this.getList()
    } else {}
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
