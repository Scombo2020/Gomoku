import pygame
from variable import *


class Board(object):
    def __init__(self, surface):
        self.board = [[0 for i in range(board_size)] for j in range(board_size)]
        self.set_image_font()
        self.surface = surface
        self.pixel_coords = []
        self.set_coords()

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
            py = pad + i * cell_size
            px = pad + i * cell_size
            #don't understand how this is still black color?
            pygame.draw.line(self.surface, BLACK, (pad, py), (board_width-pad, py), 2)
            pygame.draw.line(self.surface, BLACK, (px, pad), (px, window_height-pad), 2)

    def set_coords(self):
        for y in range(board_size):
            for x in range(board_size):
                self.pixel_coords.append((x * cell_size + 25, y * cell_size + 25))
        print(self.pixel_coords)

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
    def checkValid(mouse_pos):
        mx = mouse_pos[0] - pad
        my = mouse_pos[1] - pad
    
        i_m = my / cell_size
        j_m = mx / cell_size

        i_ref = round(i_m)
        j_ref = round(j_m)
        if abs(i_m-i_ref) < 0.18 and abs(j_m-j_ref) < 0.18:
            return True, int(i_ref), int(j_ref)
        else:
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
        