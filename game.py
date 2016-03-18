#!/usr/bin/env python
import sys, getopt
from itertools import cycle
from c4py import board
from c4py import engine
from c4py import player
from c4py import save_load

class Game:
    #Default board dimensions
    width=10
    height=10
    length=4

    def __init__(self):
        width = 10
        height = 10
        length = 4

    '''
    b = board.Board(5, 5)
    engine.place_token(1,0,b.game_board)
    b.prb()
    '''

if __name__ == "__main__":
#Attempt to read 3 command line arguments -w for width, -h for height, and -l for length
    try:
        myopts, args = getopt.getopt(sys.argv[1:],"w:h:l:")
    except getopt.GetoptError as e:
        print (str(e))
        print("Usage: %s -w width -h height -l length" % sys.argv[0])
        sys.exit(2)

#Assign arguments to variables if they are integers, exit it not
    for opt, arg in myopts:
        if opt == '-w':
            try:
                width = int(arg)
            except ValueError:
                print "Board dimensions must be integers"
                sys.exit(2)
        elif opt == '-h':
            try:
                height = int(arg)
            except ValueError:
                print "Board dimensions must be integers"
                sys.exit(2)
        elif opt == '-l':
            try:
                length = int(arg)
            except ValueError:
                print "Board dimensions must be integers"
                sys.exit(2)

    board = board.Board(width, height)
    board.prb()
    i = 0
    alternate = cycle((1,2))
    while True:
        i += 1
        player = next(alternate)
        if i == 10:
            break
        print "Player " + str(player) + " choose a column"
        choice = raw_input()
        if choice is 's':
            print "Saved!"
            to_save = save_load.Saved(board, player)
            to_save.save()
        elif choice is 'l':
            print "Loaded!"
        elif choice is 'q':
            sys.exit()
        else:
            engine.place_token(player, int(choice)-1, board.game_board)
            board.prb()

    '''
    alternate = cycle((1,2))
    p = next(alternate)
    print p
    p = next(alternate)
    print p
    p = next(alternate)
    print p
    '''
