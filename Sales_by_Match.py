#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, ar):
    # Write your code here
    socks_dict = {}
    for s in ar:
        if socks_dict.get(s):
            socks_dict[s] += 1
        else:
            socks_dict[s] = 1
    pairs = 0
    for s in socks_dict.values():
        pairs += s // 2

    return pairs


if __name__ == "__main__":
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(str(result) + "\n")
