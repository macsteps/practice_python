#!/usr/bin/env python
# goal: print long string in reverse word order.

a = "My name is Michele"

def reverse_order(a):
    b = []
    b = a.split(" ")
    return b[::-1]

b = reverse_order(a)
print ' '.join(b)
