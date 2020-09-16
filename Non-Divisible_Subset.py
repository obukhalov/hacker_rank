#!/usr/bin/env python

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    _result_lst = []
    _unsupported_comb_remainders = [ (i,k-i) for i in range(1,k+1) if i <= k - i ]
    s_remainders = list(map(lambda x: x % k, s))
    for _r_pair in _unsupported_comb_remainders:
        if _r_pair[0] != _r_pair[1]:
            if s_remainders.count(_r_pair[0]) >= s_remainders.count(_r_pair[1]):
                _result_lst.extend([i for i in s_remainders if i == _r_pair[0]])
            elif s_remainders.count(_r_pair[0]) < s_remainders.count(_r_pair[1]):
                _result_lst.extend([i for i in s_remainders if i == _r_pair[1]])
        elif _r_pair[0] == _r_pair[1]:
            _result_lst.append(_r_pair[0])
    if 0 in s_remainders:
        _result_lst.append(0)

    return len(_result_lst)


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    print(str(result) + '\n')
