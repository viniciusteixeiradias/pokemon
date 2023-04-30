import requests

from starlette.responses import Response
from pydantic.types import UUID4

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from .routers.pokemon import PokemonDAO, PokemonSchemaIn, PokemonSchemaOut

import random

from typing import List

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pokemon routes (Put this on routes/pokemon/endpoints) in the future, now not is necessary.
@app.get('/pokemon/create')
def create(pokemonDAO: PokemonDAO = Depends(PokemonDAO)):
    pokemon = PokemonSchemaIn(
        name='name_example', 
        base_experience=100, 
        height=10, 
        weight=10, 
        url_image='url_image_example'
    )

    return pokemonDAO.save(pokemonSchemaIn=pokemon)

@app.get('/pokemon/count')
def count(pokemonDAO: PokemonDAO = Depends(PokemonDAO)):
    return pokemonDAO.count()

@app.get('/pokemon/random', response_model=PokemonSchemaOut)
def get_random(pokemonDAO: PokemonDAO = Depends(PokemonDAO)):
    pokemons = get_all(pokemonDAO=pokemonDAO) 
    
    return random.choice(pokemons)


@app.get("/pokemon", response_model=List[PokemonSchemaOut])
def get_all(pokemonDAO: PokemonDAO = Depends(PokemonDAO)):
    return pokemonDAO.get_all()


@app.get('/pokemon/{name}', response_model=PokemonSchemaOut)
def get_by_name(
    name: str,
    pokemonDAO: PokemonDAO = Depends(PokemonDAO)
):
    return pokemonDAO.get_by_name(name=name) 


@app.delete('/pokemon/{uuid}', status_code=204, response_class=Response)
def delete(
    uuid: UUID4,
    pokemonDAO: PokemonDAO = Depends(PokemonDAO)
):
    return pokemonDAO.delete(uuid=uuid)

@app.get("/populate_table")
def populate_table(pokemonDAO: PokemonDAO = Depends(PokemonDAO)):
    num_pokemons = 20
    pokemon_id = 1
    pokemons = get_all(pokemonDAO=pokemonDAO)

    while len(pokemons) <= num_pokemons:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
        json_data = response.json()

        pokemon_id += 1

        if not json_data:
            continue

        name = json_data['name']
        height = json_data['height']
        weight = json_data['weight']
        base_experience = json_data['base_experience']
        url_image = json_data['sprites']['other']['official-artwork']['front_default']

        pokemon = PokemonSchemaIn(name=name, base_experience=base_experience, height=height, weight=weight, url_image=url_image)
        pokemons.append(pokemon)

        pokemonDAO.save(pokemonSchemaIn=pokemon)
    
    return pokemons

        