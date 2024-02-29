#!/usr/bin/python3
"""
Description:
    his script initializes an instance of the File_storage class
    from the models.engine.file_storage module
    and reloads data from the storage source into memory.
"""

from models.engine.file_storage import FileStorage

""" Create an instance of the File_storage class"""
storage = FileStorage()
""" Reload data from the storage source into memory"""
storage.reload()
