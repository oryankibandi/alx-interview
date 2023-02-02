#!/usr/bin/python3
"""N-Queens solutions
This project prints all positions for Queens in a chessboard of Nxn
size in a non-attacking state i.e. Every Queen should not be
on another queen's path(horizontal, vertical diagonal)
"""


import sys


global N


if len(sys.argv) > 2 or len(sys.argv) == 1:
    print("Usage: nqueens N")
    sys.exit(1)

N = int(sys.argv[1])

if not isinstance(N, int):
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)


def queens(n, i, a, b, c):
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


for position in queens(N, 0, [], [], []):
    result = []
    for i in range(len(position)):
        result.append([i, position[i]])
    print(result)
