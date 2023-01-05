#winning condition
WINNING_CONDITION = 5

#indicator of the emptiness of spot
EMPTY = 0

#player identifiers
BLACK_PIECE = 1
WHITE_PIECE = 2

#variables for colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255,200,0)
BLUE = (0, 50, 255)

#variables for making a board.
board_size = 19
board = []

#variables for size of image.
pad = 40
cell_size = 50
piece_size = 40

board_width = cell_size * (board_size - 1) + pad * 2

window_width = board_width + 300
window_height = cell_size * (board_size - 1) + pad * 2

history = []
index = 1
win = False
