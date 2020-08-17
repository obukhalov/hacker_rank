#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    _alphabet = 'abcdefghijklmnopqrstuvwxyz'
    _word_height = [ h[_alphabet.index(_s)] for _s in word ]
    return max(_word_height) * 1 * len(word)

if __name__ == '__main__':

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(str(result) + '\n')
