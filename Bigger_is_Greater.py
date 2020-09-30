#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    _alphabet = 'abcdefghijklmnopqrstuvwxyz'

#Convert symbols in w to indexes from alphabet
    _w_in_n = []
    for _s in w:
        _w_in_n.append(_alphabet.index(_s))
# Find biggest unchanged suffix
    _idx = len(w) - 1 
    _cost = 0
    while _idx >= 0:
        if _w_in_n[_idx] < _cost:
            break
        else:
            _cost = _w_in_n[_idx]
            _idx -= 1

    _turn_point_idx = _idx
    if _turn_point_idx == -1:
        return 'no answer'
# Find mim alement in suffix which is greater then turning point
    _idx = len(w) - 1 
    _cost = _w_in_n[_turn_point_idx]
    while _idx >= 0:
        if _w_in_n[_idx] > _cost:
            break
        else:
            _idx -= 1

# Swap turn point with it replacement
    _replacement = _idx
    _turn_cost = _w_in_n[_turn_point_idx]
    _repl_cost = _w_in_n[_replacement]
    _w_in_n.pop(_turn_point_idx)
    _w_in_n.insert(_turn_point_idx, _repl_cost)
    _w_in_n.pop(_replacement)
    _w_in_n.insert(_replacement, _turn_cost)
# Reverse suffix
    _first = _w_in_n[:_turn_point_idx + 1]
    _second = _w_in_n[_turn_point_idx + 1:]
    _second.reverse()
    _w_in_n = _first + _second
#Convert indexes to symbols
    _res_w = ''
    for _i in _w_in_n:
        _res_w += _alphabet[_i]



    return _res_w


if __name__ == '__main__':

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        print(result + '\n')
