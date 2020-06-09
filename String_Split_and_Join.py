#!/usr/bin/env python

def split_and_join(line):
    # write your code here
    return '-'.join(line.split())

if __name__ == '__main__':
    print(split_and_join(input()))
