def grid_to_string(grid, player):
    result = ''

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if row == player.row and col == player.col:
                result += player.display
            else:
                result += grid[row][col].display
            # TODO: If this position is the player's position,
            # add player.display to result.
            # Otherwise, add grid[row][col].display to result.

        # TODO: Add a newline after each row.
        result += '\n'
    # TODO: Add a blank line.
    result += '\n'
    # TODO: Add the water bucket message.
    # Example:
    # You have 0 water buckets.
    # You have 1 water bucket.
    result += 'You have {} water bucket{}.'.format(player.num_water_buckets,'s' if player.num_water_buckets != 1 else '')
    return result
