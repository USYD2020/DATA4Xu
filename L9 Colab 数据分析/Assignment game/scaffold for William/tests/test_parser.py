"""
Tests for game_parser.py

Run with:
    python3 tests/test_parser.py
"""
from game_parser import parse, read_lines
from cells import Air, Wall, Start, End, Water, Fire, Teleport


def test_simple_grid():
    """A 3x3 grid with X and Y."""
    lines = ['***\n', 'X Y\n', '***\n']
    grid = parse(lines)

    assert len(grid) == 3
    assert len(grid[0]) == 3
    assert isinstance(grid[0][0], Wall)
    assert grid[0][0].display == '*'
    assert isinstance(grid[1][0], Start)
    assert grid[1][0].display == 'X'
    assert isinstance(grid[1][2], End)
    assert grid[1][2].display == 'Y'
    assert isinstance(grid[1][1], Air)
    assert grid[1][1].display == ' '
    print('test_simple_grid PASSED')


def test_air_cells():
    """Empty spaces should be Air cells."""
    lines = ['***\n', '* *\n', '***\n']
    grid = parse(lines)
    assert isinstance(grid[1][1], Air)
    assert grid[1][1].display == ' '
    print('test_air_cells PASSED')


def test_missing_start():
    """No X should raise ValueError."""
    lines = ['***\n', ' Y \n', '***\n']
    try:
        parse(lines)
        assert False, 'Expected ValueError'
    except ValueError as e:
        assert 'Expected 1 starting position' in str(e)
    print('test_missing_start PASSED')


def test_multiple_starts():
    """Two X should raise ValueError."""
    lines = ['XX*\n', ' Y \n', '***\n']
    try:
        parse(lines)
        assert False, 'Expected ValueError'
    except ValueError as e:
        assert 'Expected 1 starting position' in str(e)
    print('test_multiple_starts PASSED')


def test_missing_end():
    """No Y should raise ValueError."""
    lines = ['***\n', 'X  \n', '***\n']
    try:
        parse(lines)
        assert False, 'Expected ValueError'
    except ValueError as e:
        assert 'Expected 1 ending position' in str(e)
    print('test_missing_end PASSED')


def test_bad_letter():
    """Unknown character should raise ValueError."""
    lines = ['***\n', 'XZ \n', '***\n']
    try:
        parse(lines)
        assert False, 'Expected ValueError'
    except ValueError as e:
        assert 'Bad letter' in str(e)
    print('test_bad_letter PASSED')


def test_unmatched_teleport():
    """A teleport pad with no pair should raise ValueError."""
    lines = ['***\n', 'X1 \n', '***\n']
    try:
        parse(lines)
        assert False, 'Expected ValueError'
    except ValueError as e:
        assert 'Teleport pad' in str(e)
    print('test_unmatched_teleport PASSED')


def test_valid_teleport():
    """Paired teleports should work."""
    lines = ['*****\n', 'X1 1Y\n', '*****\n']
    grid = parse(lines)
    assert isinstance(grid[1][1], Teleport)
    assert grid[1][1].display == '1'
    assert isinstance(grid[1][3], Teleport)
    assert grid[1][3].display == '1'
    print('test_valid_teleport PASSED')


def test_water_and_fire():
    """Water and Fire cells should be parsed correctly."""
    lines = ['*****\n', 'XWFY*\n', '*****\n']
    grid = parse(lines)
    assert isinstance(grid[1][1], Water)
    assert grid[1][1].display == 'W'
    assert isinstance(grid[1][2], Fire)
    assert grid[1][2].display == 'F'
    print('test_water_and_fire PASSED')


def test_zero_is_invalid():
    """Teleport pad '0' should be rejected."""
    lines = ['***\n', 'X0 \n', '***\n']
    try:
        parse(lines)
        assert False, 'Expected ValueError'
    except ValueError as e:
        assert 'Bad letter' in str(e)
    print('test_zero_is_invalid PASSED')


if __name__ == '__main__':
    test_simple_grid()
    test_air_cells()
    test_missing_start()
    test_multiple_starts()
    test_missing_end()
    test_bad_letter()
    test_unmatched_teleport()
    test_valid_teleport()
    test_water_and_fire()
    test_zero_is_invalid()
    print('\nAll parser tests passed!')
