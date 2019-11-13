#!/usr/bin/python3
"""Test of Review Class """

from models.review import Review
import datetime
import unittest
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ Test User Class """
    model = Review()

    def test_checking_for_docstring_User(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(Review.__doc__)

    def test_subclass_instance_Review(self):
        """Test if my_model 1 and 2 are subclasses of BaseModel"""
        self.assertTrue(isinstance(self.model, Review))

    def test_attribute_place_id(self):
        """ Tests attr """
        self.assertEqual(hasattr(self.model, "place_id"), True)
        self.assertEqual(hasattr(self.model, "user_id"), True)
        self.assertEqual(hasattr(self.model, "text"), True)

if __name__ == '__main__':
    unittest.main()
