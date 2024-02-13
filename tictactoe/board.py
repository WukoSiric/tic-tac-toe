from array import *

class Board: 
    grid = [" ", " ", " "] * 3
    def __init__(self): 
        pass

    def modify_board(self, position, player_id):
        if not position.is_integer():
            raise TypeError
        if position > 9 or position < 0: 
            raise IndexError
        if player_id != "X" and player_id != "O":
            raise TypeError
        
        self.grid[position] = player_id

    def reset_board(self):  
        for i in range(9): 
            self.grid[i] = " "

    def is_occupied(self, position) -> bool: 
        if self.grid[position] == " ":
            return False
        return True
    
    def has_winner(self) -> str:
        # Check rows and columns
        for i in range(3):
            if self.grid[i] != " " and self.grid[i] == self.grid[i+3] == self.grid[i+3+3]:
                return self.grid[i]  # Check columns

            if self.grid[i*3] != " " and self.grid[i*3] == self.grid[i*3+1] == self.grid[i*3+2]:
                return self.grid[i*3]  # Check rows

        # Check diagonal
        if self.grid[0] != " " and self.grid[0] == self.grid[4] == self.grid[8]:
            return self.grid[0]

        return None

    
    def is_full(self) -> bool:
        for i in range(9): 
            if self.grid[i] == " ": 
                return False
        return True