from cells import Air, Wall, Start, End, Water, Fire, Teleport


def read_lines(filename):
    try:
        file = open(filename, 'r')
        lines = file.readlines()
        file.close()
        return parse(lines)
    except FileNotFoundError:
        print(filename + ' does not exist!')
        exit()


def parse(lines):
    grid = []
    start_count = 0
    end_count = 0
    teleport_counts = {}

    for line in lines:
        line = line.rstrip('\n')
        row = []

        for ch in line:
            # TODO: Create the correct Cell object for each character.
            # '*': Wall()
            # ' ': Air()
            # 'X': Start(), and increase start_count
            # 'Y': End(), and increase end_count
            # 'W': Water()
            # 'F': Fire()
            # '1' to '9': Teleport(ch), and count the teleport number
            # Other characters: raise ValueError with the required message
            pass

        grid.append(row)

    # TODO: Check that there is exactly one X.
    # TODO: Check that there is exactly one Y.
    # TODO: Check that every teleport number appears exactly twice.

    return grid
