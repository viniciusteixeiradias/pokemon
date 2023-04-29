from fastapi import Depends, HTTPException, status
from pydantic.types import UUID4
from ...database.session import session_manager
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from .schema import PokemonSchemaIn
from .model import PokemonModel


class PokemonDAO():
    def __init__(self, session: Session = Depends(session_manager)):
        self.session = session

    def count(self):
        return self.session.query(PokemonModel).count()
    
    def get_by_uuid(self, uuid: UUID4):
        pokemon = self.session.query(PokemonModel) \
            .filter(PokemonModel.uuid == uuid) \
            .first()

        if not pokemon:
            raise HTTPException(status_code=404, detail="Address not found")
        
        return pokemon

    def save(self, pokemonSchemaIn: PokemonSchemaIn) -> PokemonModel:
        try:
            profile_dict = PokemonModel(**pokemonSchemaIn.dict())

            self.session.add(profile_dict)
            self.session.commit()
            self.session.refresh(profile_dict)

            return profile_dict
        except IntegrityError as e:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Pokemon not found: {e}")

    def delete(self, uuid: UUID4) -> None:

        pokemon = self.session.query(PokemonModel) \
            .filter(PokemonModel.uuid == uuid) \
            .first()
        
        self.session.delete(pokemon)
        self.session.commit()
