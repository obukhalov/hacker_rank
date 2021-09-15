#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    
    counter = 0
    tree = { n:[] for n in range(1,t_nodes+1)}

    for i in range(t_edges):
        tree[t_from[i]].append(t_to[i])
        tree[t_to[i]].append(t_from[i])

#    for n in tree[1]:
#        if (len(dfs(n,tree,[1])) - 1) % 2 == 0:
#            counter += 1
#BFS
    cut_eligible = []
    visited = []
    queue = []
    root = 1
    visited.append(root)
    queue.extend(tree[root])
    while queue:
        root = queue.pop(0)
        copy_visited = visited.copy()
        nodes_num = len(dfs(root,tree,copy_visited)) - len(visited)
        cut_eligible.append(nodes_num)
        visited.append(root)
        for n in tree[root]:
            if n not in queue and n not in visited:
                queue.append(n)

        
    return len([c for c in cut_eligible if c % 2 == 0])

#DFS
def dfs(start,tree,stack):
    stack.append(start)
    for next in tree[start]:
        if next not in stack:
            dfs(next,tree,stack)
    return stack


if __name__ == '__main__':

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    print(str(res) + '\n')
