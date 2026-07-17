from grid import grid_to_string
from game_parser import *

def test_grid():
    player,grid = read_lines("board_hard.txt")
    expected = '''*A*************
*       2 *   *
* *** ** **** *
* *  W*   1   *
* ***** ***** *
*  2 *   ** *F*
* ** ***  F   *
* 1********F  *
*************Y*'''
    assert grid_to_string(grid,player) == expected


def run_tests():
    test_grid()

run_tests()