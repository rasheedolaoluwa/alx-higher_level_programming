#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divides elements of two lists, handling various exceptions.

    Args:
        my_list_1 (list): First list of numerators.
        my_list_2 (list): Second list of denominators.
        list_length (int): Number of elements to process for division.

    Returns:
        list: Contains results of the divisions or 0 in case of errors.
    """
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return new_list
