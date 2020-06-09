#!/usr/bin/env python

def print_rangoli(size):
    # your code goes here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for i in list(range(size))[::-1]:
        print(('-'.join(alphabet[i:size])[::-1] + '-'.join(alphabet[i:size])[1::]).center(size * 4 - 3, '-'))
    for i in range(1, size):
        print(('-'.join(alphabet[i:size])[::-1] + '-'.join(alphabet[i:size])[1::]).center(size * 4 - 3, '-'))

        


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
