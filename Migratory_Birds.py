#!/usr/bin/env python

import math
import os
import random
import re
import sys
from itertools import groupby

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    _bird = 0
    _max_len = 0
    for k, v in groupby(sorted(arr)):
        _v_length = len(list(v))
        if _v_length > _max_len:
            _bird = k
            _max_len = _v_length
        elif  _v_length == _max_len and k < _bird:
            _bird = k

    return _bird


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(str(result) + '\n')


