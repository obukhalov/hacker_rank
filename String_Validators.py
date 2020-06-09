#!/usr/bin/env python

if __name__ == '__main__':
    s = input()
    alphanumeric = False
    alphabetical = False
    digits = False
    lowercase = False
    uppercase = False

    for _sym in s:
        if _sym.isalnum():
            alphanumeric = True
        if _sym.isalpha():
            alphabetical = True
        if _sym.isdigit():
            digits = True
        if _sym.islower():
            lowercase = True
        if _sym.isupper():
            uppercase = True
            
    print(alphanumeric)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)

