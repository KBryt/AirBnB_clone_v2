<<<<<<< HEAD
#!/usr/bin/python3
""" State Module for the HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
=======
#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
>>>>>>> f97e72919d32aedd6d35aa07962e907836a8001c
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
<<<<<<< HEAD
    """class for amenities"""
    __tablename__ = 'amenities'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                       back_populates="amenities")
    else:
        name = ""
=======
    """Representation of Amenity """
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
>>>>>>> f97e72919d32aedd6d35aa07962e907836a8001c
