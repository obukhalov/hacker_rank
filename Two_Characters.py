#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):
    #Normalize the string by removing consecutive characters
    _chg = True
    while _chg:
        _chg = False
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                s = s.replace(s[i],'')
                _chg = True
                break

    #Create an list with a combinations of pairs of symbols
    _unique = set(s)
    _unique = list(_unique)
    _len_u = len(_unique)
    _comb = [] 

    for i in range(len(_unique)):
        for j in range(i+1,len(_unique)):
            _comb.append((_unique[i],_unique[j]))


    #Create a list with substring
    _sub_lst = []
    for _c in _comb:
        _sub = ''
        for _s in s:
            if _s in _c:
                _sub += _s
        _sub_lst.append(_sub)

    #Remove invalid strings from _sub_lst
    _res_sub_lst = []
    for j in range(len(_sub_lst)):
        _sub = _sub_lst[j]
        for i in range(len(_sub)-1):
            _chg = False
            if _sub[i] == _sub[i+1]:
                _chg = True
                break
        if not _chg:
            _res_sub_lst.append(_sub_lst[j])


    #Create a list with result valid strings lenght
    _res_sub_lst_l =  [len(_sub) for _sub in _res_sub_lst]

    if len(_res_sub_lst_l ) == 0:
        return 0
    else:
        return max(_res_sub_lst_l)


if __name__ == '__main__':

    l = int(input().strip())

    s = input()

    result = alternate(s)

    print(str(result) + '\n')
