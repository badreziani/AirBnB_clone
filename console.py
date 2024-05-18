#!/usr/bin/env python3
"""
HBNB command interpreter to manage your AirBnB objects.
"""

import cmd
import shlex

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class.
    """

    ALLOWED_CLASSES = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
            ]
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Handles EOF key to exit the program\n"""
        print()
        return True

    def emptyline(self):
        """Disable the repetition of the last command\n"""
        pass

    def do_create(self, line):
        """Creates and saves a new instance of BaseModel\n"""
        args = shlex.split(line)
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.ALLOWED_CLASSES:
            print("** class doesn't exist **")
        else:
            new_obj = eval(args[0])()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance\n"""
        args = shlex.split(line)
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.ALLOWED_CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            obj = all_objs.get(f"{args[0]}.{args[1]}")
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id\n"""
        args = shlex.split(line)
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.ALLOWED_CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            found = all_objs.get(f"{args[0]}.{args[1]}") is not None
            if not found:
                print("** no instance found **")
            else:
                del all_objs[f"{args[0]}.{args[1]}"]
                storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances\n"""
        args = shlex.split(line)
        
        objs_list = []
        if len(args) == 0:
            all_objs = storage.all()
            for key, value in all_objs.items():
                objs_list.append(str(value))
            print(objs_list)
        elif len(args) >= 1 and args[0] in HBNBCommand.ALLOWED_CLASSES:
            all_objs = storage.all()
            for key, value in all_objs.items():
                if key == f"{args[0]}.{value.id}":
                    objs_list.append(str(value))
            print(objs_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id\n
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(line)
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.ALLOWED_CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            obj = all_objs.get(f"{args[0]}.{args[1]}")
            if obj is None:
                print("** no instance found **")
            else:
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    setattr(all_objs[f"{args[0]}.{args[1]}"], args[2], args[3])
                    storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
