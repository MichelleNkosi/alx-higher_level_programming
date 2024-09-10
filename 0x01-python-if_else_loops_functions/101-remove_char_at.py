#!/usr/bin/python3

def remove_char_at(str, n):
    # Check if the index n is valid
    if n < 0 or n >= len(str):
        return str

    # Return the string excluding the character at index n
    return str[:n] + str[n+1:]
