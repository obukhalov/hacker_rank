#!/usr/bin/env python

def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0';
        else:
            res += '1';

    return res

if __name__ == '__main__':
    s = input()
    t = input()
    print(strings_xor(s, t))


