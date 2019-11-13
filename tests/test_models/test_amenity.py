#!/usr/bin/python3
"""Test of Amenity Class """

from models.amenity import Amenity
import datetime
import unittest
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Test User Class """
    model = Amenity()
    model.name = "Betty"

    def test_checking_for_docstring(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_subclass_instance_User(self):
        """Test if my_model 1 and 2 are subclasses of BaseModel"""
        self.assertTrue(isinstance(self.model, Amenity))

    def test_attribute_name(self):
        """Check name"""
        self.assertTrue(hasattr(self.model, 'name'))

    def test_hasattr(self):
        """ attributes inheritated of BaseModel"""
        self.assertTrue(hasattr(self.model, 'name'))
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_attributes_types(self):
        """Tests types """
        self.assertEqual(type(self.model.name), str)
        self.assertIsInstance(self.model.created_at, datetime.datetime)
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
