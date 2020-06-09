#!/usr/bin/env python

from itertools import combinations

if __name__ == '__main__':

    _S, _k = input().split()
    print(*[ ''.join(_comb) + '\n' for i in range(1,int(_k) + 1) for _comb in combinations(sorted(_S), i) ], sep='')
