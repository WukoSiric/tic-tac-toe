from array import *

class Board: 
    grid = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    def __init__(self): 
        pass

    def modify_board(self, position, player_id):
        if not position.is_integer():
            return "Error: Not an integer"
        if position > 10 or position < 0: 
            return "Error: Invalid position"
        if player_id == int(1) or player_id == int(2):
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
                self.grid[i][j] = int(0)

def main(): 
    board = Board() 
    print(board.modify_board(6, 1))
    print(board.grid)
    board.reset_board() 
    print(board.grid)

if __name__ == "__main__": 
    main()