#!/usr/bin/python3

def raise_exception_with_message(message=""):
    """
    Raises a NameError exception with the given message.
    
    Args:
        message (str): The message to include in the exception.
    
    Raises:
        NameError: The exception with the given message.
    """
    raise NameError(message)
