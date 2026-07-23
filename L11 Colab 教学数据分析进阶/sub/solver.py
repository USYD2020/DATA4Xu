import sys


def main():
    if len(sys.argv) < 3:
        print('Usage: python3 solver.py <filename> <mode>')
        return

    filename = sys.argv[1]
    mode = sys.argv[2]

    # TODO Day 7: Implement the solver.
    # Start with BFS, then add DFS.
    # BFS should find an optimal path.
    # DFS only needs to find a valid path.
    print('Solver not implemented yet.')


if __name__ == '__main__':
    main()
