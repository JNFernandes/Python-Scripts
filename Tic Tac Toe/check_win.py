def check_win(board,marker): 
    if board[1]==board[2]==board[3]==marker or board[4]==board[5]==board[6]==marker or board[7]==board[8]==board[9]==marker \
    or board[1]==board[4]==board[7]==marker or board[2]==board[5]==board[8]==marker or board[3]==board[6]==board[9]==marker \
    or board[1]==board[5]==board[9]==marker or board[3]==board[5]==board[7]==marker:
        return True