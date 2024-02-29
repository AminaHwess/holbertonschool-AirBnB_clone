#!/usr/bin/python3
""" AirBnB clone project"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Class BaseModel that defines all common
    attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """constructor of the class"""
        if kwargs:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            kwar = kwargs.copy()
            del kwar["__class__"]
            for key in kwar:
                if key in ["created_at", "updated_at"]:
                    kwar[key] = datetime.strptime(kwar[key], date_format)
            self.__dict__ = kwar
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Prints [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        mydict = self.__dict__.copy()
        mydict["__class__"] = self.__class__.__name__
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        return mydict
