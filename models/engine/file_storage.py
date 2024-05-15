#!/usr/bin/python3
"""
file_storage module - Represents the definition of 
the class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances.
"""


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

    __file_path = None
    __objects = {}

    def all(self):
        """returns the dictionary __objects."""

        return self.__class__.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id."""

        if obj is not None and "id" in obj:
            self.__class__.__objects[obj["id"]] = obj

    def save(self):
        """serializes __objects to the JSON file."""

        pass

    def reload(self):
        """deserializes the JSON file to __objects."""

        pass
