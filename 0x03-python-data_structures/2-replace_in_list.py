#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replaces the element at the specified index in a given list.

    Parameters:
    - my_list (list): The list in which the element is to be replaced.
    - idx (int): The index of the element to be replaced.
    - element: The new element to be inserted at the specified index.

    Returns:
    - list: The modified list with the element replaced at the specified index.
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
