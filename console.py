#!/usr/bin/env python3
"""
HBNB command interpreter to manage your AirBnB objects.
"""

from cmd import Cmd

class Hbnb(Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Exits the console."""
        return True

    def do_EOF(self, line):
        """Exits the console."""
        print()
        return True

    def emptyline(self):
        print(end="")

if __name__ == "__main__":
    Hbnb().cmdloop()
