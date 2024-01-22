#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """
    Prints a value as an integer and handles exceptions.

    Args:
        value (int): The value to be printed as an integer.

    Returns:
        bool: True if the value is printed as an integer, False if a TypeError
              or ValueError occurs. In case of an exception, the error message
              is printed to standard error.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
