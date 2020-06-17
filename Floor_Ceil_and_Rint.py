#!/usr/bin/env python

import numpy

if __name__ == '__main__':
    numpy.set_printoptions(legacy='1.13')
    _array = numpy.array(list(map(float, input().split())))

    print(numpy.floor(_array))
    print(numpy.ceil(_array))
    print(numpy.rint(_array))
