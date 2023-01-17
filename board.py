import pygame
from rule import Rule
from variable import *


class Board(object):
    
    # Will be run once at the beginning of delcaration of the object.
    # Set up attributes for initiating the game and run some necessary functions for getting more attributes for the same purpose.
    def __init__(self, surface):
        self.set_image_font()
        self.surface = surface

    # Will be run at the beginning of the game.
    # Set up attributes 
    def init_game(self):
        self.board = [[0 for i in range(board_size)] for j in range(board_size)]
        self.recent_piece_coordinate = [-1, -1]
        self.turn  = BLACK_PIECE
        self.history = []
        self.rule = Rule(self.board, self.recent_piece_coordinate)
        self.draw_board()
        self.is_gameover = False
        #self.menu.show_msg(empty)
        #self.init_board()
        #self.redos = []

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

            # will work as a starting and ending point of a pair of vertical and horizontal line.
            coordinate = pad + i * cell_size 
            
            pygame.draw.line(self.surface, BLACK, (pad, coordinate), (board_width - pad, coordinate), 2)
            pygame.draw.line(self.surface, BLACK, (coordinate, pad), (coordinate, window_height - pad), 2)


    def check_valid(self, mouse_pos):
        # if clicked out of the board, return False 
        if not pygame.Rect(0, 0, board_width, window_height).collidepoint(mouse_pos):
            print("not on the board")
            return False, -1, -1

        input_without_pad_y = mouse_pos[1] - pad # will work as i (vertical index) of the matrix
        input_without_pad_x = mouse_pos[0] - pad # will work as j (horizontal index) of the matrix
    
        input_index_y = input_without_pad_y / cell_size # get i_index
        input_index_x = input_without_pad_x / cell_size # get j_index

        input_y_rounded = round(input_index_y) 
        input_x_rounded = round(input_index_x)
        
        # prevent vague clicks 
        if abs(input_index_y - input_y_rounded) < 0.2 and abs(input_index_x - input_x_rounded) < 0.2:
            print(input_y_rounded, input_x_rounded)
            #need to call drawing function?
            #return True, int(input_y_rounded), int(input_x_rounded)
            return self.draw_piece(self.surface, True, int(input_y_rounded), int(input_x_rounded))
        else:
            print("return -1")
            return False, -1, -1
        
    
    def draw_piece(self, screen, valid, i, j):

        if valid:
            
            if self.turn == BLACK_PIECE:
                coordinate_x = j * cell_size + pad - 15
                coordinate_y = i * cell_size + pad - 15
                screen.blit(self.img_black_piece, (coordinate_x,coordinate_y))
            else:
                coordinate_x = j * cell_size + pad - 15
                coordinate_y = i * cell_size + pad - 15
                screen.blit(self.img_white_piece, (coordinate_x,coordinate_y))
            
            # add history, update board and recent piece, and change turn
            self.history.append([i, j])
            
            # try to change turn by some other values from 1 and 2 that's mutable?
            self.board[i][j] = self.turn
            self.recent_piece_coordinate[0] = i
            self.recent_piece_coordinate[1] = j
            
            # check if the most recent piece ends the game.
            if self.rule.checkOmok(self.turn) == True:
                self.is_gameover = True
            else:
                self.turn = 3 - self.turn 

        # need to adjust with main.py in the future.
        # set this up to prevent going to next if for now.
        return True