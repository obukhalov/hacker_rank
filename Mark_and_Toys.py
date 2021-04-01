#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    n = len(prices)
    i = 0
    count = 0
    while k >= 0 and i < n:
        k -= prices[i]
        if k < 0:
            break
        i += 1
        count += 1

    return count 

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    print(str(result) + '\n')
