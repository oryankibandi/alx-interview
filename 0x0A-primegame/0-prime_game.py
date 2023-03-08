#!/usr/bin/python3
"""Prime Game interviwe question
"""


def is_prime(num: int) -> bool:
    """
    checks if a number is a prime
    """
    is_prime = True

    if num >= 2:
        if num % 2 == 0:
            is_prime = False
    if num >= 3:
        if num % 3 == 0:
            is_prime = False
    if num >= 5:
        if num % 5 == 0:
            is_prime = False
    if num >= 7:
        if num % 7 == 0:
            is_prime = False

    return is_prime


def generate_nums(max: int) -> list[int]:
    """
    Generates a list of numbers from 1 to max
    """

    return [n for n in range(1, max + 1)]


def remove_multiples(num: int, arr: list[int]) -> list[int]:
    """removes multiples of a number"""
    if arr is None or num is None:
        return []

    new_arr = []

    for i in arr:
        if i % num != 0:
            new_arr.append(i)

    return new_arr


def isWinner(x: int, nums: list[int]) -> str | None:
    """Gets the winner of a prime game"""
    round = 1
    maria_turn = True
    maria_victories = 0
    ben_victories = 0

    for j in nums:
        if round > x:
            break
        new_list = generate_nums(j)
        for l_num in new_list:
            if is_prime(l_num):
                new_list = remove_multiples(l_num, new_list)
                maria_turn = not maria_turn
        if maria_turn:
            maria_victories += 1
        else:
            ben_victories += 1
        round += 1

    if maria_victories > ben_victories:
        return 'Maria'
    elif maria_victories < ben_victories:
        return 'Ben'
    else:
        return None
