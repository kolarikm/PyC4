import sys, getopt

from c4py.player import Player
from c4py.board import Board

'''

mike = Player.Player("Mike", 4)

for i in hi:
    for j in i:
        print j,
    print

bo = Board(2,3)
bo.prb()

'''

def handle_opts():
    width = 0
    height = 0
    length = 0
    
    try:
        myopts, args = getopt.getopt(sys.argv[1:],"w:h:l:")
    except getopt.GetoptError as e:
        print (str(e))
        print("Usage: %s -w width -h height -l length" & sys.argv[0])
        sys.exit(2)

    for opt, arg in myopts:
        if opt == '-w':
            width = arg
        elif opt == '-h':
            height = arg
        elif opt == '-l':
            length = arg
    print ("Width: %s  Height: %s  Length: %s" % (width, height, length))

if __name__ == "__main__":
    handle_opts()
