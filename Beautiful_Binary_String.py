#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    #Generate a list with '010' pattern indexes
    _patt = []
    for i in range(len(b)-2):
        if b[i:i+3] == '010':
            #print('Indexes: {} {} {}'.format(i,i+1,i+2))
            _patt.append([i,i+1,i+2])

    #Find the number of replacement
    _count = 0
    while len(_patt) > 0:
        if len(_patt) == 1:
            _count +=1
            _patt.pop(0)
        else:
            if _patt[0][-1] == _patt[1][0]:
                _count += 1
                _patt.pop(0)
                _patt.pop(0)
            else:
                _count += 1
                _patt.pop(0)


    return _count


if __name__ == '__main__':

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    print(str(result) + '\n')
