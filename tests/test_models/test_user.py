#!/usr/bin/python3
from models.user import User
import datetime
import unittest
"""Unittests for user"""


class UserCase(unittest.TestCase):

    userx = User()

    def test_hasattr(self):
        self.assertTrue(hasattr(self.userx, "name"))
        # BaseModel Attributes
        self.assertTrue(hasattr(self.userx, "id"))
        self.assertTrue(hasattr(self.userx, "created_at"))
        self.assertTrue(hasattr(self.userx, "updated_at"))

    def test_types(self):
        self.assertIsInstance(self.userx.name, str)
        # BaseModel Attributes
        self.assertIsInstance(self.userx.id, str)
        self.assertIsInstance(self.userx.created_at, datetime.datetime)
        self.assertIsInstance(self.userx.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
