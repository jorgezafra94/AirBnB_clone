#!/usr/bin/python3
"""
File storage
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Manage and save information in files"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ return the dictionary """
        return self.__objects

    def new(self, obj):
        """ save a dictionary per key """
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """ save in file the serialized dictionary of dictionaries"""
        new = {}
        for elem in self.__objects:
            new[elem] = self.__objects[elem].to_dict()
        with open(self.__file_path, 'w') as fd:
            fd.write(json.dumps(new))

    def reload(self):
        """ load the Json from file and gets the dictionary of dictionaries"""
        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r') as fd:
                var = fd.read()
                var = json.loads(var)
                for elem in var:
                    self.__objects[elem] = BaseModel(**(var[elem]))
