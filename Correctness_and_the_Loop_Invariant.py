#!/usr/bin/env python


def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j > 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

    if l[0] > l[1]:
        _n = l.pop(0)
        _no_change = True
        for i in range(0, len(l)):
            if l[i] > _n:
                l.insert(i,_n)
                _no_change = False
                break
        if _no_change:
            l.append(_n)

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))
