import unittest
from tictactoe.board import Board

class BoardTest(unittest.TestCase): 

    def setUp(self): 
        self.board = Board() 
        pass
    
    def tearDown(self): 
        pass

    def test_modify_board_exceptions(self): 
        with self.assertRaises(TypeError): 
            self.board.modify_board(1.1, "X")

        with self.assertRaises(IndexError): 
            self.board.modify_board(100, "X")

        with self.assertRaises(IndexError): 
            self.board.modify_board(-1, "X")

        with self.assertRaises(IndexError): 
            self.board.modify_board(-100, "X")

        with self.assertRaises(IndexError): 
            self.board.modify_board(position=10, player_id="X")

    def test_reset_board(self): 
        self.board.modify_board(3, "X")
        self.board.reset_board() 
        empty_grid = [" ", " ", " "] * 3
        self.assertTrue(self.board.grid == empty_grid)

    def test_is_occupied(self): 
        pass

    def test_has_winner(self):
        pass

if __name__ == "__main__": 
    unittest.main()