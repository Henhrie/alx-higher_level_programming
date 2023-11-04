#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Prints the integers in a list in reverse order.

    Args:
        my_list (list): The list of integers to be printed in reverse order.
        Defaults to an empty list.
    Returns:
        None
    """
    if my_list:
        for elm in my_list[::-1]:
            print("{:d}".format(elm))
