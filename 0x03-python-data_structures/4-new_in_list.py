#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Updates the given list with a new element at the specified index.

    Parameters:
      my_list (list): The list to be updated.
        idx (int): The index at which the new element should be inserted.
        element (Any): The new element to be inserted.
    Returns:
        list: The updated list with the new element inserted at the specified index.
  """
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    new_list = list(my_list)
    new_list[idx] = element
    return new_list
