#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if it's allowed.

    Checks if an object allows attribute addition, then
    adds the attribute if possible.

    Args:
        obj (any): The object to which the attribute should be added.
        att (str): The name of the attribute to be added.
        value (any): The value to set for the attribute.

    Raises:
        TypeError: If the attribute cannot be added to the object.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
