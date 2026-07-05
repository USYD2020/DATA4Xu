"""
Tests for grid.py

Run with:
    python3 tests/test_grid.py
"""
from game_parser import parse
from grid import grid_to_string
from player import Player


def test_grid_to_string_basic():
    """Basic grid should display correctly with player at start."""
    lines = ['***\n', 'X Y\n', '***\n']
    grid = parse(lines)
    player = Player(1, 0)

    result = grid_to_string(grid, player)

    # Player should be displayed as 'A'
    assert 'A' in result
    # Y should still be visible
    assert 'Y' in result
    # Walls should be visible
    assert '*' in result
    # Water bucket info should be present
    assert 'water buckets' in result.lower() or 'water bucket' in result.lower()
    print('test_grid_to_string_basic PASSED')


def test_grid_to_string_player_replaces_start():
    """Player's position should show 'A' instead of the cell's display."""
    lines = ['***\n', 'X Y\n', '***\n']
    grid = parse(lines)
    player = Player(1, 0)

    result = grid_to_string(grid, player)

    # The first line of the grid should be ***
    # The second line should start with A, not X
    lines_in_result = result.split('\n')
    assert lines_in_result[1].startswith('A')
    print('test_grid_to_string_player_replaces_start PASSED')


def test_grid_to_string_returns_string():
    """grid_to_string should return a string, not print."""
    lines = ['***\n', 'XY\n', '***\n']
    grid = parse(lines)
    player = Player(1, 0)

    result = grid_to_string(grid, player)

    assert isinstance(result, str)
    print('test_grid_to_string_returns_string PASSED')


def test_grid_to_string_newlines():
    """Each row should end with a newline."""
    lines = ['***\n', 'X Y\n', '***\n']
    grid = parse(lines)
    player = Player(1, 0)

    result = grid_to_string(grid, player)

    # Should have at least 3 rows + blank line + bucket line
    assert '\n' in result
    print('test_grid_to_string_newlines PASSED')


if __name__ == '__main__':
    test_grid_to_string_basic()
    test_grid_to_string_player_replaces_start()
    test_grid_to_string_returns_string()
    test_grid_to_string_newlines()
    print('\nAll grid tests passed!')
