#!/usr/bin/python3
"""
Module BaseModel
Parent of all classes
"""
import cmd
from datetime import datetime
from uuid import uuid4
import json
from models import storage


class BaseModel():
    """Base class for Airbnb clone project
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        to_dict(self)
    """
    def __init__(self, *args, **kwargs):
        """Initialize attributes: random uuid, dates created/updated"""
        if kwargs:
            if "id" in kwargs.keys():
                self.id = kwargs["id"]
            else:
                self.id = str(uuid4())
            if "created_at" in kwargs.keys():
                self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.created_at = datetime.now()
            if "updated_at" in kwargs.keys():
                self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                    "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        storage.new(self)

    def __str__(self):
        """Return string of info about model"""
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Update instance with updated time & save to serialized file"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return dic with string formats of times; add class info to dic"""
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            dic[k] = v
        return dic
