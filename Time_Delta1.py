#!/usr/bin/env python

import math
import os
import random
import re
import sys
import pdb

# Complete the time_delta function below.
def time_delta(t1, t2):
    _regex = re.compile(r'.*\s+(\d{2})\s+(\w+)\s+(\d{1,4})\s+(\d{2}):(\d{2}):(\d{2})\s+([\+,\-,0-9]{5})')
    _t1_match = _regex.search(t1)
    _t2_match = _regex.search(t2)

    #Define first and second date and parse input
    _dict = parse_dates(_t1_match, _t2_match)

    #Get time difference for full years between two dates
    _years_sec = years_to_sec(_dict[2]['year'], _dict[1]['year'])

    #From eralier date get sec to the end of the year
    _till_the_end = till_the_end( _dict[2] )

    #From later date get sec from the beginning of the year
    _from_the_beginning = from_the_beginning( _dict[1] )

    if _dict[1]['year'] == _dict[2]['year']:
        if intercalary_year(_dict[1]['year']):
            _result =  _from_the_beginning - ( 31622400 - _till_the_end )
        else: 
            _result = _from_the_beginning - ( 31536000 - _till_the_end )
    else:
        _result = _years_sec + _till_the_end + _from_the_beginning

    _shift = shift( _dict[1], _dict[2] )

    return _result + _shift

def parse_dates(_t1, _t2):
    _t1_day = int(_t1.group(1))
    _t1_month = _t1.group(2)
    _t1_year = int(_t1.group(3))
    _t1_hour = int(_t1.group(4))
    _t1_min = int(_t1.group(5))
    _t1_sec = int(_t1.group(6))
    _t1_shift_sign = _t1.group(7)[0]
    _t1_shift_hour = int(_t1.group(7)[1:3])
    _t1_shift_min = int(_t1.group(7)[3:])

    _t2_day = int(_t2.group(1))
    _t2_month = _t2.group(2)
    _t2_year = int(_t2.group(3))
    _t2_hour = int(_t2.group(4))
    _t2_min = int(_t2.group(5))
    _t2_sec = int(_t2.group(6))
    _t2_shift_sign = _t2.group(7)[0]
    _t2_shift_hour = int(_t2.group(7)[1:3])
    _t2_shift_min = int(_t2.group(7)[3:])

    _month_list = [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec' ]

    #pdb.set_trace()

    if _t1_year > _t2_year:
        _first = 1
    elif _t1_year < _t2_year:
        _first = 2
    else:
        if _month_list.index(_t1_month) > _month_list.index(_t2_month):
            _first = 1
        elif _month_list.index(_t1_month) < _month_list.index(_t2_month):
            _first = 2
        else:
            if _t1_day > _t2_day:
                _first = 1
            elif _t1_day < _t2_day:
                _first = 2
            else:
                if _t1_hour > _t2_hour:
                    _first = 1
                elif _t1_hour < _t2_hour:
                    _first = 2
                else:
                    if _t1_min > _t2_min:
                        _first = 1
                    elif _t1_min < _t2_min:
                        _first = 2
                    else:
                        if _t1_sec > _t2_sec:
                            _first = 1
                        elif _t1_sec < _t2_sec:
                            _first = 2
                        else:
                            _first = 1

    if _first == 1:
        return { 1 : { 'day' : _t1_day, 'month' : _t1_month, 'year' : _t1_year, 'hour' : _t1_hour, 'min' : _t1_min, 'sec' : _t1_sec, 'shift_sign' : _t1_shift_sign, 'shift_hour' : _t1_shift_hour, 'shift_min' : _t1_shift_min }, 2 : { 'day' : _t2_day, 'month' : _t2_month, 'year' : _t2_year, 'hour' : _t2_hour, 'min' : _t2_min, 'sec' : _t2_sec, 'shift_sign' : _t2_shift_sign, 'shift_hour' : _t2_shift_hour, 'shift_min' : _t2_shift_min }}
    elif _first == 2:
        return { 1 : { 'day' : _t2_day, 'month' : _t2_month, 'year' : _t2_year, 'hour' : _t2_hour, 'min' : _t2_min, 'sec' : _t2_sec, 'shift_sign' : _t2_shift_sign, 'shift_hour' : _t2_shift_hour, 'shift_min' : _t2_shift_min }, 2 : { 'day' : _t1_day, 'month' : _t1_month, 'year' : _t1_year, 'hour' : _t1_hour, 'min' : _t1_min, 'sec' : _t1_sec, 'shift_sign' : _t1_shift_sign, 'shift_hour' : _t1_shift_hour, 'shift_min' : _t1_shift_min } }


def intercalary_year(_year):
    if _year % 4 != 0 or (_year % 100 == 0 and _year % 400 != 0):
        return False
    else:
        return True

def years_to_sec(_start, _end):
    _sec = 0
    for i in range(_start + 1, _end):
        if intercalary_year(i):
            _sec += 31622400
        else:
            _sec += 31536000

    return _sec

def till_the_end( _dict ):
    _month_dict = { 'Jan' : 31, 'Feb' : 28, 'Mar' : 31, 'Apr' : 30, 'May' : 31, 'Jun' : 30, 'Jul' : 31, 'Aug' : 31, 'Sep' : 30, 'Oct' : 31, 'Nov' : 30, 'Dec' : 31 } 
    _month_list = [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec' ]
   # Convert monthes till the end of the year to seconds
    _month_till_end_of_year = 0
    if _month_list.index(_dict['month']) < 11:
        for i in range(_month_list.index(_dict['month']) + 1, len(_month_list)): 
            _month_till_end_of_year += _month_dict[_month_list[i]] * 86400
        if intercalary_year(_dict['year']) and _month_list.index(_dict['month']) == 0:
            _month_till_end_of_year += 86400

    #Convert days till the end of the month
    if intercalary_year(_dict['year']) and _dict['month'] == 'Feb':
        _days_till_end_of_month = ( 29 - _dict['day'] ) * 86400
    else:
        _days_till_end_of_month = ( _month_dict[_dict['month']] - _dict['day'] ) * 86400

    # Get seconds till the end of the day
    _sec_till_the_end_of_day = 86400 - ( _dict['hour'] * 3600 + _dict['min'] * 60 + _dict['sec'] )

    return _month_till_end_of_year + _days_till_end_of_month + _sec_till_the_end_of_day

def from_the_beginning( _dict ):
    _month_dict = { 'Jan' : 31, 'Feb' : 28, 'Mar' : 31, 'Apr' : 30, 'May' : 31, 'Jun' : 30, 'Jul' : 31, 'Aug' : 31, 'Sep' : 30, 'Oct' : 31, 'Nov' : 30, 'Dec' : 31 } 
    _month_list = [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec' ]
    #Convert full monthes to seconds
    _month_from_begining = 0
    if _month_list.index(_dict['month']) > 0:
        for i in range(_month_list.index(_dict['month'])):
            _month_from_begining += _month_dict[_month_list[i]] * 86400
        if intercalary_year(_dict['year']) and _month_list.index(_dict['month']) > 1:
            _month_from_begining += 86400

    #Convert full days to seconds
    _days_from_beginning = ( _dict['day'] -1 ) * 86400

    #Get seconds from the beginning
    _seconds_from_beginning = _dict['hour'] * 3600 + _dict['min'] * 60 + _dict['sec']

    return _month_from_begining + _days_from_beginning + _seconds_from_beginning


def shift(_dict1, _dict2):
    if _dict1['shift_sign'] == '-':
        _shift1_sec = (_dict1['shift_hour'] * 3600 + _dict1['shift_min'] * 60 ) * -1
    else:
        _shift1_sec = _dict1['shift_hour'] * 3600 + _dict1['shift_min'] * 60
    if _dict2['shift_sign'] == '-':
        _shift2_sec = (_dict2['shift_hour'] * 3600 + _dict2['shift_min'] * 60 ) * -1
    else:
        _shift2_sec = _dict2['shift_hour'] * 3600 + _dict2['shift_min'] * 60
    return _shift2_sec - _shift1_sec



if __name__ == '__main__':

    t = int(input())

    _delta_list = []
    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        _delta_list.append(delta)

    print(*_delta_list, sep='\n')

