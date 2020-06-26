#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
    _regex = re.compile(r'.*\s+(\d{2})\s+(\w+)\s+(\d{1,4})\s+(\d{2}):(\d{2}):(\d{2})\s+([\+,\-,0-9]{5})')
    _match = _regex.search(t1)
    if _match:
        t1_sec = regex_to_sec(_match)
    _match = _regex.search(t2)
    if _match:
        t2_sec = regex_to_sec(_match)

    #print(t1_sec, '\n', t2_sec)

    return abs(t1_sec - t2_sec)


def regex_to_sec(_match):
    _day_to_sec = ( int(_match.group(1)) - 1 ) * 86400
    _month_to_sec = month_to_sec(_match.group(2), int(_match.group(3)))
    _years_to_sec = years_to_sec(int(_match.group(3))) 
    _hours_to_sec = int(_match.group(4)) * 3600
    _minutes_to_sec = int(_match.group(5)) * 60
    _sec = int(_match.group(6))
    _shift_sec = shift(_match.group(7))

    return  _day_to_sec + _month_to_sec + _years_to_sec + _hours_to_sec + _minutes_to_sec + _sec + _shift_sec

def intercalary_year(_year):
    if _year % 4 != 0 or (_year % 100 == 0 and _year % 400 != 0):
        return False
    else:
        return True

def years_to_sec(_year):
    _sec = 0
    for i in range(_year):
        if intercalary_year(_year):
            _sec += 31622400
        else:
            _sec += 31536000

    return _sec

def month_to_sec(_month, _year):
    _month_dict = { 'Jan' : 31, 'Feb' : 28, 'Mar' : 31, 'Apr' : 30, 'May' : 31, 'Jun' : 30, 'Jul' : 31, 'Aug' : 31, 'Sep' : 30, 'Oct' : 31, 'Nov' : 30, 'Dec' : 31 } 
    _month_list = [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec' ]
    _sec = 0
    for i in range(_month_list.index(_month)):
        _sec += _month_dict[_month_list[i]] * 86400

    if intercalary_year(_year) and _month_list.index(_month) > 1:
        return _sec + 86400
    else:
        return _sec


def shift(_shift):
    if _shift[0] == '-':
        return (int(_shift[1:3]) * 3600 + int(_shift[3:]) * 60) * -1
    else:
        return int(_shift[1:3]) * 3600 + int(_shift[3:]) * 60





if __name__ == '__main__':

    t = int(input())

    _delta_list = []
    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        _delta_list.append(delta)

    print(*_delta_list, sep='\n')

