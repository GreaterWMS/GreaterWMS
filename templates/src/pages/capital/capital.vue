<template>
  <q-page class="flex flex-top">
<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 100%">
      <q-tabs
        v-model="detaillink"
      >
  <q-route-tab name="capital" label="capital" icon="img:statics/capital/capital.png" to="/capital/capitallist" exact/>
      </q-tabs>
    </div>
  </div>
</template>
    <router-view />
  </q-page>
</template>

<script>
export default {
  name: 'Pagecapital',
  data () {
    return {
      detaillink: 'capital'
    }
  },
  methods: {
  }
}
</script>
