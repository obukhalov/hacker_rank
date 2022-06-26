#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#


def gridChallenge(grid):
    # Write your code here
    size = len(grid)
    for i in range(size):
        row_sorted = sorted(grid[i])
        grid[i] = row_sorted
    for i in range(size):
        col = []
        for row in grid:
            col.append(row[i])
        if col != sorted(col):
            return "NO"
    return "YES"


if __name__ == "__main__":

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        print(result + "\n")
