#!/usr/bin/python3
"""writing a function that divides all
    elements of a matrix"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    args:
        matrix: the input containing integers or floats
        div: the divisor
    Raises:
        TypeError: if the matrix is not a list of lists
            of integers and floats/ if the rows of the matrix
            do not have the same size/ if the divisor is
            not a number
        ZeroDivisionError: if the divisor is equal to 0
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(message)
    for row in matrix:
        if type(row) is not list:
            raise TypeError(message)
    row_size = set(len(row) for row in matrix)
    if len(row_size) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
