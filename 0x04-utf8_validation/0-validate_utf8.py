#!/usr/bin/python3
"""Valudates UTF-8 dataset"""


import typing


def single_byte(num: int) -> bool:
    """Checks if a number indicates a single byte"""
    a = num >> 7
    if (a & 1 == 0):
        return True
    else:
        return False


def is_continuation(num: int) -> bool:
    """checks if 1st and 2nd MSB 10xxxxxx are `1` and `0`"""
    a = num >> 7  # check if 1st MSB 1xxxxxxx is `1`
    b = num >> 6
    if (a & 1 == 1 and (b & 1) == 0):
        return True
    else:
        return False


def count_bytes(num: int) -> int:
    """Counts the number of bytes

    Args:
        num (int): first byte

    Returns:
        int: Number of bytes
    """
    count = 0
    n = bin(num)[2:]
    for i in n:
        if int(i) == 1:
            count += 1
        if int(i) == 0:
            break
    return count


def validUTF8(data: typing.List[int]) -> bool:
    """Validates a utf-8 dataset"""
    index = 0

    if len(data) <= 0:
        return False

    if single_byte(data[0]):
        if len(data) == 1:
            return True
        else:
            data.pop(0)
            return validUTF8(data)
    else:
        num_of_bytes = count_bytes(data[0])
        if num_of_bytes <= 1:
            return False
        for i in range(1, num_of_bytes):
            index = i
            if not is_continuation(data[i]):
                return False
        if len(data) - 1 > index:
            return validUTF8(data[(index + 1):])
        else:
            return True
