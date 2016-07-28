#!/usr/bin/env python
from random import randint

counter = 0
finished = "false"
guess = 0

while finished == "false":
    num = randint(1,9)
    while guess != num:
        guess = raw_input("Guess a number between 1 and 9 or 'exit'  -> ")
        counter = counter + 1
        if guess == "exit":
            finished = "true"
            break

        if int(guess) == num:
            print "Correct! After ", counter, " guesses."
            break
        else:
            print "Sorry. Try again."
