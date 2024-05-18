#!/usr/bin/python3
"""CMD module for AirBnB project"""
import cmd
from models.base_model import BaseModel
from models import storage


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

        if line not in self.class_list:
            print("** class doesn't exist **")
            return

        if line == "BaseModel":
            instance = BaseModel()
            instance.save()
            print(instance.id)
        return

    def do_show(self, line):
        """Prints the string representation of an instance"""

        if len(line) == 0:
            print("** class name missing **")
            return

        args = line.split()
        if args[0] not in self.class_list:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        all_objs = storage.all()
        id_flag = False

        for obj_id in all_objs.keys():
            if args[1] == all_objs[obj_id].id:
                id_flag = True
        if id_flag is False:
            print("** no instance found **")
            return

        for obj_id in all_objs.keys():
            if args[1] == all_objs[obj_id].id:
                print(all_objs[obj_id])
        return

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""

        if len(line) == 0:
            print("** class name missing **")
            return

        args = line.split()
        if args[0] not in self.class_list:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        all_objs = storage.all()
        id_flag = False

        for obj_id in all_objs.keys():
            if args[1] == all_objs[obj_id].id:
                id_flag = True

        if id_flag is False:
            print("** no instance found **")
            return

        for obj_id in all_objs.keys():
            if args[1] == all_objs[obj_id].id:
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

        if line not in self.class_list:
            print("** class doesn't exist **")
            return

        for key, obj in all_objs.items():
            if line == obj.__class__.__name__:
                string_list.append(str(obj))
        print(string_list)
        return

    def do_update(self, line):
        """Updates an instance based on the class name and id"""

        if len(line) == 0:
            print("** class name missing **")
            return

        args = line.split()

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        if args[0] not in self.class_list:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        all_objs = storage.all()
        id_flag = False

        for obj_id in all_objs.keys():
            if args[1] == all_objs[obj_id].id:
                id_flag = True

        if id_flag is False:
            print("** no instance found **")
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
                        setattr(obj, args[2], args[3].strip('"').strip("'"))
        storage.save()
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
