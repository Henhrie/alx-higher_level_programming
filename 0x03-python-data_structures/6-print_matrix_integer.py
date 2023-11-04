#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.
    Parameters:
        matrix (List[List[int]]): The matrix to be printed.    
    Returns:
        None
  """

    for row in matrix:
        for col in row:
            print("{:d}".format(col), end=" " if col != row[-1] else "")
        print()
