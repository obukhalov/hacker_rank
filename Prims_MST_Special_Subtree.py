#!/usr/bin/env python

import math
import os
import random
import re
import sys

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#

def prims(n, edges, start):
    # Write your code here
    #Create a graph dictionary
    _graph_dict = {}
    _max_weight = 0
    for _e in edges:
        if _e[2] > _max_weight:
            _max_weight = _e[2]
        if not _graph_dict.get(_e[0]):
            _graph_dict[_e[0]] = {_e[1] : _e[2]}
        else:
            _graph_dict[_e[0]][_e[1]] = _e[2]
        if not _graph_dict.get(_e[1]):
            _graph_dict[_e[1]] = {_e[0] : _e[2]}
        else:
            _graph_dict[_e[1]][_e[0]] = _e[2]
    print(_graph_dict)
    #Create a _edge key list
    _nodes_keys = [_max_weight] * n
    _nodes_keys[start - 1] = 0
    #Create an empty _mstSET list
    _mstSET = []
    #Create _Q list from all nodes
    _Q = [ i for i in range(1,n+1) ]

    _STP_weight = 0
    #Prim's algorithm
    while _Q:
        _min_idx = _nodes_keys.index(min(_nodes_keys))
        _V = _Q.pop(_min_idx)
        _mstSET.append(_V)
        _W = _nodes_keys.pop(_min_idx)
        _STP_weight += _W
        for _k in _graph_dict[_mstSET[-1]]:
            if _k not in _mstSET:
                _k_idx = _Q.index(_k)
                if _nodes_keys[_k_idx] > _graph_dict[_mstSET[-1]][_k]:
                    _nodes_keys[_k_idx] = _graph_dict[_mstSET[-1]][_k]
            

    return _STP_weight 

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    print(str(result) + '\n')

