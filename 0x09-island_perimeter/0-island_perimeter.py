#!/usr/bin/python3

"""Calculates perimeter of an island"""

global i
global j
global perimeter
i = 0
j = 0

perimeter = 0


def checkSurrounds(item: int, grid, x_xtent, y_xtent):
    """checks for any surrounding land"""
    sum = 0
    if i != 0:
        if grid[i-1][j] == 0:
            sum += 1
    if i < y_xtent:
        if grid[i+1][j] == 0:
            sum += 1
    if j != 0:
        if grid[i][j - 1]:
            sum += 1
    if j < y_xtent:
        if grid[i][j - 1]:
            sum += 1
    return sum


def island_perimeter(grid):
    """Calculates perimeter"""
    global i
    global j
    global perimeter
    y_xtent = len(grid)
    x_xtent = len(grid[0])
    for n in grid:
        for m in n:
            if m == 1:
                perimeter += checkSurrounds(m, grid, x_xtent, y_xtent)
            j += 1
        i += 1
    return perimeter
