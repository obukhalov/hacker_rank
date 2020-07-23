#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    _result = 0

    for k, g in groupby(sorted(ar)):
        _result = len(list(g))

    return _result

if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    print((str(result) + '\n'))
