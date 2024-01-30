#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """
    Print text with special formatting rules.

    Inserts two new lines after each '.', '?', and ':'. Leading
    spaces are removed after these characters and newline characters.

    Args:
        text (str): The text to be formatted and printed.

    Raises:
        TypeError: Raised if 'text' is not a string.

    Note:
        Directly prints to standard output.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text):
        print(text[c], end="")
        if text[c] in ".?:":
            print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
