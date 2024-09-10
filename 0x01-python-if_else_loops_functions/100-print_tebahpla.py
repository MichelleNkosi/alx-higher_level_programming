#!/usr/bin/python3

def print_tebahpla():
    for i in range(25, -1, -1):
        char = chr(122 - i) if i % 2 == 0 else chr(90 - i)
        print("{}".format(char), end="")
    print()  # Print a newline at the end
