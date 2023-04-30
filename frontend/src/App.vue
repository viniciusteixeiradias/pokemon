<script lang="ts" setup>
import AppPokemonList from './components/AppPokemonList.vue';
</script>

<template>
  <AppPokemonList />
</template>

<style>
body {
  margin: 0;
  padding: 0;
}

#app {
  background-color: rgb(0, 56, 93);
  height: 100vh;
  display: flex;
  justify-content: center;
  overflow: auto;
}
</style>