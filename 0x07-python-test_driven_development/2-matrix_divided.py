#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.

    This function performs element-wise division of a
    matrix by a given divisor. The function checks for
    the integrity and correctness of the matrix and the divisor.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The number by which the matrix elements
        are to be divided.

    Raises:
        TypeError: If elements of the matrix are not lists of integers
        or floats.
        TypeError: If rows of the matrix are not of equal size.
        TypeError: If div is neither an integer nor a float.
        ZeroDivisionError: If div is zero.

    Returns:
        list of lists of float: A new matrix with each element of
        the input matrix divided by the divisor, rounded to
        2 decimal places.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
