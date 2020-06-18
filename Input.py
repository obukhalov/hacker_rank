#!/usr/bin/env python

if __name__ == '__main__':
    x, k = list(map(int, input().split()))
    P = input()
    print(eval(P) == k)
