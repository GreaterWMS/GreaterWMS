<template>
  <q-page class="flex flex-top">
    <template>
      <div class="q-pa-md">
        <div class="q-gutter-y-md" style="max-width: 100%">
          <q-tabs v-model="detaillink">
            <transition appear enter-active-class="animated zoomIn">
              <q-route-tab
                name="initializeupload"
                :label="$t('upload_center.initializeupload')"
                icon="img:statics/uploadcenter/uploadinbound.png"
                :to="{ name: 'initializeupload' }"
                exact
              />
            </transition>
            <transition appear enter-active-class="animated zoomIn">
              <q-route-tab
                name="addupload"
                :label="$t('upload_center.addupload')"
                icon="img:statics/uploadcenter/addupload.png"
                :to="{ name: 'addupload' }"
                exact
              />
            </transition>
          </q-tabs>
        </div>
      </div>
    </template>
    <div class="main-table2"><router-view /></div>
  </q-page>
</template>

<script>
export default {
  name: 'upload',
  data () {
    return {
      detaillink: 'initializeupload'
    }
  }
}
</script>
