#!/usr/bin/env python

if __name__ == '__main__':
    _ = input()
    _setA = set(map(int, input().split()))
    _ = input()
    _setB = set(map(int, input().split()))


    print(*sorted(_setA.symmetric_difference(_setB)), sep='\n')
