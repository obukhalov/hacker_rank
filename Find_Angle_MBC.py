#!/usr/bin/env python

import math

if __name__ == '__main__':
    _ab = int(input())
    _bc = int(input())
    #Hypotenuse
    _ac = math.sqrt(_ab**2 + _bc**2)
    #Angle ACB
    #_angle_acb = ( math.asin( _ab / _ac ) / math.pi ) * 180
    _angle_acb = math.asin( _ab / _ac )

    _mc = _ac / 2
    #Median
    _median = math.sqrt((_bc**2 + _mc**2) - (math.cos(_angle_acb) * 2 * _bc * _mc) )

    #Cosinus of angle mbc
    _cos_mbc = (_bc**2 - _mc**2 + _median**2) / ( 2 * _bc * _median )

    _angle_mbc = ( math.acos( _cos_mbc ) / math.pi ) * 180

    print(round(_angle_mbc), '°', sep='' )
