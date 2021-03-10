def starting_player():
    coin = randint(0,1)
    if coin == 0:
        return 'Player 1'
    else:
        return 'Player 2'