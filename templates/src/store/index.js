import Vue from 'vue'
import Vuex from 'vuex'

// 首先导入模块
import datashare from './datashare'

Vue.use(Vuex)

export default function (/* { ssrContext } */) {
  const Store = new Vuex.Store({
    modules: {
      // 然后我们引用它
      datashare
    },

    // 启用严格模式（增加开销！）
    // 仅适用于开发模式
    strict: process.env.DEV
  })

  /*
    如果我们需要一些HMR魔术，我们会处理
    下面的热点更新。 注意我们实现这个
    用“process.env.DEV”代码 - 所以这不会
    进入我们的生产版本（也不应该）。
  */

  if (process.env.DEV && module.hot) {
    module.hot.accept(['./datashare'], () => {
      const newDatashare = require('./datashare').default
      Store.hotUpdate({ modules: { datashare: newDatashare } })
    })
  }

  return Store
}
