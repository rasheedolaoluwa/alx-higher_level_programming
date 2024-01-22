#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(fct, *args):
    """
    Executes a function safely, handling any exceptions that occur.

    Args:
        fct: A function object to be executed.
        *args: Variable length argument list for the function.

    Returns:
        The result of the function if no exceptions occur, or None if an
        exception is raised. In case of an exception, the error message is
        printed to standard error.
    """
    try:
        res = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return res
