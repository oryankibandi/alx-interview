#!/usr/bin/env python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """pascal_triangle - returns a list of lists of integers
    representing the Pascal’s triangle of `n`."""

    arr = []
    prev_arr = []

    if n <= 0:
        return arr

    for en in range(1, n + 1):
        new_arr = []
        for i in range(0, en):
            if i == 0 or i == (en - 1):
                new_arr.append(1)
            else:
                if (len(prev_arr)) > 0:
                    new_val = prev_arr[i] + prev_arr[i - 1]
                    new_arr.append(new_val)

        arr.append(new_arr)
        prev_arr = new_arr

    return arr
