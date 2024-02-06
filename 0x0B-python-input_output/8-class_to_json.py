#!/usr/bin/python3
"""Defines a function that converts a Python class instance
to a JSON-friendly dictionary."""


def class_to_json(obj):
    """Returns the dictionary representation of a simple
    data structure for JSON serialization.

    Extracts the `__dict__` attribute of `obj` to get a dictionary
    representation that can be easily converted to JSON format.

    Args:
        obj: An instance of a Python class.

    Returns:
        A dictionary representation of `obj`'s public attributes
        and methods.
    """
    return obj.__dict__
