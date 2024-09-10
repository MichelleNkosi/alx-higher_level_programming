#!/usr/bin/python3

def print_tebahpla():
    for i in range(25, -1, -1):
        if i % 2 == 0:
            print(chr(122 - i), end="")
        else:
            print(chr(90 - (i - 1)), end="")

print_tebahpla()
