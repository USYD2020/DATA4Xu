from game_parser import read_lines
from grid import grid_to_string
from player import Player


class Game:
    def __init__(self, filename):
        self.grid = read_lines(filename)
        self.player = self.find_player()
        self.moves = []
        self.finished = False
        self.won = False
        self.lost = False

    def find_player(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col].display == 'X':
                    return Player(row, col)
        return None

    def display(self):
        print(grid_to_string(self.grid, self.player))

    def get_delta(self, move):
        if move == 'w':
            return -1, 0
        if move == 's':
            return 1, 0
        if move == 'a':
            return 0, -1
        if move == 'd':
            return 0, 1
        if move == 'e':
            return 0, 0
        return None

    def move_player(self, move):
        # TODO Day 3: Basic movement.
        # 1. Use get_delta() to calculate the target position.
        self.position = (self.player.row,self.player.col)
        self.position = (self.position[0] + self.get_delta(move)[0] , 
                         self.position[1] + self.get_delta(move)[1])
        block = self.grid[self.position[0]][self.position[1]].display
        # 2. If the player hits a wall or goes out of bounds,
        #    print the wall message and return False.
        if block == '*':
            print('It\'s a wall.')
            return False
        # 3. If the player can move, update player.row and player.col.
        else:
            self.player.row,self.player.col = self.position
        # 4. Add the move to self.moves.
            self.moves.append(move)
        # 5. If the player reaches Y, set self.finished and self.won.
        if block == 'Y':
            self.finished = True
            self.won = True
        # TODO Day 4: Add Water and Fire.
        if block == 'W':
            self.player.num_water_buckets += 1
            self.grid[self.position[0]][self.position[1]].display = ' '
        if block == 'F':
            if self.player.num_water_buckets > 0:
                self.player.num_water_buckets -= 1
            else:
                self.lost = True
            self.grid[self.position[0]][self.position[1]].display = ' '
        # TODO Day 5: Add Teleport cells.
        if block in ['1','2','3','4','5','6','7','8','9']:
            first = True
            for row in range(len(self.grid)):
                for col in range(len(self.grid[row])):
                    if self.grid[row][col].display == block and first is True:
                        first = False
                        continue
                    if self.grid[row][col].display == block:
                        self.player.row,self.player.col = row,col