<template>
  <q-page class="flex flex-center">
    <transition appear enter-active-class="animated rubberBand">
      <h2>{{ $t('index.title') }}</h2>
    </transition>
  </q-page>
</template>

<script>
export default {
  name: 'PageIndex'
}
</script>
