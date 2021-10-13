<template>
  <div>
    <transition appear enter-active-class="animated fadeIn">
      <q-table
        class="my-sticky-header-column-table shadow-24"
        row-key="id"
        :table-style="{ height: height }"
        flat
      >
      </q-table>
    </transition>
  </div>
</template>
<router-view />
<script>
export default {
  updated () {
  },
  destroyed () {
  }
}
</script>
