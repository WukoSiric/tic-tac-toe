from board import Board
import random

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
    # def terminal_state
    # def player_turn
    # def get_actions
    # def get_Value