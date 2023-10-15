#!/usr/bin/python3
"""
This module defines the FileStorage class.
"""
import json
import os


class FileStorage:
    """
    This class handles the serialization and deserialization of
    objects to and from a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the __objects dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets the object with a key of <obj class name>.
        id in the __objects dictionary.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes the __objects to the JSON file
        located at the path: __file_path
        """
        obj_dict = {key: value.to_dict()
                    for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects (if the file exists)"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                from models.base_model import BaseModel
                from models.user import User
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.place import Place
                from models.review import Review
                classes = {
                    'BaseModel': BaseModel,
                    'User': User,
                    'State': State,
                    'City': City,
                    'Amenity': Amenity,
                    'Place': Place,
                    'Review': Review
                }
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = classes[class_name]
                    new_obj = cls(**value)
                    self.new(new_obj)
        except FileNotFoundError:
            pass
