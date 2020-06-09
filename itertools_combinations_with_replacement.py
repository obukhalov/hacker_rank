#!/usr/bin/env python

from itertools import combinations_with_replacement

if __name__ == '__main__':
    _S, _k = input().split()
    for _comb in combinations_with_replacement(''.join(sorted(_S)), int(_k)):
        print(''.join(_comb))
