#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Console"""
    prompt = "(hbtn) "

    def do_EOF(self, args):
        """ Console exit when EOF\n """
        return (True)

    def do_quit(self, args):
        """ Console quit Builtin\n """
        return (True)

    def emptyline(self):
        """ Does not perform any action """
        return (False)

    def do_create(self, args):
        """ Creates an object using the BaseModel """
        if args is None or len(args) == 0:
            print("** class name missing **")
        else:
            try:
                new = eval(str(args) + "()")
                new.save()
                print(new.id)
            except:
                print("** class doesn't exist **")

if __name__ == '__main__':
    """ Main """
    console = HBNBCommand()
    console.cmdloop()
