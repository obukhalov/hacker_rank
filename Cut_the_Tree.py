#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#
def dfs(graph, data, node, parent, total_cost, min_diff):
    node_subtree_cost = data[node - 1]

    for nbr in graph[node]:
        if nbr != parent:
            nbr_cost, diff = dfs(graph, data, nbr, node, total_cost, min_diff)
            node_subtree_cost += nbr_cost
            if diff < min_diff:
                min_diff = diff

    t2_cost = total_cost - node_subtree_cost
    diff = abs(node_subtree_cost - t2_cost)
    if diff < min_diff:
        min_diff = diff

    return node_subtree_cost, min_diff


def cutTheTree(data, edges):
    # Write your code here

    # Set new recursion limit
    sys.setrecursionlimit(10 ** 5)

    # Number of nodes
    n = len(data)

    # Build a graph
    graph = {i: [] for i in range(1, n + 1)}

    for e in edges:
        n1, n2 = e[0], e[1]
        graph[n1].append(n2)
        graph[n2].append(n1)

    # Build a list of all subtree costs, using DFS
    root = edges[0][0]
    parent = 0
    total_cost = sum(data)
    min_diff = total_cost
    _, min_diff = dfs(graph, data, root, parent, total_cost, min_diff)

    return min_diff


if __name__ == "__main__":

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    print(str(result) + "\n")
