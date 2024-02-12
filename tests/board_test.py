import unittest
from tictactoe.board import Board

class BoardTest(unittest.TestCase): 

    def setUp(self): 
        self.board = Board() 
    
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
        self.assertFalse(self.board.is_occupied(3))
        self.board.modify_board(3, "X")
        self.assertTrue(self.board.is_occupied(3))
        self.assertFalse(self.board.is_occupied(0))
        self.board.modify_board(0, "O")
        self.assertTrue(self.board.is_occupied(0))

    def test_has_winner_empty(self):
        self.assertEqual(self.board.has_winner(), None) 

    def test_has_winner_diagonal(self): 
        self.board.modify_board(0, "X")
        self.board.modify_board(4, "X")
        self.board.modify_board(8, "X")

        self.assertEqual(self.board.has_winner(), "X") 

    def test_has_winner_horizontal(self): 
        self.board.modify_board(0, "X")
        self.board.modify_board(1, "X")
        self.board.modify_board(2, "X")
        self.assertEqual(self.board.has_winner(), "X") 

if __name__ == "__main__": 
    unittest.main()