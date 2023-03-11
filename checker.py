#!/usr/bin/python3
"""this module will check the arguments 

    Returns:
        _type_: _description_
    """
className = set(["BaseModel", "User", "Review", "Place", "City", "Amenity"])


def create(args):
    """this will check the arguments passed to create 

    Args:
        args (string): arguments passed 

    Returns:
        tupple: status and the splited argument
    """
    args = args.split()
    lenarg = len(args)
    if lenarg < 1:
        return (False, "** class name missing **")
    if args[0] not in className:
        return (False, "** class doesn't exist **")
    return (True, args)


def show_destroy(args):
    """this will check the args 

    Args:
        args (_type_): _description_

    Returns:
        _type_: _description_
    """
    args = args.split()
    lenarg = len(args)
    if lenarg < 1:
        return (False, "** class name missing **")
    if args[0] not in className:
        return (False, "** class doesn't exist **")
    if lenarg < 2:
        return (False, "** instance id missing **")
    return (True, args)


def all(args):
    """this is args to check 

    Args:
        args (_type_): _description_

    Returns:
        _type_: _description_
    """
    args = args.split()
    lenarg = len(args)
    if lenarg > 0:
        if args[0] not in className:
            return (False, "** class doesn't exist **")
        else:
            return (True, args)
    return (True, None)


def update(args):
    """args to be checked 

    Args:
        args (_type_): _description_

    Returns:
        _type_: _description_
    """
    args = args.split()
    lenarg = len(args)
    if lenarg < 1:
        return (False, "** class name missing **")
    if args[0] not in className:
        return (False, "** class doesn't exist **")
    if lenarg < 2:
        return (False, "** instance id missing **")
    return (True, args[:5])
