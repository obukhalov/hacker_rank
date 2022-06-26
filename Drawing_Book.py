#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#


def pageCount(n, p):
    # Write your code here
    total_flips = n // 2
    left_to_right_flips = p // 2
    right_to_left_flips = total_flips - left_to_right_flips
    if left_to_right_flips <= right_to_left_flips:
        return left_to_right_flips
    else:
        return right_to_left_flips


if __name__ == "__main__":

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(str(result) + "\n")
