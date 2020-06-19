#!/usr/bin/env python

from collections import namedtuple

if __name__ == '__main__':
    _N = int(input())
    _columns = namedtuple('_columns', ' '.join(input().split()))
    _students = [ _columns(*input().split()) for _ in range(_N) ]

    print(sum(int(i.MARKS) for i in _students)/_N)


