#!/usr/bin/python3
"""Defines a class Square."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a square with a private size attribute.
        
        Args:
            size (int): The size of the square (default is 0).
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # This will invoke the setter to validate the size

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute.
        
        Args:
            value (int): The size of the square.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
