#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Prints a specified number of elements from a given list.

    Parameters:
        my_list (list): The list from which elements will be printed.
        x (int): The number of elements to print from 'my_list'.

    Returns:
        int: The actual number of elements successfully printed.
    """

    printed_count = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            printed_count += 1
        except IndexError:
            break

    print("")
    return printed_count

