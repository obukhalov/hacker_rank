#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the chessboardGame function below.
def chessboardGame(x, y):
    if ((x % 4 == 1) or (x % 4 == 2)) and ((y % 4 == 1) or (y % 4 == 2)):
        return 'Second'
    else:
        return 'First'

if __name__ == '__main__':

    t = int(input())

    _results = []
    for t_itr in range(t):
        xy = input().split()

        x = int(xy[0])

        y = int(xy[1])

        result = chessboardGame(x, y)
        _results.append(result)

        #print(result + '\n')
    print('*' * 20)
    for _p in _results:
        print(_p)
