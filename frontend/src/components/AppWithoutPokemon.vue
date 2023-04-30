<script lang="ts" setup>
const emits = defineEmits<{
    (e: 'populateTable'): void
}>()

const onClick = (): void => emits('populateTable')
</script>

<template>
    <p>Welcome 👋</p>
    <p>
        I know this is your first time here 😀, please click the button below to fill in your table in the database, <br>
        this process can take from 1 - 60 seconds 🕜. <br>
        
        <hr>
        <strong>The API is configured to input 20 pokemons, you can change this in the src/main.py file.</strong>
        <hr>

        <button id="load-all" @click="onClick">
            Click here to insert the pokemons in the databse table
        </button>
    </p>
</template>

<style scoped>
p {
    color: white;
}

strong {
    color: rgb(211, 255, 91);
}

p:nth-child(1) {
    font-size: 30px;
    font-weight: bold;
}
</style>