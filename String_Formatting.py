#!/usr/bin/env python

def print_formatted(number):
    # your code goes here
    print('\n'.join(['{0:>{1}} {0:>{1}o} {0:>{1}X} {0:>{1}b}'.format(i, len(bin(number).split('0b')[1])) for i in range(1,number + 1)]))

if __name__ == '__main__':

    n = int(input())
    print_formatted(n)
