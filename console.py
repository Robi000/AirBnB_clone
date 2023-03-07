#!/usr/bin/python3

import cmd
from turtle import *
import json
# model classes
from models.base_model import BaseModel
from collections import defaultdict
# argument parsers
create = __import__("checker").create
show = __import__("checker").show

klass = {
    "BaseModel": BaseModel
}


def def_value():
    return []


obj = defaultdict(def_value)


class TurtleShell(cmd.Cmd):
    prompt = '(hbnb) '
    file = None
    obj = defaultdict(def_value)

    def preloop(self):
        """this will load the object with first call
        """
        for key in klass:
            try:
                with open(key + ".json", "r") as f:
                    self.obj[key].append(json.load(f))
            except:
                pass

        print(self.obj)

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """EOF command to exit the program
        """
        return True

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

        self.obj[base[0]].append(instance.to_dict())

        with open(base[0]+".json", "w") as f:
            json.dump(self.obj[base[0]], f, indent=4)

        print(instance.id)
        return

    def do_show(self, args):
        """show id 

        Args:
            args (string): the argument 
        """
        base = show(args)
        if not base[0]:
            print(base[1])
            return
        base = base[1]
        instance = None
        for x in self.obj[base[0]]:
            if x["id"] == base[1]:
                instance = klass[base[0]](**x)
        if instance:
            print(instance)
        else:
            print("** no instance found **")


if __name__ == '__main__':
    TurtleShell().cmdloop()
