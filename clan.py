import random
from warrior import Warrior
from villager import Villager

class Clan():
    clan_counter = 1
    clans = []
    def __init__(self,ypos,xpos):
        self.ypos = ypos
        self.xpos = xpos
        self.symbol = Clan.clan_counter
        self.population = 10
        self.food = 100
        self.wood = 100
        self.gold = 50
        self.villagers = []
        self.warriors = []
        # Create initial units
        for i in range(3):
            self.villagers.append(Villager(self.ypos,self.xpos,self.ypos,self.xpos,self.symbol))
        for i in range(1):
            self.warriors.append(Warrior(self.ypos,self.xpos,self.ypos,self.xpos,self.symbol,25))

        Clan.clan_counter += 1


