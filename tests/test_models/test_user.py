#!/usr/bin/python3
"""
Test of User Class
"""


import unittest
import os
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class UserTest(unittest.TestCase):
    """
    Tests for User Class
    """

    @classmethod
    def setUpClass(cls):
        """ Setup an instance for test"""
        cls.my_model = User()
        cls.my_model.email = "123@hotmail.com"
        cls.my_model.password = "12345"
        cls.my_model.first_name = "Carlos"
        cls.my_model.last_name = "Molano"

    @classmethod
    def teardown(cls):
        """ Delete the instance at the end of tests"""
        del cls.my_model
        try:
            os.remove("file.json")
        except:
            pass

    def test_checking_for_docstring_User(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(User.__doc__)

    def test_subclass_instance_User(self):
        """Test if my_model 1 and 2 are subclasses of BaseModel"""
        self.assertTrue(issubclass(self.my_model.__class__, BaseModel))
        self.assertTrue(isinstance(self.my_model, User))

    def test_attribute_email(self):
        """ Tests email """
        self.assertTrue(hasattr(self.my_model, 'email'))
        self.assertEqual(self.my_model.email, "123@hotmail.com")
        self.assertEqual(type(self.my_model.email), str)

    def test_attribute_password(self):
        """ Test password """
        self.assertTrue(hasattr(self.my_model, 'password'))
        self.assertEqual(self.my_model.password, "12345")
        self.assertEqual(type(self.my_model.password), str)

    def test_attribute_first_name(self):
        """ Check first name """
        self.assertTrue(hasattr(self.my_model, 'first_name'))
        self.assertEqual(self.my_model.first_name, "Carlos")
        self.assertEqual(type(self.my_model.first_name), str)

    def test_attribute_last_name(self):
        """Check last name"""
        self.assertTrue(hasattr(self.my_model, 'last_name'))
        self.assertEqual(self.my_model.last_name, "Molano")
        self.assertEqual(type(self.my_model.last_name), str)

    def test_hasattr(self):
        """ attributes inheritated of BaseModel"""
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))

if __name__ == '__main__':
    unittest.main()
