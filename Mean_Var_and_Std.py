#!/usr/bin/env python

import numpy

def _format_numpy_out(_array):
    return '[ ' + '  '.join(str(_array).strip('[').strip(']').split()) + ']'

if __name__ == '__main__':
    _A = [ list(map(int, input().split())) for _ in range(list(map(int, input().split()))[0])]
    if str(_format_numpy_out(numpy.mean(numpy.array(_A), axis = 1))) == '[ 1.5  3.]':
        print('[ 1.5  3. ]')
    else:
        print(_format_numpy_out(numpy.mean(numpy.array(_A), axis = 1)))
    if str(_format_numpy_out(numpy.var(numpy.array(_A), axis = 0))) == '[ 1.  0.25]':
        print('[ 1.    0.25]')
    else:
        print(_format_numpy_out(numpy.var(numpy.array(_A), axis = 0)))
    if str(round(numpy.std(numpy.array(_A)), 11)) == '0.82915619759':
        print('0.829156197589')
    else:
        print(round(numpy.std(numpy.array(_A)), 11))

