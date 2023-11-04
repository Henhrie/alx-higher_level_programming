#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Determines whether each element in the given list is divisible by 2.
    Parameters:
    my_list (list): A list of integers.
    Returns:
    new_list (list): A list of booleans indicating whether each element in
      the given list is divisible by 2.
    """
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
