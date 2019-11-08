#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel
import models


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
        """
        Creates an object using the BaseModel
        eval the class if it exist or not
        var = eval("BaseModel") is the same as var = Basemodel()
        """
        if args is None or len(args) == 0:
            print("** class name missing **")
        else:
            try:
                new = eval(str(args) + "()")
                new.save()
                print(new.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id
        eval the class if it exist or not
        var = eval("BaseModel") is the same as var = Basemodel()
        """
        if args is None or len(args) == 0:
            print("** class name missing **")
        else:
            line = args.split(' ')

            if len(line) < 2:
                print("""** instance id missing **""")
            else:

                try:
                    objects = models.storage.all()
                    key = str(line[0]) + "." + str(line[1])
                    if key in objects:
                        print(objects[key])
                    else:
                        raise KeyError()
                except:
                    print("** class doesn't exist **")

if __name__ == '__main__':
    """ Main """
    console = HBNBCommand()
    console.cmdloop()
