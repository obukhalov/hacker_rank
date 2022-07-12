#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'crosswordPuzzle' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY crossword
#  2. STRING words
#
def find_coordinates(crossword, one_letter_word=False):

    # Get the size of crossword
    row = len(crossword)
    col = len(crossword[0])

    # Make a dictionary where key - lenght of word, value - coordinates of word in crossword
    holes = [(r, c) for r in range(row) for c in range(col) if crossword[r][c] == "-"]
    coordinates = []

    for r in range(row):
        holes_sub = [h for h in holes if h[0] == r]
        holes_sub.sort(key=lambda x: x[1])
        wl = []
        w = []

        for co in holes_sub:
            if len(w) == 0:
                w.append(co)
            else:
                if co[1] - w[-1][1] == 1:
                    w.append(co)
                else:
                    wl.append(w)
                    w = [co]
        wl.append(w)

        for w in wl:
            if len(w) > 1:
                coordinates.append(w)

    for c in range(col):
        holes_sub = [h for h in holes if h[1] == c]
        holes_sub.sort(key=lambda x: x[0])
        wl = []
        w = []

        for co in holes_sub:
            if len(w) == 0:
                w.append(co)
            else:
                if co[0] - w[-1][0] == 1:
                    w.append(co)
                else:
                    wl.append(w)
                    w = [co]
        wl.append(w)

        for w in wl:
            if one_letter_word:
                coordinates.append(w)
            else:
                if len(w) > 1:
                    coordinates.append(w)

    return coordinates


def find_crosspoints(coordinates):
    # Find all cross points
    crosspoints = []
    for c1 in coordinates:
        for c2 in coordinates:
            c1 = set(c1)
            c2 = set(c2)
            if len(c1.intersection(c2)) == 1:
                crosspoints.append(list(c1.intersection(c2))[0])

    crosspoints = list(set(crosspoints))

    return crosspoints


def crosswordPuzzle(crossword, words):
    # Write your code here

    # Convert the strings in columns into list
    crossword = [list(s) for s in crossword]

    # Get the list of words
    words = words.split(";")

    # Get coordinates of words from crossword. Also get all crosspoints
    coordinates = find_coordinates(crossword)
    crosspoints = find_crosspoints(coordinates)

    # Save original coordinates and crosspoints
    coordinates_orig = coordinates.copy()
    crosspoints_orig = crosspoints.copy()

    # Fill up all crossed words first
    while len(crosspoints) > 0:

        for cross in crosspoints:
            cw = []

            for w in coordinates:
                if cross in w:
                    cw.append(w)

            l1 = len(cw[0])
            i1 = cw[0].index(cross)
            l2 = len(cw[1])
            i2 = cw[1].index(cross)

            crossed_words = []
            for w1 in words:
                for w2 in words:
                    if len(w1) == l1 and len(w2) == l2 and w1[i1] == w2[i2]:
                        crossed_words.append(w1)
                        crossed_words.append(w2)
            if len(crossed_words) == 2:
                c1 = cw[0]
                c2 = cw[1]
                w1 = crossed_words[0]
                w2 = crossed_words[1]
                for i in range(l1):
                    c = c1[i][0]
                    r = c1[i][1]
                    crossword[c][r] = w1[i]
                for i in range(l2):
                    c = c2[i][0]
                    r = c2[i][1]
                    crossword[c][r] = w2[i]

        coordinates = find_coordinates(crossword)
        crosspoints = find_crosspoints(coordinates)

    # Fill up every other words
    coordinates = find_coordinates(crossword, one_letter_word=False)
    for lc in coordinates:
        s = lc[0]

        for oc in coordinates_orig:

            if s in oc:
                l = len(oc)
                filled_letters = {}

                for c in crosspoints_orig:
                    if c in oc:
                        idx = oc.index(c)
                        letter = crossword[c[0]][c[1]]
                        filled_letters[idx] = letter

                for w in words:

                    if len(w) == l:

                        hit = True
                        for i in filled_letters:
                            if w[i] != filled_letters[i]:
                                hit = False

                        if hit == True:
                            for i in range(l):
                                c = oc[i][0]
                                r = oc[i][1]
                                crossword[c][r] = w[i]

    # Restore the crossford dormat
    crossword = ["".join(s) for s in crossword]

    return crossword


if __name__ == "__main__":

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    print("\n".join(result))
    print("\n")
