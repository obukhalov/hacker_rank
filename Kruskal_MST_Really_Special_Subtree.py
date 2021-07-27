#!/usr/bin/env python

import math
import os
import random
import re
import sys

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def kruskals(g_nodes, g_from, g_to, g_weight):
    # Write your code here
    _node_sets = [[i] for i in range(1,g_nodes+1)]
    _stp_w = 0
    _comb_weight_lst = []
    for i in range(len(g_weight)):
        _comb_weight_lst.append([g_weight[i],[g_from[i],g_to[i]]])
    _comb_weight_lst.sort(key=lambda x: x[0])
    for _comb in _comb_weight_lst:
        for i in range(len(_node_sets)):
            if _comb[1][0] in _node_sets[i]:
                _va = i
            if _comb[1][1] in _node_sets[i]:
                _vb = i
        if _va != _vb:
            _va_set = _node_sets[_va] 
            _vb_set = _node_sets[_vb]
            _node_sets.remove(_va_set)
            _node_sets.remove(_vb_set)
            _union = _va_set + _vb_set
            _node_sets.append(_union)
            _stp_w += _comb[0]
            
    return _stp_w 

if __name__ == '__main__':

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    # Write your code here.
    print(res)

