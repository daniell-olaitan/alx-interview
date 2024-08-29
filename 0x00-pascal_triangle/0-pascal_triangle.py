#!/usr/bin/python3
"""
Module implements a function that implements the Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Implements pascal's triangle

    Args:
        n -> number of rows in the triangle

    Returns:
        List of lists representing the Pascal's Triangle
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]

    sub_triangle = pascal_triangle(n-1)
    last_row = sub_triangle[-1]
    last_row_len = len(last_row)
    new_row = (
        [1] +
        [last_row[idx] + last_row[idx-1] for idx in range(1, last_row_len)] +
        [1]
    )
    triangle = sub_triangle[:]
    triangle.append(new_row)

    return triangle
