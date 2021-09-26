<template>
    <div>
        <q-table>
          <template v-slot:top>
            <q-btn-group push>
              <q-btn :label="$t('new')" icon="add" @click="newForm = true">
                <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                  {{ $t('newtip') }}
                </q-tooltip>
              </q-btn>
              <q-btn :label="$t('refresh')" icon="refresh" @click="reFresh()">
                <q-tooltip content-class="bg-amber text-black shadow-4" :offset="[10, 10]" content-style="font-size: 12px">
                  {{ $t('refreshtip') }}
                </q-tooltip>
              </q-btn>
            </q-btn-group>
            <q-space />
            <q-input outlined rounded dense debounce="300" color="primary" v-model="filter" :placeholder="$t('search')" @blur="getSearchList()" @keyup.enter="getSearchList()">
              <template v-slot:append>
                <q-icon name="search" @click="getSearchList()"/>
              </template>
            </q-input>
          </template>
        </q-table>
    </div>
</template>

<script>
export default {
  name: 'downloadinbound'
}
</script>

<style scoped>

</style>
