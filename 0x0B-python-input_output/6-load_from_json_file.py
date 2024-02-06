#!/usr/bin/python3
"""Defines a function for creating a Python object from a JSON file."""
import json


def load_from_json_file(filename):
    """Deserializes a JSON file to a Python object.

    Reads from 'filename' and converts its JSON content into a Python object.

    Args:
        filename: The path to the JSON file to be deserialized.

    Returns:
        A Python object based on the JSON file content.
    """
    with open(filename) as f:
        return json.load(f)
