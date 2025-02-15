#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)  # Output: 1

    b2 = Base()
    print(b2.id)  # Output: 2

    b3 = Base()
    print(b3.id)  # Output: 3

    b4 = Base(12)
    print(b4.id)  # Output: 12

    b5 = Base()
    print(b5.id)  # Output: 4
