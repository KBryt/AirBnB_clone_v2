#!/usr/bin/python3
<<<<<<< HEAD
"""This module defines a class to manage file storage for hbnb clone"""
import json
import models
from models.base_model import BaseModel
from models.amenity import Amenity
=======
"""
Contains the FileStorage class
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
>>>>>>> f97e72919d32aedd6d35aa07962e907836a8001c
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
<<<<<<< HEAD


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in the storage"""
        if not cls:
            return FileStorage.__objects
        else:
            newdict = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    newdict[key] = value
            return newdict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {}
        temp.update(FileStorage.__objects)
        for key, val in temp.items():
            temp[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, "r", encoding="UTF8") as fd:
                for val in json.load(fd).values():
                    class_name = val["__class__"]
                    del val["__class__"]
                    self.new(eval(class_name)(**val))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects"""
        if obj:
=======

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
>>>>>>> f97e72919d32aedd6d35aa07962e907836a8001c
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
<<<<<<< HEAD
        """Deserializing the JSON file to objects"""
=======
        """call reload() method for deserializing the JSON file to objects"""
>>>>>>> f97e72919d32aedd6d35aa07962e907836a8001c
        self.reload()
