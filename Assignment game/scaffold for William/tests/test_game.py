"""
Tests for game.py

Run from the scaffold folder with:
    python3 -m tests.test_game
"""
from game import Game


def test_game_creation():
    """Game should load the map and find the player."""
    game = Game('board_simple.txt')
    assert game.player is not None
    assert game.player.display == 'A'
    print('test_game_creation PASSED')


def test_player_position():
    """Player should start at the X position."""
    game = Game('board_simple.txt')
    # board_simple.txt:
    # ***
    # X Y
    # ***
    # So X is at row 1, col 0
    assert game.player.row == 1
    assert game.player.col == 0
    print('test_player_position PASSED')


def test_get_delta():
    """get_delta should return correct coordinate changes."""
    game = Game('board_simple.txt')

    assert game.get_delta('w') == (-1, 0)
    assert game.get_delta('s') == (1, 0)
    assert game.get_delta('a') == (0, -1)
    assert game.get_delta('d') == (0, 1)
    assert game.get_delta('e') == (0, 0)
    assert game.get_delta('z') is None
    print('test_get_delta PASSED')


def test_move_player_updates_position():
    """Moving the player should update row/col."""
    game = Game('board_simple.txt')
    # board_simple.txt:
    # ***
    # X Y
    # ***
    # Move right twice to reach Y

    game.move_player('d')
    assert game.player.col == 1

    game.move_player('d')
    assert game.player.col == 2
    assert game.won is True
    assert game.finished is True
    print('test_move_player_updates_position PASSED')


def test_move_wall_stays_put():
    """Moving into a wall should not change position."""
    game = Game('board_simple.txt')
    # Start at (1, 0). Try moving up into wall.
    old_row = game.player.row
    old_col = game.player.col

    game.move_player('w')

    assert game.player.row == old_row
    assert game.player.col == old_col
    print('test_move_wall_stays_put PASSED')


def test_moves_recorded():
    """Valid moves should be recorded in self.moves."""
    game = Game('board_simple.txt')
    game.move_player('d')
    game.move_player('d')

    assert len(game.moves) == 2
    assert game.moves[0] == 'd'
    assert game.moves[1] == 'd'
    print('test_moves_recorded PASSED')


def test_wall_not_recorded():
    """Hitting a wall should not record the move."""
    game = Game('board_simple.txt')
    game.move_player('w')

    assert len(game.moves) == 0
    print('test_wall_not_recorded PASSED')


if __name__ == '__main__':
    test_game_creation()
    test_player_position()
    test_get_delta()
    test_move_player_updates_position()
    test_move_wall_stays_put()
    test_moves_recorded()
    test_wall_not_recorded()
    print('\nAll game tests passed!')
