<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
        <transition appear enter-active-class="animated zoomIn">
          <q-route-tab name="douyin" label="抖音" icon="img:statics/shopid/douyin.png" :to="{ name: 'douyin' }" exact/>
        </transition>
      </q-tabs>
    </div>
  </div>
</template>
    <div :style="{width: '100%', margin: '-10px 10px 0 10px'}">
      <router-view />
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'Pageshopid',
  data () {
    return {
      detaillink: 'douyin'
    }
  },
  methods: {
  }
}
</script>
