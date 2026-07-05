from game import Game

def test_game():
    game = Game("board_hard.txt")
    player,grid = game.player,game.grid
    print(grid_to_string(grid,player))


def run_tests():
    test_game()
test_game()
