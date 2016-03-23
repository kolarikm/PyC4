#!/usr/bin/env python
import sys, getopt
from itertools import cycle
from c4py import *

if __name__ == "__main__":
    #Attempt to read 3 command line arguments
    #-w for width, -h for height, and -l for length
    try:
        myopts, args = getopt.getopt(sys.argv[1:],"s:l:")
    except getopt.GetoptError as e:
        print (str(e))
        print("Usage: %s -s size -l length" % sys.argv[0])
        sys.exit(2)

        #Assign arguments to variables if they are integers, exit it not
    for opt, arg in myopts:
        if opt == '-s':
            try:
                width = int(arg)
                height = int(arg)
            except ValueError:
                print "Board dimensions must be integers"
                sys.exit(2)
        if opt == '-l':
            try:
                length = int(arg)
            except ValueError:
                print "Board dimensions must be integers"
                sys.exit(2)

    #Game loop
    try:
        board = board.Board(width, height)
    except NameError:
	print "No parameters specified\nUsage: ./game.py -s size -l length"
	sys.exit()
    engine.print_title()
    board.prb()
    cur_game = save_load.Saved(board, 1)
    alternate = cycle((1,2))
    player = next(alternate)
    win = 0
    play = True
    while play is True:
        print "Player " + str(player) + " choose a column"
        choice = raw_input()
        print
        if choice is 's':
            print "Saved!"
            to_save = save_load.Saved(board, player)
            to_save.save()
            sys.exit()
        elif choice is 'l':
            try:
                cur_game = cur_game.load()
                board = cur_game.board
                player = cur_game.cur_player
                board.prb()
            except IOError:
                print "Error loading saved game."
                continue;
            print "Loaded!"
            continue
        elif choice is 'q':
            print "Goodbye!"
            sys.exit()
        else:
            try:
                engine.place_token(player, int(choice)-1, board.game_board)
		win = engine.winner(board.game_board, length)
            except ValueError:
                print "Incompatible input"
        board.prb()
	if win > 0:
	    print "Player %s wins!\n" % win
	    play = False
        player = next(alternate)
