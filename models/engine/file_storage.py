import json
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

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    cls = {
                        "BaseModel": BaseModel,
                        "User": User,
                        "State": State,
                        "City": City,
                        "Amenity": Amenity,
                        "Place": Place,
                        "Review": Review
                    }.get(class_name)
                    if cls:
                        FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            if key in self.__objects:
                del self.__objects[key]