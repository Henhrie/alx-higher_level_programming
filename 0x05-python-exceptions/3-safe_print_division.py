
#!/usr/bin/python3


def safe_print_division(a, b):
    """
    Safely divides two numbers and prints the result.
    
    Args:
        a: The numerator.
        b: The denominator.
    
    Returns:
        The division result.
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result:", div)
    return (div)

