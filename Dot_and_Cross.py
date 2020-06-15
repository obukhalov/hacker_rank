#!/usr/bin/env python

import numpy

if __name__ == '__main__':
    _N = int(input())
    _A = numpy.array([ list(map(int, input().split())) for _ in range(_N) ])
    _B = numpy.array([ list(map(int, input().split())) for _ in range(_N) ])
#    _matrix = []
#
#    for _row in range(_N):
#        _matrix.append([])
#        for _col in range(_N):
#            _element = 0
#            for i in range(_N):
#                _element += _A[_row][i] * _B[i][_col]
#            _matrix[_row].append(_element)

    print(numpy.dot(_A, _B))
