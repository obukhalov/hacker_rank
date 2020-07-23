#!/usr/bin/env python

import calendar

if __name__ == '__main__':

    _month, _day, _year = list(map(int, input().split()))
    print( calendar.day_name[calendar.weekday(_year, _month, _day)].upper() )
