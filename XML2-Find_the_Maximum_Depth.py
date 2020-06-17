#!/usr/bin/env python

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if level == -1:
        level += 1
    if list(elem) and maxdepth <= level:
        level += 1
        maxdepth = level
        for i in list(elem):
            depth(i, level)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
