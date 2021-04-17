#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(n):
    _w = n // 3
    _l = n % 3
    _res = False
    for i in range(_w,-1,-1):
        _whole = i*3
        _left = ((_w-i)*3)+_l
        if _whole != 0 and _left == 0:
            _res = '5'*_whole
            break
        elif _whole != 0 and _left % 5 == 0:
            _res = '5'*_whole + '3'*_left
            break
        elif _whole == 0 and _left % 5 == 0:
            _res = '3'*_left
            break

    if _res:
        print(_res)
    else:
        print('-1')

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)

