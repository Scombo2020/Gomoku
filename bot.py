from variable import *
import copy
import numpy as np

class Bot(object):
    
    def __init__(self, board, recent_piece):
        self.board = np.array(board)
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

        return succ_list, turn

    # need to define which data to receive as a parameter.
    # maybe succ list?
    # then, think about how to determine the heuristic.
    # don't care about complicated rule for now.
    # return value and TF from rules, and simply make use of it!
    def heuristic_game_value(self, succ_list, turn):

        my_best_score = 0
        opp_best_score = 0

        for succ in succ_list:
            for row in range(board_size):
                for col in range(board_size):
                    if succ[row][col] == turn: 
                        pass
                        
                    