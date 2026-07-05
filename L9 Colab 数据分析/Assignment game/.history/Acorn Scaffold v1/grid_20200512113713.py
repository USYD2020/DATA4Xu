from game_parser import read_lines

def grid_to_string(grid, player):
    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """
    to_print = []
    for row in grid:
        line = []
        for cell in row:
            line.append(cell.display)
    to_print[player.row][player.col] = 'A'
    return "".join(to_print)

player,grid = read_lines("board_hard.txt")
print(player.row, player.col)
print("gird size", len(grid),len(grid[0]))
print(grid_to_string(grid,player))
