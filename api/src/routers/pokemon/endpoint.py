from fastapi import Depends, APIRouter
from typing import Sequence
from .schema import PokemonSchemaOut
from .dao import PokemonDAO


router = APIRouter()


@router.get('/', response_model=Sequence[PokemonSchemaOut])
def profiles(pokemonDAO: PokemonDAO = Depends(PokemonDAO)):
    return pokemonDAO.count()
