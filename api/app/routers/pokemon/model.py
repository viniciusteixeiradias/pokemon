import uuid

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.database.models import Base
from sqlalchemy_utils import UUIDType


class PokemonModel(Base):
    __tablename__ = 'pokemon'

    id = Column(Integer, primary_key=True)
    uuid = Column(UUIDType, default=uuid.uuid4, nullable=False)
    name = Column(String, nullable=False)
    base_experience = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    url_image = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return (
            f'PokemonModel(id={self.id}, uuid={self.uuid}, '
            f'name={self.name}, base_experience={self.base_experience}, '
            f'height={self.height}, weight={self.weight}, ' 
            f'url_image={self.url_image}, created={self.created})'
        )