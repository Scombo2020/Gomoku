import pygame
from variable import *


class Board(object):
    def __init__(self, surface):
        self.board = [[0 for i in range(board_size)] for j in range(board_size)]
        self.set_image_font()
        self.surface = surface

    def init_game(self):
        #self.turn  = black_stone
        self.draw_board()
        #self.menu.show_msg(empty)
        #self.init_board()
        #self.coords = []
        #self.redos = []
        #self.id = 1
        #self.is_gameover = False

    def set_image_font(self):
        img_background = pygame.image.load("./image/board.png")
        self.img_background = pygame.transform.scale(img_background, (board_width, window_height))
        img_black_piece = pygame.image.load("./image/black.png")
        self.img_black_piece = pygame.transform.scale(img_black_piece, (piece_size,piece_size))
        img_white_piece = pygame.image.load("./image/white.png")
        self.img_white_piece = pygame.transform.scale(img_white_piece, (piece_size,piece_size))

        self.font_piece = pygame.font.SysFont("nanumgothicbold", 35)

    def draw_board(self):
        self.surface.blit(self.img_background, (0,0))
        for i in range(board_size):
            py = pad + i * cell_size
            px = pad + i * cell_size
            #don't understand how this is still black color?
            pygame.draw.line(self.surface, BLACK, (pad, py), (board_width-pad, py), 2)
            pygame.draw.line(self.surface, BLACK, (px, pad), (px, window_height-pad), 2)