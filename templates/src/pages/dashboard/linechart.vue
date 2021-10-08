<template>
 <div :style="{width: width, height: height}">
      <line-chart style="height: 200px"></line-chart>
  </div>
</template>

<script>
import LineChart from 'components/LineChart'
import { getauth } from 'boot/axios_request'
import { database } from '../../db/database'
import { LocalStorage } from 'quasar'
export default {
  name: 'linechart',
  components: { LineChart },
  data () {
    return {
      width: '100%',
      height: '',
      pathname: 'asn/detail/?asn_status=5&ordering=-id&max-page:10000'
    }
  },
  mounted () {
    var _this = this
    _this.getdata()
    if (_this.$q.platform.is.electron) {
      _this.height = String(_this.$q.screen.height) + 'px'
    } else {
      _this.height = _this.$q.screen.height + '' + 'px'
    }
  },
  methods: {
    getdata () {
      var _this = this
      var chart = database.getInstance().get().linechart
      if (LocalStorage.has('auth')) {
        // 获取后台数据
        getauth(_this.pathname, {
        }).then(res => {
          _this.table_list = res.results
          console.log(_this.table_list)
          if (res.count > 0) {
            var drops = []
            var monthlist = []
            var goodslist = []
            var goodquantity = []
            var gcName = []
            var NamesCheck = 0
            var ctNames = []
            var gqName = []
            // 遍历获取的数据
            res.results.forEach((item, index) => {
              var ct = (item.create_time).toString().split('-')
              var ctName = ct[0] + '-' + ct[1]
              var gc = item.goods_code
              var gq = item.goods_qty
              // 将月份数据放入前端数据库
              monthlist.push(ctName)
              // 将商品编码数据放入前端数据库
              goodslist.push(gc)
              // 将商品数量数据放入前端数据库
              goodquantity.push(gq)
            })
            // 月份数据去重
            monthlist.forEach((xxx, index) => {
              if (ctNames.length === 0) {
                ctNames.push(xxx)
              } else {
                ctNames.forEach((yyy, index) => {
                  if (yyy === xxx) {
                    NamesCheck = 1
                  }
                })
                if (NamesCheck === 0) {
                  ctNames.push(xxx)
                  NamesCheck = 0
                } else {
                  NamesCheck = 0
                }
              }
            })
            // 商品编码数据去重
            goodslist.forEach((m, index) => {
              if (gcName.length === 0) {
                gcName.push(m)
              } else {
                gcName.forEach((l, index) => {
                  if (l === m) {
                    NamesCheck = 1
                  }
                })
                if (NamesCheck === 0) {
                  gcName.push(m)
                  NamesCheck = 0
                } else {
                  NamesCheck = 0
                }
              }
            })
            chart.bulkDelete([1])
            chart.add({
              id: 1,
              legend: gcName,
              xAxis: ctNames,
              serise: []
            }).then(function (lastkey) {
              console.log(lastkey)
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
