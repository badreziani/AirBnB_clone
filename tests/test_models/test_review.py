#!/usr/bin/python3
"""This module defines a test suite for the Review class"""

import sys
import unittest
from io import StringIO
from datetime import datetime

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """This class defines test suites"""

    def setUp(self):
        """Sets up Review class instances"""

        self.r1 = Review()
        self.r2 = Review()

    def tearDown(self):
        """Tears down instances"""

        del self.r1
        del self.r2

    def test_instance_class_type(self):
        """Instance created correctly"""

        self.assertEqual(self.r1.__class__.__name__, "Review")
        self.assertEqual(type(self.r1), Review)
        self.assertTrue(isinstance(self.r1, BaseModel))
        self.assertTrue(issubclass(self.r1.__class__, BaseModel))
        self.assertTrue(isinstance(self.r1, Review))

    def test_instance_attributes(self):
        """Test for instance attributes"""

        # test for id attribute
        self.assertTrue(hasattr(self.r1, 'id'))
        self.assertEqual(type(self.r1.id), str)
        self.assertNotEqual(self.r1.id, self.r2.id)

        # test for created_at and updated_at attributes
        self.assertEqual(type(self.r1.created_at), datetime)
        self.assertNotEqual(self.r1.created_at, self.r1.updated_at)
        self.assertNotEqual(self.r1.created_at, self.r2.updated_at)

    def test_str_output(self):
        """Test for str method"""

        id_ = self.r2.id
        dict_ = self.r2.__dict__

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.r2)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[{:s}] ({:s}) {}".format(
                self.r2.__class__.__name__, id_, dict_
                )
        self.assertEqual(printed_output, expected_output)

        # reset stdout to terminal output
        sys.stdout = sys.__stdout__

    def test_save_method(self):
        """Test the save() method"""

        time1 = self.r1.updated_at
        self.r1.save()
        time2 = self.r1.updated_at

        self.assertEqual(type(time1), datetime)
        self.assertEqual(type(time2), datetime)
        self.assertNotEqual(time1, time2)

    def test_to_dict(self):
        """Test the to_dict() method"""

        dictionary = self.r1.to_dict()
        self.assertTrue("__class__" in dictionary.keys())
        self.assertTrue("id" in dictionary.keys())
        self.assertTrue("updated_at" in dictionary.keys())
        self.assertTrue("created_at" in dictionary.keys())
        self.assertTrue(type(dictionary["created_at"]), str)
        self.assertTrue(type(dictionary["updated_at"]), str)

    def test_init_method(self):
        """Test for updated init method"""

        b1_dict = self.r2.to_dict()

        # test for when *kwargs is empty or None
        new_b1_instance = Review(None)
        self.assertTrue(hasattr(new_b1_instance, "__class__"))

        # test for when *kwargs is not empty
        new_b2_instance = Review(**b1_dict)
        self.assertEqual(new_b2_instance.__class__.__name__, "Review")
        self.assertTrue(hasattr(new_b2_instance, "__class__"))
        self.assertTrue(hasattr(new_b2_instance, "created_at"))
        self.assertTrue(hasattr(new_b2_instance, "updated_at"))
        self.assertTrue(hasattr(new_b2_instance, "id"))
        self.assertTrue(type(new_b2_instance.id), str)
        self.assertTrue(type(new_b2_instance.created_at), datetime)
        self.assertTrue(type(new_b2_instance.updated_at), datetime)
        self.assertFalse(new_b2_instance == self.r2)

    def test_file_storage_class(self):
        """ Test instance serialization to JSON file """

        pass
