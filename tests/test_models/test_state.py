#!/usr/bin/python3
"""This module defines a test suite for the State class"""

import sys
import unittest
from io import StringIO
from datetime import datetime

from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """This class defines test suites"""

    def setUp(self):
        """Sets up State class instances"""

        self.s1 = State()
        self.s1.name = "Holberton"

        self.s2 = State()

    def tearDown(self):
        """Tears down instances"""

        del self.s1
        del self.s2

    def test_instance_class_type(self):
        """Instance created correctly"""

        self.assertEqual(self.s1.__class__.__name__, "State")
        self.assertEqual(type(self.s1), State)
        self.assertTrue(isinstance(self.s1, BaseModel))
        self.assertTrue(issubclass(self.s1.__class__, BaseModel))
        self.assertTrue(isinstance(self.s1, State))

    def test_instance_attributes(self):
        """Test for instance attributes"""

        # test for id attribute
        self.assertTrue(hasattr(self.s1, 'id'))
        self.assertEqual(type(self.s1.id), str)
        self.assertNotEqual(self.s1.id, self.s2.id)

        # tests for last_name attribute
        self.assertTrue(hasattr(self.s1, 'name'))
        self.assertEqual(type(self.s1.name), str)

        # test for created_at and updated_at attributes
        self.assertEqual(type(self.s1.created_at), datetime)
        self.assertNotEqual(self.s1.created_at, self.s1.updated_at)
        self.assertNotEqual(self.s1.created_at, self.s2.updated_at)

    def test_str_output(self):
        """Test for str method"""

        id_ = self.s2.id
        dict_ = self.s2.__dict__

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.s2)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[{:s}] ({:s}) {}".format(
                self.s2.__class__.__name__, id_, dict_
                )
        self.assertEqual(printed_output, expected_output)

        # reset stdout to terminal output
        sys.stdout = sys.__stdout__

    def test_save_method(self):
        """Test the save() method"""

        time1 = self.s1.updated_at
        self.s1.save()
        time2 = self.s1.updated_at

        self.assertEqual(type(time1), datetime)
        self.assertEqual(type(time2), datetime)
        self.assertNotEqual(time1, time2)

    def test_to_dict(self):
        """Test the to_dict() method"""

        dictionary = self.s1.to_dict()
        self.assertTrue("__class__" in dictionary.keys())
        self.assertTrue("id" in dictionary.keys())
        self.assertTrue("name" in dictionary.keys())
        self.assertTrue("updated_at" in dictionary.keys())
        self.assertTrue("created_at" in dictionary.keys())
        self.assertTrue(type(dictionary["created_at"]), str)
        self.assertTrue(type(dictionary["updated_at"]), str)

    def test_init_method(self):
        """Test for updated init method"""

        b1_dict = self.s2.to_dict()

        # test for when *kwargs is empty or None
        new_b1_instance = State(None)
        self.assertTrue(hasattr(new_b1_instance, "__class__"))

        # test for when *kwargs is not empty
        new_b2_instance = State(**b1_dict)
        self.assertEqual(new_b2_instance.__class__.__name__, "State")
        self.assertTrue(hasattr(new_b2_instance, "__class__"))
        self.assertTrue(hasattr(new_b2_instance, "created_at"))
        self.assertTrue(hasattr(new_b2_instance, "updated_at"))
        self.assertTrue(hasattr(new_b2_instance, "id"))
        self.assertTrue(type(new_b2_instance.id), str)
        self.assertTrue(type(new_b2_instance.created_at), datetime)
        self.assertTrue(type(new_b2_instance.updated_at), datetime)
        self.assertFalse(new_b2_instance == self.s2)

    def test_file_storage_class(self):
        """ Test instance serialization to JSON file """

        pass
