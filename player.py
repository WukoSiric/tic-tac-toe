from board import Board

class Player: 
    move = "X"
    def __init__(self): 
        pass

    def make_move(self, position: int, board: Board) -> None: 
        print("Make your move: ")
        position = int(input())

        if not board.is_occupied(position):
            print("Position is occupied")
            return 
        board.modify_board(position, "X")
        print("modified board")