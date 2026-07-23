from game import Game
import sys


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 run.py <filename> [play]')
        return

    filename = sys.argv[1]
    game = Game(filename)
    game.display()

    while not game.finished:
        move = input('Input a move: ').lower()

        if move == 'q':
            print('Bye!')
            return

        if move not in ['w', 'a', 's', 'd', 'e']:
            print('Please enter a valid move (w, a, s, d, e, q).')
            continue

        game.move_player(move)
        game.display()

    # TODO Day 4: Print the final win or game-over message.


if __name__ == '__main__':
    main()
