#!/usr/bin/python3
def no_c(my_string):
    """
    Removes all occurrences of the character "c" (case-insensitive)
    from the given string.
    Args:
        my_string (str): The input string.

    Returns:
        str: The modified string with all occurrences of "c" removed.
    """
    new_string = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            new_string += elements
    return new_string
