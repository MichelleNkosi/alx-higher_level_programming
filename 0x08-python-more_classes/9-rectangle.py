#!/usr/bin/python3
# 9-rectangle.py
"""Defines a Rectangle class."""

class Rectangle:
    """Represents a rectangle.
    
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol: Used as the symbol for string representation (can be any type).
    """
    
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.
        
        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.
        
        Args:
            value (int): The new width value.
        
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.
        
        Args:
            value (int): The new height value.
        
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle.
        
        If width or height is equal to 0, the perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle using print_symbol.
        
        If width or height is equal to 0, return an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = str(self.print_symbol) * self.__width
        return "\n".join([rect_str for _ in range(self.__height)])

    def __repr__(self):
        """Return a string representation of the rectangle for reproduction with eval().
        
        The string returned is in the form: Rectangle(width, height).
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted and decrease the instance count."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the greater area or rect_1 if both are equal.
        
        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.
        
        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        
        Returns:
            Rectangle: The rectangle with the greater area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size.
        
        Args:
            size (int): The size of the square.
        
        Returns:
            Rectangle: A new Rectangle instance with both width and height equal to size.
        """
        return cls(size, size)