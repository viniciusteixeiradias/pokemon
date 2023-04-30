<script lang="ts" setup>
import type { Pokemon } from '../models/pokemon';

const props = defineProps<{
    pokemon: Pokemon
}>()
</script>

<template>
    <div class="app-pokemon">
        <img :alt="`pokemon-${props.pokemon.name}`" :src="props.pokemon.urlImage" />

        <div>
            <p>Name: {{ props.pokemon.name }}</p>
            <div>
                <span>Height: {{ props.pokemon.height }}</span> <br>
                <span>Weight: {{ props.pokemon.weight }}</span> <br>
                <span>Base Experience: {{ props.pokemon.baseExperience }}</span>
            </div>
        </div>
    </div>
</template>

<style scoped>
.app-pokemon {
    display: flex;
}

span {
    color: white;
}

p {
    color: white;
    font-size: 24px;
    font-weight: bold;
}

img {
    height: 200px;
    width: 200px;
}
</style>