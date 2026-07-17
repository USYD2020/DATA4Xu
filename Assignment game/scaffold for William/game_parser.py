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
            if ch == '*':
                row.append(Wall())
            elif ch == ' ':
                row.append(Air())
            elif ch == 'X':
                row.append(Start())
                start_count += 1
            elif ch == 'Y':
                row.append(End())
                end_count += 1
            elif ch == 'W':
                row.append(Water())
            elif ch == 'F':
                row.append(Fire())
            elif ch in ['1','2','3','4','5','6','7','8','9']:
                row.append(Teleport(ch))
                if ch not in teleport_counts:
                    teleport_counts[ch] = 0
                teleport_counts[ch] += 1
            else:
                raise ValueError('Bad letter in file: ' + ch)

        grid.append(row)

    # TODO: Check that there is exactly one X.
    if start_count != 1:
        raise ValueError('Expected 1 starting position')
    # TODO: Check that there is exactly one Y.
    if end_count != 1:
        raise ValueError('Expected 1 ending position')
    # TODO: Check that every teleport number appears exactly twice.
    for tele,count in teleport_counts.items():
        if count != 2:
            raise ValueError('Teleport pad ' + tele + ' does not have an exclusive pair')
    return grid

print(read_lines("board_simple.txt"))