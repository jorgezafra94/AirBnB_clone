#!/usr/bin/python3
"""Test of Place Class """

from models.place import Place
import datetime
import unittest
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """ Test Place Class """
    model = Place()
    model.name = "Betty"

    def test_checking_for_docstring(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(Place.__doc__)

    def test_subclass_instance(self):
        """Test if my_model 1 and 2 are subclasses of BaseModel"""
        self.assertEqual(isinstance(self.model, Place), True)

    def test_attribute_city_id(self):
        """ Tests city_id """
        self.assertEqual(hasattr(self.model, 'city_id'), True)

    def test_attribute_user_id(self):
        """ Test user_id """
        self.assertEqual(hasattr(self.model, 'user_id'), True)

    def test_attribute_name(self):
        """ Check name """
        self.assertEqual(hasattr(self.model, 'name'), True)

    def test_attribute_description(self):
        """Check description"""
        self.assertEqual(hasattr(self.model, 'description'), True)

    def test_attribute_number_rooms(self):
        """Check number_rooms"""
        self.assertEqual(hasattr(self.model, 'number_rooms'), True)

    def test_attribute_number_bathrooms(self):
        """Check number_bathrooms"""
        self.assertEqual(hasattr(self.model, 'number_bathrooms'), True)

    def test_attribute_max_guest(self):
        """Check max_guest"""
        self.assertEqual(hasattr(self.model, 'max_guest'), True)

    def test_attribute_price_by_night(self):
        """Check price_by_night"""
        self.assertEqual(hasattr(self.model, 'price_by_night'), True)

    def test_attribute_latitude(self):
        """Check latitude"""
        self.assertEqual(hasattr(self.model, 'latitude'), True)

    def test_attribute_longitude(self):
        """Check longitude"""
        self.assertEqual(hasattr(self.model, 'longitude'), True)

    def test_attribute_amenity_ids(self):
        """Check amenity_ids"""
        self.assertEqual(hasattr(self.model, 'amenity_ids'), True)

    def test_hasattr(self):
        """ attributes inheritated of BaseModel"""
        self.assertEqual(hasattr(self.model, 'name'), True)
        self.assertEqual(hasattr(self.model, 'id'), True)
        self.assertEqual(hasattr(self.model, 'created_at'), True)
        self.assertEqual(hasattr(self.model, 'updated_at'), True)

if __name__ == '__main__':
    unittest.main()
