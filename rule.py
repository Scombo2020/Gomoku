import pygame
from variable import *

#rule = Rule(self.board)

class Rule(object):

    # get board and the coordinate of last piece
    # is this board a reference, meaning that it will keep the latest version of board?
    # yes, 
    def __init__(self, board, recent_piece, turn):
        self.board = board
        self.recent_piece = recent_piece
        self.turn = turn

    def checkHorizontalOmok(self):
        count = 0
        for j in range(self.recent_piece[1], -1, -1):
            if j < 0:
                break
            if self.board[self.recent_piece[0]][j] == self.turn:
                count += 1
                if count == WINNING_CONDITION:
                    return True
            else:
                break
        for j in range(self.recent_piece[1]+1, self.recent_piece[1] + 1 + WINNING_CONDITION - count):
            if j > board_size - 1:
                break
            if self.board[self.recent_piece[0]][j] == self.turn:
                count += 1
                if count == WINNING_CONDITION:
                    return True
            else:
                break
        return False

    def checkVerticalOmok(self):
        count = 0
        for i in range(self.recent_piece[0], -1, -1):
            if i < 0:
                break
            if self.board[i][self.recent_piece[1]] == self.turn:
                count += 1
                if count == WINNING_CONDITION:
                    return True
            else:
                break
        for i in range(self.recent_piece[0] + 1, self.recent_piece[0] + 1 + WINNING_CONDITION - count):
            if i > board_size - 1:
                break
            if self.board[i][self.recent_piece[1]] == self.turn:
                count += 1
                if count == WINNING_CONDITION:
                    return True
            else:
                break
        return False

    def checkFirstDiagOmok(self):
        count = 0
        for d in range(0, WINNING_CONDITION):
            if self.recent_piece[0] - d < 0 or self.recent_piece[1] + d > board_size - 1:
                break
            if self.board[self.recent_piece[0] - d][self.recent_piece[1] + d] == self.turn:
                count += 1
                if count == WINNING_CONDITION:
                    return True
            else:
                break
        for d in range(1, WINNING_CONDITION):
            if self.recent_piece[0] + d > board_size - 1 or self.recent_piece[1] - d < 0:
                break
            if self.board[self.recent_piece[0] + d][self.recent_piece[1] - d] == self.turn:
                count += 1
                if count == WINNING_CONDITION:
                    return True
            else:
                break
        return False

    def checkSecondDiagOmok(self):
        count = 0
        for d in range(0, WINNING_CONDITION):
            if self.recent_piece[0] - d < 0 or self.recent_piece[1] - d < 0:
                break
            if self.board[self.recent_piece[0] - d][self.recent_piece[1] - d] == self.turn:
                count += 1
                if count == WINNING_CONDITION:
                    return True
            else:
                break
        for d in range(1, WINNING_CONDITION):
            if self.recent_piece[0] + d > board_size - 1 or self.recent_piece[1] + d > board_size - 1:
                break
            if self.board[self.recent_piece[0] + d][self.recent_piece[1] + d] == self.turn:
                count += 1
                if count == WINNING_CONDITION:
                    return True
            else:
                break
        return False
    
    def checkOmok(self):
        #print(self.recent_piece)
        if self.checkHorizontalOmok():
            return True
        elif self.checkVerticalOmok():
            return True
        elif self.checkFirstDiagOmok():
            return True
        elif self.checkSecondDiagOmok():
            return True
        else:
            return False