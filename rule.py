import pygame
from variable import *

#rule = Rule(self.board)

class Rule(object):

    # get board and the coordinate of last piece
    # is this board a reference, meaning that it will keep the latest version of board?
    # yes, 
    def __init__(self, board, recent_piece_coordinate):
        self.board = board
        self.recent_piece_coordinate = recent_piece_coordinate

    def checkHorizontalOmok(self, new_i, new_j, bturn):
        count = 0
        for j in range(new_j, -1, -1):
            if j < 0:
                break
            if self.board[new_i][j] == (BLACK if bturn else WHITE):
                count += 1
                if count == WINNING_CONDITION:
                    return True
            else:
                break
        for j in range(new_j+1, new_j + 1 + WINNING_CONDITION - count):
            if j > board_width - 1:
                break
            if self.board[new_i][j] == (BLACK if bturn else WHITE):
                count += 1
                if count == WINNING_CONDITION:
                    return True
            else:
                break
        return False