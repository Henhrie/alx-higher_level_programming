#!/usr/bin/python3


def safe_print_list(items, limit):
    count = 0
    index = 0
    while index < limit:
        try:
            print(f"{items[index]}", end="")
            count += 1
        except IndexError:
            break
        index += 1
    print("")
    return count
