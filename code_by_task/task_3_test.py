#!/usr/bin/python3
"""This module defines a test suite for the base model class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBase(unittest.TestCase):
    """This class defines test suites"""

    def setUp(self):
        """Sets up Base class instances"""

        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def tearDown(self):
        """Tears down instances"""

        del self.b1
        del self.b2

    def test_instance_class_type(self):
        """Instance created correctly"""

        self.assertEqual(self.b1.__class__.__name__, "BaseModel")
        self.assertEqual(type(self.b1), BaseModel)
        self.assertTrue(isinstance(self.b1, BaseModel))

    def test_instance_attributes(self):
        """Test for instance attributes"""

        # test for id attribute
        self.assertTrue(hasattr(self.b1, 'id'))
        self.assertEqual(type(self.b1.id), str)
        self.assertNotEqual(self.b1.id, self.b2.id)

        # test for created_at and updated_at attributes
        self.assertEqual(type(self.b1.created_at), datetime)
        self.assertNotEqual(self.b1.created_at, self.b1.updated_at)
        self.assertNotEqual(self.b1.created_at, self.b2.updated_at)

    def test_str_output(self):
        """Test for str method"""

        pass

    def test_save_method(self):
        """Test the save() method"""

        time1 = self.b1.updated_at
        self.b1.save()
        time2 = self.b1.updated_at

        self.assertEqual(type(time1), datetime)
        self.assertEqual(type(time2), datetime)
        self.assertNotEqual(time1, time2)

    def test_to_dict(self):
        """Test the to_dict() method"""

        dictionary = self.b1.to_dict()
        self.assertTrue("__class__" in dictionary.keys())
        self.assertTrue(type(dictionary["created_at"]), str)
        self.assertTrue(type(dictionary["updated_at"]), str)
