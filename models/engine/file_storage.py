#!/usr/bin/python3
"""
file_storage module - Represents the definition of 
the class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances.
"""

import json


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
            self.__class__.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """serializes __objects to the JSON file."""
        
        try:
            with open(self.__class__.__file_path, "w") as f:
                dict_to_save = {k: v.to_dict() for k, v in self.__class__.__objects.items()}
                json.dump(dict_to_save, f)
        except Exception as err:
            print(err)
            

    def reload(self):
        """deserializes the JSON file to __objects."""
        try:
            with open(self.__class__.__file_path) as f:
                loaded_dict = json.load(f)
                self.__class__.__objects = loaded_dict
        except Exception as err:
            print(f"Error {err}")
