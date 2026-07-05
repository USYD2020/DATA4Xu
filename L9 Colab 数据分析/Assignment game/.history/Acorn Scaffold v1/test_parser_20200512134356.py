from game_parser import *

def test_parse():
    lines = ["*X1*\n","* 1*","*Y**"]
    grid,player = parse(lines)
    assert len(grid) == 3
    assert len(grid[0]) == 4

def test_readline():
    grid,player = read_lines("board_hard.txt")
    assert len(grid) == 9
    assert len(grid[0]) == 15

def run_tests():
    test_parse()

run_tests()