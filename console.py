#!/usr/bin/python3
"""

Console for Arbnb clone

"""
import cmd
import sys
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
import json

classes = {'BaseModel': BaseModel, 'User': User, 'State': State, 'City': City,
           'Amenity': Amenity, 'Place': Place, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """
    Console
    main class

    """
    prompt = "(hbnb) "

    def do_EOF(self, args):
        "Quit the console - Usage: EOF\n"
        print("")
        return (True)

    def do_quit(self, args):
        "Quit command to exit the program\n"
        return (True)

    def emptyline(self):
        " Does not perform any action "
        pass

    def do_create(self, args):
        """Create a new instance - Usage: create <Classname>\n"""
        if args is None or len(args) == 0:
            print("** class name missing **")
        else:
            if args in classes:
                new = eval(str(args) + "()")
                new.save()
                print(new.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        """Show the representation of an instance - Usage show <Classname>\n"""
        if args is None or len(args) == 0:
            print("** class name missing **")
        else:
            line = args.split()

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
        """Delete the instance of a given class -
        Usage: destroy <classname> <id>\n"""
        if args is None or len(args) == 0:
            print("** class name missing **")
        else:
            line = args.split()

            if len(line) < 2:
                print("""** instance id missing **""")
            else:

                try:
                    objects = models.storage.all()
                    key = str(line[0]) + "." + str(line[1])
                    if key in objects:
                        del(objects[key])
                        models.storage.save()
                    else:
                        print("** no instance found **")
                except:
                    print("** class doesn't exist **")

    def do_all(self, args):
        """Print all instances of a class - Usage: all <classname>\n"""
        objects = models.storage.all()
        objList = []
        if args is "":
            for key in objects:
                objList.append(str(objects[key]))
            print(objList)
        else:
            try:
                line = args.split()
                eval(line[0])
                for elem in objects:
                    aux = objects[elem].to_dict()
                    if aux['__class__'] == line[0]:
                        objList.append(str(objects[elem]))
                print(objList)
            except:
                print("** class doesn't exist **")

    def do_update(self, args):
        """Update or set att in an instance -
        Usage: update <classname> <id> <att_name> <att_value>\n"""
        line = shlex.split(args)
        if len(line) == 0:
            print("** class name missing **")
        else:
            try:
                eval(str(line[0]))
            except:
                print("** class doesn't exist **")
                return
            if len(line) == 1:
                print("** instance id missing **")
            else:
                objects = models.storage.all()
                key = str(line[0]) + "." + str(line[1])
                if key not in objects:
                    print("** no instance found **")
                else:
                    if len(line) == 2:
                        print("** attribute name missing **")
                    else:
                        if len(line) == 3:
                            print("** value missing **")
                        else:
                            setattr(objects[key], line[2], line[3])
                            models.storage.save()

    def do_count(self, args):
        """Count the number of type of class - Usage: count <classname>"""
        cont = 0
        objects = models.storage.all()
        new = {}
        for elem in objects:
            new[elem] = objects[elem].to_dict()
        for elem in new:
            if (args == new[elem]['__class__']):
                cont = cont + 1
        print(cont)

    def default(self, args):
        """ Handle alternative command representations """
        first = args.split('.')
        if len(first) > 1:
            class_name = first[0]
            methods = first[1]
            first[1] = first[1].replace('(', '&(')
            second = first[1].split('&')
            comando = class_name

            if methods == "all()":
                self.do_all(comando)
            elif methods == "count()":
                self.do_count(comando)
            else:
                methods = second[0]
                elems = second[1]
                elems = elems.replace('(', '')
                elems = elems.replace(')', '')
                elems = elems.replace('{', '"{')
                elems = elems.replace('}', '}"')
                third = shlex.split(elems)
                for i in range(len(third)):
                    third[i] = third[i].replace(',', ' ')
                    third[i] = third[i].strip()
                id = third[0]
                comando = comando + ' ' + id
                comando = comando.replace('\"', '')
                if methods == "show" and len(third) == 1:
                    self.do_show(comando)
                elif methods == "destroy" and len(third) == 1:
                    self.do_destroy(comando)
                elif methods == "update":
                    print(third)
                    if third[1][0] == '{' and third[1][-1] == '}':
                        third[1] = third[1].replace('{', '')
                        third[1] = third[1].replace('}', '')
                        third[1] = third[1].replace(': ', ':')
                        sub = shlex.split(third[1], ', ')
                        new = []
                        for ele in sub:
                            sub2 = ele.split(':')
                            if len(sub2) < 2:
                                sub2.append('')
                            new.append(tuple(sub2))
                        dicti = dict(new)
                        print(dicti)
                        for key in dicti:
                            new_comand = comando + ' '
                            new_comand += str(key)
                            new_comand = new_comand.replace('\"', '')
                            new_comand = new_comand.replace('\'', '')
                            new_comand += ' \"' + str(dicti[key]) + '\"'
                            self.do_update(new_comand)
                    else:
                        for i in range(1, len(third)):
                            if i == 1:
                                comando = comando + ' ' + third[i]
                            if i == 2:
                                comando = comando + ' '
                                comando += '\"' + third[i] + '\"'
                        self.do_update(comando)
                else:
                    return cmd.Cmd.default(self, args)
        else:
            return cmd.Cmd.default(self, args)

if __name__ == '__main__':
    """ Main """
    HBNBCommand().cmdloop()
