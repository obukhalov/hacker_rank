#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#
def next_step(r, c, m_grid, step, queue, n):
    # Go up,down,left,right from the given cell and replace it with value spep+1 if it's not X 
    # DOWN by X
    for i in range(r + 1, n):
        if m_grid[i][c] != '.':
            break
        else:
            m_grid[i][c] = step + 1
            queue.remove([i, c])
    # UP by X
    for i in range(r - 1, -1, -1): 
        if m_grid[i][c] != '.':
            break
        else:
            m_grid[i][c] = step + 1
            queue.remove([i, c])
    # RIGHT by Y
    for i in range(c + 1, n):
        if m_grid[r][i] != '.':
            break
        else:
            m_grid[r][i] = step + 1
            queue.remove([r, i])
    # LEFT by Y
    for i in range(c - 1, -1, -1):
        if m_grid[r][i] != '.':
            break
        else:
            m_grid[r][i] = step + 1
            queue.remove([r, i])

    return m_grid, queue


def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here
    n = len(grid)
    #Rows is X
    #Columns is Y

    # Modify grid
    m_grid = []
    for r in range(n):
        r_lst = []
        for c in range(n):
            r_lst.append(grid[r][c])
        m_grid.append(r_lst)

    #Set start point as 0
    m_grid[startX][startY] = 0

    # Generate a queue of cells that need to be modified
    queue = []
    for r in range(n):
        for c in range(n):
            if m_grid[r][c] == '.':
                queue.append([r,c])
    #Init step
    step = 0

    len_queue_before_change = len(queue)

    while len_queue_before_change != 0:

        for r in range(n):
            for c in range(n):
                if m_grid[r][c] == step:
                    m_grid, queue = next_step(r, c, m_grid, step, queue, n)

        len_queue_after_change = len(queue)
        if len_queue_before_change == len_queue_after_change:
            break
        else:
            len_queue_before_change = len_queue_after_change
            step += 1

    if m_grid[goalX][goalY] == '.' or m_grid[goalX][goalY] == 'X':
        return 0
    else:
        return m_grid[goalX][goalY]


if __name__ == '__main__':

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    print(str(result) + '\n')
