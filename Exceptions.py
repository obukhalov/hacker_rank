#!/usr/bin/env python

if __name__ == '__main__':
    for _ in range(int(input())):
        try:
            _a, _b = list(map(int, input().split()))
            print(int(_a // _b))
        except (ZeroDivisionError, ValueError) as _error_code:
            print('Error Code: {}'.format(_error_code))
