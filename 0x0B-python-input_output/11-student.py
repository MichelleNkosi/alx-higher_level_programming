#!/usr/bin/python3
class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes the student with the given attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attributes in the list are retrieved.
        Otherwise, all attributes are retrieved.
        """
        if attrs is None:
            return self.__dict__
        
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from the json dictionary.
        Assumes json is a dictionary where the keys match the public attributes of the instance.
        """
        for key, value in json.items():
            setattr(self, key, value)

