#!/usr/bin/python3
"""This module defines a test suite for the base model class"""

import unittest
from models.base_model import BaseModel
from models.city import City
# from models.engine.file_storage import FileStorage
# from models import storage
from datetime import datetime
from io import StringIO
import sys


class TestCity(unittest.TestCase):
    """This class defines test suites"""

    def setUp(self):
        """Sets up City class instances"""

        self.c1 = City()
        self.c2 = City()

    def tearDown(self):
        """Tears down instances"""

        del self.c1
        del self.c2

    def test_instance_class_type(self):
        """Instance created correctly"""

        self.assertEqual(self.c1.__class__.__name__, "City")
        self.assertEqual(type(self.c1), City)

    def test_inheritance(self):
        """Test for inheritance"""

        self.assertTrue(isinstance(self.c1, City))
        self.assertTrue(isinstance(self.c1, BaseModel))

    def test_instance_attributes(self):
        """Test for instance attributes"""

        # test for inherited id attribute
        self.assertTrue(hasattr(self.c1, 'id'))
        self.assertEqual(type(self.c1.id), str)
        self.assertNotEqual(self.c1.id, self.c2.id)

        # test for inherited created_at and updated_at attributes
        self.assertEqual(type(self.c1.created_at), datetime)
        self.assertNotEqual(self.c1.created_at, self.c1.updated_at)
        self.assertNotEqual(self.c1.created_at, self.c2.updated_at)

        # test for self attributes and their types
        self.assertTrue(hasattr(self.c1, 'name'))
        self.assertTrue(hasattr(self.c1, 'state_id'))
        self.assertEqual(type(self.c1.name), str)
        self.assertEqual(type(self.c1.state_id), str)

        # test for the instance values after instantiation
        self.assertEqual(self.c1.state_id, "")
        self.assertEqual(self.c1.name, "")

    def test_str_output(self):
        """Test for str method"""

        id_ = self.c2.id
        dict_ = self.c2.__dict__

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.c2)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[{:s}] ({:s}) {}".format(
                self.c2.__class__.__name__, id_, dict_
                )
        self.assertEqual(printed_output, expected_output)

        # reset stdout to terminal output
        sys.stdout = sys.__stdout__

    def test_save_method(self):
        """Test the save() method"""

        time1 = self.c1.updated_at
        self.c1.save()
        time2 = self.c1.updated_at

        self.assertEqual(type(time1), datetime)
        self.assertEqual(type(time2), datetime)
        self.assertNotEqual(time1, time2)

    def test_to_dict(self):
        """Test the to_dict() method"""

        dictionary = self.c1.to_dict()
        self.assertTrue("__class__" in dictionary.keys())
        self.assertTrue("id" in dictionary.keys())
        self.assertTrue("updated_at" in dictionary.keys())
        self.assertTrue("created_at" in dictionary.keys())
        self.assertTrue(type(dictionary["created_at"]), str)
        self.assertTrue(type(dictionary["updated_at"]), str)

    def test_init_method(self):
        """Test for updated init method"""

        c1_dict = self.c1.to_dict()

        # test for when *kwargs is empty or None
        new_c1_instance = BaseModel(None)
        self.assertTrue(hasattr(new_c1_instance, "__class__"))

        # test for when *kwargs is not empty
        new_c2_instance = BaseModel(**c1_dict)
        self.assertEqual(new_c2_instance.__class__.__name__, "BaseModel")
        self.assertTrue(hasattr(new_c2_instance, "__class__"))
        self.assertTrue(hasattr(new_c2_instance, "created_at"))
        self.assertTrue(hasattr(new_c2_instance, "updated_at"))
        self.assertTrue(hasattr(new_c2_instance, "id"))
        self.assertTrue(hasattr(new_c2_instance, "id"))
        self.assertTrue(type(new_c2_instance.id), str)
        self.assertTrue(type(new_c2_instance.created_at), datetime)
        self.assertTrue(type(new_c2_instance.updated_at), datetime)
        self.assertFalse(new_c2_instance == self.c1)

    def test_file_storage_class(self):
        """ Test instance serialization to JSON file """

        pass
