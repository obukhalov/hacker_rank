#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    a.sort()
    i = 0
    unique = 0
    len_a = len(a)
    while i < len_a:
        if i == len_a - 1:
            unique = a[i]
            i += 1
        else:
            if a[i] == a[i+1]:
                i += 2
            else:
                unique = a[i]
                break
    return unique

if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    print(str(result) + '\n')
