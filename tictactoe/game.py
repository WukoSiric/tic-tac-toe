from board import Board
from player import Player
from enemy import Enemy
import os

def clear_screen(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def main(): 
    board = Board() 
    player = Player()
    enemy = Enemy()
    game_over = False

# Start while loop
    print("Setting up board!")
    board.reset_board() 
    board.display_board()

    while not board.is_full() and board.has_winner() == None:
        clear_screen()
        board.display_board()
        player.make_move(board)
        enemy.make_move(board)

    clear_screen()
    board.display_board()
    winner = board.has_winner()
    if winner == None:
        print("No one has won... ")
    print(winner + " wins the round!")

if __name__ == "__main__": 
    main() 