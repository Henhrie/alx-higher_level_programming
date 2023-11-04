#!/usr/bin/python3
def multiple_returns(sentence):
 """
    Calculate the length of a given sentence and return a tuple containing
    the length and the first character of the sentence.
    Parameters:
    sentence (str): The sentence to calculate the length of.
    Returns:
    tuple: A tuple containing two elements:
           - sen_len (int): The length of the sentence.
           - first_char (str): The first character of the sentence.
    """
    if not sentence:
        sentence = None
    if sentence:
        sen_len = len(sentence)
    else:
        sen_len = 0
    return (sen_len, sentence if not sentence else sentence[:1])
