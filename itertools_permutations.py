#!/usr/bin/env python

from itertools import permutations

if __name__ == '__main__':
    _S, _k = input().split()

    print( *[ ''.join(i) for i in permutations(sorted(_S), int(_k)) ], sep='\n')
