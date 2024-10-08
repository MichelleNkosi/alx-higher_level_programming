#!/usr/bin/python3
"""
This module provides a function print_square that prints a square with
the character '#'.
"""

def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size: The size of the square, must be an integer and >= 0.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """

    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is greater than or equal to 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)
