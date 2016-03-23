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
    return 0

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
    return 0

def check_f_d(board, length):
    for r in xrange(length-1, len(board), 1):
        for c in xrange(len(board[r])-length+1):
            match = 0
            if board[r][c] != 0:
                for x in xrange(length):
                    if board[r-x][c+x] == board[r][c]:
                        match += 1
                if match == length:
                    return board[r][c]
    return 0

def check_b_d(board, length):
    for r in xrange(len(board)-length+1):
        for c in xrange(len(board[r])-length+1):
            match = 0
            if board[r][c] != 0:
                for x in xrange(length):
                    if board[r+x][c+x] == board[r][c]:
                        match += 1
                if match == length:
                    return board[r][c]
    return 0

def winner(board, length):
    h_win = check_h(board, length)
    v_win = check_v(board, length)
    fd_win = check_f_d(board, length)
    bd_win = check_b_d(board, length)

    if h_win > 0:
        return h_win
    elif v_win > 0:
        return v_win
    elif fd_win > 0:
        return fd_win
    elif bd_win > 0:
        return bd_win
    else:
        return -1

def print_title():
    print " _____                             _       ___ "
    print "/  __ \                           | |     /   |"
    print "| /  \/ ___  _ __  _ __   ___  ___| |_   / /| |"
    print "| |    / _ \| '_ \| '_ \ / _ \/ __| __| / /_| |"
    print "| \__/\ (_) | | | | | | |  __/ (__| |_  \___  |"
    print " \____/\___/|_| |_|_| |_|\___|\___|\__|     |_/\n"
