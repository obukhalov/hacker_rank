#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    sticks.sort(reverse=True)
    _tr = []
    for i in range(len(sticks)-2):
        if sticks[i] < sticks[i+1] + sticks[i+2]:
            _tr.append([sticks[i],sticks[i+1],sticks[i+2]])
    if len(_tr) == 0:
        return [-1]
    _tr_sum = list(map(sum,_tr))
    _max = max(_tr_sum)
    _tr_max = []
    for i in range(len(_tr_sum)):
        if _tr_sum[i] == _max:
            _tr_max.append(_tr[i])
    _tr_min_side = list(map(min,_tr_max))

    return sorted(_tr_max[_tr_min_side.index(max(_tr_min_side))])
    #print(_tr_min_side)

    

if __name__ == '__main__':

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    print(' '.join(map(str, result)))
    print('\n')
