#!/usr/bin/env python

num = int(raw_input("Enter a number: "))
if num % 4 == 0:
    print "Your number is a multiple of 4."
elif num % 2 == 0:
    print "Your number is even."
else:
    print "Your number is odd."
