from board import Board
from player import Player
from enemy import Enemy
from printer import clear_screen, display_board

def main(): 
    board = Board() 
    player = Player()
    enemy = Enemy()
    game_over = False

    # Start while loop
    print("Setting up board!")
    board.reset_board() 
    display_board(board)

    while not board.is_full() and board.has_winner() is None:
        clear_screen()
        display_board(board)
        player.make_move(board)

        if not board.is_full():
            enemy.make_move(board)


    clear_screen()
    display_board(board)
    winner = board.has_winner()
    if winner == None:
        print("GAME OVER")
        print("No one has won... ")
        return
    print("GAME OVER")
    print(winner + " wins the round!")

if __name__ == "__main__": 
    main() 