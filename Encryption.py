#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    _space_free_s = s.replace(' ','')
    if math.sqrt(len(_space_free_s)) == int(math.sqrt(len(_space_free_s))):
        _row = int(math.sqrt(len(_space_free_s)))
        _col = _row
    else:
        _row = int(math.sqrt(len(_space_free_s)))
        _col = _row + 1
    if _row * _col < len(_space_free_s):
        _row = _row + 1

    _grid_s = []
    _start = 0
    _end = _col
    for _ in range(_row):
        _grid_s.append(_space_free_s[_start:_end])
        _start += _col
        _end += _col

#    for _sub in _grid_s:
#        print(_sub)
    _encr = ''
    for i in range(_col):
        for _sub in _grid_s:
            try:
                _encr += _sub[i]
            except IndexError:
                pass
        _encr += ' '

    _encr = _encr.rstrip()
    return _encr


if __name__ == '__main__':

    s = input()

    result = encryption(s)

    print(result + '\n')
