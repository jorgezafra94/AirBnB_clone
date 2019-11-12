#!/usr/bin/python3
"""

Console for Arbnb clone

"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Console
    main class

    """
    prompt = "(hbtn) "

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

if __name__ == '__main__':
    """ Main """
    HBNBCommand().cmdloop()
