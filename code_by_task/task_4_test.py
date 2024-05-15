#!/usr/bin/python3
"""This module defines a test suite for the base model class"""

import unittest
from models.base_model import BaseModel
# from models.engine.file_storage import FileStorage
# from models import storage
from datetime import datetime
from io import StringIO
import sys


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

        id_ = self.b2.id
        dict_ = self.b2.__dict__

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.b2)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[{:s}] ({:s}) {}".format(
                self.b2.__class__.__name__, id_, dict_
                )
        self.assertEqual(printed_output, expected_output)
        
        # reset stdout to terminal output
        sys.stdout = sys.__stdout__

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
        self.assertTrue("id" in dictionary.keys())
        self.assertTrue("updated_at" in dictionary.keys())
        self.assertTrue("created_at" in dictionary.keys())
        self.assertTrue(type(dictionary["created_at"]), str)
        self.assertTrue(type(dictionary["updated_at"]), str)

    def test_init_method(self):
        """Test for updated init method"""

        b1_dict = self.b1.to_dict()

        # test for when *kwargs is empty or None
        new_b1_instance = BaseModel(None)
        self.assertTrue(hasattr(new_b1_instance, "__class__"))

        # test for when *kwargs is not empty
        new_b2_instance = BaseModel(**b1_dict)
        self.assertEqual(new_b2_instance.__class__.__name__, "BaseModel")
        self.assertTrue(hasattr(new_b2_instance, "__class__"))
        self.assertTrue(hasattr(new_b2_instance, "created_at"))
        self.assertTrue(hasattr(new_b2_instance, "updated_at"))
        self.assertTrue(hasattr(new_b2_instance, "id"))
        self.assertTrue(hasattr(new_b2_instance, "id"))
        self.assertTrue(type(new_b2_instance.id), str)
        self.assertTrue(type(new_b2_instance.created_at), datetime)
        self.assertTrue(type(new_b2_instance.updated_at), datetime)
        self.assertFalse(new_b2_instance == self.b1)

    def test_file_storage_class(self):
        """ Test instance serialization to JSON file """

        pass
