#!/usr/bin/python3
"""Defines a class Square."""

class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with optional size and position.
        
        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position to place the square (default is (0, 0)).
        
        Raises:
            TypeError: If size is not an integer or if position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or if position contains negative integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position attribute.
        
        Args:
            value (tuple): A tuple of two positive integers for position.
        
        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #.
        
        The position determines where the square is printed. If size is 0,
        an empty line is printed.
        """
        if self.__size == 0:
            print("")
            return

        # Print new lines to account for position[1]
        print("\n" * self.__position[1], end="")

        # Print the square with spaces for position[0]
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
