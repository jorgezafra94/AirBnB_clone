#!/usr/bin/python3
"""Test of Review Class """

from models.review import Review
import datetime
import unittest
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ Test User Class """
    model = Review()
    model.name = "Betty"

    def test_checking_for_docstring_User(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(Review.__doc__)

    def test_subclass_instance_Review(self):
        """Test if my_model 1 and 2 are subclasses of BaseModel"""
        self.assertEqual(isinstance(self.model, Review), True)

    def test_attribute_place_id(self):
        """ Tests place id """
        self.assertEqual(hasattr(self.model, 'place_id'), True)

    def test_attribute_user_id(self):
        """ Test place id """
        self.assertEqual(hasattr(self.model, 'user_id'), True)

    def test_attribute_text(self):
        """ Check text """
        self.assertEqual(hasattr(self.model, 'text'), True)

    def test_hasattr(self):
        """ attributes inheritated of BaseModel"""
        self.assertEqual(hasattr(self.model, 'name'), True)
        self.assertEqual(hasattr(self.model, 'id'), True)
        self.assertEqual(hasattr(self.model, 'created_at'), True)
        self.assertEqual(hasattr(self.model, 'updated_at'), True)

    def test_attributes_types(self):
        """Tests types """
        self.assertEqual(type(self.model.place_id), str)
        self.assertEqual(type(self.model.user_id), str)
        self.assertEqual(type(self.model.text), str)
        self.assertIsInstance(self.model.created_at, datetime.datetime)
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
