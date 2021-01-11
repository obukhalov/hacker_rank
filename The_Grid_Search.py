#!/usr/bin/env python

import math
import os
import random
import re
import sys
import pprint


# Complete the gridSearch function below.
def gridSearch(G, P):
    R = len(G)
    r = len(P)
    for i in range(R - r + 1):
        _sub_G = []
        for j in range(r):
            if P[j] in G[i+j]:
                _sub_G.append(G[i+j])

        if len(_sub_G) == r:
            _idx_lst = []
            for j in range(r):
                _idx_lst.append([ _m.start() for _m in re.finditer('(?=' + P[j] + ')', _sub_G[j]) ])

            for _idx in _idx_lst[0]:
                _res = 'YES'
                for _i in range(1, r):
                    if _idx not in _idx_lst[_i]:
                        _res = 'NO'
                        break
                if _res == 'YES':
                    return _res

    return 'NO' 

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        print(result + '\n')
