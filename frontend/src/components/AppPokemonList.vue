<script lang="ts" setup>
import { reactive, ref, onMounted, computed } from 'vue';
import axios, { AxiosError } from 'axios';
import AppPokemon from './AppPokemon.vue';
import AppWithoutPokemon from './AppWithoutPokemon.vue';
import type { Pokemon } from '../models/pokemon';
import AppLoading from './AppLoading.vue';

interface State {
    pokemons: Pokemon[]
}

const state = reactive<State>({
    pokemons: []
})

const searchText = ref<string>('')
const loading = ref<boolean>(false)

const API_URL = 'http://127.0.0.1:8000/pokemon';

const hasPokemon = computed<boolean>(() => !!state.pokemons.length)

const request = async <T>(endpoint: string = API_URL): Promise<T | undefined> => {
    try {
        loading.value = true;

        const { data } = await axios.get<T>(endpoint)

        return data
    } catch (error: any) {

        if (error instanceof AxiosError) {
            alert(error.response?.data.detail)
        }

    } finally {
        loading.value = false;
    }
}

const loadAllPokemons = async (): Promise<void> => {
    const data = await request<Pokemon[]>();

    if (!data) {
        return;
    }

    state.pokemons = [...data]
}

const onPopulateTable = async (): Promise<void> => {
    await request<void>('http://127.0.0.1:8000/populate_table');
    await loadAllPokemons()
}

const cleanrListAndAddPokemon = (pokemon: Pokemon): void => {
    state.pokemons = []
    state.pokemons.push(pokemon)
}

const loadRandom = async (): Promise<void> => {
    const data = await request<Pokemon>(`${API_URL}/random`);

    if (!data) {
        return;
    }

    cleanrListAndAddPokemon(data)
}

const loadByName = async (): Promise<void> => {
    const data = await request<Pokemon>(`${API_URL}/${searchText.value}`)

    if (!data) {
        return;
    }

    cleanrListAndAddPokemon(data)
}

onMounted(loadAllPokemons)
</script>

<template>
    <AppLoading v-if="loading" />

    <div v-else class="app-pokemon-list">
        <AppWithoutPokemon v-if="!hasPokemon" @populate-table="onPopulateTable" />
        
        <template v-else>
            <div class="app-pokemon-list__search">
                <label for="search">Pokemon name (lowercase)</label> <br>
                <input id="search" v-model="searchText" type="text" placeholder="ex: bulbasaur" /> 
                <button @click="loadByName">Search</button>
            </div>

            <button @click="loadAllPokemons">Load All Pokemons</button>
            <button @click="loadRandom">Load a Random Pokemon</button>

            <AppPokemon 
                v-for="pokemon in state.pokemons" 
                :key="pokemon.uuid"
                :pokemon="pokemon"
            />
        </template>
    </div>
</template>

<style>
.app-pokemon-list__search {
    color: white;
    font-size: 18px;
    padding-block: 30px;
}
</style>