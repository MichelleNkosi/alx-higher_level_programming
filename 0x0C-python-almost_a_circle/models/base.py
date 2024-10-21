#!/usr/bin/python3
"""
Base module
"""

class Base:
    """
    Base class for managing id attribute across future classes
    """

    __nb_objects = 0  # Private class attribute to track number of objects

    def __init__(self, id=None):
        """
        Initialize a new Base instance.
        Args:
            id (int, optional): The id of the object. If None, the id will be auto-assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
