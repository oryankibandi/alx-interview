#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return -1

    num_times = 0
    sorted_l = sorted(coins)

    while total > 0:
        if len(sorted_l) == 0:
            return -1
        total -= max(sorted_l)
        num_times += 1
        if total == 0:
            return num_times
        if total < 0:
            return -1
        if total < max(sorted_l):
            sorted_l.pop()
