from board import Board
import os

def clear_screen(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def display_board(board: Board): 
    print(" **** BOARD ****")
    print()
    for i in range(0, 9, 3):
        print("     " + board.display_slot(board.grid[i]) + "  " + board.display_slot(board.grid[i+1]) + "  " + board.display_slot(board.grid[i+2]))
    print()

def display_slot(grid_position: str) -> str: 
    if grid_position == " ": 
        return "—" 
    return grid_position