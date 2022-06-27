#!/bin/python3

import math
import os
import random
import re
import sys
from pprint import pprint

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#


def exploison(row, col, grid):
    grid_explosion = [["O" for _ in range(col)] for _ in range(row)]
    for r in range(row):
        for c in range(col):
            if grid[r][c] == "O":
                if r > 0 and r < (row - 1) and c > 0 and c < (col - 1):
                    grid_explosion[r][c] = "."
                    grid_explosion[r + 1][c] = "."
                    grid_explosion[r - 1][c] = "."
                    grid_explosion[r][c + 1] = "."
                    grid_explosion[r][c - 1] = "."
                elif r == 0 and c > 0 and c < (col - 1):
                    grid_explosion[r][c] = "."
                    if row > 1:
                        grid_explosion[r + 1][c] = "."
                    grid_explosion[r][c + 1] = "."
                    grid_explosion[r][c - 1] = "."
                elif r > 0 and r < (row - 1) and c == 0:
                    grid_explosion[r][c] = "."
                    grid_explosion[r + 1][c] = "."
                    grid_explosion[r - 1][c] = "."
                    if col > 1:
                        grid_explosion[r][c + 1] = "."
                elif r == (row - 1) and c > 0 and c < (col - 1):
                    grid_explosion[r][c] = "."
                    grid_explosion[r - 1][c] = "."
                    grid_explosion[r][c + 1] = "."
                    grid_explosion[r][c - 1] = "."
                elif r > 0 and r < (row - 1) and c == (col - 1):
                    grid_explosion[r][c] = "."
                    grid_explosion[r + 1][c] = "."
                    grid_explosion[r - 1][c] = "."
                    grid_explosion[r][c - 1] = "."
                elif r == 0 and c == 0:
                    grid_explosion[r][c] = "."
                    if row > 1:
                        grid_explosion[r + 1][c] = "."
                    if col > 1:
                        grid_explosion[r][c + 1] = "."
                elif r == 0 and c == (col - 1):
                    grid_explosion[r][c] = "."
                    if row > 1:
                        grid_explosion[r + 1][c] = "."
                    grid_explosion[r][c - 1] = "."
                elif r == (row - 1) and c == 0:
                    grid_explosion[r][c] = "."
                    grid_explosion[r - 1][c] = "."
                    if col > 1:
                        grid_explosion[r][c + 1] = "."
                elif r == (row - 1) and c == (col - 1):
                    grid_explosion[r][c] = "."
                    grid_explosion[r - 1][c] = "."
                    grid_explosion[r][c - 1] = "."
    grid_explosion = ["".join(col) for col in grid_explosion]
    return grid_explosion


def bomberMan(n, grid):
    # Write your code here
    row = len(grid)
    col = len(grid[0])

    grid_full = ["".join(["O" for _ in range(col)]) for _ in range(row)]
    grid_3sec = exploison(row, col, grid)
    grid_5sec = exploison(row, col, grid_3sec)

    if n == 0 or n == 1:
        return grid
    elif n % 4 == 3:
        return grid_3sec
    elif n % 4 == 1:
        return grid_5sec
    else:
        return grid_full


if __name__ == "__main__":

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    print("\n".join(result))
    print("\n")
