#!/usr/bin/python3
import json
from sqlalchemy import delete
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
	__file_path = "file.json"
	__objects = {}

	def all(self, cls = None):
		return self.__objects

	def new(self, obj):
		object_name = obj.__class__.__name__
		FileStorage.__objects["{}.{}".format(object_name, obj.id)] = obj

	def save(self):
		object_dictionary = {}
		for key, obj in FileStorage.__objects.items():
			object_dictionary[key] = obj.to_dict()
		with open(FileStorage.__file_path, "w") as f:
			json.dump(object_dictionary, f)

	def reload(self):
		try:
			with open(FileStorage.__file_path) as f:
				object_dictionary = json.load(f)
				for key, value in object_dictionary.items():
					FileStorage.__objects[key] = BaseModel(**value)
		except FileNotFoundError:
			pass

	def delete(self, obj = None):
		if obj is not None:
			key = obj.__class__.__name__ + "." + obj.id
			if key in self.__objects:
				del self.__objects[key]