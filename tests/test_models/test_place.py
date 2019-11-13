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
        self.assertTrue(isinstance(self.model, Place))

    def test_attribute_city_id(self):
        """ Tests city_id """
        self.assertTrue(hasattr(self.model, 'city_id'))

    def test_attribute_user_id(self):
        """ Test user_id """
        self.assertTrue(hasattr(self.model, 'user_id'))

    def test_attribute_name(self):
        """ Check name """
        self.assertTrue(hasattr(self.model, 'name'))

    def test_attribute_description(self):
        """Check description"""
        self.assertTrue(hasattr(self.model, 'description'))

    def test_attribute_number_rooms(self):
        """Check number_rooms"""
        self.assertTrue(hasattr(self.model, 'number_rooms'))

    def test_attribute_number_bathrooms(self):
        """Check number_bathrooms"""
        self.assertTrue(hasattr(self.model, 'number_bathrooms'))

    def test_attribute_max_guest(self):
        """Check max_guest"""
        self.assertTrue(hasattr(self.model, 'max_guest'))

    def test_attribute_price_by_night(self):
        """Check price_by_night"""
        self.assertTrue(hasattr(self.model, 'price_by_night'))

    def test_attribute_latitude(self):
        """Check latitude"""
        self.assertTrue(hasattr(self.model, 'latitude'))

    def test_attribute_longitude(self):
        """Check longitude"""
        self.assertTrue(hasattr(self.model, 'longitude'))

    def test_attribute_amenity_ids(self):
        """Check amenity_ids"""
        self.assertTrue(hasattr(self.model, 'amenity_ids'))

    def test_hasattr(self):
        """ attributes inheritated of BaseModel"""
        self.assertTrue(hasattr(self.model, 'name'))
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_attributes_types(self):
        """Tests types """
        self.assertEqual(type(self.model.city_id), str)
        self.assertEqual(type(self.model.user_id), str)
        self.assertEqual(type(self.model.name), str)
        self.assertEqual(type(self.model.description), str)
        self.assertEqual(type(self.model.number_rooms), int)
        self.assertEqual(type(self.model.number_bathrooms), int)
        self.assertEqual(type(self.model.max_guest), int)
        self.assertEqual(type(self.model.price_by_night), int)
        self.assertEqual(type(self.model.latitude), float)
        self.assertEqual(type(self.model.longitude), float)
        self.assertEqual(type(self.model.amenity_ids), list)
        self.assertIsInstance(self.model.created_at, datetime.datetime)
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
