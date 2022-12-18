from lib.utils.ai import AI
from lib.models.board import Board
import os
import numpy as np


def test_minimax():
    board = [-1, 0, 0,
             0, 0, 0,
             0, 0, 0]
    assert AI.minimax(board, 2) == 0


def test_minimax2():
    board = [0, 0, 0,
             0, 0, 0,
             0, 0, 0]
    assert AI.minimax(board, 1) == 0


def test_minimax3():
    board = [-1, -1, -1,
             0,  0,  1,
             0,  0,  1]
    assert AI.minimax(board, 2) == -2


def test_analyze_board():
    board = [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    assert AI.analyze_board(board) == 0


def test_analyze_board2():
    board = [-1, -1, -1,
             1, 0, 1, 0, 1, 0, 0]
    assert AI.analyze_board(board) == -1


def test_analyze_board3():
    board = [-1, -1, -1, 0, 0, 1, 0, 0, 1, 0]
    assert AI.analyze_board(board) == -1


def test_make_decision():
    board = Board(1)
    board.board_array = np.array([-1, -1, -1,
                                  0,  0,  1,
                                  0,  0,  1])
    board.map_value = {-1: 'X', 1: 'O', 0: ' '}
    board.map_value_file = {
        -1: 'X',
        1: 'O',
        0: " "
    }
    board.session_file = open("test.txt", "w", encoding="utf-8")
    assert AI.make_decision(board) == 1
    os.remove("test.txt")


def test_make_decision2():
    board = Board(1)
    board.board_array = np.array([-1, 0, 0,
                                  0, 0, 0,
                                  0, 0, 0])
    board.map_value = {-1: 'X', 1: 'O', 0: ' '}
    board.map_value_file = board.map_value_file = {
        -1: 'X',
        1: 'O',
        0: " "
    }
    board.session_file = open("test.txt", "w", encoding="utf-8")
    assert AI.make_decision(board) == 0
    os.remove("test.txt")


def test_make_decision3():
    board = Board(1)
    board.board_array = np.array([1,  1,   1,
                                  0,  0,  -1,
                                  0,  0,  -1])
    board.map_value = {-1: 'X', 1: 'O', 0: ' '}
    board.map_value_file = {
        -1: 'X',
        1: 'O',
        0: " "
    }
    board.session_file = open("test.txt", "w", encoding="utf-8")
    assert AI.make_decision(board) == 2
    os.remove("test.txt")
