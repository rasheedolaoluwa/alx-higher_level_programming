#!/usr/bin/python3
"""Defines a function for writing to a file."""


def write_file(filename="", text=""):
    """Writes a string to a UTF8-encoded text file
    and returns the character count.

    This function opens or creates a file specified
    by 'filename' and writes 'text' to it in UTF-8
    encoding, overwriting any existing content.

    Args:
        filename (str): The path to the file.
        text (str): The content to write into the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
