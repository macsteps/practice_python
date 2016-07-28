#!/usr/bin/env python
from random import randint

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = []
b = []
for x in range(1,20):
    b.append(randint(1,100))

for y in range(1,25):
    a.append(randint(1,100))

set_a = set(a)
set_b = set(b)
final = []

for i in set_a:
    if i in set_b:
        final.append(i)

print final
