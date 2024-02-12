from board import Board
import random
import math 
from enum import Enum

class Enemy:
    def __init__(self): 
        pass 

    def make_move(self, board: Board):
        while True: 
            chosen_position = random.randrange(0, 9)
            if not board.is_occupied(chosen_position): 
                board.modify_board(chosen_position, "O")
                break

    # Minimax functions 
    def terminal_state(self, board: Board) -> bool:
        if board.is_full(): 
            return True 
        if board.has_winner() == "X" or board.has_winner() == "O": 
            return True
        return False
    
    def player_turn(self, board: Board) -> str:
        x_count = board.grid.count("X")
        o_count = board.grid.count("O")

        if x_count <= o_count:
            return "X"
        else:
            return "O"

    def get_actions(self, board: Board):
        pass
        
    def get_value(self, board: Board) -> int:
        if board.has_winner() == "X": 
            return -1
        elif board.has_winner() == "O": 
            return 1 
        else: 
            return 0