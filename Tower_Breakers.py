#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the towerBreakers function below.
def towerBreakers(n, m):
    if m == 1:
        return 2
    if n % 2 == 1:
        return 1
    else:
        return 2

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = towerBreakers(n, m)

        print(str(result) + '\n')
