#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#


def knightlOnAChessboard(n):
    # Write your code here

    # Find the shortest path down the tree from (0,0) to (n-1,n-1). Use BFS.
    result = []

    for a in range(1, n):
        sub_result = []

        for b in range(1, n):
            # I will try to solve the problem as a tree.
            # visited_cells is a dictionary where key - cell, value - True/False. (False means that cell is already visited)
            # cell_weight is a dictionary where key - cell, value - cost from root (0,0) to that cell.
            visited_cells = {}
            cell_weight = {}

            for i in range(n):

                for j in range(n):
                    visited_cells[(i, j)] = True
                    cell_weight[(i, j)] = 0

            # BFS
            root = (0, 0)
            queue = [root]
            visited_cells[root] = False

            while len(queue) > 0:
                x, y = queue.pop(0)
                parent = (x, y)

                nbrs = [
                    (x + a, y + b),
                    (x - a, y + b),
                    (x + a, y - b),
                    (x - a, y - b),
                    (x + b, y + a),
                    (x - b, y + a),
                    (x + b, y - a),
                    (x - b, y - a),
                ]

                for nx, ny in nbrs:

                    if (0 <= nx <= n - 1) and (0 <= ny <= n - 1):
                        child = (nx, ny)

                        if visited_cells[child] == True:
                            queue.append(child)
                            visited_cells[child] = False
                            cell_weight[child] = cell_weight[parent] + 1

                            if child == (n - 1, n - 1):
                                sub_result.append(cell_weight[child])
                                break

            if cell_weight[(n - 1, n - 1)] == 0:
                sub_result.append(-1)

        result.append(sub_result)

    return result


if __name__ == "__main__":

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    print("\n".join([" ".join(map(str, x)) for x in result]))
    print("\n")
