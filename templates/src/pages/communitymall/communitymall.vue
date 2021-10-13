<template>
  <q-page class="flex flex-top">
    <template>
      <div class="q-pa-md">
        <div class="q-gutter-y-md" style="max-width: 100%">
          <q-tabs
            v-model="detaillink"
          >
            <transition appear enter-active-class="animated zoomIn">
              <q-route-tab v-show="$q.localStorage.getItem('staff_type') !== 'Supplier' &&
                          $q.localStorage.getItem('staff_type') !== 'Customer'
                         " name="cm" :label="$t('community_mall.communitymall')" icon="img:statics/communitymall/cm.png" to="/communitymall/cm" exact/>
            </transition>
          </q-tabs>
        </div>
      </div>
    </template>
    <div class="main-table">
      <router-view />
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'upload'
}
</script>

<style scoped>

</style>
