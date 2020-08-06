#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    _modify = []
    _etalon = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    _delta = [ abs(_etalon[i][j] - s[i][j]) for i in range(3) for j in range(3) ]
    _modify.append(sum(_delta))

    #First rotare
    _rotate1 = [ [s[0][2], s[1][2], s[2][2]], [s[0][1], s[1][1], s[2][1]], [s[0][0], s[1][0], s[2][0]] ]
    _delta = [ abs(_etalon[i][j] - _rotate1[i][j]) for i in range(3) for j in range(3) ]
    _modify.append(sum(_delta))

    #Second rotare
    _rotate2 = [ [s[2][2], s[2][1], s[2][0]], [s[1][2], s[1][1], s[1][0]], [s[0][2], s[0][1], s[0][0]] ]
    _delta = [ abs(_etalon[i][j] - _rotate2[i][j]) for i in range(3) for j in range(3) ]
    _modify.append(sum(_delta))
    
    #Third rotare
    _rotate3 = [ [s[2][0], s[1][0], s[0][0]], [s[2][1], s[1][1], s[0][1]], [s[2][2], s[1][2], s[0][2]] ]
    _delta = [ abs(_etalon[i][j] - _rotate3[i][j]) for i in range(3) for j in range(3) ]
    _modify.append(sum(_delta))

    #Third rotare
    _rotate4 = [ [s[2][0], s[2][1], s[2][2]], [s[1][0], s[1][1], s[1][2]], [s[0][0], s[0][1], s[0][2]] ]
    _delta = [ abs(_etalon[i][j] - _rotate4[i][j]) for i in range(3) for j in range(3) ]
    _modify.append(sum(_delta))

    #Fourth rotare
    _rotate5 = [ [s[0][2], s[0][1], s[0][0]], [s[1][2], s[1][1], s[1][0]], [s[2][2], s[2][1], s[2][0]] ]
    _delta = [ abs(_etalon[i][j] - _rotate5[i][j]) for i in range(3) for j in range(3) ]
    _modify.append(sum(_delta))

    #Fifth rotare
    _rotate6 = [ [s[2][2], s[1][2], s[0][2]], [s[2][1], s[1][1], s[0][1]], [s[2][0], s[1][0], s[0][0]] ]
    _delta = [ abs(_etalon[i][j] - _rotate6[i][j]) for i in range(3) for j in range(3) ]
    _modify.append(sum(_delta))

    #Sixth rotare
    _rotate7 = [ [s[0][0], s[1][0], s[2][0]], [s[0][1], s[1][1], s[2][1]], [s[0][2], s[1][2], s[2][2]] ]
    _delta = [ abs(_etalon[i][j] - _rotate7[i][j]) for i in range(3) for j in range(3) ]
    _modify.append(sum(_delta))

    #print(_modify)

    return min(_modify)

if __name__ == '__main__':

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print(str(result) + '\n')
