#!/usr/bin/env python
# goal: answer boolean whether number is inside list.

def is_match(a_list, user_guess):
    if user_guess in a_list:
        return True
    else:
        return False

if __name__=="__main__":
    a_list = [1, 3, 5, 30, 42, 43, 500]
    response = False
    check = []
    while response == False:
        user_guess = raw_input("Guess a number -> ")
        if user_guess == "exit":
            break
        else:
            user_guess = int(user_guess)

        response = is_match(a_list, user_guess)
        print response
