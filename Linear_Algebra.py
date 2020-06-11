#!/usr/bin/env python

import numpy

if __name__ == '__main__':
    _A = [ list(map(float, input().split())) for _ in range(int(input()))]

    print('{:.2}'.format(numpy.linalg.det(_A)))

