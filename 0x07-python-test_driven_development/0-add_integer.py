#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """
    Calculate the sum of two numbers, where the numbers
    are either integers or floats.

    If either argument is a float, it is typecasted to
    an integer before the addition.

    Args:
        a (int or float): The first number to be added.
        b (int or float, optional): The second number to
        be added. Defaults to 98.

    Raises:
        TypeError: If either 'a' or 'b' is neither an
        integer nor a float.

    Returns:
        int: The sum of 'a' and 'b'.
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
