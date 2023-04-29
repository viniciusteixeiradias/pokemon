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

    # def save(self, pokemonSchemain: PokemonSchemaIn) -> PokemonModel:
    #     try:
    #         profile_dict = PokemonModel(**pokemonSchemain.dict())

    #         self.session.add(profile_dict)
    #         self.session.commit()
    #         self.session.refresh(profile_dict)

    #         return profile_dict
    #     except IntegrityError as e:
    #         self.session.rollback()
    #         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Pokemon not found: {e}")

    # def update(
    #     self,
    #     uuid: UUID4,
    #     profile_in: ProfileModelIn
    # ) -> Profile:

    #     profile_dict = profile_in.dict()

    #     profile_db = self.session.query(Profile).filter(
    #         Profile.uuid == uuid).first()

    #     if not profile_db:
    #         raise HTTPException(
    #             status_code=404, detail="Profile not found")

    #     for key, value in profile_dict.items():
    #         setattr(profile_db, key, value)

    #     self.session.add(profile_db)
    #     self.session.commit()
    #     self.session.refresh(profile_db)

    #     return profile_db

    # def delete(self, uuid: UUID4) -> None:

    #     obj = self.session.query(Profile).filter(
    #         Profile.uuid == uuid).first()
    #     self.session.delete(obj)
    #     self.session.commit()
