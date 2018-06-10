#!/usr/bin/python3
'''File Storage'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''serializes and deserialzes json files'''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''Return dictionary of <class>.<id> : object instance'''
        return self.__objects

    def new(self, obj):
        '''Add new obj to existing dictionary of instances'''
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''Save obj dictionaries to json file'''
        my_dict = {}
        if self.__objects:
            for key, obj in self.__objects.items():
                '''if type(obj) is dict:
                    my_dict[key] = obj
                else:'''
                my_dict[key] = obj.to_dict()
            with open(self.__file_path, 'w+') as f:
                json.dump(my_dict, f)

    def reload(self):
        '''If json file exists, convert obj dicts back to instances'''
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
            for key, val in new_obj.items():
                name = val['__class__']
                self.__objects[key] = eval(name)(**val)
        except FileNotFoundError:
            pass
