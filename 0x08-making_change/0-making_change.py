#!/usr/bin/python3
"""Make change interview task"""


def makeChange(coins: list, total: int) -> int:
    """determines the fewest number of coins needed
    to meet a given amount `total`"""
    if total <= 0:
        return -1

    num_times = 0
    sorted_l = sorted(coins)

    while total > 0:
        if len(sorted_l) == 0:
            return -1
        if total < max(sorted_l):
            sorted_l.pop()
        else:
            total -= max(sorted_l)
            num_times += 1
            if total == 0:
                return num_times
            if total < 0:
                return -1
