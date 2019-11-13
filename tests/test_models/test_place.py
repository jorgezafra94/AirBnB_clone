#!/usr/bin/python3
"""Test of Place Class """

from models.place import Place
import datetime
import unittest


class TestPlace(unittest.TestCase):
    """ Test Place Class """
    model = Place()

    def test_checking_for_docstring(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(Place.__doc__)

    def test_instance(self):
        """Test if my_model 1 and 2 are subclasses of BaseModel"""
        self.assertTrue(isinstance(self.model, Place))

    def test_attribute_city_id(self):
        """ Tests attributes """
        self.assertEqual(hasattr(self.model, "city_id"), True)
        self.assertEqual(hasattr(self.model, "user_id"), True)
        self.assertEqual(hasattr(self.model, "name"), True)
        self.assertEqual(hasattr(self.model, "description"), True)
        self.assertEqual(hasattr(self.model, "number_rooms"), True)
        self.assertEqual(hasattr(self.model, "number_bathrooms"), True)
        self.assertEqual(hasattr(self.model, "max_guest"), True)
        self.assertEqual(hasattr(self.model, "price_by_night"), True)
        self.assertEqual(hasattr(self.model, "latitude"), True)
        self.assertEqual(hasattr(self.model, "longitude"), True)
        self.assertEqual(hasattr(self.model, "amenity_ids"), True)

if __name__ == '__main__':
    unittest.main()
