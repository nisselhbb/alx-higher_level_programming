#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    result = []
    for row in matrix:
        square_row = []
        for i in row:
            square_i = i ** 2
            square_row.append(square_i)
        result.append(square_row)
    return result
