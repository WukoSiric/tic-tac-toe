from board import Board

class Player: 
    move = "X"
    def __init__(self): 
        pass

    def make_move(self, board: Board) -> None: 
        print("Make your move: ")
        
        while True: 
            position = int(input())
            if board.is_occupied(position):
                print("Position is occupied")
                continue 
            board.modify_board(position, "X")
            return