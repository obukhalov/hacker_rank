#!/usr/bin/env python

if __name__ == '__main__':
    _n = int(input())
    integer_list = map(int, input().split())

    print(hash(tuple(integer_list)))
