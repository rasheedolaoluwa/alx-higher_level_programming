#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print elements from a list up to a specified limit.

    Args:
        my_list (list): List from which to print elements.
        x (int): Number of elements to print from the list.

    Returns:
        Number of elements actually printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return count
