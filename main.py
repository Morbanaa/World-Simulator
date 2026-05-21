# President
# TR JG
# Idiotball Studios

import time
from game_manager import Game_Manager

def main():
    game_speed = 0.05
    game_manager = Game_Manager(40,100)
    game_manager.world_gen()
    while True:

        game_manager.update()
        game_manager.render_world()
        game_manager.clear_move_cursor()
        time.sleep(game_speed)

if __name__ == "__main__":
    main()








