#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#


def bfs(n, m, edges, s):
    # Write your code here

    # Create a graph representation in the form of dictionary,
    # where key in node and value is a list of its neighbours
    graph_dict = {node: [] for node in range(1, n + 1)}

    for e in edges:
        graph_dict[e[0]].append(e[1])
        graph_dict[e[1]].append(e[0])

    # The dictionary with distances from start node to every other nodes
    distances = {node: -1 for node in range(1, n + 1)}

    # BFS
    visited = [False] * (n + 1)
    queue = [s]
    # Distance of start node is 0
    distances[s] = 0

    while len(queue) > 0:
        node = queue.pop(0)
        visited[node] = True

        for nbr in graph_dict[node]:
            if not visited[nbr] and nbr not in queue:
                queue.append(nbr)
                distances[nbr] = distances[node] + 6

    # Delete distance for start node
    del distances[s]

    return list(distances.values())


if __name__ == "__main__":

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        print(" ".join(map(str, result)))
        print("\n")
