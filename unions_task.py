#!/usr/bin/env python

if __name__ == '__main__':
    _input = []

    # Input part
    line1 = int(input())
    _input.append(line1)
    line2 = input().split()
    _input.append(line2)
    line3 = int(input())
    _input.append(line3)

    for i in range(line3):
        _tmp_lst = []
        _action = input().split()
        _tmp_lst.append(_action)
        line = input().split()
        _tmp_lst.append(line)
        _input.append(_tmp_lst)

    # Output part
    _setA = set(line2)
    for i in range(3,len(_input)):
        if 'intersection_update' in _input[i][0]:
            _setA.intersection_update(set(_input[i][1]))
        elif 'update' in _input[i][0]:
            _setA.update(set(_input[i][1]))
        elif 'symmetric_difference_update' in _input[i][0]:
            _setA.symmetric_difference_update(set(_input[i][1]))
        elif 'difference_update' in _input[i][0]:
            _setA.difference_update(set(_input[i][1]))

    _sum = 0
    for i in _setA:
        _sum += int(i)

    print(_sum)
