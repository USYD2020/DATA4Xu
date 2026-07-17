from grid import grid_to_string
from game_parser import *

def test_grid():
    player,grid = read_lines("board_hard.txt")
    print(grid_to_string(grid,player))


def run_tests():
    test_grid()

run_tests()