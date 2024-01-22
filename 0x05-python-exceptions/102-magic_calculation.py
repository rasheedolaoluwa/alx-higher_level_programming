#!/usr/bin/python3
def magic_calculation(a, b):
    """
    Performs a custom calculation based on input values.

    The function iterates through a range and performs a calculation involving
    'a' and 'b'. If a certain condition based on 'i' and 'a' is met, an
    exception is raised and handled within the loop.

    Args:
        a: First input value.
        b: Second input value.

    Returns:
        The calculated result based on the logic defined in the function.
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += a ** b / i
        except Exception:
            result = b + a
            break
    return result
