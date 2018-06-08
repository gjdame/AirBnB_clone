#!/usr/bin/python3
'''File Storage'''
import json
from models.base_model import BaseModel

class FileStorage:
    '''serializes and deserialzes json files'''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = '{}{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
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
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
            for key, val in new_obj.items():
                name = val['__class__']
                self.__objects[key] = eval(name)(**val)
        except FileNotFoundError:
            pass
