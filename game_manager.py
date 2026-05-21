# World Simulator
# TR 
# Morbanaa Studios

import sys
import random
from cursor import Cursor
from update import Update
from clan import Clan

# Colors
BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY  = '\033[90m'
CRIMSON        = '\033[38;5;160m'
GOLD_ORANGE    = '\033[38;5;208m'
BROWN = '\033[38;5;52m'

BRIGHT_BLACK   = '\033[90m'
BRIGHT_RED     = '\033[91m'
BRIGHT_GREEN   = '\033[92m'
BRIGHT_YELLOW  = '\033[93m'
BRIGHT_BLUE    = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN    = '\033[96m'
BRIGHT_WHITE   = '\033[97m'

DARK_GREEN = '\033[32m'

# Reset Color
RESET = '\033[0m'

class Game_Manager():
    ####################################
    #       Constructor
    ####################################
    def __init__(self,game_height,game_width):
        self.game_height = game_height
        self.game_width = game_width
        self.game_map = []
        self.cursor = Cursor(self.game_height//2,self.game_width//2)


    ####################################
    #       World Gen
    ####################################
    def world_gen(self):
        # Initial Set Up
        for y in range (self.game_height):
            row =[]
            for x in range(self.game_width):
                if y == 0 or y == self.game_height -1 or x == 0 or x == self.game_width -1:
                    row.append("@")
                else:
                    row.append(".")
            self.game_map.append(row)
        
        # Creates starting points to grow mountains lakes and forests
        for y in range(self.game_height):
            for x in range(self.game_width):
                barrier_starter = random.randint(1,175)
                water_starter = random.randint(1,150)
                timber_starter = random.randint(1,100)

                if barrier_starter == 1 and self.game_map[y][x] != "@":
                    self.game_map[y][x] = "M"
                    if self.game_map[y-1][x] != "@":
                        self.game_map[y-1][x] = "M"
                    if self.game_map[y][x-1] != "@":
                        self.game_map[y][x-1] = "M"
                elif water_starter == 1 and self.game_map[y][x] != "@":
                    self.game_map[y][x] = "w"
                    if self.game_map[y-1][x] != "@":
                        self.game_map[y-1][x] = "w"
                    if self.game_map[y][x-1] != "@":
                        self.game_map[y][x-1] = "w"
                elif timber_starter == 1 and self.game_map[y][x] != "@":
                    self.game_map[y][x] = "t"
                    if self.game_map[y-1][x] != "@":
                        self.game_map[y-1][x] = "t"
                    if self.game_map[y][x-1] != "@":
                        self.game_map[y][x-1] = "t"

        # Fill in mountains lakes and forests
        for y in range(self.game_height):
            for x in range(self.game_width):
                # Mountains
                if self.game_map[y][x] == "M":
                    chance = random.randint(1,2)
                    if chance == 1:
                        if self.game_map[y -1][x] != "@":
                            self.game_map[y -1][x] = "M"
                        if self.game_map[y +1][x] != "@":
                            self.game_map[y +1][x] = "M"
                        if self.game_map[y][x -1] != "@":
                            self.game_map[y][x -1] = "M"
                        if self.game_map[y][x +1] != "@":
                            self.game_map[y][x +1] = "M"
                
                # Lakes
                if self.game_map[y][x] == "w":
                    chance = random.randint(1,2)
                    if chance == 1:
                        if self.game_map[y -1][x] != "@":
                            self.game_map[y -1][x] = "w"
                        if self.game_map[y +1][x] != "@":
                            self.game_map[y +1][x] = "w"
                        if self.game_map[y][x -1] != "@":
                            self.game_map[y][x -1] = "w"
                        if self.game_map[y][x +1] != "@":
                            self.game_map[y][x +1] = "w"
        
                # Forests
                if self.game_map[y][x] == "t":
                    chance = random.randint(1,2)
                    if chance == 1:
                        if self.game_map[y -1][x] != "@":
                            self.game_map[y -1][x] = "t"
                        if self.game_map[y +1][x] != "@":
                            self.game_map[y +1][x] = "t"
                        if self.game_map[y][x -1] != "@":
                            self.game_map[y][x -1] = "t"
                        if self.game_map[y][x +1] != "@":
                            self.game_map[y][x +1] = "t"
        
        # Gold Food
        bad_tile = ["@","w","t","M"]
        for y in range(self.game_height):
            for x in range(self.game_width):
                # Gold
                if self.game_map[y][x] not in bad_tile:
                    chance = random.randint(1,100)
                    if chance == 1:
                        self.game_map[y][x] = "g"

                # Food
                if self.game_map[y][x] not in bad_tile:
                    chance = random.randint(1,50)
                    if chance == 1:
                        self.game_map[y][x] = "f"


    ####################################
    #       Create Clans
    ####################################
    def create_clans(self):
        bad_tile = ["@","w","t","M","f","g"]

        for i in range(6):
            while True:
                randY = random.randint(5,self.game_height-5)
                randX = random.randint(6,self.game_width-6)

                is_there = False
                for clan in Clan.clans:
                    if clan.ypos == randY and clan.xpos == randX:
                        is_there = True
                if is_there == False and self.game_map[randY][randX] not in bad_tile:
                    Clan.clans.append(Clan(randY,randX,))
                    break
                    
                   
    ####################################
    #       Update Objects
    ####################################
    def update(self):
        # Update Objects
        self.cursor.update(self.game_map)

        # Update Map
        Update.update(self.game_map,self.game_height,self.game_width)


    ####################################
    #       Render World
    ####################################
    def render_world(self):
        for y in range(self.game_height):
            for x in range(self.game_width):

                # Prints Clans
                clan_here = False
                for clan in Clan.clans:
                    if clan.ypos == y and clan.xpos == x:
                        clan_here = True
                        print(f"{BRIGHT_WHITE}{clan.symbol}{RESET}",end="")
                        self.game_map[y-1][x] = "#"
                        self.game_map[y+1][x] = "#"
                        self.game_map[y][x-1] = "#"
                        self.game_map[y][x+1] = "#"
                        break
                if clan_here:
                    continue

                if y == self.cursor.ypos and x == self.cursor.xpos:
                    print("^",end="")
                elif self.game_map[y][x] == "#":
                    print(f"{WHITE}#{RESET}",end="")
                elif self.game_map[y][x] == "@":
                    print(f"{DARK_GRAY}@{RESET}",end="")
                elif self.game_map[y][x] == ".":
                    print(f"{GREEN}.{RESET}",end="")
                elif self.game_map[y][x] == "M":
                    print(f"{BROWN}M{RESET}",end="")
                elif self.game_map[y][x] == "w":
                    print(f"{BRIGHT_BLUE}w{RESET}",end="")
                elif self.game_map[y][x] == "t":
                    print(f"{DARK_GREEN}t{RESET}",end="")
                elif self.game_map[y][x] == "g":
                    print(f"{GOLD_ORANGE}g{RESET}",end="")
                elif self.game_map[y][x] == "f":
                    print(f"{GOLD_ORANGE}f{RESET}",end="")
                else:
                    print(self.game_map[y][x],end="")
            print()
    

    ####################################
    #       Move cursor top left
    ####################################
    def clear_move_cursor(self):
        sys.stdout.write("\033[H")
        sys.stdout.flush()