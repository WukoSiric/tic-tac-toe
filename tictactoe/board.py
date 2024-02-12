from array import *

class Board: 
    grid = [" ", " ", " "] * 3
    def __init__(self): 
        pass

    def display_board(self): 
        print(" **** BOARD ****")
        print()
        for i in range(0, 9, 3):
            print("     " + self.display_slot(self.grid[i]) + "  " + self.display_slot(self.grid[i+1]) + "  " + self.display_slot(self.grid[i+2]))
        print()

    def display_slot(self, grid_position: str) -> str: 
        if grid_position == " ": 
            return "—" 
        return grid_position

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
        # check rows
        for i in range(0, 9, 3):
            if self.grid[i] == " ": 
                continue
            if self.grid[i] == self.grid[i+1] == self.grid[i+1+1]: 
                return self.grid[i]

        # check columns
        for i in range(3):
            if self.grid[i] == " ": 
                continue
            if self.grid[i] == self.grid[i+3] == self.grid[i+3+3]: 
                return self.grid[i]
            
        # check diagonal 
        if self.grid[0] != " " and self.grid[0] == self.grid[4] == self.grid[8]: 
            return self.grid[0]

        return None
    
    def is_full(self) -> bool:
        for i in range(9): 
            if self.grid[i] == " ": 
                return False
        return True