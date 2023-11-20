#!/usr/bin/python3


def list_division(list_1, list_2, length):
return [list_1[i] / list_2[i] if list_2[i] != 0 else 0 for i in range(length)]
