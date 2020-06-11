#!/usr/bin/env python

import numpy

if __name__ == '__main__':
    _A = [ list(map(int, input().split())) for _ in range(list(map(int, input().split()))[0])]
    print(numpy.prod(numpy.sum(numpy.array(_A), axis = 0)))


