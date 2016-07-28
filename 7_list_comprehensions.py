#!/usr/bin/env python

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#for i in a:
#    if i % 2 == 0:
#        b.append(i)
#print b

# as one line
print [i for i in a if i % 2 == 0 ]
