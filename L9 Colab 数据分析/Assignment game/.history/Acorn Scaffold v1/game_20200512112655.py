from game_parser import read_lines
from grid import grid_to_string
from player import Player


class Game:
    def __init__(self, filename):
        self.player, self.grid = read_lines(filename)

    def game_move(self, move):
        pass

# game = Game("board_hard.txt")
# player,grid = game.player,game.grid
# print(grid_to_string(grid,player))
