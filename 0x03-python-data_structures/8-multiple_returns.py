#!/usr/bin/python3
def multiple_returns(sentence):

"""
Calculate the length of the sentence and return a tuple containing the length of the
    sentence and the first character of the sentence.

Parameters:
    sentence (str): The input sentence.

Returns:

tuple: A tuple containing the length of the sentence and the first character
of the sentence.
"""
    my_tuple = ()
    if len(sentence) == 0:
        my_tuple = 0, "None"
    else:
        my_tuple = len(sentence), sentence[0]
    return my_tuple
