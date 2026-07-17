from grid import grid_to_string
from game_parser import *


def test_grid():
    grid, player = read_lines("board_hard.txt")
    actual = grid_to_string(grid, player)
    expected = '''*A*************
*       2 *   *
* *** ** **** *
* *  W*   1   *
* ***** ***** *
*  2 *   ** *F*
* ** ***  F   *
* 1********F  *
*************Y*
'''
    assert actual == expected


def run_tests():
    test_grid()


run_tests()
