#!/usr/bin/env python
# goal: check lists for winner (don't worry about how moves were made)
# 0 = empty, 1 = player1 token, 2 = player2 token

def check_vertical(board_list):
    for player in (1, 2):
        for i in range(0, 2):
            if board_list[0][i] == player and board_list[1][i] == player and board_list[2][i] == player:
                return player
    return "none"

def check_horizontal(board_list):
    for player in (1, 2):
        for i in range(0, 2):
            if board_list[i][0] == player and board_list[i][1] == player and board_list[i][2] == player:
                return player
    return "none"

def check_diagonal(board_list):
    for player in (1, 2):
        if board_list[0][0] == player and board_list[1][1] == player and board_list[2][2] == player:
            return player
        if board_list[0][2] == player and board_list[1][1] == player and board_list[2][0] == player:
            return player
    return "none"


if __name__=="__main__":
    winner = "none"
    winner_vertical = [[2, 2, 0], [2, 1, 0], [2, 1, 1]]
    winner_horizontal = [[2, 2, 2], [0, 1, 2], [1, 0, 0]]
    winner_diagonal = [[2, 2, 1], [0, 1, 2], [1, 0, 0]]
    winner_none = [[2, 2, 1], [0, 1, 2], [2, 0, 0]]

    winner = check_vertical(winner_vertical)
    print "Vertical winner is ", winner
    winner = check_horizontal(winner_horizontal)
    print "Horizontal winner is ", winner
    winner = check_diagonal(winner_diagonal)
    print "Diagonal winner is: ", winner

    winner = check_vertical(winner_none)
    print "None winner is: ", winner
    winner = check_diagonal(winner_none)
    print "None winner is: ", winner
    winner = check_horizontal(winner_none)
    print "None winner is: ", winner
