#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#


def componentsInGraph(gb):
    # Write your code here

    # Find maximun number of nodes
    n = 0
    for e in gb:
        if e[0] > n:
            n = e[0]
        if e[1] > n:
            n = e[1]

    # Create a dictionary where a key is a number of node and a value is number of region to which that node belongs
    n_to_reg = {i: i for i in range(1, n + 1)}

    # Create a dictionary where a key is region number and value is a list of nodes of this dictionary
    regions = {i: [i] for i in range(1, n + 1)}

    # Build a regions of connected nodes
    for e in gb:
        n1, n2 = e[0], e[1]
        r1, r2 = n_to_reg[n1], n_to_reg[n2]
        if r1 == r2:
            continue
        if len(regions[r1]) >= len(regions[r2]):
            for node in regions[r2]:
                regions[r1].append(node)
                n_to_reg[node] = r1
            n_to_reg[n2] = r1
            del regions[r2]
        else:
            for node in regions[r1]:
                regions[r2].append(node)
                n_to_reg[node] = r2
            n_to_reg[n1] = r2
            del regions[r1]

    # Find min and max region size
    rsizes = {len(regions[r]) for r in regions if len(regions[r]) > 1}
    mn = min(rsizes)
    mx = max(rsizes)

    return [mn, mx]


if __name__ == "__main__":

    n = int(input().strip())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    print(" ".join(map(str, result)))
    print("\n")
