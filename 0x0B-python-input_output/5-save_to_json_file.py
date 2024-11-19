#!/usr/bin/python3
"""
This module defines a function that saves an object to a text file
using its JSON representation.
"""
import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj (object): The object to be serialized to JSON and written to the file.
        filename (str): The name of the file to write the JSON data to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

