from board import Board

def place_token(player, column, board):
    if (column > (len(board[0])-1) or column < 0):
        print "Invalid column selection"
        return

    for i in range(len(board)-1, -1, -1):
        if board[i][column] == 0:
            board[i][column] = player
            return

def check_h(board, length):
    for r in xrange(len(board)):
        for c in xrange(len(board[r])-length+1):
            match = 0
            if board[r][c] != 0:
                for x in xrange(length):
                    if board[r][c+x] == board[r][c]:
                        match += 1
                if match == length:
                    return board[r][c]
    return "No winner!"

def check_v(board, length):
    for r in xrange(len(board)-1, length, -1):
        for c in xrange(len(board)):
            match = 0
            if board[r][c] != 0:
                for x in xrange(length):
                    if board[r-x][c] == board[r][c]:
                        match += 1
                if match == length:
                    return board[r][c]
    return "No winner!"

def check_b_d(board, length):
    i = 0
    for r in xrange((length)-1):
        for c in xrange(len(board[r])-length+1):
            i += 1
            print i
                

gb = Board(10,10)

place_token(1, 1, gb.game_board)
place_token(1, 2, gb.game_board)
place_token(1, 3, gb.game_board)
#place_token(1, 4, gb.game_board)

place_token(1, 1, gb.game_board)
place_token(1, 1, gb.game_board)
place_token(1, 1, gb.game_board)

gb.prb()

#win = check_h(gb.game_board, 4)
#print win

#w = check_v(gb.game_board, 4)
#print w

check_b_d(gb.game_board, 4)
