#!/usr/bin/python3
def class_to_json(obj):
    """Return the dictionary description for JSON serialization of an object."""
    return {key: value for key, value in obj.__dict__.items() 
            if isinstance(value, (list, dict, str, int, bool))}

