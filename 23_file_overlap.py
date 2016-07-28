#!/usr/bin/env python
# goal: find numbers that exist in both files.

def read_file(file_name):
    with open(file_name, 'r') as a_file:
        return a_file.readlines()

if __name__=="__main__":
    prime_numbers = ""
    happy_numbers = ""
    final = []

    prime_numbers = read_file('primenumbers.txt')
    prime_numbers = [int(str_i) for str_i in prime_numbers]
    happy_numbers = read_file('happynumbers.txt')
    happy_numbers = [int(str_i) for str_i in happy_numbers]

    for prime_i in prime_numbers:
        if prime_i in happy_numbers:
            final.append(prime_i)

    print final
