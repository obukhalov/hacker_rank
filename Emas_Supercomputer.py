#!/usr/bin/env python

import math
import os
import random
import re
import sys
from pprint import pprint

# Complete the twoPluses function below.
def twoPluses(grid):
    _N = len(grid)
    _M = len(grid[0])
    _prod_values = [0]
    if _N > _M:
        if _M % 2 == 1:
            _max = _M
        else:
            _max = _M - 1
    elif _M > _N:
        if _N % 2 == 1:
            _max = _N
        else:
            _max = _N - 1
    else:
        if _N % 2 == 1:
            _max = _N
        else:
            _max = _N - 1

    _crosses = {}
    for _d in range(1,_max+1,2):
        _crosses[_d] = []
        _S = _d // 2
        for n in range(_S,_N-_S):
            for m in range(_S,_M-_S):
                _good_flag = True
                if grid[n][m] != 'G':
                    continue
                for i in range(_S+1):
                    if grid[n+i][m] != 'G' or grid[n-i][m] != 'G':
                        _good_flag = False
                        break
                    if grid[n][m+i] != 'G' or grid[n][m-i] != 'G':
                        _good_flag = False
                        break
                if _good_flag:
                    _crosses[_d].append([n,m])


    for _d in range(_max,0,-2):
        _S = _d // 2
        if _d == 1 and len(_crosses[_d]) > 0:
            _prod_values.append(1)
            return max(_prod_values) 
        _len = len(_crosses[_d])
        for _plus1 in _crosses[_d]:
            for _dd in range(_d,0,-2):
                if (2*_d-1) * (2*(_dd)-1) not in _prod_values:
                    _SS = _dd // 2
                    for _plus2 in _crosses[_dd]:
                        if (2*_d-1) * (2*(_dd)-1) not in _prod_values:
                            _H = abs(_plus1[0] - _plus2[0])
                            _L = abs(_plus1[1] - _plus2[1])
                            _nointercect = True
                            if _plus1[0] == _plus2[0] and _plus1[1] == _plus2[1]:
                                _nointercect = False
                            if _plus1[0] == _plus2[0] and _L > _S+_SS:
                                pass
                            elif _plus1[0] == _plus2[0] and _L <= _S+_SS:
                                _nointercect = False
                            if _plus1[1] == _plus2[1] and _H > _S+_SS:
                                pass
                            elif _plus1[1] == _plus2[1] and _H <= _S+_SS:
                                _nointercect = False
                            if (_S >= _H and _SS >= _L) or (_SS >= _H and _S >= _L):
                                _nointercect = False
                            else:
                                pass


                            if _nointercect:
                                _prod_values.append((2*_d-1) * (2*(_dd)-1))
        

    return max(_prod_values) 


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    print(str(result) + '\n')
