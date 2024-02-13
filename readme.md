# Tic Tac Toe Game

This is a simple command-line Tic Tac Toe game I've worked on to help me get a more thorough grasp of Python and recursion. The game allows a human player to play against a computer opponent using a basic AI strategy based on the minimax algorithm. My project is specifically based off [Spanning Tree's Minimax Video](https://www.youtube.com/watch?v=SLgZhpDsrfc&t=509s), where his pseudocode most deviates from others by discarding a turn  parameters in the minimax function, instead opting for a separate function to determine whether the current frame is for the MAX or MIN player. 

## How to Play

1. Clone the repository to your local machine.
2. Run the game by executing `python tictactoe/game.py`.
3. Make your moves by entering positions from 0 to 9 when prompted.
4. The computer opponent will use a mix of randomness and the minimax algorithm to make intelligent moves.

## Task List
- [x] Implement board.py unit testing  
- [x] Implement enemy logic (random for now) 
- [x] Create working game loop  
- [x] Improve enemy AI with Minimax algorithm 
- [ ] Fix pytest import statements 

## Testing 
I have implemented unit testing for the Board and Enemy class. Due to some janky import statements however only the board tests can be ran for now. To run the unit tests, navigate to the root of the project and run `pytest`

## Game Components

### 1. `board.py`

The `Board` class represents the Tic Tac Toe board and provides methods for modifying the board, checking for a winner, and more.

### 2. `player.py`

The `Player` class represents the human player and includes a method for making moves on the board.

### 3. `enemy.py`

The `Enemy` class represents the computer opponent and implements a basic AI strategy using the minimax algorithm. The minimax algorithm is a decision-making algorithm commonly used in two-player games to determine the optimal move for a player, assuming that the opponent is also playing optimally.

- `make_random_move(board)`: Makes a random move on the board.
- `make_move_minimax(board)`: Uses the minimax algorithm to make an intelligent move.

### 4. `printer.py`

The `printer` module contains functions for clearing the console screen (`clear_screen`) and displaying the Tic Tac Toe board (`display_board`).

### 5. `main.py`

The `main` module serves as the entry point for the game. It initializes the board, player, and enemy objects, runs the game loop, and determines the winner.

## Minimax Algorithm

The minimax algorithm is a recursive decision-making algorithm used in two-player games. In the context of this Tic Tac Toe game:

- The `minimax` function in `enemy.py` recursively evaluates all possible moves on the board to find the best move for the computer player ("O").
- The algorithm considers different scenarios, assigns values to each board state, and selects the move with the highest value for the computer player and the lowest value for the human player.

Enjoy playing Tic Tac Toe!
