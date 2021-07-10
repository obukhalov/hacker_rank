#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def connectedCell(matrix):
    # Write your code here
    n = len(matrix)
    m = len(matrix[0])

    _regions = []

    for _n in range(n):
        for _m in range(m):
            if matrix[_n][_m] == 1:
                _sign = True

                for _r in _regions:
                    if [_n,_m] in _r:
                        _sign = False
                        try:
                            if matrix[_n][_m+1] == 1:
                                if [_n,_m+1] not in _r:
                                    _r.append([_n,_m+1])
                        except:
                            pass
                        try:
                            if matrix[_n][_m-1] == 1:
                                if [_n,_m-1] not in _r and _m-1 >= 0:
                                    _r.append([_n,_m-1])
                        except:
                            pass
                        try:
                            if matrix[_n+1][_m] == 1:
                                if [_n+1,_m] not in _r:
                                    _r.append([_n+1,_m])
                        except:
                            pass
                        try:
                            if matrix[_n-1][_m] == 1:
                                if [_n-1,_m] not in _r and _n-1 >= 0:
                                    _r.append([_n-1,_m])
                        except:
                            pass
                        try:
                            if matrix[_n-1][_m-1] == 1:
                                if [_n-1,_m-1] not in _r and _n-1 >= 0 and _m-1 >= 0:
                                    _r.append([_n-1,_m-1])
                        except:
                            pass
                        try:
                            if matrix[_n-1][_m+1] == 1:
                                if [_n-1,_m+1] not in _r and _n-1 >= 0:
                                    _r.append([_n-1,_m+1])
                        except:
                            pass
                        try:
                            if matrix[_n+1][_m-1] == 1:
                                if [_n+1,_m-1] not in _r and _m-1 >= 0:
                                    _r.append([_n+1,_m-1])
                        except:
                            pass
                        try:
                            if matrix[_n+1][_m+1] == 1:
                                if [_n+1,_m+1] not in _r:
                                    _r.append([_n+1,_m+1])
                        except:
                            pass
                if _sign:
                    _regions.append([[_n,_m]])
                    _r = _regions[-1]
                    try:
                        if matrix[_n][_m+1] == 1:
                            if [_n,_m+1] not in _r:
                                _r.append([_n,_m+1])
                    except:
                        pass
                    try:
                        if matrix[_n][_m-1] == 1:
                            if [_n,_m-1] not in _r and _m-1 >= 0:
                                _r.append([_n,_m-1])
                    except:
                        pass
                    try:
                        if matrix[_n+1][_m] == 1:
                            if [_n+1,_m] not in _r:
                                _r.append([_n+1,_m])
                    except:
                        pass
                    try:
                        if matrix[_n-1][_m] == 1:
                            if [_n-1,_m] not in _r and _n-1 >= 0:
                                _r.append([_n-1,_m])
                    except:
                        pass
                    try:
                        if matrix[_n-1][_m-1] == 1:
                            if [_n-1,_m-1] not in _r and _n-1 >= 0 and _m-1 >= 0:
                                _r.append([_n-1,_m-1])
                    except:
                        pass
                    try:
                        if matrix[_n-1][_m+1] == 1:
                            if [_n-1,_m+1] not in _r and _n-1 >= 0:
                                _r.append([_n-1,_m+1])
                    except:
                        pass
                    try:
                        if matrix[_n+1][_m-1] == 1:
                            if [_n+1,_m-1] not in _r and _m-1 >= 0:
                                _r.append([_n+1,_m-1])
                    except:
                        pass
                    try:
                        if matrix[_n+1][_m+1] == 1:
                            if [_n+1,_m+1] not in _r:
                                _r.append([_n+1,_m+1])
                    except:
                        pass


    return max(list(map(len,_regions))) 

if __name__ == '__main__':

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    print(str(result) + '\n')
