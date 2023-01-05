import pygame
from pygame import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP

#winning condition
WINNING_CONDITION = 5

#indicator of the emptiness of spot
EMPTY = 0

#player identifiers
BLACK = 1
WHITE = 2

#variables for colors
RED = (255, 0, 0)
#WHITE = (255, 255, 255)
#BLACK = (0, 0, 0)
YELLOW = (255,200,0)

#variables for making a board.
board_width, board_height = 19, 19
board = []

#variables for size of image.
pad = 40
cell_size = 50
piece_size = 40
w = cell_size * (board_width - 1) + pad * 2
h = cell_size * (board_height - 1) + pad * 2


history = []
index = 1
win = False

img_bg = pygame.image.load("./image/board.png")
img_bg = pygame.transform.scale(img_bg, (w,h))
img_go_black = pygame.image.load("./image/black.png")
img_go_black = pygame.transform.scale(img_go_black, (piece_size,piece_size))
img_go_white = pygame.image.load("./image/white.png")
img_go_white = pygame.transform.scale(img_go_white, (piece_size,piece_size))

pygame.font.init()
font_size = 80
font_size_piece = 35
myfont = pygame.font.SysFont("nanumgothicbold", font_size)
myfont_piece = pygame.font.SysFont("nanumgothicbold", font_size_piece)


#fill the board with 19 * 19
for i in range(board_height):
    row = []
    for j in range(board_width):
        row.append(EMPTY)
    board.append(row)


#print current board
def printBoard():
    for row in board:
        print(row)
    print()

def printHistory():
    for record in history:
        print(record)

#draw lines on the board
def draw_board(screen):
    screen.blit(img_bg, (0,0))
    for i in range(board_height):
        py = pad + i * cell_size
        px = pad + i * cell_size
        #don't understand how this is still black color?
        pygame.draw.line(screen, BLACK, (pad, py), (w-pad, py), 2)
        pygame.draw.line(screen, BLACK, (px, pad), (px, h-pad), 2)


def draw_dols_order(screen, bgn=0, end=len(history)):
    for i in range(bgn, end):
        px = pad + history[i][1] * cell_size - piece_size //2
        py = pad + history[i][0] * cell_size - piece_size //2
        if history[i][2] == BLACK:
            screen.blit(img_go_black, (px,py))
            #text_surface = myfont.render(str(len(dols_order)), False, (255, 0, 0))
            #screen.blit(myfont_piece.render(str(len(history)), False, (255, 0, 0)), (px + 15,py + 10))
        else:
            screen.blit(img_go_white, (px,py))
            #text_surface = myfont.render(str(len(dols_order)), False, (255, 0, 0))
            #screen.blit(myfont_piece.render(str(len(history)), False, (255, 0, 0)), (px + 15,py + 10))

def draw_order(screen, new_i, new_j):
    px = pad + new_i * cell_size - piece_size //2
    py = pad + new_j * cell_size - piece_size //2
    #if history[i][2] == BLACK:
    #    screen.blit(myfont_piece.render(str(len(history)), False, (255, 0, 0)), (px + 15,py + 10))
    #else:
    screen.blit(myfont_piece.render(str(len(history)), False, (255, 0, 0)), (px + 15,py + 10))
    


#check if the click was valid in the board
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

#check if horizontal straight of 5 pieces is made.
def checkHorizontalOmok(new_i, new_j, bturn):
    count = 0
    for j in range(new_j, -1, -1):
        if j < 0:
            break
        if board[new_i][j] == (BLACK if bturn else WHITE):
            count += 1
            if count == WINNING_CONDITION:
                return True
        else:
            break
    for j in range(new_j+1, new_j + 1 + WINNING_CONDITION - count):
        if j > board_width - 1:
            break
        if board[new_i][j] == (BLACK if bturn else WHITE):
            count += 1
            if count == WINNING_CONDITION:
                return True
        else:
            break
    return False

#check if vertical straight of 5 pieces is made.
def checkVerticalOmok(new_i, new_j, bturn):
    count = 0
    for i in range(new_i, -1, -1):
        if i < 0:
            break
        if board[i][new_j] == (BLACK if bturn else WHITE):
            count += 1
            if count == WINNING_CONDITION:
                return True
        else:
            break
    for i in range(new_i + 1, new_i + 1 + WINNING_CONDITION - count):
        if i > board_height - 1:
            break
        if board[i][new_j] == (BLACK if bturn else WHITE):
            count += 1
            if count == WINNING_CONDITION:
                return True
        else:
            break
    return False

#check if diagonal straight of 5 pieces is made.
def checkFirstDiagOmok(new_i, new_j, bturn):
    count = 0
    for d in range(0, WINNING_CONDITION):
        if new_i - d < 0 or new_j + d > board_width - 1:
            break
        if board[new_i - d][new_j + d] == (BLACK if bturn else WHITE):
            count += 1
            if count == WINNING_CONDITION:
                return True
        else:
            break
    for d in range(1, WINNING_CONDITION):
        if new_i + d > board_height - 1 or new_j - d < 0:
            break
        if board[new_i + d][new_j - d] == (BLACK if bturn else WHITE):
            count += 1
            if count == WINNING_CONDITION:
                return True
        else:
            break
    return False

#check if diagonal straight of 5 pieces is made.
def checkSecondDiagOmok(new_i, new_j, bturn):
    count = 0
    for d in range(0, WINNING_CONDITION):
        if new_i - d < 0 or new_j - d < 0:
            break
        if board[new_i - d][new_j - d] == (BLACK if bturn else WHITE):
            count += 1
            if count == WINNING_CONDITION:
                return True
        else:
            break
    for d in range(1, WINNING_CONDITION):
        if new_i + d > board_height - 1 or new_j + d > board_height - 1 :
            break
        if board[new_i + d][new_j + d] == (BLACK if bturn else WHITE):
            count += 1
            if count == WINNING_CONDITION:
                return True
        else:
            break
    return False

#if any kind of straight 5 pieces is made, it wins.
def checkOmok(new_i, new_j, bturn):
    if checkHorizontalOmok(new_i, new_j, bturn):
        return True
    elif checkVerticalOmok(new_i, new_j, bturn):
        return True
    if checkFirstDiagOmok(new_i, new_j, bturn):
        return True
    elif checkSecondDiagOmok(new_i, new_j, bturn):
        return True
    else:
        return False

def main():
    
    #initial settings of the game
    pygame.init()
    SURFACE = pygame.display.set_mode((w,h))
    clock = pygame.time.Clock()
    
    black_turn = True
    playing = True
    is_down = False
    is_valid = False
    new_pos = (0,0)
    i_new = -1
    j_new = -1

    while playing:
        for e in pygame.event.get():
            if e.type == QUIT:
                running = False
            elif e.type == MOUSEBUTTONDOWN:
                is_down = True
            elif e.type == MOUSEBUTTONUP:
                if is_down:
                    is_valid, i_new, j_new = checkValid(pygame.mouse.get_pos())
                    if is_valid:
                        is_down = False
                        if board[i_new][j_new] == EMPTY:
                            board[i_new][j_new] = BLACK if black_turn else WHITE
                            history.append((i_new, j_new, board[i_new][j_new]))
                            printBoard()
                            printHistory()
                            if checkOmok(i_new,j_new, black_turn):
                                playing = False
                                win = BLACK if black_turn else WHITE
                            black_turn = not black_turn
        SURFACE.fill(YELLOW)
        draw_board(SURFACE)
        draw_dols_order(SURFACE, 0, len(history))
        if (i_new != -1 and j_new != -1):
            draw_order(SURFACE, i_new, j_new)
            print("common...")
        pygame.display.update()
        clock.tick(30)

    if win:
        win_text = "Black" if win == BLACK else "White"
        win_text += " Wins!"
        text_surface = myfont.render(win_text, False, (0, 0, 255))
        SURFACE.blit(text_surface, (w//2 - 200, h//2-font_size))
        pygame.display.update()
        for i in range(6):
            clock.tick(1)



    pygame.quit()

if __name__ == '__main__':
    main()