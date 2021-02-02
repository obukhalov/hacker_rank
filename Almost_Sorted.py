#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr):
    _idx = set()
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            _idx.add(i)
            _idx.add(i+1)

    if len(_idx) == 0:
        return 'yes'
    elif len(_idx) == 2:
        _unsorted = []

        for i in _idx:
            _unsorted.append(arr[i])
        _unsorted.reverse()
        j = 0
        for i in _idx:
            arr[i] = _unsorted[j]
            j += 1
        _idx_swap = set()
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                _idx_swap.add(i)
                _idx_swap.add(i+1)
        if len(_idx_swap) == 0:
            print('yes')
            print('swap {} {}'.format(list(_idx)[0] + 1,list(_idx)[-1] + 1))
        else:
            print('no')
    else:
        _idx_lst = list(_idx)
        _idx_lst.sort()
# Try to find if it possible to sort an array with a single reverse 
        if _idx_lst[-1] == _idx_lst[0] + len(_idx_lst) - 1:
            _unsorted = []
            for i in _idx:
                _unsorted.append(arr[i])
            _unsorted.reverse()
            j = 0
            for i in _idx:
                arr[i] = _unsorted[j]
                j += 1

            _idx_reverse = set()
            for i in range(len(arr) - 1):
                if arr[i] > arr[i+1]:
                    _idx_reverse.add(i)
                    _idx_reverse.add(i+1)
            if len(_idx_reverse) == 0:
                print('yes')
                print('reverse {} {}'.format(_idx_lst[0] + 1,_idx_lst[-1] + 1))
            else:
                _unsorted = []
                _sorted = []

                for i in _idx_lst:
                    _unsorted.append([i,arr[i]])

                _sorted = _unsorted.copy()
                _sorted.sort(key=lambda i: i[1])

                _sorted_diff = []
                for i in range(len(_unsorted)):
                    if _unsorted[i] != _sorted[i]:
                        _sorted_diff.append(_unsorted[i])

                if len(_sorted_diff) == 2:
                    arr[_sorted_diff[0][0]] = _sorted_diff[1][1]
                    arr[_sorted_diff[1][0]] = _sorted_diff[0][1]
                    _idx_reverse = set()
                    for i in range(len(arr) - 1):
                        if arr[i] > arr[i+1]:
                            _idx_reverse.add(i)
                            _idx_reverse.add(i+1)
                    if len(_idx_reverse) == 0:
                        print('yes')
                        print('swap {} {}'.format(_sorted_diff[0][0] + 1,_sorted_diff[1][0] + 1))
                    else:
                        print('no')
                else:
                    print('no')
        else:
# Try to find if it possible to sort an array with a single swap
            _unsorted = []
            _sorted = []

            for i in _idx_lst:
                _unsorted.append([i,arr[i]])

            _sorted = _unsorted.copy()
            _sorted.sort(key=lambda i: i[1])

            _sorted_diff = []
            for i in range(len(_unsorted)):
                if _unsorted[i] != _sorted[i]:
                    _sorted_diff.append(_unsorted[i])

            if len(_sorted_diff) == 2:
                arr[_sorted_diff[0][0]] = _sorted_diff[1][1]
                arr[_sorted_diff[1][0]] = _sorted_diff[0][1]
                _idx_reverse = set()
                for i in range(len(arr) - 1):
                    if arr[i] > arr[i+1]:
                        _idx_reverse.add(i)
                        _idx_reverse.add(i+1)
                if len(_idx_reverse) == 0:
                    print('yes')
                    print('swap {} {}'.format(_sorted_diff[0][0] + 1,_sorted_diff[1][0] + 1))
                else:
                    print('no')
            else:
                print('no')


if __name__ == '__main__':
    n = int(input())


    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)

