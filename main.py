"""
a side project of game omok
omok is a board game of which the player who makes 5 straight lines on the board wins.
reference1 : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=dnpc7848&logNo=221503651970
reference2 : https://github.com/yurokji/omok/tree/main/omok_2players
"""


import pygame
from pygame import QUIT, MOUSEBUTTONUP
from board import Board
from menu import Menu
from variable import *


fps_clock = pygame.time.Clock()

def main():
    pygame.init()
    surface = pygame.display.set_mode((window_width, board_width))
    pygame.display.set_caption("Omok game")

    board = Board(surface)
    menu = Menu(surface)

    while True:
        run_game(surface, board, menu)

def run_game(surface, board, menu):
    board.init_game()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                menu.terminate()
            elif event.type == MOUSEBUTTONUP:
                if not board.check_board(event.pos):
                    if menu.check_rect(event.pos, board):
                        board.init_game()

        #if board.is_gameover:
        #    return

        pygame.display.update()
        fps_clock.tick(60)

if __name__ == '__main__':
    main()