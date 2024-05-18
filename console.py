#!/usr/bin/python3
"""CMD module for AirBnB project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command line processor"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit program"""

        return True

    def do_EOF(self, line):
        """EOF command to exit program with CTRL + D"""

        print()
        return True

    def help_quit(self):
        """Help command to document quit program"""

        print("Quit command to exit the program")

    def emptyline(self):
        """executes nothing when emptyline is enter in prompt"""

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
