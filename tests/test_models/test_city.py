#!/usr/bin/python3
"""Test of City Class """

from models.city import City
import datetime
import unittest
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ Test City Class """
    model = City()

    def test_checking_for_docstring_User(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(City.__doc__)

    def test_subclass_instance_User(self):
        """Test if my_model 1 and 2 are subclasses of BaseModel"""
        self.assertTrue(isinstance(self.model, City))

    def test_attribute(self):
        """ Tests attributes """
        self.assertEqual(hasattr(self.model, "state_id"), True)
        self.assertEqual(hasattr(self.model, "name"), True)

if __name__ == '__main__':
    unittest.main()
