#!/usr/bin/python
"""Model for City class."""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from os import getenv
import models
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place

class City(BaseModel, Base):
    """This is the class representation for City
    Attributes:
        state_id: The state id
        name: input name
    """
    if models.storage_t == "db":
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", delete = 'delete-orphan',
                              backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize City """
        super().__init__(*args, **kwargs)
