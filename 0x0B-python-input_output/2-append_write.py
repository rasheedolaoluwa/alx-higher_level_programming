#!/usr/bin/python3
"""Defines a function for appending text to a file."""


def append_write(filename="", text=""):
    """Appends a given string to the end of a UTF-8 encoded text file.

    This function will add the specified 'text' to the file named 'filename'.
    If the file does not exist, it will be created.

    Args:
        filename (str): The file to which the text will be appended.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
