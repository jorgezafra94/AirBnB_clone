#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel
import models
import json


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
                        print("** no instance found **")
                except:
                    print("** class doesn't exist **")

    def do_destroy(self, args):
        """delete the object and update json file"""
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
                        del(objects[key])
                        new = {}
                        for elem in objects:
                            new[elem] = str(objects[elem])
                        with open("file.json", 'w') as fd:
                            fd.write(json.dumps(new))
                    else:
                        print("** no instance found **")
                except:
                    print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not
        on the class name"""
        objects = models.storage.all()
        objList = []
        if args is "":
            for key in objects:
                objList.append(str(objects[key]))
            print(objList)
        try:
            line = args.split(" ")
            eval(line[0])
            for key in objects:
                objList.append(str(objects[key]))
            print(objList)
        except:
            print("** class doesn't exist **")

if __name__ == '__main__':
    """ Main """
    console = HBNBCommand()
    console.cmdloop()
