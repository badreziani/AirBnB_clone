#!/usr/bin/python3
"""
file_storage module - Represents the definition of
the class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances.
"""

import os
import json
from json.decoder import JSONDecodeError
from ..base_model import BaseModel
from ..user import User
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..place import Place
from ..review import Review


class FileStorage:
    """FileStorage class.

    Private class attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - empty but will store all objects

    Public instance methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects."""
        return self.__class__.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id."""

        if obj is not None and hasattr(obj, "id"):
            cls_name = obj.__class__.__name__
            self.__class__.__objects[f'{cls_name}.{obj.id}'] = obj

    def save(self):
        """serializes __objects to the JSON file."""

        with open(self.__class__.__file_path, "w") as f:
            dict_of_dicts = {}
            for key, value in self.__class__.__objects.items():
                dict_of_dicts[key] = value.to_dict()
            json.dump(dict_of_dicts, f)

    def reload(self):
        """deserializes the JSON file to __objects."""

        # We check if file exists otherwise error will be raised
        if os.path.isfile(self.__class__.__file_path):
            with open(self.__class__.__file_path, "r+") as f:
                try:
                    loaded_dict = json.load(f)
                    for key, value in loaded_dict.items():
                        cls_name = value.get("__class__")
                        obj = eval(cls_name)(**value)
                        self.new(obj)
                except JSONDecodeError:
                    json.dump({}, f)

        else:
            with open(self.__class__.__file_path, "w") as f:
                json.dump({}, f)
