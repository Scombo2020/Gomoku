import pygame, sys
from variable import *

class Menu(object):
    def __init__(self, surface):
        self.font = pygame.font.SysFont("nanumgothicbold", 30)
        self.surface = surface
        self.draw_menu()

    def draw_menu(self):
        top, left = window_height - 30, window_width - 200
        self.new_rect = self.make_text(self.font, 'New Game', BLUE, None, top - 30, left)
        self.quit_rect = self.make_text(self.font, 'Quit Game', BLUE, None, top, left)
        self.show_rect = self.make_text(self.font, 'Hide Number', BLUE, None, top - 60, left)
        self.undo_rect = self.make_text(self.font, 'Undo', BLUE, None, top - 150, left)
        self.uall_rect = self.make_text(self.font, 'Undo All', BLUE, None, top - 120, left)
        self.redo_rect = self.make_text(self.font, 'Redo', BLUE, None, top - 90, left)

    def make_text(self, font, text, color, bgcolor, top, left, position = 0):
        surf = font.render(text, False, color, bgcolor)
        rect = surf.get_rect()
        if position:
            rect.center = (left, top)
        else:    
            rect.topleft = (left, top)
        self.surface.blit(surf, rect)
        return rect

    def terminate(self):
        pygame.quit()
        sys.exit()
    
    # need to remove the message after new game is started
    def winning_message(self, turn):
        if turn == 1:
            winning_message = "Black Wins!"
        else:
            winning_message = "White Wins!"
        
        self.make_text(self.font, winning_message, BLUE, None, window_height -500, window_width - 200)


    def remove_winning_message(self):
        print("I got you here")
        #self.make_text(self.font, "            ", BLACK, None, window_height -500, window_width - 200)

        
        #self.surface.fill(BLACK, rect = None)
        #(left, top, width, height)
        self.surface.fill(BLACK, (window_width - 200, window_height - 500, 200, 30))
    
    def check_rect(self, pos, omok):
        if self.new_rect.collidepoint(pos):
            return True
        elif self.show_rect.collidepoint(pos):
            self.show_hide(omok)
        elif self.undo_rect.collidepoint(pos):
            omok.undo()
        elif self.uall_rect.collidepoint(pos):
            omok.undo_all()
        elif self.redo_rect.collidepoint(pos):
            omok.redo()
        elif self.quit_rect.collidepoint(pos):
            self.terminate()
        return False
        
