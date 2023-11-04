#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Returns the maximum integer from a given list.
    Parameters:
    my_list (list): The input list of integers. Defaults to an empty list.
   Returns:
  int or None: The maximum integer from the input list.
  Returns None if the list is empty.
    """
    new_list = []
    if my_list:
        my_list.sort(reverse=True)
        return (my_list[0])
    return (None)
