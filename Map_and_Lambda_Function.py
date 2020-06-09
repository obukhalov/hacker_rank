#!/usr/bin/env python

cube = lambda x: x**3 # complete the lambda function

def fibonacci(n):
    # return a list of fibonacci numbers
    _fibonacci = [ 0, 1 ]
    for i in range(2, n):
        _fibonacci.append(_fibonacci[-1] + _fibonacci[-2])

    return _fibonacci[:n]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
