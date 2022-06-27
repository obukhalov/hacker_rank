#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#


def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here

    if c_road > c_lib:
        return n * c_lib

    city_to_region = {i: i for i in range(1, n + 1)}
    regions = {i: set([i]) for i in range(1, n + 1)}

    for edge in cities:
        r1 = city_to_region[edge[0]]
        r2 = city_to_region[edge[1]]
        if r1 != r2:
            if len(regions[r1]) >= len(regions[r2]):
                for c in regions[r2]:
                    regions[r1].add(c)
                    city_to_region[c] = r1
                del regions[r2]
            else:
                for c in regions[r1]:
                    regions[r2].add(c)
                    city_to_region[c] = r2
                del regions[r1]

    costs = 0

    for i in regions:
        nc = len(regions[i])
        min_roads = nc - 1
        cost1 = min_roads * c_road + c_lib
        cost2 = nc * c_lib
        if cost1 <= cost2:
            costs += cost1
        else:
            costs += cost2

    return costs


if __name__ == "__main__":

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        print(str(result) + "\n")
