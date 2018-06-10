#!/usr/bin/python3
"""
Entry to command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    Entry to command interpreter
    """
    prompt = "(hbnb)"
    classes = {"BaseModel", "State", "City", "Amenity", "Place", "Review", "User"}

    def do_EOF(self, line):
        """Exit on Ctrl-D"""
        return True

    def do_quit(self, line):
        """Exit on quit"""
        return True

    def emptyline(self):
        """Overwrite default behavior to repeat last cmd"""
        pass

    def do_create(self, line):
        """Create instance specified by user"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Print string representation: name and id"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, line):
        """Destroy instance specified by user; Save changes to JSON file"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[name]
        except IndexError:
            print("** instance id missing **")

    def do_all(self, line):
        """Print all objects or all objects of specified class"""
        args = parse(line)
        obj_list = []
        if len(line) == 0:
            for objs in storage.all().values():
                obj_list.append(str(objs))
            print("[", end="")
            print(", ".join(o for o in obj_list), end="")
            print("]")
        elif args[0] in HBNBCommand.classes:
            for key, objs in storage.all().items():
                if args[0] in key:
                    obj_list.append(str(objs))
            print("[", end="")
            print(", ".join(o for o in obj_list), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Update if given exact object, exact attribute"""
        args = parse(line)
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            setattr(storage.all()[key], args[2], args[3])
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def default(self, line):
        """accepts class name followed by arguement"""
        functions = ['all', 'show', 'destroy']
        args = line.split('.')
        arg1 = args[0]
        if arg1 not in HBNBCommand.classes:
            print("**invalid syntax**")
            return
        args = args[1].split('(')
        arg2 = args[0]
        args = args[1].split(')')
        arg3 = args[0]
        arg3 = arg3.strip("'")
        print(type(arg2))
        if arg2 in functions:
            if arg2 == 'all':
                print('inside all if')
                HBNBCommand.do_all(self, arg1)
            elif arg2 == 'show':
                arg = arg1 + ' ' + arg3
                HBNBCommand.do_show(self, arg)
            elif arg2 == 'destroy':
                arg = arg1 + ' ' + arg3
                HBNBCommand.do_destroy(self, arg)
        else:
            print("**invalid syntax**")
def parse(line):
    """Helper method to parse user typed input"""
    return tuple(line.split())

if __name__ == "__main__":
    HBNBCommand().cmdloop()
