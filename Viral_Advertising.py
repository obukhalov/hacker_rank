#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    _shared = 0
    _liked = 0
    _cumulative = 0
    for i in range(1,n + 1):
        if i == 1:
            _shared = 5
            _liked = _shared // 2
            _cumulative += _liked 
        else:
            _shared = _liked * 3
            _liked = _shared // 2
            _cumulative += _liked 

    return _cumulative


if __name__ == '__main__':

    n = int(input())

    result = viralAdvertising(n)

    print(str(result) + '\n')
