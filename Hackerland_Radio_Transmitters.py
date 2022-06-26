#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#


def hackerlandRadioTransmitters(x, k):
    # Write your code here
    x.sort()
    len_x = len(x)
    counter = 0
    while len_x > 0:
        begin = x[0]
        end = begin + k
        counter += 1
        while len_x > 0 and x[0] <= end:
            begin = x.pop(0)
            len_x -= 1
        end = begin + k
        while len_x > 0 and x[0] <= end:
            begin = x.pop(0)
            len_x -= 1

    return counter


if __name__ == "__main__":

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    print(str(result) + "\n")
