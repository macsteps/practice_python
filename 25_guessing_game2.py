#!/usr/bin/env python
# goal: continue guessing until the number a user is thinking is guessed.

def guess(num):
    print num
    result = raw_input("Correct? (y/n)")
    if result == "n":
        result = raw_input("Is your number higher or lower? h/l ")
    return result

if __name__=="__main__":
    possible_numbers = []
    possible_numbers = range(100)
    answer = "incorrect"

    while answer == "incorrect":
        middle = len(possible_numbers) / 2
        result = guess(possible_numbers[middle])
        if result == "y":
            print "Game over"
            answer = "correct"
        elif result == "higher" or result == "h":
            possible_numbers = possible_numbers[middle:]
        else:
            possible_numbers = possible_numbers[:middle]
