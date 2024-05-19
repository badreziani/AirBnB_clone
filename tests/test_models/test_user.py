#!/usr/bin/python3
"""This module defines a test suite for the User class"""

import sys
import unittest
from io import StringIO
from datetime import datetime

from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """This class defines test suites"""

    def setUp(self):
        """Sets up User class instances"""

        self.u1 = User()
        self.u1.first_name = "Betty"
        self.u1.last_name = "Bar"
        self.u1.email = "airbnb@mail.com"
        self.u1.password = "root"

        self.u2 = User()

    def tearDown(self):
        """Tears down instances"""

        del self.u1
        del self.u2

    def test_instance_class_type(self):
        """Instance created correctly"""

        self.assertEqual(self.u1.__class__.__name__, "User")
        self.assertEqual(type(self.u1), User)
        self.assertTrue(isinstance(self.u1, BaseModel))
        self.assertTrue(issubclass(self.u1.__class__, BaseModel))
        self.assertTrue(isinstance(self.u1, User))

    def test_instance_attributes(self):
        """Test for instance attributes"""

        # test for id attribute
        self.assertTrue(hasattr(self.u1, 'id'))
        self.assertEqual(type(self.u1.id), str)
        self.assertNotEqual(self.u1.id, self.u2.id)

        # tests for email attribute
        self.assertTrue(hasattr(self.u1, 'email'))
        self.assertEqual(type(self.u1.email), str)
        self.assertTrue("@" in str(self.u1.email))

        # tests for password attribute
        self.assertTrue(hasattr(self.u1, 'password'))
        self.assertEqual(type(self.u1.password), str)

        # tests for first_name attribute
        self.assertTrue(hasattr(self.u1, 'first_name'))
        self.assertEqual(type(self.u1.first_name), str)

        # tests for last_name attribute
        self.assertTrue(hasattr(self.u1, 'last_name'))
        self.assertEqual(type(self.u1.last_name), str)

        # test for created_at and updated_at attributes
        self.assertEqual(type(self.u1.created_at), datetime)
        self.assertNotEqual(self.u1.created_at, self.u1.updated_at)
        self.assertNotEqual(self.u1.created_at, self.u2.updated_at)

    def test_str_output(self):
        """Test for str method"""

        id_ = self.u2.id
        dict_ = self.u2.__dict__

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.u2)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[{:s}] ({:s}) {}".format(
                self.u2.__class__.__name__, id_, dict_
                )
        self.assertEqual(printed_output, expected_output)

        # reset stdout to terminal output
        sys.stdout = sys.__stdout__

    def test_save_method(self):
        """Test the save() method"""

        time1 = self.u1.updated_at
        self.u1.save()
        time2 = self.u1.updated_at

        self.assertEqual(type(time1), datetime)
        self.assertEqual(type(time2), datetime)
        self.assertNotEqual(time1, time2)

    def test_to_dict(self):
        """Test the to_dict() method"""

        dictionary = self.u1.to_dict()
        self.assertTrue("__class__" in dictionary.keys())
        self.assertTrue("id" in dictionary.keys())
        self.assertTrue("email" in dictionary.keys())
        self.assertTrue("password" in dictionary.keys())
        self.assertTrue("first_name" in dictionary.keys())
        self.assertTrue("last_name" in dictionary.keys())
        self.assertTrue("updated_at" in dictionary.keys())
        self.assertTrue("created_at" in dictionary.keys())
        self.assertTrue(type(dictionary["created_at"]), str)
        self.assertTrue(type(dictionary["updated_at"]), str)

    def test_init_method(self):
        """Test for updated init method"""

        b1_dict = self.u2.to_dict()

        # test for when *kwargs is empty or None
        new_b1_instance = User(None)
        self.assertTrue(hasattr(new_b1_instance, "__class__"))

        # test for when *kwargs is not empty
        new_b2_instance = User(**b1_dict)
        self.assertEqual(new_b2_instance.__class__.__name__, "User")
        self.assertTrue(hasattr(new_b2_instance, "__class__"))
        self.assertTrue(hasattr(new_b2_instance, "created_at"))
        self.assertTrue(hasattr(new_b2_instance, "updated_at"))
        self.assertTrue(hasattr(new_b2_instance, "id"))
        self.assertTrue(type(new_b2_instance.id), str)
        self.assertTrue(type(new_b2_instance.created_at), datetime)
        self.assertTrue(type(new_b2_instance.updated_at), datetime)
        self.assertFalse(new_b2_instance == self.u2)

    def test_file_storage_class(self):
        """ Test instance serialization to JSON file """

        pass
