#!/usr/bin/python3
"""Defines a function to check if an object is an inherited instance
of a specified class."""


def inherits_from(obj, a_class):
    """
    Determines if an object inherits from a class, excluding direct
    instances of that class.

    Args:
        obj: The object under inspection.
        a_class: The class used for comparison.

    Returns:
        True if obj is an inherited instance of a_class
        (not a direct instance), False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
