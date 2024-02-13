import unittest
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

if __name__ == "__main__": 
    unittest.main()