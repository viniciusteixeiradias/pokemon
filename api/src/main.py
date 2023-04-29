import requests

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from typing import Sequence
from .routers.pokemon import PokemonDAO

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

@app.get("/vinicius")
def req():
    response = requests.get("https://pokeapi.co/api/v2/berry/3/")
    return response.json()

@app.get('/count')
def profiles(pokemonDAO: PokemonDAO = Depends(PokemonDAO)):
    return pokemonDAO.count()
