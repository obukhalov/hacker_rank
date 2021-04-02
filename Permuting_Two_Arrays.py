#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the twoArrays function below.
def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    n = len(A)
    for i in range(n):
        if A[i] + B[i] < k:
            return 'NO'

    return 'YES'

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        print(result + '\n')
