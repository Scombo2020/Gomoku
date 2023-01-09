import pygame
from variable import *

#rule = Rule(self.board)

class Rule(object):

    # get board and the coordinate of last piece
    # is this board a reference, meaning that it will keep the latest version of board?
    def __init__(self, board):
        self.board = board