#!/usr/bin/env python

num = int(raw_input("Enter a number: "))

for i in range(1, num):
    if num % i == 0:
        print num, "is divisible by ", i
