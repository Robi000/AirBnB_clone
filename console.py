import cmd
import sys
from turtle import *


class TurtleShell(cmd.Cmd):
    prompt = '(hbnb) '
    file = None

    def do_quit(self, args):
        exit()


if __name__ == '__main__':
    TurtleShell().cmdloop()
