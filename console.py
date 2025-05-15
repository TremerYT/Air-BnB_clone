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

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    
    def do_create(self, arg):
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        args = shlex.split(arg)
        objects = []
        if len(args) == 0:
            for obj in storage.all().values():
                objects.append(str(obj))
        else:
            class_name = args[0]
            if class_name not in classes:
                print("** class doesn't exist **")
                return
            for key, obj in storage.all().items():
                if key.startswith(class_name + "."):
                    objects.append(str(obj))
        print(objects)

    def do_update(self, arg):
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        obj = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3]
        try:
            if attr_value.isdigit():
                attr_value = int(attr_value)
            else:
                try:
                    attr_value = float(attr_value)
                except ValueError:
                    attr_value = attr_value.strip('"')
        except Exception:
            pass
        if attr_name not in ["id", "created_at", "updated_at"]:
            setattr(obj, attr_name, attr_value)
            obj.save()

    def default(self, line):
        if '.' in line:
            parts = line.split('.', 1)
            class_name = parts[0]
            if parts[1] == "all()":
                return self.do_all(class_name)
            elif parts[1].startswith("show(") and parts[1].endswith(")"):
                id_arg = parts[1][5:-1].strip('"').strip("'")
                if not class_name:
                    print("** class name missing **")
                    return
                if class_name not in classes:
                    print("** class doesn't exist **")
                    return
                if not id_arg:
                    print("** instance id missing **")
                    return
                key = "{}.{}".format(class_name, id_arg)
                if key not in storage.all():
                    print("** no instance found **")
                    return
                print(storage.all()[key])
                return
            elif parts[1].startswith("destroy(") and parts[1].endswith(")"):
                id_arg = parts[1][8:-1].strip('"').strip("'")
                if not class_name:
                    print("** class name missing **")
                    return
                if class_name not in classes:
                    print("** class doesn't exist **")
                    return
                if not id_arg:
                    print("** instance id missing **")
                    return
                key = "{}.{}".format(class_name, id_arg)
                if key not in storage.all():
                    print("** no instance found **")
                    return
                del storage.all()[key]
                storage.save()
                return
            elif parts[1].startswith("update(") and parts[1].endswith(")"):
                # Parse arguments inside update()
                args_str = parts[1][7:-1]
                args = shlex.split(args_str)
                if not class_name:
                    print("** class name missing **")
                    return
                if class_name not in classes:
                    print("** class doesn't exist **")
                    return
                if len(args) == 0:
                    print("** instance id missing **")
                    return
                if len(args) == 1:
                    print("** attribute name missing **")
                    return
                if len(args) == 2:
                    print("** value missing **")
                    return
                key = "{}.{}".format(class_name, args[0])
                if key not in storage.all():
                    print("** no instance found **")
                    return
                attr_name = args[1]
                attr_value = args[2]
                obj = storage.all()[key]
                try:
                    if attr_value.isdigit():
                        attr_value = int(attr_value)
                    else:
                        try:
                            attr_value = float(attr_value)
                        except ValueError:
                            attr_value = attr_value.strip('"')
                except Exception:
                    pass
                if attr_name not in ["id", "created_at", "updated_at"]:
                    setattr(obj, attr_name, attr_value)
                    obj.save()
                return
        print("*** Unknown syntax: {}".format(line))

    def do_quit(self, _):
        return True

    def do_EOF(self, _):
        print()
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()