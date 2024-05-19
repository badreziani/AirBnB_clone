#!/usr/bin/python3
"""CMD module for AirBnB project"""
import cmd
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command line processor"""

    prompt = "(hbnb) "
    class_list = [
            "BaseModel", "User", "State",
            "State", "City", "Amenity",
            "Place", "Review"
            ]

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

    def do_create(self, line):
        """Creates a new instance"""

        if len(line) == 0:
            print("** class name missing **")
            return

        if line not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return

        for clas in HBNBCommand.class_list:
            if line == clas:
                instance = eval(line)()
                instance.save()
                print(instance.id)
                return

    def do_show(self, line):
        """Prints the string representation of an instance"""

        if len(line) == 0:
            print("** class name missing **")
            return

        args = line.split()

        if args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        if args[1]:
            args[1] = args[1].strip('"').strip("'")

        all_objs = storage.all()
        id_flag = False

        for obj_id in all_objs.keys():
            class_name = all_objs[obj_id].__class__.__name__
            if args[0] == class_name and args[1] == all_objs[obj_id].id:
                id_flag = True
                break

        if id_flag is False:
            print("** no instance found **")
            return

        for obj_id in all_objs.keys():
            cls = all_objs[obj_id].__class__.__name__
            if args[0] == cls and args[1] == all_objs[obj_id].id:
                print(all_objs[obj_id])
        return

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""

        if len(line) == 0:
            print("** class name missing **")
            return

        args = line.split()
        if args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        if args[1]:
            args[1] = args[1].strip('"').strip("'")

        all_objs = storage.all()
        id_flag = False

        for obj_id in all_objs.keys():
            class_name = all_objs[obj_id].__class__.__name__
            if args[0] == class_name and args[1] == all_objs[obj_id].id:
                id_flag = True
                break

        if id_flag is False:
            print("** no instance found **")
            return

        for obj_id in all_objs.keys():
            cls = all_objs[obj_id].__class__.__name__
            if args[0] == cls and args[1] == all_objs[obj_id].id:
                del all_objs[obj_id]
                storage.save()
                return

    def do_all(self, line):
        """Prints all string representation of all instances"""

        all_objs = storage.all()
        string_list = []

        if len(line) == 0:
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                string_list.append(str(obj))
            print(string_list)
            string_list = []
            return

        args = line.split()
        if args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return

        for key, obj in all_objs.items():
            if args[0] == obj.__class__.__name__:
                string_list.append(str(obj))
        print(string_list)
        return

    def do_update(self, line):
        """Updates an instance based on the class name and id"""

        if len(line) == 0:
            print("** class name missing **")
            return

        pattern = r'\".*?\"|\'.*?\'|\S+'
        matches = re.findall(pattern, line)
        args = [match.strip('"') for match in matches]
        all_objs = storage.all()

        if args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        if args[1]:
            args[1] = args[1].strip('"').strip("'")

        id_flag = False
        for obj_id in all_objs.keys():
            cls = all_objs[obj_id].__class__.__name__
            if len(args) >= 2:
                if (args[0] == cls) and (args[1] == all_objs[obj_id].id):
                    id_flag = True
                    break

        if id_flag is False:
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        for key, obj in all_objs.items():
            if args[0] == obj.__class__.__name__ and args[1] == obj.id:
                try:
                    args[3] = int(args[3])
                    setattr(obj, args[2], args[3])
                except ValueError:
                    try:
                        args[3] = float(args[3])
                        setattr(obj, args[2], args[3])
                    except ValueError:
                        setattr(
                                obj, args[2].strip('"').strip("'"),
                                args[3].strip('"').strip("'")
                                )
        storage.save()
        return

    def do_count(self, line):
        """Retrieves the number of instances of a class"""

        args = line.split()
        all_objs = storage.all()
        count = 0
        for key, obj in all_objs.items():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)
        return

    def precmd(self, line):
        """Pre-process commands before dispatching"""

        # command = line.split()[0]
        # print(command)
        pattern = re.compile(r'^(\w+)\.(\w+)\((.*)\)$')
        match = pattern.match(line)
        if match:
            cls = match.group(1)
            method = match.group(2)
            args = match.group(3).split(', ')
            if len(args) > 3:
                args = args[0:3]
                print(args)

            if len(args) >= 1:
                arg1 = args[0].strip('"').strip("'")
            else:
                arg1 = ""

            if len(args) >= 2:
                arg2 = args[1].strip('"').strip("'")
            else:
                arg2 = ""

            if len(args) >= 3:
                arg3 = args[2]
            else:
                arg3 = ""

            # arg2 = match.group(4)
            # arg3 = match.group(5)

            line = "{:s} {:s} {:s} {:s} {:s}".format(
                    method, cls, arg1, arg2, arg3
                    )

        return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
