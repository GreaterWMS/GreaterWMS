<template>
  <router-view />
</template>

<script>
import { defineComponent } from 'vue'
import Vconsole from "vconsole";
const vConsole = new Vconsole()

export default defineComponent({
  name: 'App'
})
</script>
