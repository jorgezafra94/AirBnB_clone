#!/usr/bin/python3
"""Unittest for base_model"""

import os
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def test_base_model(self):
        """testing the BaseModel"""
        dog = BaseModel()
        self.assertIs(type(dog.id), str)
        self.assertIs(type(dog.created_at), datetime)
        self.assertIs(type(dog.updated_at), datetime)
        self.assertEqual(dog.created_at, dog.updated_at)
        self.assertFalse(dog.updated_at == datetime.utcnow())
        old_updated = dog.updated_at
        dog.save()

    def test_save_model(self):
        """ tests to see if the return type of save is a string """
        dog = BaseModel()
        dog.save()
        self.assertIsInstance(dog.to_dict()['created_at'], str)
        self.assertIsInstance(dog.to_dict()['updated_at'], str)
        d = dog.to_dict()
        self.assertEqual(type(d), dict)
        self.assertEqual(d['__class__'], "BaseModel")
        self.assertEqual(d['created_at'], dog.created_at.isoformat())
        self.assertEqual(d['updated_at'], dog.updated_at.isoformat())
        self.assertEqual(d['id'], dog.id)


if __name__ == '__main__':
    unittest.main()
