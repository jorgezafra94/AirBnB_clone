#!/usr/bin/python3
"""
Test of Amenity Class
x
"""

from models.amenity import Amenity
import datetime
import unittest


class TestAmenity(unittest.TestCase):
    """ Test User Class """
    model = Amenity()

    def test_checking_for_docstring(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_subclass_instance_User(self):
        """Test if my_model 1 and 2 are subclasses of BaseModel"""
        self.assertTrue(isinstance(self.model, Amenity))

    def test_attribute_name(self):
        """Check name"""
        self.assertEqual(hasattr(self.model, 'name'), True)

if __name__ == '__main__':
    unittest.main()
