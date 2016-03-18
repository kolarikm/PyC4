import pickle

class Saved:
    def __init__(self, board, cur_player):
        self.board = board
        self.cur_player = cur_player

    def save(self):
        with open('saved_game.dat', 'wb') as f:
            to_save = Saved(self.board, self.cur_player)
            pickle.dump(to_save, f)

    def load(self):
        with open('saved_game.dat', 'rb') as f:
            to_load = pickle.load(f)
        return to_load
