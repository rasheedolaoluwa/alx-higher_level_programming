#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a function for converting a JSON string to a Python object."""
import json


def from_json_string(my_str):
    """Converts a JSON string to its corresponding Python object.

    Args:
        my_str: A JSON string to be deserialized.

    Returns:
        The Python object representation of 'my_str'.
    """
    return json.loads(my_str)
