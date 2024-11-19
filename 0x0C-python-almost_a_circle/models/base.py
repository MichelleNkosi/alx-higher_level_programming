#!/usr/bin/python3

import json
import os

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id if id is not None else Base.__nb_objects + 1
        Base.__nb_objects += 1

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy Square instance
        else:
            dummy = None

        if dummy is not None:
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file."""
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as file:
            json_string = file.read()
            list_dicts = cls.from_json_string(json_string)
            return [cls.create(**d) for d in list_dicts]

