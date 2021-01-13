#!/usr/bin/env python

import math
import os
import random
import re
import sys
from pprint import pprint

# Complete the surfaceArea function below.
def surfaceArea(A):
    _H = len(A)
    _W = len(A[0])
    _sliced_A = []
    _surf_area = 0

    _L = 0
    for _sub_l in A:
        for i in _sub_l:
            if i > _L:
                _L = i


    for _ in range(_L):
        _level_L = []
        for i in range(_H):
            _level_H = []
            for j in range(_W):
                if A[i][j] > 0:
                    _level_H.append(1)
                    A[i][j] -= 1
                else:
                    _level_H.append(0)
            _level_L.append(_level_H)
        _sliced_A.append(_level_L)

    #Surface area calculation
    for _l in range(_L):
        for _h in range(_H):
            for _w in range(_W):
                if _sliced_A[_l][_h][_w] == 1:
                    if _w == 0:
                        _surf_area += 1
                    if _w == _W - 1:
                        _surf_area += 1
                    if _w == 0 and _W >= 2:
                        if _sliced_A[_l][_h][_w + 1] == 0:
                            _surf_area += 1
                    if _w == _W - 1 and _W >= 2:
                        if _sliced_A[_l][_h][_w - 1] == 0:
                            _surf_area += 1
                    if _w > 0 and _w < _W - 1:
                        if _sliced_A[_l][_h][_w + 1] == 0:
                            _surf_area += 1
                        if _sliced_A[_l][_h][_w - 1] == 0:
                            _surf_area += 1
                             
                        
                    if _h == 0:
                        _surf_area += 1
                    if _h == _H - 1:
                        _surf_area += 1
                    if _h == 0 and _H >= 2:
                        if _sliced_A[_l][_h + 1][_w] == 0:
                            _surf_area += 1
                    if _h == _H - 1 and _H >= 2:
                        if _sliced_A[_l][_h - 1][_w] == 0:
                            _surf_area += 1
                    if _h > 0 and _h < _H - 1:
                        if _sliced_A[_l][_h + 1][_w] == 0:
                            _surf_area += 1
                        if _sliced_A[_l][_h - 1][_w] == 0:
                            _surf_area += 1

                    if _l == 0:
                        _surf_area += 1
                    if _l == _L - 1:
                        _surf_area += 1
                    if _l < _L - 1:
                         if _sliced_A[_l + 1][_h][_w] == 0:
                            _surf_area += 1


    return _surf_area

if __name__ == '__main__':

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    print(str(result) + '\n')
