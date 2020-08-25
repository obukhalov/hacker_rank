#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    if (m % n + s - 1) % n == 0:
        return n
    else:
        return (m % n + s - 1) % n


if __name__ == '__main__':

    t = int(input())

    _results = []
    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)
        _results.append(result)

        #print(str(result) + '\n')

    for _num in _results:
        print(str(_num))
