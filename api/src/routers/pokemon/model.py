import uuid

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from src.database.models import Base
from sqlalchemy_utils import UUIDType


class PokemonModel(Base):
    __tablename__ = 'pokemon'

    id = Column(Integer, primary_key=True)
    uuid = Column(UUIDType, default=uuid.uuid4, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return (
            f'PokemonModel(id={self.id}, name={self.name},'
            f'description={self.description}, created={self.created})'
        )