#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    _alpha_counts = {}
    _alpha_idx = {}
    for _sym in b:
        if _sym.isalpha():
            _alpha_counts[_sym] = b.count(_sym)

    #print(_alpha_counts)

    if '_' in b and 1 not in _alpha_counts.values():
        return 'YES'
    elif len(_alpha_counts) == 1 and 1 not in _alpha_counts.values():
        return 'YES'
    elif len(_alpha_counts) == 0:
        return 'YES'
    elif '_' not in b and 1 and 1 not in _alpha_counts.values():
        for _sym in b:
            if not _alpha_idx.get(_sym):
                _alpha_idx[_sym] = [ _match.start() for _match in re.finditer('(?=' + _sym + ')', b) ]
        #print(_alpha_idx)
        for _lst in _alpha_idx.values():
            for i in range(len(_lst)):
                try:
                    if _lst[i+1] != _lst[i] + 1:
                        return 'NO'
                except IndexError:
                    pass

        return 'YES'
    else:
        return 'NO'
            

if __name__ == '__main__':

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        print(result + '\n')
