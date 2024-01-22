#!/usr/bin/python3

def safe_print_integer(value):
    """
    Attempt to print a value as an integer.

    Args:
        value (int): The value to be printed as an integer.

    Returns:
        bool: False if a TypeError or ValueError occurs, True otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
