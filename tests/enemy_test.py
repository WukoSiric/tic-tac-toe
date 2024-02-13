import unittest
import logging
from tictactoe.enemy import Enemy
from tictactoe.board import Board

class EnemyTest(unittest.TestCase): 
    def setUp(self): 
        self.enemy = Enemy() 
        self.board = Board()

    def tearDown(self): 
        self.enemy = None 
        self.board.reset_board() 

    def test_get_player_turn_o(self): 
        self.board.modify_board(0, "X")
        self.assertEqual(self.enemy.get_player_turn(self.board), "O")

    def test_get_player_turn_x(self):
        self.board.modify_board(0, "X")
        self.board.modify_board(4, "O")
        self.assertEqual(self.enemy.get_player_turn(self.board), "X")

    def test_get_possible_boards_1(self): 
        self.board.modify_board(0, "X")
        self.board.modify_board(1, "O")
        self.board.modify_board(2, "X")
        self.board.modify_board(3, "X")
        self.board.modify_board(4, "O")
        self.board.modify_board(5, "O")
        self.board.modify_board(6, "O")
        self.board.modify_board(7, "X")
        possible_boards = self.enemy.get_possible_boards(self.board, "X")
        self.assertEqual(len(possible_boards), 1)
        self.assertEqual(possible_boards[0].grid, ["X", "O", "X", "X", "O", "O", "O", "X", "X"])

    def test_get_possible_boards_2(self): 
        self.board.modify_board(0, "X")
        self.board.modify_board(1, "O")
        self.board.modify_board(2, "X")
        self.board.modify_board(3, "X")
        self.board.modify_board(4, "O")
        self.board.modify_board(6, "O")
        possible_boards = self.enemy.get_possible_boards(self.board, "X")
        self.assertEqual(len(possible_boards), 3)
        self.assertEqual(possible_boards[0].grid, ["X", "O", "X", "X", "O", "X", "O", " ", " "])
        self.assertEqual(possible_boards[1].grid, ["X", "O", "X", "X", "O", " ", "O", "X", " "])
        self.assertEqual(possible_boards[2].grid, ["X", "O", "X", "X", "O", " ", "O", " ", "X"])

if __name__ == "__main__": 
    unittest.main()