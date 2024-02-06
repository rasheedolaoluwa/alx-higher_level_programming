#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a specific string in a file.

    Reads through 'filename', and after each line containing 'search_string',
    'new_string' is inserted into the file.

    Args:
        filename (str): The path to the file to be modified.
        search_string (str): The text to search for within the file.
        new_string (str): The text to append after each occurrence
        of search_string.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
