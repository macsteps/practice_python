#!/usr/bin/env python

word = raw_input("Enter a word: ")
reverse = word[::-1]

if word == reverse:
    print "palindrome"
else:
    print "not a palindrome"
