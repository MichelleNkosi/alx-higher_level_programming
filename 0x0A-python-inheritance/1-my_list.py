#!/usr/bin/python3
"""
Module 1-my_list: contains the class MyList.
"""

class MyList(list):
    """Inherits from the built-in list class."""

    def print_sorted(self):
        """Prints the list, sorted in ascending order."""
        print(sorted(self))

