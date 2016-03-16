#from board import Board

def place_token(player, column, board):
    if (column > (len(board[0])-1) or column < 0):
        print "Invalid column selection"
        return

    for i in range(len(board)-1, -1, -1):
        if board[i][column] == 0:
            board[i][column] = player
            return
'''    
gb = Board(5,5)

place_token(1, 1, gb.game_board)
place_token(1, 1, gb.game_board)
place_token(1, 1, gb.game_board)
place_token(1, 1, gb.game_board)
place_token(1, 1, gb.game_board)
place_token(2, 2, gb.game_board)


gb.prb()


for i in range(len(gb.game_board[0])-1, -1, -1):
    print i
'''

