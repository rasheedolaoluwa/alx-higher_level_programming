#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Safely computes and prints the division of two numbers.

    Args:
        a: Numerator.
        b: Denominator.

    Returns:
        The result of division, or None if an error occurs.
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
