import math
import os
import random
import re
import sys
from itertools import groupby

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    _pairs = 0
    for _key, _value in groupby(sorted(ar)):
        _pairs += len(list(_value)) // 2

    return _pairs

if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(str(result) + '\n')
