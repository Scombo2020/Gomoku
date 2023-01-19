import pygame
from variable import *

#a class checking if the game is done.
class Rule(object):

    # get board and the coordinate of last piece
    # board and recent piece will be copied by reference, so they only need to be declared here once.
    # however, since the turn is int, which is copied by value, need to get it as a parameter everytime.
    def __init__(self, board, recent_piece):
        self.board = board
        self.recent_piece = recent_piece

    # check how many pieces are aligned horizontally.
    def checkHorizontalOmok(self, turn):
        count = 0
        for j in range(self.recent_piece[1], -1, -1):
            if j < 0:
                break
            if self.board[self.recent_piece[0]][j] == turn:
                count += 1
                if count == WINNING_CONDITION:
                    return True
            else:
                break
        for j in range(self.recent_piece[1]+1, self.recent_piece[1] + 1 + WINNING_CONDITION - count):
            if j > board_size - 1:
                break
            if self.board[self.recent_piece[0]][j] == turn:
                count += 1
                if count == WINNING_CONDITION:
                    return True
            else:
                break
        return False

    # check how many pieces are aligned vertically.
    def checkVerticalOmok(self, turn):
        count = 0
        for i in range(self.recent_piece[0], -1, -1):
            if i < 0:
                break
            if self.board[i][self.recent_piece[1]] == turn:
                count += 1
                if count == WINNING_CONDITION:
                    return True
            else:
                break
        for i in range(self.recent_piece[0] + 1, self.recent_piece[0] + 1 + WINNING_CONDITION - count):
            if i > board_size - 1:
                break
            if self.board[i][self.recent_piece[1]] == turn:
                count += 1
                if count == WINNING_CONDITION:
                    return True
            else:
                break
        return False

    # check how many pieces are aligned diagnolly.
    # check with direction of  y = -x.
    def checkFirstDiagOmok(self, turn):
        count = 0
        for d in range(0, WINNING_CONDITION):
            if self.recent_piece[0] - d < 0 or self.recent_piece[1] + d > board_size - 1:
                break
            if self.board[self.recent_piece[0] - d][self.recent_piece[1] + d] == turn:
                count += 1
                if count == WINNING_CONDITION:
                    return True
            else:
                break
        for d in range(1, WINNING_CONDITION):
            if self.recent_piece[0] + d > board_size - 1 or self.recent_piece[1] - d < 0:
                break
            if self.board[self.recent_piece[0] + d][self.recent_piece[1] - d] == turn:
                count += 1
                if count == WINNING_CONDITION:
                    return True
            else:
                break
        return False

    # check how many pieces are aligned diagnolly.
    # check with directoin of  y = x
    def checkSecondDiagOmok(self, turn):
        count = 0
        for d in range(0, WINNING_CONDITION):
            if self.recent_piece[0] - d < 0 or self.recent_piece[1] - d < 0:
                break
            if self.board[self.recent_piece[0] - d][self.recent_piece[1] - d] == turn:
                count += 1
                if count == WINNING_CONDITION:
                    return True
            else:
                break
        for d in range(1, WINNING_CONDITION):
            if self.recent_piece[0] + d > board_size - 1 or self.recent_piece[1] + d > board_size - 1:
                break
            if self.board[self.recent_piece[0] + d][self.recent_piece[1] + d] == turn:
                count += 1
                if count == WINNING_CONDITION:
                    return True
            else:
                break
        return False
    
    # don't need to get parameter from the rule attribute.
    # by getting turn value each time from the board attribute, could avoid the case of change of turn value not reflected.
    def checkOmok(self, turn):
        if self.checkHorizontalOmok(turn):
            return True
        elif self.checkVerticalOmok(turn):
            return True
        elif self.checkFirstDiagOmok(turn):
            return True
        elif self.checkSecondDiagOmok(turn):
            return True
        else:
            return False