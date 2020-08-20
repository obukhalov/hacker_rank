#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    return len([ _b for _b in range(i,j+1) if (_b - int(str(_b)[::-1])) % k == 0 ])
    

if __name__ == '__main__':

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    print(str(result) + '\n')
