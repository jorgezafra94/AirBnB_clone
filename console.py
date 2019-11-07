#!/usr/bin/python3
import cmd

class HBNB(cmd.Cmd):
    """Console"""
    intro = 'Welcome to the console. Type help or ? to list commands.\n'
    prompt = "(hbtn)"
    def do_EOF(self, args):
	"""Console exit when EOF\n"""
	return(True)
    def do_quit(self, args):
	"""Console quit Builtin\n"""
	return(True)
    def emptyline(self):
	"""Does not perform any action"""
	pass

if __name__ == '__main__':
    """Main""
    console = HBNB()
    console.cmdloop()
