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
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                instance_dictionary = json.load(file)
                from models.base_model import BaseModel
                # de-serialize each dictionary object loaded with a loop
                for key, value in instance_dictionary.items():
                    instance = BaseModel(**value)
                    FileStorage.__objects[key] = instance
