#!/usr/bin/env python

# Complete the solve function below.
def solve(s):
    _space = True
    s1 = ''
    for _c in s:
        if _space and _c.isalnum():
            s1 += _c.upper()
            _space = False
        elif _c.isspace():
            _space = True
            s1 += _c
        else:
            s1 += _c

    return s1

if __name__ == '__main__':

    s = input()

    result = solve(s)

    print(result + '\n')

