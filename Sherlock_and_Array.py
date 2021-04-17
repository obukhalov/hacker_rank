#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    _sum1 = 0
    _sum2 = sum(arr) - arr[0]
    if _sum2 == 0:
        return 'YES'
    #_sum2 -= arr[0]
    #print('Sum1={}  Sum2={}'.format(_sum1,_sum2))
    for i in range(1,len(arr)):
        _sum1 += arr[i-1]
        _sum2 -= arr[i]
        #print('Index={}'.format(i))
        #print('Sum1={}  Sum2={}'.format(_sum1,_sum2))
        if _sum1 == _sum2:
            return 'YES'

    return 'NO'



if __name__ == '__main__':

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        print(result + '\n')
