#!/usr/bin/env python

import numpy

if __name__ == '__main__':
    _N, _M, _P = map(int, input().split())
    _A = numpy.array([ list(map(int, input().split())) for _ in range(_N) ])
    _B = numpy.array([ list(map(int, input().split())) for _ in range(_M) ])

    print(numpy.concatenate((_A, _B), axis = 0))

