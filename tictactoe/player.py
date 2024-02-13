from board import Board

class Player: 
    move = "X"
    def __init__(self): 
        pass

    def make_move(self, board: Board) -> None: 
        print("Make your move (Enter 0 to 9): ")

        while True: 
            position = input()
            try: 
                position = int(position)
            except ValueError: 
                print("Not an integer between 0 and 9. Try again: ")
                continue

            try: 
                if board.is_occupied(position):
                    print("Position is occupied. Try again:")
                    continue 
            except IndexError: 
                print("Index is not between 0 and 9. Try again: ")
                continue

            board.modify_board(position, "X")
            return