#!/usr/bin/env python

import numpy

#def _array_format(_array):
#
#    counter1 = 1
#    for _row in  numpy.eye(_N, _M):
#        counter2 = 1
#        if counter1 == 1:
#            for _i in _row:
#                if counter2 == 1:
#                    print('[[', str(_i)[:-1], end= '')
#                    counter2 += 1
#                elif counter2 == _M:
#                    print('  ', str(_i)[:-1], ']', sep='', end= '\n')
#                    counter2 += 1
#                else:
#                    print('  ',str(_i)[:-1], sep='', end= '')
#                    counter2 += 1
#            counter1 += 1
#        elif counter1 == _N:
#            for _i in _row:
#                if counter2 == 1:
#                    print(' [', str(_i)[:-1], end= '')
#                    counter2 += 1
#                elif counter2 == _M:
#                    print('  ', str(_i)[:-1], ']]', sep='', end= '\n')
#                    counter2 += 1
#                else:
#                    print('  ',str(_i)[:-1], sep='', end= '')
#                    counter2 += 1
#            counter1 += 1
#        else:
#            for _i in _row:
#                if counter2 == 1:
#                    print(' [', str(_i)[:-1], end= '')
#                    counter2 += 1
#                elif counter2 == _M:
#                    print('  ', str(_i)[:-1], ']', sep='', end= '\n')
#                    counter2 += 1
#                else:
#                    print('  ',str(_i)[:-1], sep='', end= '')
#                    counter2 += 1
#            counter1 += 1
#
#
#
#
if __name__ == '__main__':
    _N, _M = list(map(int, input().split()))
#    _array_format(numpy.eye(_N, _M))
    numpy.set_printoptions(legacy='1.13')
    print(numpy.eye(_N, _M))
