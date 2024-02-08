from array import *

class Board: 
    grid = [" ", " ", " "] * 3
    def __init__(self): 
        pass

    def modify_board(self, position, player_id):
        if not position.is_integer():
            return "Error: Not an integer"
        if position > 10 or position < 0: 
            return "Error: Invalid position"
        if player_id == "X" or player_id == "O":
            pass
        else:
            return "Error: Wrong player_id"
        
        self.grid[position] = player_id
        return "Succesfully modified"

    def reset_board(self):
        for i in range(9): 
            self.grid[i] = " "

    def is_occupied(self, position) -> bool: 
        if self.grid[position] == " ":
            return False
        return True
    
    def has_winner(self) -> (str): 
        #   0  1  2
        # 0 [] [] []
        # 1 [] [] []
        # 2 [] [] []

        # check rows
        for i in range(0, 9, 3):
            if self.grid[i] == " ": 
                continue
            if self.grid[i] == self.grid[i+1] == self.grid[i+1]: 
                return self.grid[i]

        # check columns
        for i in range(3):
            if self.grid[i] == " ": 
                continue
            if self.grid[i] == self.grid[i+3] == self.grid[i+3+3]: 
                return self.grid[i]
            
        # check diagonal 
        if self.grid[0] == self.grid[4] == self.grid[8]: 
            return self.grid[0]

        return None