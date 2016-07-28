#!/usr/bin/env python
from random import randint

def get_play():
    plays = ["rock", "paper", "scissors"]
    play = plays[randint(0, 2)]
    return play

def determine_winner(player1, player2):
    if player1 == player2:
        return "tie"
    if player1 == "rock" and player2 == "scissors":
        return "Player1"
    if player1 == "scissors" and player2 == "paper":
        return "Player1"
    if player1 == "paper" and player2 == "rock":
        return "Player1"
    if player2 == "rock" and player1 == "scissors":
        return "Player2"
    if player2 == "scissors" and player1 == "paper":
        return "Player2"
    if player2 == "paper" and player1 == "rock":
        return "Player2"


winner = "none"

while winner == "none":
    player1 = get_play()
    player2 = get_play()
    print "Player1: ", player1
    print "Player2: ", player2
    winner = determine_winner(player1, player2)
    print "Winner: ", winner
    again = raw_input("Wanna play again? (y/n)")
    if again == "y":
        winner = "none"
