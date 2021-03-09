#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    _l = len(s)
    # Convert string to decimal values
    _ord_s = list(map(ord,s))
    # Reverse string and convert it to decimal values
    _ord_rev_s = list(map(ord,s[::-1]))

    # Generate a list with absolute difference of neighboring elements of a string
    _s_delta = []
    for i in range(_l-1):
        _s_delta.append(abs(_ord_s[i] - _ord_s[i+1]))

    #print(_s_delta)
    
    # Generate a list with absolute difference of neighboring elements of a reverse string
    _s_rev_delta = []
    for i in range(_l-1):
        _s_rev_delta.append(abs(_ord_rev_s[i] - _ord_rev_s[i+1]))

    #print(_s_rev_delta)

    if _s_delta == _s_rev_delta:
        return 'Funny'
    else:
        return 'Not Funny'






if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        print(result + '\n')
