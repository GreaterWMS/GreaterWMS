<template>
  <q-page v-show="!fab1 && !fab2 && !fab3 && !fab4" class="flex flex-top">
    <div :style="{ width: screenwidth + '' + 'px', height: (screenheight - 160) + '' + 'px', marginTop: '10px'}">
      <q-input
        dense
        outlined
        square
        readonly
        v-model="apptitle"
        :label="$t('index.app_title')"
        style="margin: 0 15px 0 15px"
      />
      <q-input
        dense
        outlined
        square
        readonly
        v-model="slogan"
        :label="$t('index.slogan')"
        style="margin: 15px 15px 0 15px"
      />
      <q-input
        dense
        outlined
        square
        v-model="openid"
        :label="$t('index.your_openid')"
        style="margin: 15px 15px 0 15px"
      />
      <q-input
        dense
        outlined
        square
        v-model="server"
        :label="$t('index.server')"
        style="margin: 15px 15px 0 15px"
      />
    </div>
  </q-page>
</template>

<script>
import { computed, defineComponent, ref } from "vue";
import { useStore } from "vuex";

export default defineComponent({
  data () {
    return {
    }
  },
  computed: {
    screenwidth: {
      get() {
        return this.$store.state.screenchange.screenwidth
      },
    },
    screenheight: {
      get() {
        return this.$store.state.screenchange.screenheight
      },
    }
  },
  setup () {
    const staff_name = ref('')
    const check_code = ref('')
    const admin_name = ref('')
    const password = ref('')
    const login_mode = ref(0)
    const $store = useStore()
    const fab1 = computed({
      get: () => $store.state.fabchange.fab1,
    })
    const fab2 = computed({
      get: () => $store.state.fabchange.fab2,
    })
    const fab3 = computed({
      get: () => $store.state.fabchange.fab3,
    })
    const fab4 = computed({
      get: () => $store.state.fabchange.fab4,
    })
    const apptitle = computed({
      get: () => $store.state.settings.apptitle,
      set: val => {
        $store.commit('settings/APPTitle', val)
      }
    })
    const server = computed({
      get: () => $store.state.settings.server,
      set: val => {
        $store.commit('settings/Server', val)
      }
    })
    const openid = computed({
      get: () => $store.state.settings.openid,
      set: val => {
        $store.commit('settings/Openid', val)
      }
    })
    const slogan = computed({
      get: () => $store.state.settings.slogan,
      set: val => {
        $store.commit('settings/Slogan', val)
      }
    })
    return {
      fab1,
      fab2,
      fab3,
      fab4,
      apptitle,
      server,
      openid,
      slogan
    }
  }
})
</script>

<style scoped>

</style>
