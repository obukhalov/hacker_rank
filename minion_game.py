#!/usr/bin/env python

def minion_game(string):
    # your code goes here

    _vowels = 'AEIOU'
    _consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
    players = { 'Kevin': 0, 'Stuart': 0 }


    for i in range(len(string)):
        if string[i] in _consonants:
            players['Stuart'] += len(string) -i
        elif string[i] in _vowels:
            players['Kevin'] += len(string) -i


    if players['Stuart'] > players['Kevin']:
        print('{} {}'.format('Stuart', players['Stuart']))
    elif players['Kevin'] > players['Stuart']:
        print('{} {}'.format('Kevin', players['Kevin']))
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
