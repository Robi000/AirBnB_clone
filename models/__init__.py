#!/usr/bin/python3
"""this module will create engine instance 
    """
from .engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
