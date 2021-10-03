<template>
  <div :style="{width: width, height: height}">
          <bar-chart style="height: 200px"></bar-chart>
  </div>
</template>
<script>
import BarChart from 'components/BarChart'
import { database } from 'src/db/database'
import { LocalStorage } from 'quasar'
import { getauth } from 'boot/axios_request'
export default {
  name: 'barchart',
  components: { BarChart },
  data () {
    return {
      pathname: 'asn/detail/?asn_status=5&ordering=-id&max-page:10000',
      height: '',
      width: '100%'
    }
  },
  mounted () {
    var _this = this
    _this.getData()
    if (_this.$q.platform.is.electron) {
      _this.height = String(_this.$q.screen.height) + 'px'
    } else {
      _this.height = _this.$q.screen.height + '' + 'px'
    }
  },
  methods: {
    getData () {
      var _this = this
      var chart = database.getInstance().get().barchart
      if (LocalStorage.has('auth')) {
        // 获取后台数据
        getauth(_this.pathname, {
        }).then(res => {
          _this.table_list = res.results
          console.log(_this.table_list)
          if (res.count > 0) {
            var weeklist = []
            var ctNames = []
            var nameCheck = 0
            var goodsclass = []
            var gcName = []
            // 遍历数组
            res.results.forEach((item, index) => {
              var ct = (item.create_time).toString().split('-')
              var ctName = ct[0] + '-' + ct[1]
              var gc = item.goods_code // 实际为种类
              // 将周数份存入前端数据库
              weeklist.push(ctName)
              // 将商品种类存入前端数据库
              goodsclass.push(gc)
            })
            // 周数去重
            weeklist.forEach((a, index) => {
              if (ctNames.length === 0) {
                ctNames.push(a)
              } else {
                ctNames.forEach((b, index) => {
                  if (b === a) {
                    nameCheck = 1
                  }
                })
                if (nameCheck === 0) {
                  ctNames.push(a)
                  nameCheck = 0
                } else {
                  nameCheck = 0
                }
              }
            })
            // 商品总类去重
            goodsclass.forEach((m, index) => {
              if (gcName.length === 0) {
                gcName.push(m)
              } else {
                gcName.forEach((l, index) => {
                  if (l === m) {
                    nameCheck = 1
                  }
                })
                if (nameCheck === 0) {
                  gcName.push(m)
                  nameCheck = 0
                } else {
                  nameCheck = 0
                }
              }
            })
            chart.bulkDelete([1])
            chart.add({
              id: 1,
              dataset: gcName,
              xAxis: ctNames,
              series: []
            })
          }
        }).catch(err => {
          _this.$q.notify({
            message: err.detail,
            icon: 'close',
            color: 'negative'
          })
        })
      }
    }
  }
}
</script>
