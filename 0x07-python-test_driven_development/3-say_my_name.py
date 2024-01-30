#!/usr/bin/python3
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """
    Print a full name by combining a first name and an optional last name.

    This function prints a string in the format
    "My name is <first_name> <last_name>".

    Args:
        first_name (str): The first name to be printed.
        last_name (str): The last name to be printed;
        it is optional and defaults to an empty string.

    Raises:
        TypeError: If either 'first_name' or 'last_name' is not a string.

    Note:
        The function prints directly to standard output.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
