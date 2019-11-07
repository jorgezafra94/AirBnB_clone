#!/usr/bin/python3
"""
Parent class BaseModel
"""

import uuid
from datetime import datetime


class BaseModel:
    """Defines the common attributes of new objects"""
    def __init__(self, name='', my_number=0, id='', created='', updated=''):
        """Class constructor"""
        self.name = name
        self.my_number = my_number
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Saves the object"""
        value = datetime.now()
        setattr(self, 'updated_at', value)

    def __str__(self):
        """Returns specific info"""
        className = "[" + self.__class__.__name__ + "] "
        classId = "(" + self.id + ") "
        classDict = str(self.__dict__)
        return className + classId + classDict

    def to_dict(self):
        """Gets the __dict__ and add the key __class__"""
        new = {}
        var = self.__dict__
        for elem in var:
            if elem == 'created_at' or elem == 'updated_at':
                new[elem] = var[elem].strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                new[elem] = var[elem]
        new['__class__'] = self.__class__.__name__
        return (new)
