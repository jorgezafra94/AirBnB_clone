#!/usr/bin/python3
""" Test of User Class"""


import unittest
import os
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class UserTest(unittest.TestCase):
    """Tests for User Class"""

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
        del cls.my_model2
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

    def test_attribute_password(self):
        """ Test password """
        self.assertTrue(hasattr(self.my_model, 'password'))
        self.assertEqual(self.my_model.password, "12345")

    def test_attribute_first_name(self):
        """ Check first name """
        self.assertTrue(hasattr(self.my_model, 'first_name'))
        self.assertEqual(self.my_model.first_name, "Carlos")

    def test_attribute_last_name(self):
        """Check last name"""
        self.assertTrue(hasattr(self.my_model, 'last_name'))
        self.assertEqual(self.my_model.last_name, "Molano")

    def test_hasattr(self):
        """ attributes inheritated of BaseModel"""
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))

    def test_str(self):
        """Test if __str__ method show the right output"""
        string = "[User] ({}) {}".format(self.my_model.id,
                                         self.my_model.__dict__)
        self.assertEqual(string, str(self.my_model))

    def test_save_User(self):
        """Test if updated at changes"""
        self.my_model.save()
        self.assertNotEqual(self.my_model.created_at, self.my_model.updated_at)

    def test_to_dict_User(self):
        """If the convertion to dictionary works:
        __class__: has to be created
        created_at and updated at have to change the format"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        model_dict = self.my_model.to_dict()
        self.assertEqual(self.my_model.__class__.__name__, 'User')
        self.assertEqual(type(model_dict['created_at']), str)
        self.assertEqual(type(model_dict['updated_at']), str)
        self.assertEqual(model_dict["created_at"],
                         self.my_model.created_at.strftime(t_format))
        self.assertEqual(model_dict["updated_at"],
                         self.my_model.updated_at.strftime(t_format))

    def test_from_dict_to_User(self):
        """Test if we can create an instance from a dictionary"""
        my_model_json = self.my_model.to_dict()
        my_new_model = User(**my_model_json)
        self.assertTrue(isinstance(my_new_model, User))
        self.assertTrue(isinstance(my_new_model, BaseModel))
        self.assertTrue(issubclass(my_new_model.__class__, BaseModel))
        self.assertEqual(my_new_model.email, "123@hotmail.com")
        self.assertEqual(my_new_model.password, "12345")
        self.assertEqual(my_new_model.first_name, "Carlos")
        self.assertEqual(my_new_model.last_name, "Molano")
        self.assertEqual(my_new_model.id, self.my_model.id)
        self.assertEqual(my_new_model.created_at, self.my_model.created_at)
        self.assertEqual(my_new_model.updated_at, self.my_model.updated_at)
        self.assertNotEqual(my_new_model, self.my_model)

if __name__ == '__main__':
    unittest.main()
