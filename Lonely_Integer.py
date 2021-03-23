#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the lonelyinteger function below.
def lonelyinteger(a):
    for i in range(len(a)):
        if a.count(a[i]) == 1:
            return a[i]

if __name__ == '__main__':

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    print(str(result) + '\n')
