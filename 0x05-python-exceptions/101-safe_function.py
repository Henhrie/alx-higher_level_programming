#!/usr/bin/python3

import sys


def safe_function(func, *args):
    try:
        result = func(*args)
        return result
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None
    