#!/usr/bin/python3
"""
This module is the engin for the whole project 
"""
import json
from collections import defaultdict


def def_value():
    """this will return default dic

    Returns:
        {}: just empty dic
    """
    return {}


class FileStorage():
    """serializes instances to a JSON file and deserializes JSON file to instances:
    """
    __file_path = "store.json"
    __objects = defaultdict(def_value)

    def all(self):
        """returns the dictionary ++objects 
        """

        return self.__objects

    def new(self, obj):
        """this will add new object to the self.__object dectionary 

        Args:
            obj (obj): just obj
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self, obj=None):
        """this will  save to the file 

        Args:
            obj (obj, optional): obj form instance save . Defaults to None.
        """
        if obj:
            key = obj.__class__.__name__+"." + obj.id
            self.__objects[key] = obj
            # print(obj.to_dict())
        serialize = {}
        for key in self.__objects:
            # print(f"------> {key} <--------")
            if self.__objects[key] is not {}:
                serialize[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(serialize, f, indent=2)

    def reload(self):
        """reload the objects from the file whien the program start 
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State

        klass = {
            "BaseModel": BaseModel,
            "User": User,
            "Review": Review,
            "Place": Place,
            "City": City,
            "Amenity": Amenity,
            "State": State,
        }
        obj = {}
        try:
            with open(self.__file_path, "r") as f:
                obj = json.load(f)
        except Exception as e:
            pass

        self.__objects = defaultdict(def_value)

        if obj:
            for key in obj:
                clss = klass[obj[key]["__class__"]]
                kwarg = obj[key]
                self.__objects[key] = clss(**kwarg)

    def destroy(self, key):
        """remove a an object form __object and save it 

        Args:
            key (str): key to the object 

        Returns:
            status : true or false
        """
        instance = self.__objects.get(key, {})
        if instance == {}:
            return "** no instance found **"
        del self.__objects[key]
        self.save()
        return None

    def update(self, arg):
        """this will accept argument and return sth

        Args:
            arg (list ): list of arguments 

        Returns:
            status : if changed or not 
        """
        key = arg[0]+"."+arg[1]
        instance = self.__objects.get(key, {})
        if instance == {}:
            return "** no instance found **"
        if len(arg) < 3:
            return "** attribute name missing **"
        if len(arg) < 4:
            return "** value missing **"
        if arg[3][-1] == '"':
            val = arg[3][1:-1]
        else:
            val = int(arg[3])
        instance.__dict__[arg[2]] = val
        instance.save()
        return None
