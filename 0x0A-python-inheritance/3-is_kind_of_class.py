#!/usr/bin/python3
"""Defines a function to check object class inheritance."""


def is_kind_of_class(obj, a_class):
    """
    Determine if an object is or inherits from a specified class.

    Args:
        obj: The object to evaluate.
        a_class: The reference class for comparison.

    Returns:
        True if obj is an instance or inherits from a_class, False otherwise.
    """
    return isinstance(obj, a_class)
