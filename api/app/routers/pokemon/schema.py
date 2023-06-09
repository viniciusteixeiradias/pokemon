from app.utils.camel_model import CamelModel
from pydantic.types import UUID4
class PokemonSchema(CamelModel):
    name: str
    base_experience: int
    height: int
    weight: int
    url_image: str
    
    class Config:
        orm_mode = True


class PokemonSchemaIn(PokemonSchema):
    pass


class PokemonSchemaOut(PokemonSchema):
    uuid: UUID4
