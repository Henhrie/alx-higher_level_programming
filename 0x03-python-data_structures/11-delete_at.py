#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes an element at a specified index in a list.
    Parameters:
        my_list (list): The list from which the element is to be deleted.
        Defaults to an empty list.
        idx (int): The index of the element to be deleted. Defaults to 0.
    Returns:
    list: The updated list after deleting the element at the specified index.
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        del my_list[idx]
    return my_list
