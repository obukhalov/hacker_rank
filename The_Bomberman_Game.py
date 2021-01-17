#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the bomberMan function below.
def bomberMan(n, grid):
    _R = len(grid)
    _C = len(grid[0])
    _new_grid = [['O' for _ in range(_C)] for _ in range(_R)]

#Define the grid on 3rd second
    for i in range(_R):
        for j in range(_C):
            if grid[i][j] == 'O':
                if _R != 1:
                    if i == 0:
                        _new_grid[i+1][j] = '.'
                    elif i == _R - 1:
                        _new_grid[i-1][j] = '.'
                    else:
                        _new_grid[i+1][j] = '.'
                        _new_grid[i-1][j] = '.'
                if _C != 1:
                    if j == 0:
                        _new_grid[i][j+1] = '.'
                    elif j == _C - 1:
                        _new_grid[i][j-1] = '.'
                    else:
                        _new_grid[i][j+1] = '.'
                        _new_grid[i][j-1] = '.'
                _new_grid[i][j] = '.'
    grid3 = [''.join(_l) for _l in _new_grid]
    _new_grid = [['O' for _ in range(_C)] for _ in range(_R)]

#Define the grid on 5rd second
    for i in range(_R):
        for j in range(_C):
            if grid3[i][j] == 'O':
                if _R != 1:
                    if i == 0:
                        _new_grid[i+1][j] = '.'
                    elif i == _R - 1:
                        _new_grid[i-1][j] = '.'
                    else:
                        _new_grid[i+1][j] = '.'
                        _new_grid[i-1][j] = '.'
                if _C != 1:
                    if j == 0:
                        _new_grid[i][j+1] = '.'
                    elif j == _C - 1:
                        _new_grid[i][j-1] = '.'
                    else:
                        _new_grid[i][j+1] = '.'
                        _new_grid[i][j-1] = '.'
                _new_grid[i][j] = '.'
    grid5 = [''.join(_l) for _l in _new_grid]
    _new_grid = [['O' for _ in range(_C)] for _ in range(_R)]

    if n == 1:
        return grid
    elif n % 2 == 0:
        return [''.join(_l) for _l in _new_grid]
    elif (n - 3) % 4 == 0:
        return grid3
    elif (n - 5) % 4 == 0:
        return grid5


if __name__ == '__main__':

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    print('\n'.join(result))
    print('\n')
