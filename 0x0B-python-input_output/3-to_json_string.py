#!/usr/bin/python3
"""Defines a function that converts a Python object to a JSON string."""
import json


def to_json_string(my_obj):
    """Converts a Python object into its JSON string representation.

    Takes a Python object and returns its JSON string format.

    Args:
        my_obj: A Python object to be serialized to a JSON string.

    Returns:
        A string: JSON representation of 'my_obj'.
    """
    return json.dumps(my_obj)
