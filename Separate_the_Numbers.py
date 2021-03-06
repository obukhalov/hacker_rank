#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    _l = len(s)
    if _l == 1 or s[0] == 0:
        print('NO')
        return True
    else:
        for i in range(1,_l//2+1):
            _n = int(s[:i])
            _predict = ''
            while True:
                if len(_predict + str(_n)) > _l:
                    break
                _predict += str(_n)
                _n += 1

            if _predict == s:
                print('YES ' + s[:i])
                return True

    print('NO')

            



if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
#    s = '99910001001'
#    separateNumbers(s)
