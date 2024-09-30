#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))  # Try to format and print the integer
        return True
    except (ValueError, TypeError):  # Catch exceptions if value is not an integer
        return False
