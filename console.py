#!/usr/bin/python3
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
		print(new_instance.id)
		new_instance.save()
		
	def do_show(self, arg):
		args = shlex.split(arg)
		if len(args) == 0:
			print("** class name missing **")
			return
		if args[0] not in classes:
			print("** class doesn't exist **")
			return
		if len(args) == 1:
			print("** instance id missing **")
			return
		key = "{}.{}".format(args[0], args[1])
		if key not in storage.all():
			print("** no instance found **")
			return
		print(storage.all()[key])

	def do_destroy(self, arg):
		args = shlex.split(arg)
		if len(args) == 0:
			print("** class name missing **")
			return
		if args[0] not in classes:
			print("** class doesn't exist **")
			return
		if len(args) == 1:
			print("** instance id missing **")
			return
		key = "{}.{}".format(args[0], args[1])
		if key not in storage.all():
			print("** no instance found **")
			return
		del storage.all()[key]
		storage.save()

	def do_all(self, arg):
		args = shlex.split(arg)
		object_list = []
		if len(args) == 0:
			for values in storage.all().values():
				object_list.append(str(values))
		else:
			if args[0] not in classes:
				print("** class doesn't exist **")
				return
			for key, value in storage.all().items():
				if key.startswith(args[0] + "."):
					object_list.append(str(value))
		print(object_list)

	def do_update(self, arg):
		args = shlex.split(arg)
		if len(args) == 0:
			print("** class name missing **")
			return
		if args[0] not in classes:
			print("** class doesn't exist **")
			return
		if len(args) == 1:
			print("** instance id missing **")
			return
		key = "{}.{}".format(args[0], args[1])
		if key not in storage.all():
			print("** no instance found **")
			return
		if len(args) == 2:
			print("** attribute name missing **")
			return
		if len(args) == 3:
			print("** value missing **")
			return
		objects = storage.all()[key]
		attribute_name = args[2]
		attribute_value = args[3]

		try:
			if attribute_value.isdigit():
				attribute_value = int(attribute_value)
			else:
				try:
					attribute_value = float(attribute_value)
				except ValueError:
					attribute_value = str(attribute_value)
		except Exception:
			pass

		if attribute_name not in ["id", "created_at", "updated_at"]:
			setattr(objects, attribute_name, attribute_value)
			objects.save()

	def do_count(self, arg):
		args = shlex.split(arg)
		if len(args) == 0:
			print("** class name missing **")
			return
		if args[0] not in classes:
			print("** class doesn't exist **")
			return
		count = 0
		for key in storage.all().keys():
			if key.startswith(args[0] + "."):
				count += 1
		print(count)

	def do_quit(self, _):
		return True

	def do_EOF(self, _):
		print()
		return True

	def emptyline(self):
		pass


if __name__ == '__main__':
	HBNBCommand().cmdloop()