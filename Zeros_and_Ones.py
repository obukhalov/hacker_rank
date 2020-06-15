#!/usr/bin/env python

import numpy

if __name__ == '__main__':
    _dim = tuple(list(map(int, input().split())))
    #print(_dim)
    print(numpy.zeros((_dim), dtype = numpy.int))
    print(numpy.ones((_dim), dtype = numpy.int))
