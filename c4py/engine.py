from board import Board

def place_token(player, column, board):
    if (column > (len(board[0])-1) or column < 0):
        print "Invalid column selection"
        return

    for i in range(len(board)-1, -1, -1):
        if board[i][column] == 0:
            board[i][column] = player
            return
'''
def check_horizontal(board, length):
    for r in range(0, len(board), 1):
        for c in range(len(board[0])-length):
            match = 0
            print board[r][c]
            if int(board[r][c]) != 0:
                for x in range(0, length+1, 1):
                    if board[r][c+x] == board[r][c]:
                        match += 1
                        print match
                if match == length:
                    return board[r][c]
    return 0
'''

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
                

gb = Board(5,5)

place_token(1, 1, gb.game_board)
place_token(1, 2, gb.game_board)
place_token(1, 3, gb.game_board)
#place_token(1, 4, gb.game_board)


gb.prb()

win = check_h(gb.game_board, 4)
print win
'''
for (i, row) in enumerate(gb.game_board):
    for (j, value) in enumerate(row):
        print gb.game_board[i][j]
        if gb.game_board[i][j] != 0:
            print "Yes"


for i in range(len(gb.game_board[0])-1, -1, -1):
    print i
'''

