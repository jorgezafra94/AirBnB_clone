#!/usr/bin/python3
"""Test of State Class """

from models.state import State
import datetime
import unittest
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ Test User Class """
    model = State()
    model.name = "Betty"

    def test_checking_for_docstring_User(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(State.__doc__)

    def test_subclass_instance_User(self):
        """Test if my_model 1 and 2 are subclasses of BaseModel"""
        self.assertEqual(isinstance(self.model, State), True)

    def test_attribute_name(self):
        """ Tests name """
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
        self.assertIsInstance(self.model.created_at, datetime.datetime)
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
