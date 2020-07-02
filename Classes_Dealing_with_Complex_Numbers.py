#!/usr/bin/env python

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
        
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)
        
    def __mul__(self, other):
        return Complex( (self.real * other.real - self.imaginary * other.imaginary), (self.imaginary * other.real + self.real * other.imaginary) )

    def __truediv__(self, other):
        _new_real = round( (self.real * other.real + self.imaginary * other.imaginary) / (other.real ** 2 + other.imaginary ** 2) , ndigits=2 )
        _new_imaginary = round( (self.imaginary * other.real - self.real * other.imaginary) / (other.real ** 2 + other.imaginary ** 2 ), ndigits=2 )
        return Complex(_new_real, _new_imaginary)

    def mod(self):
       return Complex(round(math.sqrt(self.real ** 2 + self.imaginary ** 2), ndigits=2 ) , 0 )

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    _real, _imaginary = list(map(int, input().split()))
    _C = Complex(_real, _imaginary)
    _real, _imaginary = list(map(int, input().split()))
    _D = Complex(_real, _imaginary)
    print(_C + _D)
    print(_C - _D)
    print(_C * _D)
    print(_C / _D)
    print(_C.mod())
    print(_D.mod())

