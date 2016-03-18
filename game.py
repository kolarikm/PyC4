#!/usr/bin/env python
import sys, getopt
from itertools import cycle
from c4py import board
from c4py import engine
from c4py import player
from c4py import save_load
from pprint import pprint

class Game:
    def __init__(self):
        #defaults
        width = 10
        height = 10
        length = 4

if __name__ == "__main__":
    #Attempt to read 3 command line arguments
    #-w for width, -h for height, and -l for length
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

    #Game loop
    engine.print_title()
    board = board.Board(width, height)
    board.prb()
    cur_game = save_load.Saved(board, 1)
    alternate = cycle((1,2))
    player = next(alternate)
    while True:
        print "Player " + str(player) + " choose a column"
        choice = raw_input()
        print
        if choice is 's':
            print "Saved!"
            to_save = save_load.Saved(board, player)
            to_save.save()
        elif choice is 'l':
            print "Loaded!"
            cur_game = cur_game.load()
            board = cur_game.board
            player = cur_game.cur_player
            board.prb()
            continue
        elif choice is 'q':
            sys.exit()
        else:
            try:
                engine.place_token(player, int(choice)-1, board.game_board)
            except ValueError:
                print "Incompatible input"
            board.prb()
            player = next(alternate)
