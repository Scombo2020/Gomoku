from variable import *
import copy

class Bot(object):
    
    def __init__(self, board, recent_piece):
        self.board = board
        self.recent_piece = recent_piece

    # collect the possible status
    def succ(self, turn):

        succ_list = []

        #going through each coordinate, and if it's empty, that one of possible options for the next piece.
        for row in range(board_size):
            for col in range(board_size):
                if self.board[row][col] == 0:
                    succ = copy.deepcopy(self.board)
                    succ[row][col] = turn
                    print(succ)
                    succ_list.append(succ)

    
