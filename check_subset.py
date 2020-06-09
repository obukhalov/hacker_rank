#!/usr/bin/env python

if __name__ == '__main__':
    
    T = int(input())

    for i in range(T):
        _lenA = int(input())
        _setA = set(input().split())
        _lenB = int(input())
        _setB = set(input().split())

        _len_setB_before_update = len(_setB)
        _setB.update(_setA)
        _len_setB_after_update = len(_setB)
        if _len_setB_before_update == _len_setB_after_update:
            print('True')
        else:
            print('False')


        
