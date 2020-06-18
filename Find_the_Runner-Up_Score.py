#!/usr/bin/env python

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    _new_list_arr = [ i for i in arr if i != max(list(arr)) ]
    print(max(_new_list_arr))
