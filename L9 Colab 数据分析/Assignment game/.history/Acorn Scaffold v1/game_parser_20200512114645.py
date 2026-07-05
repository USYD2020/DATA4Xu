from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
from player import Player


def read_lines(filename):
    """Read in a file, process them using parse(),
    and return the contents as a list of list of cells."""
    try:
        lines = open(filename).readlines()
        return parse(lines)
    except FileNotFoundError:
        print(filename + " does not exist!")
        exit()


def parse(lines):
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        list -- contains list of lists of Cells
    """
    grid = []
    countX = 0
    countY = 0
    unmatched_teleports = []
    for row, line in enumerate(lines):
        cells = []
        for col, ch in enumerate(line.strip()):
            if ch == '*':
                cells.append(Wall())
            elif ch == 'X':
                cells.append(Start())
                player = Player(row, col)
                countX += 1
            elif ch == 'Y':
                cells.append(End())
                countY += 1
            elif ch == ' ':
                cells.append(Air())
            elif ch == 'F':
                cells.append(Fire())
            elif ch == 'W':
                cells.append(Water())
            elif ch.isdigit():
                if ch == '0':
                    raise ValueError(
                        "Bad letter in configuration file: {}.".format(ch))
                else:
                    cells.append(Teleport(ch))
                    if ch not in unmatched_teleports:
                        unmatched_teleports.append(ch)
                    else:
                        unmatched_teleports.remove(ch)
            else:
                raise ValueError(
                    "Bad letter in configuration file: {}.".format(ch))
        grid.append(cells)
    if(countX != 1):
        raise ValueError(
            "Expected 1 starting position, got {}.".format(countX))
    if(countY != 1):
        raise ValueError("Expected 1 ending position, got {}.".format(countY))
    if len(unmatched_teleports) != 0:
        raise ValueError("Teleport pad {} does not have an exclusively matching pad.".format(
            unmatched_teleports[0]))
    return grid,player
#print(read_lines("board_hard.txt"))
