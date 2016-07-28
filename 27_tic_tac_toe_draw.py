#!/usr/bin/env python
# goal: allow 2 players to enter moves as coordinates (e.g. 1, 2)
# first number is list (row), 2nd is place (vertical)
# ensure moves are legal: not already taken
#

def update_board(row, col, player, board):
    row = int(row)
    col = int(col)
    if board[row][col] != 0:
        return "invalid", board
    else:
        board[row][col] = player
        return "success", board

def get_guess(player):
    if player == "x":
        player_name = "Player1"
    else:
        player_name = "Player2"
    print "Next up: ", player_name
    guess = raw_input("Enter board coordinates as row, column -> ")
    row, col = guess.rstrip('\n').split(',')
    row = int(row) - 1
    col = int(col) - 1
    return row, col

def main():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    player1 = "x"
    player2 = "o"
    row = 0
    col = 0
    keep_playing = True
    while keep_playing == True:
        # player1
        row, col = get_guess(player1)
        message, board = update_board(row, col, player1, board)
        if message == "invalid":
            print "Space already taken. You lose your turn."

        # player2
        row, col = get_guess(player2)
        message, board = update_board(row, col, player2, board)
        if message == "invalid":
            print "Space already taken. You lose your turn."

        # check if there are any open spaces
        for sublist in board:
            if 0 in sublist:
                keep_playing = True
                break
            else:
                print "No more spaces left. Game Over"
                keep_playing = False

if __name__=="__main__":
    main()
