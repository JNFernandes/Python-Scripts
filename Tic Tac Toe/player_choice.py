def player_choice(board):
    position = int(input('Choose a position from 1 to 9 (ONLY INTEGERS): '))
    while position not in range(1,10) or not check_space(board,position):
        print('Either you selected an already filled position or the number is out of range! Try again')
        position = int(input('Choose a position from 1 to 9: '))
    return position    