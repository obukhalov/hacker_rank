#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    _s = [ int(i) for i in str(n) if i != '0' ]
    _divisor = [ i for i in _s if n % i == 0 ]
    return len(_divisor)


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        print(str(result) + '\n')
