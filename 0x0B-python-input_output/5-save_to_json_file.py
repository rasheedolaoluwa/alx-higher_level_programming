#!/usr/bin/python3
"""Defines a function for writing an object to a file in JSON format."""
import json


def save_to_json_file(my_obj, filename):
    """Serializes a Python object and writes it to a text file in JSON format.

    Args:
        my_obj: The Python object to serialize.
        filename: The name of the file where the JSON string will be written.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
