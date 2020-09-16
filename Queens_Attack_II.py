#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    _attack = 0
    _north = n - r_q
    _south = r_q - 1
    _west = n - c_q
    _east = c_q - 1
#Find source north-west attack points
    _north_west = 0
    _x = c_q + 1
    _y = r_q + 1
    while _x <= n and _y <= n:
        _north_west += 1
        _x += 1
        _y += 1
#Find source south-east attack points
    _south_east = 0
    _x = c_q - 1
    _y = r_q - 1
    while _x > 0 and _y > 0:
        _south_east += 1
        _x -= 1
        _y -= 1
#Find source south-west attack points
    _south_west = 0
    _x = c_q + 1
    _y = r_q - 1
    while _x <= n and _y > 0:
        _south_west += 1
        _x += 1
        _y -= 1
#Find source north-east attack points
    _north_east = 0
    _x = c_q - 1
    _y = r_q + 1
    while _x > 0 and _y <= n:
        _north_east += 1
        _x -= 1
        _y += 1


    for _obst in obstacles:
        if _obst[1] == c_q:
            if _obst[0] > r_q:
                if _north > _obst[0] - r_q - 1:
                    _north = _obst[0] - r_q - 1
            if _obst[0] < r_q:
                if _south > r_q - _obst[0] - 1:
                    _south = r_q - _obst[0] - 1

        if _obst[0] == r_q:
            if _obst[1] > c_q:
                if _west > _obst[1] - c_q - 1:
                    _west = _obst[1] - c_q - 1
            if _obst[1] < c_q:
                if _east > c_q - _obst[1] - 1:
                    _east = c_q - _obst[1] - 1

        if abs(_obst[0] - r_q) == abs(_obst[1] - c_q):
            if _obst[0] > r_q and _obst[1] > c_q:
                if _north_west > abs(_obst[0] - r_q):
                    _north_west = abs(_obst[0] - r_q) - 1
            if _obst[0] < r_q and _obst[1] < c_q:
                if _south_east > abs(_obst[0] - r_q):
                    _south_east = abs(_obst[0] - r_q) - 1
            if _obst[0] < r_q and _obst[1] > c_q:
                if _south_west > abs(_obst[0] - r_q):
                    _south_west = abs(_obst[0] - r_q) - 1
            if _obst[0] > r_q and _obst[1] < c_q:
                if _north_east > abs(_obst[0] - r_q):
                    _north_east = abs(_obst[0] - r_q) - 1


    _attack = _north + _south + _east + _west + _north_west + _south_east + _south_west + _north_east

    return _attack

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(str(result) + '\n')
