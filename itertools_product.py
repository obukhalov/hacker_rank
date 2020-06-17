#!/usr/bin/env python

from itertools import product

if __name__ == '__main__':
    _A = list(map(int, input().split()))
    _B = list(map(int, input().split()))

    print(*list(product(_A, _B)), sep=' ')
