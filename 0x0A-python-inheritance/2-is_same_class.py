#!/usr/bin/python3
"""Defines a function to check if an object belongs to a specific class."""


def is_same_class(obj, a_class):
    """
    Determine if an object is exactly an instance of the specified class.

    Args:
        obj: The object to evaluate.
        a_class: The class to compare the object against.

    Returns:
        True if obj is exactly an instance of a_class, False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
