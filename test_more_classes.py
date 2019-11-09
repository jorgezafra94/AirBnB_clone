#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new State --")
my_state = State()
my_state.name = "Bogota D.C"
my_state.save()
print(my_state)

print("-- Create a new City --")
my_city = City()
my_city.state_id = "948"
my_city.name = "Bogota"
my_city.save()
print(my_city)

print("-- Create a Amenity --")
my_amenity = Amenity()
my_amenity.name = "wifi"
my_amenity.save()
print(my_amenity)

print("-- Create a Place --")
x = Place()
x.city_id = "1"
x.user_id = "primero"
x.name = "casa de Charlie"
x.description = "gran casa cuenta con 2 habitaciones y 1 bano, wifi y un TV"
x.number_rooms = 2
x.number_bathrooms = 1
x.max_guest = 1
x.price_by_night = 900000
x.latitude = 98.89
x.longitude = 41.14
x.amenity_ids = "wifi, luz, aire acondicionado"
x.save()
print(x)

print("-- Review --")
rev = Review()
rev.place_id = "123"
rev.user_id = "1908"
rev.text = "perfecto una experiencia agradable"
rev.save()
print(rev)
