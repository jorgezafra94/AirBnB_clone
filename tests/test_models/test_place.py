#!/usr/bin/python3
""" Test of Place Class"""


import unittest
import os
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime


class PlaceTest(unittest.TestCase):
    """Tests for Amenity Class"""

    @classmethod
    def setUpClass(cls):
        """ Setup an instance for test"""
        # Instance 1
        cls.my_model = Place()
        cls.my_model.city_id = "c001"
        cls.my_model.user_id = "u001"
        cls.my_model.name = "Loft Bogota"
        cls.my_model.description = "Ubicado en Chapinero"
        cls.my_model.number_rooms = 1
        cls.my_model.number_bathrooms = 1
        cls.my_model.max_guest = 2
        cls.my_model.price_by_night = 100
        cls.my_model.latitude = 1.52
        cls.my_model.longitude = 2.36
        cls.my_model.amenity_ids = ['001', '002', '003']
        # Instance 2
        cls.my_model2 = Place()
        cls.my_model2.city_id = "c002"
        cls.my_model2.user_id = "u002"
        cls.my_model2.name = "Apto Medellin"
        cls.my_model2.description = "Ubicado en El Poblado"
        cls.my_model2.number_rooms = 2
        cls.my_model2.number_bathrooms = 2
        cls.my_model2.max_guest = 3
        cls.my_model2.price_by_night = 200
        cls.my_model2.latitude = 2.53
        cls.my_model2.longitude = 3.42
        cls.my_model2.amenity_ids = ['004', '005', '006']

    @classmethod
    def teardown(cls):
        """ Delete the instance at the end of tests"""
        del cls.my_model
        del cls.my_model2

    def tearDown(self):
        """ Remove file at the end of tests"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_checking_for_docstring_Place(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(Place.__doc__)

    def test_subclass_instance_Place(self):
        """Test if my_model 1 and 2 are subclasses of BaseModel,
        also if they are instances of Place
        if are instances checks if the attributes were well
        assigned"""
        self.assertTrue(issubclass(self.my_model.__class__, BaseModel))
        self.assertTrue(issubclass(self.my_model2.__class__, BaseModel))
        self.assertTrue(isinstance(self.my_model, BaseModel))
        self.assertTrue(isinstance(self.my_model2, BaseModel))
        self.assertTrue(isinstance(self.my_model, Place))
        self.assertTrue(isinstance(self.my_model2, Place))
        # Instance 1
        self.assertEqual(self.my_model.city_id, "c001")
        self.assertEqual(self.my_model.user_id, "u001")
        self.assertEqual(self.my_model.name, "Loft Bogota")
        self.assertEqual(self.my_model.description, "Ubicado en Chapinero")
        self.assertEqual(self.my_model.number_rooms, 1)
        self.assertEqual(self.my_model.number_bathrooms, 1)
        self.assertEqual(self.my_model.max_guest, 2)
        self.assertEqual(self.my_model.price_by_night, 100)
        self.assertEqual(self.my_model.latitude, 1.52)
        self.assertEqual(self.my_model.longitude, 2.36)
        self.assertEqual(self.my_model.amenity_ids, ['001', '002', '003'])
        # Instance 2
        self.assertEqual(self.my_model2.city_id, "c002")
        self.assertEqual(self.my_model2.user_id, "u002")
        self.assertEqual(self.my_model2.name, "Apto Medellin")
        self.assertEqual(self.my_model2.description, "Ubicado en El Poblado")
        self.assertEqual(self.my_model2.number_rooms, 2)
        self.assertEqual(self.my_model2.number_bathrooms, 2)
        self.assertEqual(self.my_model2.max_guest, 3)
        self.assertEqual(self.my_model2.price_by_night, 200)
        self.assertEqual(self.my_model2.latitude, 2.53)
        self.assertEqual(self.my_model2.longitude, 3.42)
        self.assertEqual(self.my_model2.amenity_ids, ['004', '005', '006'])

    def test_diff_instances_Place(self):
        """ Test if two instences were created at different time
        and have different id's"""
        self.assertNotEqual(self.my_model.created_at,
                            self.my_model2.created_at)
        self.assertNotEqual(self.my_model.id, self.my_model2.id)

    def test_str(self):
        """Test if __str__ method show the right output"""
        string = "[Place] ({}) {}".format(self.my_model.id,
                                          self.my_model.__dict__)
        self.assertEqual(string, str(self.my_model))

    def test_save_Place(self):
        """Test if updated at changes"""
        self.my_model.save()
        self.assertNotEqual(self.my_model.created_at, self.my_model.updated_at)

    def test_to_dict_Place(self):
        """If the convertion to dictionary works:
        __class__: has to be created
        created_at and updated at have to change the format"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        model_dict = self.my_model.to_dict()
        self.assertEqual(self.my_model.__class__.__name__, 'Place')
        self.assertEqual(type(model_dict['created_at']), str)
        self.assertEqual(type(model_dict['updated_at']), str)
        self.assertEqual(model_dict["created_at"],
                         self.my_model.created_at.strftime(t_format))
        self.assertEqual(model_dict["updated_at"],
                         self.my_model.updated_at.strftime(t_format))

    def test_from_dict_to_Place(self):
        """Test if we can create an instance from a dictionary"""
        my_model_json = self.my_model.to_dict()
        my_new_model = Place(**my_model_json)
        self.assertTrue(isinstance(my_new_model, Place))
        self.assertTrue(isinstance(my_new_model, BaseModel))
        self.assertTrue(issubclass(my_new_model.__class__, BaseModel))

        self.assertEqual(my_new_model.city_id, "c001")
        self.assertEqual(my_new_model.user_id, "u001")
        self.assertEqual(my_new_model.name, "Loft Bogota")
        self.assertEqual(my_new_model.description, "Ubicado en Chapinero")
        self.assertEqual(my_new_model.number_rooms, 1)
        self.assertEqual(my_new_model.number_bathrooms, 1)
        self.assertEqual(my_new_model.max_guest, 2)
        self.assertEqual(my_new_model.price_by_night, 100)
        self.assertEqual(my_new_model.latitude, 1.52)
        self.assertEqual(my_new_model.longitude, 2.36)
        self.assertEqual(my_new_model.amenity_ids, ['001', '002', '003'])

        self.assertEqual(my_new_model.id, self.my_model.id)
        self.assertEqual(my_new_model.created_at, self.my_model.created_at)
        self.assertEqual(my_new_model.updated_at, self.my_model.updated_at)
        self.assertNotEqual(my_new_model, self.my_model)

if __name__ == '__main__':
    unittest.main()
