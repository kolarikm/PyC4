class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        board = lambda w, h: [[0] * w for i in range(h)]
        self.game_board = board(width, height)

    def prb(self):
        for i in self.game_board:
            for j in i:
                print j,
            print
