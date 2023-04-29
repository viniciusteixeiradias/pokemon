import requests
from starlette.responses import Response
from pydantic.types import UUID4

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from .routers.pokemon import PokemonDAO, PokemonSchema, PokemonSchemaOut

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.get("/vinicius")
# def req():
#     response = requests.get("https://pokeapi.co/api/v2/berry/3/")
#     return response.json()

@app.get('/count')
def profiles(pokemonDAO: PokemonDAO = Depends(PokemonDAO)):
    return pokemonDAO.count()

@app.get('/create')
def profiles(pokemonDAO: PokemonDAO = Depends(PokemonDAO)):
    return pokemonDAO.save(pokemonSchemaIn = PokemonSchema(name='picachu', description='Essa é a descrição'))

@app.get('/{uuid}', response_model=PokemonSchemaOut)
def get_address(
    uuid: UUID4,
    pokemonDAO: PokemonDAO = Depends(PokemonDAO)
):
    return pokemonDAO.get_by_uuid(uuid=uuid) 

@app.delete('/{uuid}', status_code=204, response_class=Response)
def delete(
    uuid: UUID4,
    pokemonDAO: PokemonDAO = Depends(PokemonDAO)
):
    return pokemonDAO.delete(uuid=uuid)

