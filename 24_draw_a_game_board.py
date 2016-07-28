#!/usr/bin/env python
# goal: ask user for a number corresponding to size, then print game board.

def print_board(size):
    for i in range(size):
        print " ---" * size
        print "|   " * (size + 1)

    print " ---" * size

if __name__=="__main__":
    size = int(raw_input("What size board -> "))
    print_board(size)
