class Board:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.game_board  = [[0 for i in xrange(height)] for j in xrange(width)]

    def prb(self):
        for i in self.game_board:
            for j in i:
                print j,
            print
