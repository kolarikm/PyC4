#!/usr/bin/env python
import sys, getopt
from itertools import cycle
from c4py import board
from c4py import engine
from c4py import player


#Default board dimensions
width=10
height=10
length=4

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
'''
b = board.Board(5, 5)
engine.place_token(1,0,b.game_board)
b.prb()
'''

if __name__ == "__main__":
    board = board.Board(width, height)
    board.prb()
    player = 1
    i = 0
    while True:
        i += 1

        if i == 5:
            break
        print "Player " + str(player) + " choose a column"
        play_col = int(raw_input())
        
        engine.place_token(player, int(play_col), board.game_board)
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
    
        

