from board import Board
from player import Player

board = Board() 
player = Player()

print("Setting up board!")

board.modify_board(2, "X")
board.modify_board(1, "X")
board.modify_board(0, "O")
print(board.grid)
print(board.has_winner())
board.reset_board() 
print(board.grid)