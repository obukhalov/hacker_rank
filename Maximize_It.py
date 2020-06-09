#!/usr/bin/env python

from itertools import product

if __name__ == '__main__':
    _K, _M = list(map(int,input().split()))

    _K_lists = [ list(map(int,input().split()))[1:] for i in range(_K) ] 

    _S_max = 0
    for _comb in product(*_K_lists):
        _S = 0
        for _i in _comb:
            _S += _i**2
        if _S % _M > _S_max:
            _S_max = _S %_M

    print(_S_max)


