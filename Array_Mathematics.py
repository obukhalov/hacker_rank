#!/usr/bin/env python

import numpy

if __name__ == '__main__':
    numpy.set_printoptions(legacy='1.13')
    _N, _M = list(map(int, input().split()))
    _A = numpy.array([ list(map(int, input().split())) for _ in range(_N) ], int)
    _B = numpy.array([ list(map(int, input().split())) for _ in range(_N) ], int)

    print(numpy.add(_A, _B))
    print(numpy.subtract(_A, _B))
    print(numpy.multiply(_A, _B))
    print(numpy.floor_divide(_A, _B))
    print(numpy.mod(_A, _B))
    print(numpy.power(_A, _B))


