from game import Game
import os
import sys

if (len(sys.argv == 1)):
    print("Usage: python3 run.py")
    exit()
elif (len(sys.argv == 2)):
    print("Usage: python3 run.py "+sys.argv[1])
    exit()
mode_play = sys.argv[2]
if mode_play != "play":
    exit()


def wait():
    pass

def get_moves_string(move_list):
    i = 0
    move_str = '' 
    while i < len(move_list):
        move_str += (move_list[i] + ", ")
        i+=1
    move_str = move_str.rstrip(", ")
    return move_str

def print_success(move_list):
    length = len(move_list)
    moves_string = get_moves_string(move_list)
    SUCCESS_MSG = """
You conquer the treacherous maze set up by the Fire Nation and reclaim the
Honourable Furious Forest Throne, restoring your hometown back to its former
glory of rainbow and sunshine! Peace reigns over the lands.

Your made {} moves.
Your moves: {}

=====================
====== YOU WIN! =====
=====================
""".format(length, moves_string)
    print(SUCCESS_MSG)

def print_Game_Over(move_list):
    length = len(move_list)
    moves_string = get_moves_string(move_list)
    FAIL_MSG = '''
When the player finishes the game unsuccessfully, print:
The Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of
ash and is scattered to the winds by the next storm... You have been roasted.
Your made {} moves.
Your moves: {}
=====================
===== GAME OVER =====
=====================
'''.format(length, moves_string)
    print(FAIL_MSG)

filename = sys.argv[1]
game = Game(filename)
grid = game.get_grid()
player = game.get_player()
move_list = []

while True:
    print()
    cmd = input("Input a move: ")
    #print message to avoid invalid cmds
    if cmd != "w" or cmd !="a" or cmd!="s" or cmd!="d" or cmd!= "e" or cmd!= "q":
        print("Please enter a valid move (w, a, s, d, e, q).")
        continue
    # direction cmds
    elif cmd == "w" or cmd == "a" or cmd == "s" or cmd == "d" or cmd == "e":
        move_list.append(cmd)
        # move to up
        if cmd == "w":
            #change player's direction
            pass
        #move to left
        elif cmd == "a":
            pass
        #move to down
        elif cmd == "s":
            pass
        #move to right
        elif cmd == "d":
            pass
        #wait a turn
        elif cmd == "e":
            wait()
        os.system("clear")
        game.display()
   #quit the game cmd
    elif cmd == "q":
        print("Bye!")
        sys.exit()
    
    #print success messages if the player reaches the ending  cell
    if grid[player.row][player.col].display == 'Y':
        print_success(move_list)
        exit()
    #print game over messages if the player is out of water
    if player.num_water_buckets == 0:
        print_Game_Over(move_list)
        exit()
        
        
        