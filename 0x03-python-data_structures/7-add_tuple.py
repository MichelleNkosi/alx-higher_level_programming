#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure tuple_a and tuple_b have at least 2 elements by appending zeros where needed
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Add the first and second elements of each tuple
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    
    return new_tuple
