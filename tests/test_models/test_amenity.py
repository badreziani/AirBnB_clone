#!/usr/bin/python3
"""This module defines a test suite for the base model class"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
# from models.engine.file_storage import FileStorage
# from models import storage
from datetime import datetime
from io import StringIO
import sys


class TestAmenity(unittest.TestCase):
    """This class defines test suites"""

    def setUp(self):
        """Sets up Amenity class instances"""

        self.a1 = Amenity()
        self.a2 = Amenity()

    def tearDown(self):
        """Tears down instances"""

        del self.a1
        del self.a2

    def test_instance_class_type(self):
        """Instance created correctly"""

        self.assertEqual(self.a1.__class__.__name__, "Amenity")
        self.assertEqual(type(self.a1), Amenity)
        self.assertTrue(isinstance(self.a1, BaseModel))
        self.assertTrue(issubclass(self.a1.__class__, BaseModel))
        self.assertTrue(isinstance(self.a1, Amenity))

    def test_inheritance(self):
        """Test for inheritance"""

        self.assertTrue(isinstance(self.a1, Amenity))
        self.assertTrue(isinstance(self.a1, BaseModel))

    def test_instance_attributes(self):
        """Test for instance attributes"""

        # test for inherited id attribute
        self.assertTrue(hasattr(self.a1, 'id'))
        self.assertEqual(type(self.a1.id), str)
        self.assertNotEqual(self.a1.id, self.a2.id)

        # test for inherited created_at and updated_at attributes
        self.assertEqual(type(self.a1.created_at), datetime)
        self.assertNotEqual(self.a1.created_at, self.a1.updated_at)
        self.assertNotEqual(self.a1.created_at, self.a2.updated_at)

        # test for self attributes and their types
        self.assertTrue(hasattr(self.a1, 'name'))
        self.assertEqual(type(self.a1.name), str)

        # test for the instance values after instantiation
        self.assertEqual(self.a1.name, "")

    def test_str_output(self):
        """Test for str method"""

        id_ = self.a2.id
        dict_ = self.a2.__dict__

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.a2)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[{:s}] ({:s}) {}".format(
                self.a2.__class__.__name__, id_, dict_
                )
        self.assertEqual(printed_output, expected_output)

        # reset stdout to terminal output
        sys.stdout = sys.__stdout__

    def test_save_method(self):
        """Test the save() method"""

        time1 = self.a1.updated_at
        self.a1.save()
        time2 = self.a1.updated_at

        self.assertEqual(type(time1), datetime)
        self.assertEqual(type(time2), datetime)
        self.assertNotEqual(time1, time2)

    def test_to_dict(self):
        """Test the to_dict() method"""

        dictionary = self.a1.to_dict()
        self.assertTrue("__class__" in dictionary.keys())
        self.assertTrue("id" in dictionary.keys())
        self.assertFalse("name" in dictionary.keys())
        self.assertTrue("updated_at" in dictionary.keys())
        self.assertTrue("created_at" in dictionary.keys())
        self.assertTrue(type(dictionary["created_at"]), str)
        self.assertTrue(type(dictionary["updated_at"]), str)

    def test_init_method(self):
        """Test for updated init method"""

        a1_dict = self.a1.to_dict()

        # test for when *kwargs is empty or None
        new_a1_instance = BaseModel(None)
        self.assertTrue(hasattr(new_a1_instance, "__class__"))

        # test for when *kwargs is not empty
        new_a2_instance = BaseModel(**a1_dict)
        self.assertEqual(new_a2_instance.__class__.__name__, "BaseModel")
        self.assertTrue(hasattr(new_a2_instance, "__class__"))
        self.assertTrue(hasattr(new_a2_instance, "created_at"))
        self.assertTrue(hasattr(new_a2_instance, "updated_at"))
        self.assertTrue(hasattr(new_a2_instance, "id"))
        self.assertTrue(hasattr(new_a2_instance, "id"))
        self.assertTrue(type(new_a2_instance.id), str)
        self.assertTrue(type(new_a2_instance.created_at), datetime)
        self.assertTrue(type(new_a2_instance.updated_at), datetime)
        self.assertFalse(new_a2_instance == self.a1)
