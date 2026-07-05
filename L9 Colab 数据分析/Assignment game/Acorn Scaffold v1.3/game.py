from game_parser import read_lines
from grid import grid_to_string
from player import Player


class Game:
    def __init__(self, filename):
        self.grid = read_lines(filename)
        self.player = self.get_player()

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

    def cell_at(self, row, col):
        return self.grid[row][col]

    def check_the_move(self, cell):
        if cell.display == '*':
            return False
        else:
            return True

    def teleport(self, given_cell, player):
        target = given_cell.display
        for i in range(len(self.grid)):
            line = self.grid[i]
            # len(grid) should be greater than 0, so we can use grid[0]
            for j in range(len(self.grid[0])):
                cell = line[j]
                if cell.display == target and not (i == player.row and j == player.col):
                    player.row = i
                    player.col = j
                    return True
        return False

    def game_move(self, move):
        if move == "a":
            changes = (0, -1)
        elif move == "d":
            changes = (0, 1)
        elif move == "w":
            changes = (-1, 0)
        elif move == "s":
            changes = (1, 0)
        # get the next cell
        cell = self.cell_at(self.player.row + changes[0],
                            self.player.col + changes[1])
        # do not move if next move hit a wall
        if not self.check_the_move(cell):
            print("wall oops")
            return None
        if cell.display == "W":
            self.player.num_water_buckets += 1
            self.player.row += changes[0]
            self.player.col += changes[1]
        elif cell.display == "F":
            self.player.num_water_buckets -= 1
            self.player.row += changes[0]
            self.player.col += changes[1]
        elif cell.display == " ":
            self.player.row += changes[0]
            self.player.col += changes[1]
        elif cell.display == "X":
            self.player.row += changes[0]
            self.player.col += changes[1]
        elif cell.display == "Y":
            self.player.row += changes[0]
            self.player.col += changes[1]
        elif cell.display.isdigit():
            self.player.row += changes[0]
            self.player.col += changes[1]
            self.teleport(cell, self.player)


game = Game("board_hard.txt")
player, grid = game.player, game.grid
print(grid_to_string(grid, player))
