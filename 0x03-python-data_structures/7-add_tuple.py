#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
  Calculates the sum of two tuples and returns a new tuple.
    Parameters:
    tuple_a: The first tuple to be added. Default value is an empty tuple.
    tuple_b: The second tuple to be added. Default value is an empty tuple.
    Returns:
    new_tuple: The resulting tuple after adding tuple_a and tuple_b.
    Example:
    >>> add_tuple((1, 2), (3, 4))
    (4, 6)
    """
    new_tuple = ()
    tuple_1 = tuple_a + (0, 0)
    tuple_2 = tuple_b + (0, 0)
    new_tuple = tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1]
    return new_tuple
