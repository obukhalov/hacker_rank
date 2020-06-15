#!/usr/bin/env python

import numpy

if __name__ == '__main__':
    _A = numpy.array( list(map(int, input().split())) )
    _B = numpy.array( list(map(int, input().split())) )

    print(numpy.inner(_A, _B))
    print(numpy.outer(_A, _B))
