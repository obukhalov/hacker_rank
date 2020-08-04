#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    _ = bill.pop(k)
    _diff = int(b - (sum(bill) / 2))
    if _diff == 0:
        print('Bon Appetit')
    else:
        print(_diff)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

