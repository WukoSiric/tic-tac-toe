import unittest
from tictactoe.board import Board

class BoardTest(unittest.TestCase): 

    def setUp(self): 
        self.board = Board() 
        pass
    
    def tearDown(self): 
        pass

    def test_modify_board(self): 
        pass

    def test_reset_board(self): 
        self.board.modify_board(3, "X")
        self.board.reset_board() 
        self.assertTrue(self.board.grid == [" ", " ", " "] * 3)

    def test_is_occupied(self): 
        pass

    def test_has_winner(self):
        pass

if __name__ == "__main__": 
    unittest.main()