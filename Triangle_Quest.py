#!/usr/bin/env python

if __name__ == '__main__':
    for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
        print(i * sum(map(lambda x: 10**x, range(i))))
