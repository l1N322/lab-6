#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def flatten(data):
    """
    Рекурсивно преобразует вложенный список в плоский список.
    """
    result = []

    for element in data:
        if type(element) == list:
            result.extend(flatten(element))
        else:
            result.append(element)

    return result

if __name__ == "__main__":
    print(flatten([1, [2, [3, 4], 5]]))
    print(flatten([0, [1, 2, [3, [4], 5], 6]]))