#!/usr/bin/python3
"""defining a pascal_tringle function"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
        the Pascal’s triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        curr_row = triangle[-1]
        new_row = [1]

    for i in range(len(curr_row) - 1):
        new_row.append(curr_row[i] + cuur_row[i + 1])

    new_row.append(1)
    triangle.append(new_row)
    return triangle
