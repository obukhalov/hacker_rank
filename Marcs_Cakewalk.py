#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    _len = 0
    for i in range(len(calorie)):
        _len += (2**i)*calorie[i]

    return _len


if __name__ == '__main__':

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    print(str(result) + '\n')
