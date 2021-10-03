<template>
<div :style="{height:height,width:width}">
  <pie-chart></pie-chart>
</div>
</template>

<script>
import PieChart from 'components/PieChart'
import { database } from 'src/db/database'
import { LocalStorage } from 'quasar'
import { getauth } from 'boot/axios_request'
export default {
  name: 'piechart',
  components: { PieChart },
  data () {
    return {
      height: '',
      width: '',
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
      var chart = database.getInstance().get().piechart
      if (LocalStorage.has('auth')) {
        getauth(_this.pathname, {
        }).then(res => {
          _this.table_list = res.results
          console.log(_this.table_list)
          if (res.count > 0) {
            var goodslist = []
            var gcName = []
            var NamesCheck = []
            res.results.forEach((item, index) => {
              var gc = item.goods_code
              goodslist.push(gc)
            })
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
              name: gcName
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

<style scoped>

</style>
