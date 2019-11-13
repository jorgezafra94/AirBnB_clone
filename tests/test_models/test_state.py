#!/usr/bin/python3
"""Test of State Class """

from models.state import State
import datetime
import unittest
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ Test User Class """
    model = State()

    def test_checking_for_docstring_User(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(State.__doc__)

    def test_subclass_instance_User(self):
        """Test if my_model 1 and 2 are subclasses of BaseModel"""
        self.assertTrue(isinstance(self.model, State))

    def test_attribute(self):
        """ Tests attr """
        self.assertEqual(hasattr(self.model, "name"), True)

if __name__ == '__main__':
    unittest.main()
