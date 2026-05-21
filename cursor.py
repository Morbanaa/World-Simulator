# President
# TR JG
# Idiotball Studios

import keyboard

class Cursor():
    def __init__(self,ypos,xpos):
        self.ypos = ypos
        self.xpos = xpos

    def update(self,game_map):
        if keyboard.is_pressed("W") and game_map[self.ypos -1][self.xpos] != "@":
            self.ypos -= 1

        if keyboard.is_pressed("S") and game_map[self.ypos +1][self.xpos] != "@":
            self.ypos += 1

        if keyboard.is_pressed("A") and game_map[self.ypos][self.xpos -1] != "@":
            self.xpos -= 1

        if keyboard.is_pressed("D") and game_map[self.ypos][self.xpos +1] != "@":
            self.xpos += 1