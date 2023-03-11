#!/usr/bin/python3

""" this is the base model that will used as base for other 
"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():
    """BaseModel that defines all common attributes/methods for other classes
    """
    id = None
    created_at = None
    updated_at = None

    def __init__(self, *args, **kwargs) -> None:
        """initialize the base class 

        """
        if kwargs:
            for key, Value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        Value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        Value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[key] = Value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            storage.new(self)

    def __str__(self) -> str:
        """string representation 

        Returns:
            str: will return the string representation of any inherited class
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save(self)

    def to_dict(self):
        """changes the the object to string representatnion 

        Returns:
            dict : string representation of the object 
        """
        result = {}
        result = {** self.__dict__}
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()

        return result
