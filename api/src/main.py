from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/vinicius")
def req():
    response = requests.get("https://pokeapi.co/api/v2/berry/3/")
    return response.json()
