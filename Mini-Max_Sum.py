#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    _sum_lst = []
    for i in range(len(arr)):
        _tmp_lst = arr.copy()
        _tmp_lst.pop(i)
        _sum_lst.append(sum(_tmp_lst))

    print('{} {}'.format(min(_sum_lst), max(_sum_lst)))



if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

