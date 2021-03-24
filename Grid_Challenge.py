#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):
    _c = len(grid[0])
    _r = len(grid)
    _sorted_raws = []
    for _str in grid:
        _sorted_raws.append(sorted(_str))

    for i in range(_c):
        _col = []
        for j in range(_r):
            _col.append(_sorted_raws[j][i])
        if _col != sorted(_col):
            return 'NO'

    return 'YES'

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        print(result + '\n')
