#!/usr/bin/python3
"""Test of City Class """

from models.city import City
import datetime
import unittest
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ Test City Class """
    model = City()
    model.name = "Betty"

    def test_checking_for_docstring_User(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(City.__doc__)

    def test_subclass_instance_User(self):
        """Test if my_model 1 and 2 are subclasses of BaseModel"""
        self.assertEqual(isinstance(self.model, City), True)

    def test_attribute_state_id(self):
        """ Tests email """
        self.assertEqual(hasattr(self.model, 'state_id'), True)

    def test_attribute_name(self):
        """ Test password """
        self.assertEqual(hasattr(self.model, 'name'), True)

    def test_hasattr(self):
        """ attributes inheritated of BaseModel"""
        self.assertEqual(hasattr(self.model, 'name'), True)
        self.assertEqual(hasattr(self.model, 'id'), True)
        self.assertEqual(hasattr(self.model, 'created_at'), True)
        self.assertEqual(hasattr(self.model, 'updated_at'), True)

    def test_attributes_types(self):
        """Tests types """
        self.assertEqual(type(self.model.name), str)
        self.assertEqual(type(self.model.state_id), str)
        self.assertIsInstance(self.model.created_at, datetime.datetime)
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
