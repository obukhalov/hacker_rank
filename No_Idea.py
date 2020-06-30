#!/usr/bin/env python

if __name__ == '__main__':
    _n, _m = list(map(int, input().split()))
    _array = list(map(int, input().split()))
    _setA = set(map(int, input().split()))
    _setB = set(map(int, input().split()))

    print( sum([(i in _setA) - (i in _setB) for i in _array]) )
