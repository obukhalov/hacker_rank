#!/usr/bin/env python

from itertools import combinations

if __name__ == '__main__':
    _N = int(input())
    _S = input()
    _K = int(input())

    _a_count = 0
    _all_count = 0
    for _comb in combinations(_S.replace(' ', ''), _K):
        _all_count += 1
        if 'a' in _comb:
            _a_count += 1

    print(_a_count / _all_count)


