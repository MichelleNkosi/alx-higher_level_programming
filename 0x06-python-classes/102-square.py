#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        
        Args:
            size (int or float): The size of the new square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.
        
        Args:
            value (int or float): The size of the square.
        
        Raises:
            TypeError: If value is not a number (float or int).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare two squares for equality based on their area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare two squares for inequality based on their area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if one square's area is less than another."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if one square's area is less than or equal to another."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if one square's area is greater than another."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if one square's area is greater than or equal to another."""
        return self.area() >= other.area()
