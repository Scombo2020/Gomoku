import pygame, sys
from variable import *

#a class of managing what happens on the menu.
class Menu(object):
    
    # setup necessary attributes.
    def __init__(self, surface):
        self.font = pygame.font.SysFont("nanumgothicbold", 30)
        self.surface = surface
        self.draw_menu()

    # draw a menu on the board.
    def draw_menu(self):
        top, left = window_height - 30, window_width - 200
        self.new_rect = self.make_text(self.font, 'New Game', BLUE, None, top - 30, left)
        self.quit_rect = self.make_text(self.font, 'Quit Game', BLUE, None, top, left)
        #will be implemented in the future.
        #self.show_rect = self.make_text(self.font, 'Hide Number', BLUE, None, top - 60, left)
        #self.undo_rect = self.make_text(self.font, 'Undo', BLUE, None, top - 150, left)
        #self.uall_rect = self.make_text(self.font, 'Undo All', BLUE, None, top - 120, left)
        #self.redo_rect = self.make_text(self.font, 'Redo', BLUE, None, top - 90, left)

    # draw a text on the window.
    # may need to modify in the future; it's quite inconvinient.
    def make_text(self, font, text, color, bgcolor, top, left, position = 0):
        surf = font.render(text, False, color, bgcolor)
        rect = surf.get_rect()
        if position:
            rect.center = (left, top)
        else:    
            rect.topleft = (left, top)
        self.surface.blit(surf, rect)
        return rect

    # quit the game by closing the window.
    def terminate(self):
        pygame.quit()
        sys.exit()
    
    # generate a winning message on the window.
    def winning_message(self, turn):
        if turn == 1:
            winning_message = "Black Wins!"
        else:
            winning_message = "White Wins!"
        
        self.make_text(self.font, winning_message, BLUE, None, window_height -500, window_width - 200)


    # remove the winning message by covering it with the background color.
    def remove_winning_message(self):
        self.surface.fill(BLACK, (window_width - 200, window_height - 500, 200, 30))
    
    
    #show_hide, undo, undo_all, redo need to be implemented later.
    #make options for AI mode and choosing the color of piece.
    def check_rect(self, pos, board):
        if self.new_rect.collidepoint(pos):
            board.init_game()
            self.remove_winning_message()
        #elif self.show_rect.collidepoint(pos):
        #    self.show_hide(board)
        #elif self.undo_rect.collidepoint(pos):
        #    board.undo()
        #elif self.uall_rect.collidepoint(pos):
        #    board.undo_all()
        #elif self.redo_rect.collidepoint(pos):
        #    board.redo()
        elif self.quit_rect.collidepoint(pos):
            self.terminate()
        
