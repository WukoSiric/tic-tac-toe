from board import Board

class Player: 
    move = "X"
    def __init__(self): 
        pass

    def make_move(self, position: int, board: Board) -> None: 
        print("Make your move: ")
        position = input()
        position = int(position)

        if not board.is_occupied(position):
            board.modify_board(position, "X")
        else: 
            print("Position is occupied")
            return 