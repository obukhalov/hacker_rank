#!/usr/bin/env python

import math
import os
import random
import re
import sys
from itertools import groupby

# Complete the equalizeArray function below.
def equalizeArray(arr):
    _group_length_list = []

    for _ , _g in groupby(sorted(arr)):
        _group_length_list.append(len(list(_g)))

    _max_elements = max(_group_length_list)

    return len(arr) - _max_elements



if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(str(result) + '\n')
