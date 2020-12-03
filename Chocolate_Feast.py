#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    _chocolates = n // c 
    _wrapper = _chocolates

    while _wrapper >= m:
        _tmp_choc = _wrapper // m
        _tmp_wrap = _wrapper % m
        _chocolates += _tmp_choc
        _wrapper = _tmp_choc + _tmp_wrap

    return _chocolates


        

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        print(str(result) + '\n')
