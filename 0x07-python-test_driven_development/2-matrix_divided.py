#!/usr/bin/python3
"""
This module provides a function matrix_divided that divides all elements
of a matrix by a number.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor, must be a number (integer or float).

    Returns:
        A new matrix with all elements divided by div and rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats.
        TypeError: If all rows of the matrix are not the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is zero.
    """

    # Check if matrix is a list of lists of integers or floats
    if (not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(ele, (int, float)) for row in matrix for ele in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div and round to 2 decimal places
    return [[round(ele / div, 2) for ele in row] for row in matrix]
