#!/usr/bin/env python

if __name__ == '__main__':

    _N, _X = list(map(int, input().split()))
    _subj = [ list(map(float, input().split())) for _ in range(_X) ]

    print( *[ sum(_tup)/_X for _tup in zip(*_subj) ], sep='\n' )
