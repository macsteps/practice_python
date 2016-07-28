#!/usr/bin/env python
# goal: generate random 4-digit number; user has to guess.
# number correct, in correct place = cow
# number correct, in wrong place = bull

from random import randint

counter = 0

def gen_number():
    return randint(1000,9999)

def get_cows(answer, guess):
    cows = []
    # use list comprehension to preserve place in number
    cows = [i for i, j in zip(answer, guess) if i == j]
    return len(cows)

def get_bulls(answer, guess):
    bulls = []
    # place doesn't matter, only intersection
    bulls = set(answer).intersection(guess)
    return len(bulls)

def return_as_list(num):
    lst = [int(i) for i in str(num)]
    return lst

if __name__=="__main__":
    cows = 0
    bulls = 0
    answer_lst = []
    guess_lst = []
    answer = gen_number()
    while cows < 4:
        guess = int(raw_input("Guess the 4-digit number (0 to exit)-> "))
        if guess == 0:
            break

        answer_lst = return_as_list(answer)
        guess_lst = return_as_list(guess)
        cows = get_cows(answer_lst, guess_lst)
        bulls = get_bulls(answer_lst, guess_lst)

        # since a bull is also a cow, but not vice versa
        bulls = bulls - cows
        if bulls < 1:
            bulls = 0

        print "Cows = ", cows
        print "Bulls = ", bulls
        counter = counter + 1
        if cows == 4:
            print "You guessed correctly!"

    print "Game over after ", counter, " tries."
