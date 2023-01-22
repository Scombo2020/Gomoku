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

    def heuristic_game_value(self, state):

        #Only proceed if it is not a terminal state.
        if self.game_value(state) == 0:
            my_best_score = 0
            opp_best_score = 0
            for row in range(5):
                for col in range(5):
                    if state[row][col] == self.my_piece:

                        my_score = 0
                        for y in range(2):
                            for x in range(2):
                                if row + y < 5 and col + x < 5 and state[row + y][col + x] == self.my_piece:
                                    my_score += 0.25
                        if my_score > my_best_score:
                            my_best_score = my_score
                        
                        my_score = 0
                        counter = 0
                        while col + counter < 5 and state[row][col + counter] == self.my_piece:
                            my_score += 0.25
                            counter += 1
                        if my_score > my_best_score:
                            my_best_score = my_score


                        my_score = 0
                        counter = 0
                        while row + counter < 5 and state[row + counter][col] == self.my_piece:
                            my_score += 0.25
                            counter += 1
                        if my_score > my_best_score:
                            my_best_score = my_score

                        my_score = 0
                        counter = 0
                        while row + counter < 5 and col + counter < 5 and state[row + counter][col + counter] == self.my_piece:
                            my_score += 0.25
                            counter += 1
                        if my_score > my_best_score:
                            my_best_score = my_score

                        my_score = 0
                        counter = 0
                        while row - counter > -1 and col + counter < 5 and state[row - counter][col + counter] == self.my_piece:
                            my_score += 0.25
                            counter += 1
                        if my_score > my_best_score:
                            my_best_score = my_score

                    elif state[row][col] == self.opp:

                        opp_score = 0
                        counter = 0
                        while col + counter < 5 and state[row][col + counter] == self.opp:
                            opp_score -= 0.25
                            counter += 1
                        if opp_score < opp_best_score:
                            opp_best_score = opp_score


                        opp_score = 0
                        counter = 0
                        while row + counter < 5 and state[row + counter][col] == self.opp:
                            opp_score -= 0.25
                            counter += 1
                        if opp_score < opp_best_score:
                            opp_best_score = opp_score

                        opp_score = 0
                        counter = 0
                        while row + counter < 5 and col + counter < 5 and state[row + counter][col + counter] == self.opp:
                            opp_score -= 0.25
                            counter += 1
                        if opp_score < opp_best_score:
                            opp_best_score = opp_score

                        opp_score = 0
                        counter = 0
                        while row - counter > -1 and col + counter < 5 and state[row - counter][col + counter] == self.opp:
                            opp_score -= 0.25
                            counter += 1
                        if opp_score < opp_best_score:
                            opp_best_score = opp_score

            return my_best_score + opp_best_score
        else:
            return self.game_value(state)
