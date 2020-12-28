#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    n = len(grid)
    _spikes = []
    for i in range(n):
        if i != 0 and i != n - 1:
            for j in range(n):
                if j != 0 and j != n - 1:
                    if int(grid[i][j]) > int(grid[i-1][j]) and int(grid[i][j]) > int(grid[i+1][j]) and int(grid[i][j]) > int(grid[i][j-1]) and int(grid[i][j]) > int(grid[i][j+1]):
                        _spikes.append([i,j])

    for i,j in _spikes:
        grid[i] = grid[i][:j] + 'X' + grid[i][j+1:]

    return grid


if __name__ == '__main__':

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    print('\n'.join(result))
    print('\n')
