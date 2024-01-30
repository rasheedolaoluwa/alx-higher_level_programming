#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """
    Print a square of a given size using the '#' character.

    This function prints a square where both the height and
    the width are equal to the 'size' argument.
    The square is printed using the '#' character.

    Args:
        size (int): The height and width of the square.

    Raises:
        TypeError: If 'size' is not an integer.
        ValueError: If 'size' is less than 0.

    Note:
        Each line of the square ends with a newline character.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
