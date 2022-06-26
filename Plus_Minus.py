#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    arr_len = len(arr)
    posivive_len = len([ i for i in arr if i > 0 ])
    negative_len = len([ i for i in arr if i < 0 ])
    zero_len = len([ i for i in arr if i == 0 ])
    print('{:.6f}'.format(posivive_len / arr_len))
    print('{:.6f}'.format(negative_len / arr_len))
    print('{:.6f}'.format(zero_len / arr_len))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

