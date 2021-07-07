#!/usr/bin/env python

import math
import os
import random
import re
import sys
from pprint import pprint

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    _len_s = len(s)
    _counter = 0
    for _len in range(1,_len_s):
        _comb = []
        for _i in range(_len_s):
            if len(s[_i:_i+_len]) == _len:
                _comb.append(''.join(sorted(s[_i:_i+_len])))
        for i in range(len(_comb)):
            for j in range(i+1,len(_comb)):
                if _comb[i] == _comb[j]:
                    _counter += 1

    return _counter 


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(str(result) + '\n')
