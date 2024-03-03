#!/usr/bin/python3
"""
Description:
    This module defines the File_storage class, which provides functionality
    for managing data storage in a JSON file.

Classes:
    File_storage: A class for managing data storage in a JSON file.

Methods:
    all(self): Returns a dictionary containing all stored objects.
    new(self, obj): Adds a new object to the storage.
    save(self): Saves stored objects to the JSON file.
    reload(self): Reloads stored objects from the JSON file into memory.

Attributes:
    __file_path (str): The file path of the JSON file for storage.
    __objects (dict): A dictionary containing stored objects.
"""

import json
from os.path import isfile


class FileStorage:
    """
    File_storage class:
        Manages data storage in a JSON file.

    Attributes:
        __file_path (str): The file path of the JSON file for storage.
        __objects (dict): A dictionary containing stored objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary containing all stored objects."""

        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj: The object to be added.
        """

        let_key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects.update({let_key: obj})

    def save(self):
        """Saves stored objects to the JSON file."""

        dictt = {}
        with open(self.__file_path, "w", encoding="utf-8") as file:
            for let_key, obj in self.__objects.items():
                dictt[let_key] = obj.to_dict()
            file.write(json.dumps(dictt))

    def reload(self):
        """
        Reloads stored objects from the JSON file into memory.

        Notes:
            It assumes that the stored objects are instances of classes
            defined in modules imported at runtime.
        """

        from models.base_model import BaseModel
        from models.user import User


        if not isfile(self.__file_path):
            return
        with open(self.__file_path, "r") as file:
            loads = json.load(file)
            for key, value in loads.items():
                cls, cls_id = key.split(".")
                cls_obj = eval(cls)
                self.__objects[key] = cls_obj(**value)
