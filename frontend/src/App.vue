<script lang="ts" setup>
import { ref } from 'vue';
import axios from 'axios';

const result = ref()

const get = async () => {
  const { data } = await axios.get('http://127.0.0.1:8000/')
  result.value = data
}
</script>

<template>
  App.vue
  <button @click="get">Get</button>

  <hr>
  <h1>Response:</h1>
  {{ result }}
</template>