#!/usr/bin/python3
""" Test of City"""


import unittest
import os
from models.base_model import BaseModel
from models.city import City
from datetime import datetime


class CityTest(unittest.TestCase):
    """Tests for City Class"""

    @classmethod
    def setUpClass(cls):
        """ Setup an instance for test"""
        cls.my_model = City()
        cls.my_model.name = "Bogota"
        cls.my_model.state_id = "001"
        cls.my_model2 = City()
        cls.my_model2.name = "Medellin"
        cls.my_model2.state_id = "002"

    @classmethod
    def teardown(cls):
        """ Delete the instance at the end of tests"""
        del cls.my_model
        del cls.my_model2
        try:
            os.remove("file.json")
        except:
            pass

    def test_checking_for_docstring_City(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(City.__doc__)

    def test_subclass_instance_City(self):
        """Test if my_model 1 and 2 are subclasses of BaseModel,
        also if they are instances of City
        if are instances checks if the attributes were well
        assigned"""
        self.assertTrue(issubclass(self.my_model.__class__, BaseModel))
        self.assertTrue(issubclass(self.my_model2.__class__, BaseModel))
        self.assertTrue(isinstance(self.my_model, BaseModel))
        self.assertTrue(isinstance(self.my_model2, BaseModel))
        self.assertTrue(isinstance(self.my_model, City))
        self.assertTrue(isinstance(self.my_model2, City))
        self.assertEqual(self.my_model.name, "Bogota")
        self.assertEqual(self.my_model.state_id, "001")
        self.assertEqual(self.my_model2.name, "Medellin")
        self.assertEqual(self.my_model2.state_id, "002")

    def test_diff_instances_City(self):
        """ Test if two instences were created at different time
        and have different id's"""
        self.assertNotEqual(self.my_model.id, self.my_model2.id)

    def test_str(self):
        """Test if __str__ method show the right output"""
        string = "[City] ({}) {}".format(self.my_model.id,
                                         self.my_model.__dict__)
        self.assertEqual(string, str(self.my_model))

    def test_save_City(self):
        """Test if updated at changes"""
        self.my_model.save()
        self.assertNotEqual(self.my_model.created_at, self.my_model.updated_at)

    def test_to_dict_City(self):
        """If the convertion to dictionary works:
        __class__: has to be created
        created_at and updated at have to change the format"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        model_dict = self.my_model.to_dict()
        self.assertEqual(self.my_model.__class__.__name__, 'City')
        self.assertEqual(type(model_dict['created_at']), str)
        self.assertEqual(type(model_dict['updated_at']), str)
        self.assertEqual(model_dict["created_at"],
                         self.my_model.created_at.strftime(t_format))
        self.assertEqual(model_dict["updated_at"],
                         self.my_model.updated_at.strftime(t_format))

    def test_from_dict_to_City(self):
        """Test if we can create an instance from a dictionary"""
        my_model_json = self.my_model.to_dict()
        my_new_model = City(**my_model_json)
        self.assertTrue(isinstance(my_new_model, City))
        self.assertTrue(isinstance(my_new_model, BaseModel))
        self.assertTrue(issubclass(my_new_model.__class__, BaseModel))
        self.assertEqual(my_new_model.name, "Bogota")
        self.assertEqual(my_new_model.state_id, "001")
        self.assertEqual(my_new_model.id, self.my_model.id)
        self.assertEqual(my_new_model.created_at, self.my_model.created_at)
        self.assertEqual(my_new_model.updated_at, self.my_model.updated_at)
        self.assertNotEqual(my_new_model, self.my_model)

if __name__ == '__main__':
    unittest.main()
