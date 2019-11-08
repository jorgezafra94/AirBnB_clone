#!/usr/bin/python3
import cmd


class HBNB(cmd.Cmd):
    """Console"""
    prompt = "(hbtn)"

    def do_EOF(self, args):
        """ Console exit when EOF\n """
        return (True)

    def do_quit(self, args):
        """ Console quit Builtin\n """
        return (True)

    def emptyline(self):
        """ Does not perform any action """
        pass

if __name__ == '__main__':
    """ Main """
    console = HBNB()
    console.cmdloop()
