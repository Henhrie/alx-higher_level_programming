#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Returns the element at the specified index in the given list.

    Parameters:
        my_list (list): The list from which to retrieve the element.
        idx (int): The index of the element to retrieve.

    Returns:
        The element at the specified index in the given list. If the index is
        out of range (less than 0 or greater than or equal to the length of
        the list), None is returned.
    """
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    return my_list[idx]
