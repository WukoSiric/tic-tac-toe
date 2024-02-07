from array import *

class Board: 
    grid = [[" "] * 3]
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
        
        row = int(position / 3)
        col = int(position % 3)
        self.grid[row][col] = player_id
        return "Succesfully modified"
    
    def reset_board(self): 
        for i in range(3): 
            for j in range(3): 
                self.grid[i][j] = " "