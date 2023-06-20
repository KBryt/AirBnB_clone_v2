<<<<<<< HEAD
#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
=======
#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
>>>>>>> f97e72919d32aedd6d35aa07962e907836a8001c
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
<<<<<<< HEAD
    """ The city class, contains state ID & name """
    __tablename__ = "cities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="all, delete, delete-orphan")
    else:
        state_id = ""
        name = ""
=======
    """Representation of city """
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
>>>>>>> f97e72919d32aedd6d35aa07962e907836a8001c
