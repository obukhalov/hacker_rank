#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the beautifulPairs function below.
def beautifulPairs(A, B):
    _len = len(A)
    _dict_A = {}
    _dict_B = {}
    for i in range(_len):
        if _dict_A.get(A[i]):
            _dict_A[A[i]].append(i)
        else:
            _dict_A[A[i]] = [i]
        if _dict_B.get(B[i]):
            _dict_B[B[i]].append(i)
        else:
            _dict_B[B[i]] = [i]

    #print(_dict_A,'\n',_dict_B)
    _beauty = []
    for _key in _dict_A:
        if _dict_B.get(_key):
            for _val_A in _dict_A[_key]:
                for _val_B in _dict_B[_key]:
                    _sign = True
                    for _set in _beauty:
                        if _set[0] == _val_A or _set[1] == _val_B:
                            _sign = False
                            break
                    if _sign:
                        _beauty.append((_val_A,_val_B))
    #print(len(_beauty))
    print(_beauty)
    if len(_beauty) == _len:
        return _len - 1
    else:
        return len(_beauty) + 1

    return 1

if __name__ == '__main__':

    n = int(input())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    print(str(result) + '\n')
