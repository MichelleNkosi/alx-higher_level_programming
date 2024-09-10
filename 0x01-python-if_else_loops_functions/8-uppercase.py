#!/usr/bin/python3
# Function to print a string in uppercase

def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            print(chr(ord(char) - 32), end="")
        else:
            print(char, end="")
    print()  # Print a newline at the end
