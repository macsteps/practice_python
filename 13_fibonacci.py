#!/usr/bin/env python
# goal: user enters number in fibonacci sequence and print

def gen_sequence(num):
    last1 = 1
    last2 = 0
    sequence = []
    for i in range(1, num+1):
        last = last1 + last2
        sequence.append(last)
        last1 = last2
        last2 = last

    return sequence

num = int(raw_input("How many Fibonacci numbers? -> "))
sequence = gen_sequence(num)
print sequence
