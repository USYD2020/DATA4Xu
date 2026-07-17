from game_parser import read_lines
from grid import grid_to_string
from player import Player


class Game:
    def __init__(self, filename):
        self.grid = read_lines(filename)

    def get_grid(self):
        return self.grid

    def get_player(self):
        for i in range(len(self.grid)):
            line = self.grid[i]
            # len(grid) should be greater than 0, so we can use grid[0]
            for j in range(len(self.grid[0])):
                cell = line[j]
                if cell.display == 'X':
                    return Player(i, j)
        return None
    def display(self):
        print(grid_to_string(self.grid, self.player))

    def game_move(self, move):
        pass

# game = Game("board_hard.txt")
# player,grid = game.player,game.grid
# print(grid_to_string(grid,player))
