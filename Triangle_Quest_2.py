#!/usr/bin/env python

if __name__ == '__main__':
    for i in range(1,int(input())+1):
        print( sum(map(lambda x: 10**x, range(i))) ** 2 )
