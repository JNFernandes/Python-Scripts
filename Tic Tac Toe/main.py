# Game play 
import display_board
import player_choose
import starting_player
import player_choice
import check_space
import assing_markers
import check_win
import check_tie
import replay

board_game = [' ']*10
player1_marker,player2_marker = player_choose()
turn = starting_player()
print(f'{turn} will go first')
    
play_game = input('Ready to go? y or n')
if play_game == 'y':
    game_on = True
else:
    game_on = False

while game_on:
    if turn == 'Player 1':
        display_board(board_game)
        position = player_choice(board_game)
        assing_markers(board_game,player1_marker,position)
        if check_win(board_game,player1_marker):
            display_board(board_game)
            print("PLAYER 1 HAS WON!")
            game_on = False
        else:
            if check_tie(board_game):
                print("THE GAME WAS A TIE")
                game_on = False
            else:
                turn = 'Player 2'
    else:
        display_board(board_game)
        position = player_choice(board_game)
        assing_markers(board_game,player2_marker,position)
        if check_win(board_game,player2_marker):
            display_board(board_game)
            print("PLAYER 2 HAS WON!")
            game_on = False
        else:
            if check_tie(board_game):
                print("THE GAME WAS A TIE")
                game_on = False
            else:
                turn = 'Player 1'
                
if replay()=='no':
    game_on = False