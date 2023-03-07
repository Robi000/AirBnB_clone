className = ["BaseModel"]


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


def show(args):
    args = args.split()
    lenarg = len(args)
    if lenarg < 1:
        return (False, "** class name missing **")
    if args[0] not in className:
        return (False, "** class doesn't exist **")
    if lenarg < 2:
        return (False, "** instance id missing **")
    return (True, args)
