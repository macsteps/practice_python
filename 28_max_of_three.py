#!/usr/bin/env python
import sys

if len(sys.argv) < 4:
  print "Usage: sysargv[0] num1 num2 num3\n\n"
  sys.exit(1)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])

if (num1 > num2) and (num1 > num3):
  print "The largest number is ", num1
elif (num2 > num1) and (num2 > num3):
  print "The largest number is ", num2
elif (num3 > num1) and (num3 > num2):
  print "The largest number is ", num3
else:
  print "Not sure"


