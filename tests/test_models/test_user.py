#!/usr/bin/python3
"""Test of User Class """

from models.user import User
import datetime
import unittest


class UserTest(unittest.TestCase):
    """ Test User Class """
    my_model = User()
    my_model.email = "123@hotmail.com"
    my_model.password = "12345"
    my_model.first_name = "Carlos"
    my_model.last_name = "Molano"

    def test_checking_for_docstring_User(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(User.__doc__)

    def test_subclass_instance_User(self):
        """Test if my_model 1 and 2 are subclasses of BaseModel"""
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

    def test_attributes_types(self):
        """Tests types """
        self.assertEqual(type(self.my_model.email), str)
        self.assertEqual(type(self.my_model.last_name), str)
        self.assertEqual(type(self.my_model.first_name), str)
        self.assertEqual(type(self.my_model.password), str)
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
