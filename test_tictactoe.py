import pytest

import TicTacToe_2016 as ttt

class TestZone:

    def testtrue(self):
        assert 1

    def test_create_grid(self):
        b = ttt.create_grid()
        print(b)
        assert b == [[" ", " ", " "],
                     [" ", " ", " "],
             [" ", " ", " "]]
        
    def test_sym(self):
        s1, s2 = ttt.sym()
        assert s1 == "X" or s1 == "O"
        assert s2 == "X" or s2 == "O"
        assert s1 != s2