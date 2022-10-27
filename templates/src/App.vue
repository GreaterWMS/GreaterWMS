<template>
  <div id="q-app">
    <router-view />
  </div>
</template>
<script >
import Vconsole from "vconsole";
if (process.env.NODE_ENV !== 'production') {
  const vConsole = new Vconsole()
}

export default {
  name: 'App'
}
</script>
