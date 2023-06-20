<<<<<<< HEAD
#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
=======
#!/usr/bin/python
""" holds class Review"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
>>>>>>> f97e72919d32aedd6d35aa07962e907836a8001c
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
<<<<<<< HEAD
    """ Review class to store review information """
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
=======
    """Representation of Review """
    if models.storage_t == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
>>>>>>> f97e72919d32aedd6d35aa07962e907836a8001c
