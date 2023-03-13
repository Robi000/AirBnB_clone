#!/usr/bin/python3

"""this is a file that run as cmd on the terminal 
    """
import cmd

# model classes
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from collections import defaultdict
# argument parsers
create = __import__("checker").create
show_destroy = __import__("checker").show_destroy
all = __import__("checker").all
update = __import__("checker").update

klass = {
    "BaseModel": BaseModel,
    "User": User,
    "Review": Review,
    "Place": Place,
    "City": City,
    "Amenity": Amenity,
    "State": State
}


class HBNBCommand(cmd.Cmd):
    """this is the main starting class

    Args:
        cmd (its just inheritance ): _description_

    Returns:
        None: this will start the loop later 
    """
    prompt = '(hbnb) '

    def functions(self, fun):
        """treturn fuction for the loop back 

        Args:
            fun (str): name of fun

        Returns:
            fun: the fun that exist in this class
        """
        func = {
            "create": self.do_create,
            "show": self.do_show,
            "all": self.do_all,
            "count": self,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        return func.get(fun, None)

    def do_quit(self, arg):
        """Exit the HBNB console:  quit"""
        return True

    def do_EOF(self, arg):
        """Exit the HBNB console:  EOF"""
        return True

    def emptyline(self):
        """Empty line + Enter will just return the prompt without any error.
        i.e. the prompt will not execute the previous command"""
        return False

    def postloop(self):
        """Print a new line when program exits"""
        print()

    def do_create(self, args):
        """create a model instance 

        Args:
            args (string ): notheing 
        """
        base = create(args)
        if not base[0]:
            print(base[1])
            return
        base = base[1]
        instance = klass[base[0]]()
        instance.save()
        print(instance.id)
        return

    def do_show(self, args):
        """show id 

        Args:
            args (string): the argument 
        """
        base = show_destroy(args)
        if not base[0]:
            print(base[1])
            return
        base = base[1]
        instance = None
        key = base[0]+"."+base[1]
        instance = storage.all().get(key, None)
        if instance:
            print(instance.__str__())
            return

        print("** no instance found **")
        return

    def do_destroy(self, args):
        """destroy an instance from the file 

        Args:
            args (id and class): object to delete 
        """
        base = show_destroy(args)
        if not base[0]:
            print(base[1])
            return
        base = base[1]
        key = base[0]+"."+base[1]
        result = storage.destroy(key)
        if result:
            print(result)

    def do_all(self, args):
        """this is another fun to display existing objects 

        Args:
            args (class or none ): classes
        """
        base = all(args)
        if not base[0]:
            print(base[1])
            return
        base = base[1]
        result = []
        objs = storage.all()
        if base:
            for key in objs:
                check = key.split(".")
                if check[0] == base[0]:
                    result.append(objs[key].__str__())

        else:
            for val in objs.values():
                result.append(val.__str__())

        print(result)

    def do_update(self, args):
        """update an instance with given arguments 

        Args:
            args (str): will be parced for ease of use 
        """
        base = update(args)
        if not base[0]:
            print(base[1])
            return
        base = base[1]
        result = storage.update(base)
        if result:
            print(result)

    def default(self, line: str) -> None:
        """for the advanced commands 

        Args:
            line (str ): line inserted 

        Returns:
            nothing : just nothing 
        """
        args = line.split(".")
        if args[0] not in klass:
            return False
        if len(args) < 2:
            return False
        args[1] = args[1][:-1].split("(")
        func = self.functions(args[1][0])
        if not func:
            return False
        if args[1][0] == "all":
            func(args[0])
            return
        if args[1][0] == "show":
            arg = args[0] + " " + args[1][1][1:-1]
            print(arg)
            func(arg)
            return
        if args[1][0] == "destroy":
            arg = args[0] + " " + args[1][1][1:-1]
            print(arg)
            func(arg)
            return
        if args[1][0] == "update":
            args[1][1] = args[1][1].split(",")
            arg = args[0] + " "
            if len(args[1][1]) > 0:
                arg = arg + args[1][1][0][1:-1] + " "
            if len(args[1][1]) > 1:
                arg = arg + args[1][1][1][2:-1] + " "
            if len(args[1][1]) > 2:
                arg = arg + args[1][1][2][1:]
            func(arg)
            return

        cmd.Cmd.default()
