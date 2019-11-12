#!/usr/bin/python3
"""
Entry point of the command interpreter
Use: ./console.py
(hbnb) <command>
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Use of cmd class as an interpreter
    Class Attributes:
        prompt (str): custom prompt
        name_classes: dictionay of classes
        name_dotcommand: commands/functions with dot format
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, arg):
        'Ctr + D to exit the program\n'
        print()
        return True

    def emptyline(self):
        'Overrides the empty line method inherited from cmd'
        pass

if __name__ == '__main__':
    console = HBNBCommand()
    console.cmdloop()
