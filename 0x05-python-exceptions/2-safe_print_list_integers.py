#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Print up to x integer elements from a list.

    Args:
        my_list (list): List from which to print integer elements.
        x (int): Maximum number of integer elements to print.

    Returns:
        int: Number of integer elements actually printed.
    """
    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count
