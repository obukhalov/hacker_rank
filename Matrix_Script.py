#!/usr/bin/env python

import math
import os
import random
import re
import sys


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    matrix = []

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

    _decoded_str = ''.join([ matrix[y][i] for i in range(m) for y in range(n)])
    print(re.sub(r'(\w)(\W+)(\w)', r'\1 \3', _decoded_str))
