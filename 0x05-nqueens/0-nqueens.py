#!/usr/bin/python3
"""N-Queens solutions"""


import sys


def printSolution(board):
    for i in range(n):
        for j in range(n):
            # print(board[i][j], end=" ")
            print(f'[{i}][{j}]', end=" ")
        print()


def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solveNQUtil(board, col):
    if col >= n:
        printSolution(board)
        return
    for i in range(n):
        if isSafe(board, i, col):
            board[i][col] = 1
            solveNQUtil(board, col + 1)
            board[i][col] = 0


if __name__ == '__main__':
    n = int(sys.argv[1])

    if len(sys.argv) > 2:
        print('Usage: nqueens N')
        sys.exit(1)
    elif not isinstance(n, int):
        print('N must be a number')
        sys.exit(1)
    elif n < 4:
        print('N must be at least 4')
        sys.exit(1)
    else:
        board = [[0 for x in range(n)] for y in range(n)]
        solveNQUtil(board, 0)
