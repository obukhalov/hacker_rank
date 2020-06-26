#!/usr/bin/env python

import numpy

if __name__ == '__main__':
    print(numpy.reshape(numpy.array(list(map(int, input().split()))), (3, 3)))
