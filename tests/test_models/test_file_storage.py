#!/usr/bin/python3
"""This module defines a test suite for the FileStorage class"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import sys
import os


class TestFileStorage(unittest.TestCase):
    """This class defines test suites"""

    def setUp(self):
        """Sets up FileStorage class instances"""

        self.instance = BaseModel()
        self.instance.name = "Ifiok"
        self.instance.my_number = 2710
        self.instance.save()

    def tearDown(self):
        """
        The method tears down the json file that was open for testing
        """
        del self.instance
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        """Test for 'all' method"""

        obj = storage.all()
        for key, value in obj.items():
            key = self.instance.__class__.__name__ + "." + self.instance.id
            self.assertTrue(isinstance(obj, dict))
            self.assertIn(key, obj)
            model = BaseModel(**value.to_dict())
            self.assertTrue(isinstance(model, BaseModel))

    def test_new(self):
        """Test for the new method"""

        new_instance1 = BaseModel()
        new_instance2 = BaseModel()
        storage.new(new_instance1)
        storage.new(new_instance2)
        instances = storage.all()
        self.assertTrue(isinstance(instances, dict))
        # for key, value in instances.items():
        #     self.assertTrue(isinstance(value, dict))

    def test_save(self):
        """Tests for the save method
        """
        pass

    def test_reload(self):
        """Tests for the reload method
        """
        pass
