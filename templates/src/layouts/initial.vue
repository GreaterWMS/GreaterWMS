<template>
  <router-view />
</template>

<script>

export default {
  name: 'initial',
  data () {
    return {
    }
  },
  methods: {
  },
  beforeCreate () {
    var _this = this
    _this.$router.push({ name: 'web_index' })
  }
}
</script>

<style scoped>

</style>
