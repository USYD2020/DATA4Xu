def grid_to_string(grid, player):
    '''
    Convert the grid and player position into a string representation.

    Arguments:
        grid: list of lists of cells
        player: Player object

    Returns:
        string: the grid and player position as a string
    '''
    result = ''

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # TODO: If this position is the player's position,
            # add player.display to result.
            # Otherwise, add grid[row][col].display to result.
            result += grid[row][col].display if (row, col) != (
                player.row, player.col) else player.display

        # TODO: Add a newline after each row.
        result += '\n'

    # TODO: Add a blank line.
    result += '\n'

    # TODO: Add the water bucket message.
    # Example:
    # You have 0 water buckets.
    # You have 1 water bucket.
    isplural = player.num_water_buckets != 1
    result += 'You have {} water bucket{}.'.format(player.num_water_buckets,  "s" if isplural else "")
    return result
