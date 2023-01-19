"""
a side project of game omok
omok is a board game of which the player who first makes 5 straight lines on the board wins.
reference1 : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=dnpc7848&logNo=221503651970
reference2 : https://github.com/yurokji/omok/tree/main/omok_2players 
reference1 for the structure of gram (board, menu)
reference2 for the algorithm of detecting the winning status
"""


import pygame
from pygame import QUIT, MOUSEBUTTONUP
from board import Board
from menu import Menu
from variable import *


def main():
    
    #basic setup of the program.
    pygame.init()
    surface = pygame.display.set_mode((window_width, board_width))
    pygame.display.set_caption("Omok game")

    #generate instances for the game.
    board = Board(surface)
    menu = Menu(surface)

    #keep running it until the window is closed.
    while True:
        run_game(surface, board, menu)

def run_game(surface, board, menu):
    
    #start the game for the first time.
    board.init_game()

    #keep checking events.
    while True:
        for event in pygame.event.get():
            
            #if a player closes the window or clicks "Quit Game", end the game.
            if event.type == QUIT:
                menu.terminate()
            
            elif event.type == MOUSEBUTTONUP:
                #if the player makes proper move on the board, a piece will be generated. 
                if not board.check_valid(event.pos):
                    #if the player clicks out of the board, check if it's in the menu and if so, work as clicked.
                    menu.check_rect(event.pos, board)

        #when either of players wins, shows the winning message.
        #it doesn't close the game!
        if board.is_gameover:
            menu.winning_message(board.turn)

        #should be placed here for the first game initialization.
        pygame.display.update()

if __name__ == '__main__':
    main()
