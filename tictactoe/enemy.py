from board import Board
import random
import copy
import math 

class Enemy:
    def __init__(self): 
        self.best_move = None
        pass 

    def make_random_move(self, board: Board) -> None:
        while True: 
            chosen_position = random.randrange(0, 9)
            if not board.is_occupied(chosen_position): 
                board.modify_board(chosen_position, "O")
                break
    
    def make_move_minimax(self, board: Board) -> None: 
        result = self.minimax(board) 
        if board.grid == ["X", " ", " ", " ", " ", " ", " ", " ", " "]:
            board.modify_board(4, "O") 
            return
        board.modify_board(self.best_move, "O") 

    # Minimax functions 
    def minimax(self, board: Board) -> int:
        if self.is_terminal_state(board):
            return self.get_value(board)
        
        if self.get_player_turn(board) == "O": #max player 
            value = -math.inf 
            possible_boards = self.get_possible_boards(board, "O") 
            for possible_board in possible_boards: 
                current_value = self.minimax(possible_board)
                if current_value > value: 
                    value = current_value
                    self.best_move = self.find_difference(board, possible_board)
            return value
        
        if self.get_player_turn(board) == "X": #min player
            value = math.inf
            possible_boards = self.get_possible_boards(board, "X") 
            for possible_board in possible_boards:
                current_value = min(value, self.minimax(possible_board))
                if current_value < value: 
                    value = current_value
            return value

    def is_terminal_state(self, board: Board) -> bool:
        if board.is_full(): 
            return True 
        if board.has_winner() == "X" or board.has_winner() == "O": 
            return True
        return False
    
    def get_player_turn(self, board: Board) -> str:
        x_count = board.grid.count("X")
        o_count = board.grid.count("O")

        if x_count <= o_count:
            return "X"
        else:
            return "O"

    def get_possible_boards(self, board: Board, player: str) -> list[Board]:
        possible_boards = [] 
        for i in range(9): 
            if board.is_occupied(i): 
                continue
            new_board = Board() 
            new_board.grid = copy.copy(board.grid)
            new_board.modify_board(i, player)
            possible_boards.append(new_board)
        return possible_boards
        
    def get_value(self, board: Board) -> int:
        if board.has_winner() == "X": 
            return -1
        elif board.has_winner() == "O": 
            return 1 
        elif board.is_full(): 
            return 0
        else: 
            return 0
        
    def find_difference(self, board: Board, board2: Board) -> int: 
        for i in range(9): 
            if board.grid[i] != board2.grid[i]: 
                return i
