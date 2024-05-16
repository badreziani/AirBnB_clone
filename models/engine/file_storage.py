#!/usr/bin/python3
"""This module defines a storage class"""

import json
import os


class FileStorage:
    """Serializes instances to a JSON file and vice versa"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """sets obj in __objects dictionary"""

        # __objects contains instances at this point
        # so we have to keep them in a serializable form
        for key, value in FileStorage.__objects.items():
            FileStorage.__objects[key] = value.to_dict()

        # make the new obj serializable as well
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes dictionary __objects to JSON file"""

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """desirializes saved content in JSON file to __objects dictionary"""

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                instance_dictionary = json.load(file)
                from models.base_model import BaseModel
                # de-serialize each dictionary object loaded with a loop
                for key, value in instance_dictionary.items():
                    instance = BaseModel(**value)
                    FileStorage.__objects[key] = instance
