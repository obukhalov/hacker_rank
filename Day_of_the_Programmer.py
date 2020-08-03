#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    _usual_year_months = { 1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31 }
    _leap_year_months = { 1 : 31, 2 : 29, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31 }
    _gregorian = { 1 : 31, 2 : 15, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31 }

    if year < 1918:
        if year % 4 == 0:
            _days = 256
            for _m in _leap_year_months:
                if _days - _leap_year_months[_m] > 0:
                    _month = _m
                    _days -= _leap_year_months[_m]
        else:
            _days = 256
            for _m in _usual_year_months:
                if _days - _usual_year_months[_m] > 0:
                    _month = _m
                    _days -= _usual_year_months[_m]

        
    elif year > 1918:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            _days = 256
            for _m in _leap_year_months:
                if _days - _leap_year_months[_m] > 0:
                    _month = _m
                    _days -= _leap_year_months[_m]
        else:
            _days = 256
            for _m in _usual_year_months:
                if _days - _usual_year_months[_m] > 0:
                    _month = _m
                    _days -= _usual_year_months[_m]

    elif year == 1918:
        _days = 256
        for _m in _gregorian:
            if _days - _gregorian[_m] > 0:
                _month = _m
                _days -= _gregorian[_m]

# Format date
    _f_year = str(year)

    if _month + 1 < 10:
        _f_month = '0' + str(_month + 1)
    else:
        _f_month = str(_month + 1)

    if _days < 10:
        _f_days = '0' + str(_days)
    else:
        _f_days = str(_days)


    _f_date = _f_days + '.' + _f_month + '.' + _f_year

    return _f_date



if __name__ == '__main__':

    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result + '\n')
