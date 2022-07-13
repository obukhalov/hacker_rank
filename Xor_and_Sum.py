#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'xorAndSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def xorAndSum(a, b):
    # Write your code here
    a = int(a, 2)
    b = int(b, 2)

    s = 0
    for i in range(314160):
        s += a ^ (b << i)

    ms = s % (10**9 + 7)

    return ms


if __name__ == '__main__':

    a = input()

    b = input()

    result = xorAndSum(a, b)

    print(str(result) + '\n')
