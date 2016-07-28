#!/usr/bin/env/python
# goal: get fist and last elements (ends) of an array using a function.

a = [5, 10, 15, 20, 25]

def get_ends(a):
    length = len(a)
    return a[0], a[length-1]

first, last = get_ends(a)
print first, last
