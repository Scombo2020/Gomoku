import pygame
from variable import *


class Board(object):
    
    # Will be run once at the beginning of delcaration of the object.
    # Set up attributes for initiating the game and run some necessary functions for getting more attributes for the same purpose.
    def __init__(self, surface):
        self.board = [[0 for i in range(board_size)] for j in range(board_size)]
        self.set_image_font()
        self.surface = surface
        self.pixel_coords = []
        self.set_coords()

    # Will be run at the beginning of the game.
    # Set up attributes 
    def init_game(self):
        self.turn  = BLACK_PIECE
        self.draw_board()
        #self.menu.show_msg(empty)
        #self.init_board()
        self.coords = []
        #self.redos = []
        self.id = 1
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

            # will work as a starting and ending point of a pair of vertical and horizontal line.
            coordinate = pad + i * cell_size 
            
            pygame.draw.line(self.surface, BLACK, (pad, coordinate), (board_width - pad, coordinate), 2)
            pygame.draw.line(self.surface, BLACK, (coordinate, pad), (coordinate, window_height - pad), 2)

    def set_coords(self):
        for y in range(board_size):
            for x in range(board_size):
                self.pixel_coords.append((x * cell_size + 25, y * cell_size + 25))
        #print(self.pixel_coords)

    def get_coord(self, pos):
        for coord in self.pixel_coords:
            x, y = coord
            rect = pygame.Rect(x, y, cell_size, cell_size)
            if rect.collidepoint(pos):
                return coord
        return None

    def check_board(self, pos):
        coord = self.get_coord(pos)
        if not coord:
            return False
        x, y = self.get_point(coord)
        if self.board[y][x] != EMPTY:
            return True

        self.coords.append(coord)
        self.draw_stone(coord, self.turn, 1)
        #if self.check_gameover(coord, 3 - self.turn):
        #    self.is_gameover = True
        #if len(self.redos):
        #    self.redos = []
        return True

    def get_point(self, coord):
        x, y = coord
        x = (x - 25) // cell_size
        y = (y - 25) // cell_size
        return x, y
    
    def draw_stone(self, coord, stone, increase):
        x, y = self.get_point(coord)
        self.board[y][x] = stone
        #self.hide_numbers()
        #if self.is_show:
        #    self.show_numbers()
        self.id += increase
        self.turn = 3 - self.turn

    def check_gameover(self, coord, stone):
        x, y = self.get_point(coord)
        if self.id > board_size * board_size:
            self.show_winner_msg(stone)
            return True
        elif 5 <= self.rule.is_gameover(x, y, stone):
            self.show_winner_msg(stone)
            return True
        return False

    # make this function the one checks validality of the board.
    # Then how does it add the image?
    def check_valid(self, mouse_pos):
        print(mouse_pos)

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

    # adjust this function and connect to add the image
    def draw_dols_order(self, screen, bgn=0, end=len(history)):
        for i in range(bgn, end):
            px = pad + history[i][1] * cell_size - piece_size //2
            py = pad + history[i][0] * cell_size - piece_size //2
            if history[i][2] == BLACK:
                screen.blit(self.img_black_piece, (px,py))
            else:
                screen.blit(self.img_white_piece, (px,py))
        
    def draw_piece(self, screen, valid, i, j):

        if valid:
            print("I came here!")
            coordinate_x = j * cell_size + pad
            coordinate_y = i * cell_size + pad
            screen.blit(self.img_black_piece, (coordinate_x,coordinate_y)) 