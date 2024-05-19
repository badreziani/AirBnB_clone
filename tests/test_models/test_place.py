#!/usr/bin/python3
"""This module defines a test suite for the base model class"""

import unittest
from models.base_model import BaseModel
from models.place import Place
# from models.engine.file_storage import FileStorage
# from models import storage
from datetime import datetime
from io import StringIO
import sys


class TestPlace(unittest.TestCase):
    """This class defines test suites"""

    def setUp(self):
        """Sets up Place class instances"""

        self.p1 = Place()
        self.p2 = Place()

    def tearDown(self):
        """Tears down instances"""

        del self.p1
        del self.p2

    def test_instance_class_type(self):
        """Instance created correctly"""

        self.assertEqual(self.p1.__class__.__name__, "Place")
        self.assertEqual(type(self.p1), Place)

    def test_inheritance(self):
        """Test for inheritance"""

        self.assertTrue(isinstance(self.p1, Place))
        self.assertTrue(isinstance(self.p1, BaseModel))

    def test_instance_attributes(self):
        """Test for instance attributes"""

        # test for inherited id attribute
        self.assertTrue(hasattr(self.p1, 'id'))
        self.assertEqual(type(self.p1.id), str)
        self.assertNotEqual(self.p1.id, self.p2.id)

        # test for inherited created_at and updated_at attributes
        self.assertEqual(type(self.p1.created_at), datetime)
        self.assertNotEqual(self.p1.created_at, self.p1.updated_at)
        self.assertNotEqual(self.p1.created_at, self.p2.updated_at)

        # test for self attributes and their types
        self.assertTrue(hasattr(self.p1, 'city_id'))
        self.assertTrue(hasattr(self.p1, 'user_id'))
        self.assertTrue(hasattr(self.p1, 'name'))
        self.assertTrue(hasattr(self.p1, 'description'))
        self.assertTrue(hasattr(self.p1, 'number_rooms'))
        self.assertTrue(hasattr(self.p1, 'number_bathrooms'))
        self.assertTrue(hasattr(self.p1, 'max_guest'))
        self.assertTrue(hasattr(self.p1, 'price_by_night'))
        self.assertTrue(hasattr(self.p1, 'latitude'))
        self.assertTrue(hasattr(self.p1, 'longitude'))
        self.assertTrue(hasattr(self.p1, 'amenity_ids'))
        self.assertEqual(type(self.p1.city_id), str)
        self.assertEqual(type(self.p1.user_id), str)
        self.assertEqual(type(self.p1.name), str)
        self.assertEqual(type(self.p1.description), str)
        self.assertEqual(type(self.p1.number_rooms), int)
        self.assertEqual(type(self.p1.number_bathrooms), int)
        self.assertEqual(type(self.p1.max_guest), int)
        self.assertEqual(type(self.p1.price_by_night), int)
        self.assertEqual(type(self.p1.latitude), float)
        self.assertEqual(type(self.p1.longitude), float)
        self.assertEqual(type(self.p1.amenity_ids), list)

        # test for the instance values after instantiation
        self.assertEqual(self.p1.city_id, "")
        self.assertEqual(self.p1.user_id, "")
        self.assertEqual(self.p1.name, "")
        self.assertEqual(self.p1.description, "")
        self.assertEqual(self.p1.number_rooms, 0)
        self.assertEqual(self.p1.number_bathrooms, 0)
        self.assertEqual(self.p1.max_guest, 0)
        self.assertEqual(self.p1.price_by_night, 0)
        self.assertEqual(self.p1.latitude, 0.0)
        self.assertEqual(self.p1.longitude, 0.0)
        self.assertEqual(self.p1.amenity_ids, [])

    def test_str_output(self):
        """Test for str method"""

        id_ = self.p2.id
        dict_ = self.p2.__dict__

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.p2)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[{:s}] ({:s}) {}".format(
                self.p2.__class__.__name__, id_, dict_
                )
        self.assertEqual(printed_output, expected_output)

        # reset stdout to terminal output
        sys.stdout = sys.__stdout__

    def test_save_method(self):
        """Test the save() method"""

        time1 = self.p1.updated_at
        self.p1.save()
        time2 = self.p1.updated_at

        self.assertEqual(type(time1), datetime)
        self.assertEqual(type(time2), datetime)
        self.assertNotEqual(time1, time2)

    def test_to_dict(self):
        """Test the to_dict() method"""

        dictionary = self.p1.to_dict()
        self.assertTrue("__class__" in dictionary.keys())
        self.assertTrue("id" in dictionary.keys())
        self.assertTrue("updated_at" in dictionary.keys())
        self.assertTrue("created_at" in dictionary.keys())
        self.assertTrue(type(dictionary["created_at"]), str)
        self.assertTrue(type(dictionary["updated_at"]), str)

    def test_init_method(self):
        """Test for updated init method"""

        p1_dict = self.p1.to_dict()

        # test for when *kwargs is empty or None
        new_p1_instance = BaseModel(None)
        self.assertTrue(hasattr(new_p1_instance, "__class__"))

        # test for when *kwargs is not empty
        new_p2_instance = BaseModel(**p1_dict)
        self.assertEqual(new_p2_instance.__class__.__name__, "BaseModel")
        self.assertTrue(hasattr(new_p2_instance, "__class__"))
        self.assertTrue(hasattr(new_p2_instance, "created_at"))
        self.assertTrue(hasattr(new_p2_instance, "updated_at"))
        self.assertTrue(hasattr(new_p2_instance, "id"))
        self.assertTrue(hasattr(new_p2_instance, "id"))
        self.assertTrue(type(new_p2_instance.id), str)
        self.assertTrue(type(new_p2_instance.created_at), datetime)
        self.assertTrue(type(new_p2_instance.updated_at), datetime)
        self.assertFalse(new_p2_instance == self.p1)

    def test_file_storage_class(self):
        """ Test instance serialization to JSON file """

        pass
