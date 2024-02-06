#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Reads and prints the contents of a UTF8 text file to standard output.

    Opens a file specified by 'filename' and prints its contents to stdout,
    ensuring the text is interpreted in UTF-8 encoding.

    Args:
        filename (str): The name of the file to read.
        Defaults to an empty string.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
