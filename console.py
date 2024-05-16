#!/usr/bin/env python3
"""
HBNB command interpreter to manage your AirBnB objects.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class.
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Handles EOF key to exit the program\n"""
        print()
        return True

    def emptyline(self):
        print(end="")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
