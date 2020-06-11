#!/usr/bin/env python

import numpy

if __name__ == '__main__':
    P = list(map(float, input().split()))
    x = float(input())

    print(numpy.polyval(P, x))
