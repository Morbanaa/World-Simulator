# World Simulator
# TR 
# Morbanaa Studios

import random


bad_tile = ["@","w","t","M","f","g"]
class Update():

    # 
    def update(game_map,game_height,game_width):
        for y in range(game_height):
            for x in range(game_width):
                chance = random.randint(1,2000)

                # update Tree
                if game_map[y][x] == "t":
                    if chance == 1 and game_map[y-1][x] not in bad_tile:
                        game_map[y-1][x] = "t"
                    elif chance == 2 and game_map[y+1][x] not in bad_tile:
                        game_map[y+1][x] = "t"
                    elif chance == 3 and game_map[y][x+1] not in bad_tile:
                        game_map[y][x+1] = "t"
                    elif chance == 4 and game_map[y][x-1] not in bad_tile:
                        game_map[y][x-1] = "t"
                    # Overpopulation
                    elif chance == 5 and game_map[y-1][x] == "t" and game_map[y+1][x] == "t" and game_map[y][x+1] == "t" and game_map[y][x-1] == "t":
                        game_map[y][x] = "."

                # update Animal
                if game_map[y][x] == "f":
                    # Move Animal
                    chance_fast = random.randint(1,500)
                    if chance_fast == 1 and game_map[y+1][x] not in bad_tile:
                        game_map[y][x] = "."
                        game_map[y+1][x] = "f"
                    elif chance_fast == 2 and game_map[y-1][x] not in bad_tile:
                        game_map[y][x] = "."
                        game_map[y-1][x] = "f"
                    elif chance_fast == 3 and game_map[y][x+1] not in bad_tile:
                        game_map[y][x] = "."
                        game_map[y][x+1] = "f"
                    elif chance_fast == 4 and game_map[y][x-1] not in bad_tile:
                        game_map[y][x] = "."
                        game_map[y][x-1] = "f"

                    # New animal
                    chance_slow = random.randint(1,5000)
                    if chance_slow == 1 and game_map[y-1][x] not in bad_tile:
                        game_map[y-1][x] = "f"
                    elif chance_slow == 2 and game_map[y+1][x] not in bad_tile:
                        game_map[y+1][x] = "f"
                    elif chance_slow == 3 and game_map[y][x+1] not in bad_tile:
                        game_map[y][x+1] = "f"
                    elif chance_slow == 4 and game_map[y][x-1] not in bad_tile:
                        game_map[y][x-1] = "f"
                    # Overpopulation
                    elif chance_fast == 1 and game_map[y-1][x] == "f" and game_map[y+1][x] == "f":
                        game_map[y][x] = "."
                    


