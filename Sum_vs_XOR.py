#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    # Write your code here
    if n != 0:
        _zero_count = bin(n)[2:].count('0')

        return 2 ** _zero_count
    else:
        return 1


if __name__ == '__main__':

    n = int(input().strip())

    result = sumXor(n)

    print(str(result) + '\n')
