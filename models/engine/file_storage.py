#!/usr/bin/python3
"""This module defines a storage class"""

import os
import json
from json.decoder import JSONDecodeError

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and vice versa"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """sets obj in __objects dictionary"""

        # make the new obj serializable as well
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes dictionary __objects to JSON file"""

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            temp_dict = FileStorage.__objects.copy()
            for key, value in temp_dict.items():
                temp_dict[key] = value.to_dict()
            json.dump(temp_dict, file)

    def reload(self):
        """desirializes saved content in JSON file to __objects dictionary"""

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, "r+", encoding="utf-8") as file:
                try:
                    instance_dictionary = json.load(file)
                    # de-serialize each dictionary object loaded with a loop
                    for key, value in instance_dictionary.items():
                        cls = value.get("__class__")
                        instance = eval(cls)(**value)
                        FileStorage.__objects[key] = instance
                except JSONDecodeError:
                    json.dump({}, file)
