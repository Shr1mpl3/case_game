import random
from inventory import Inventory

class Player:
    def __init__(self, name: str, aura: int, luck: int, money: int, keys: int):
        self.name = name
        self.luck = luck
        self.money = money
        self.keys = keys
        self.best_weapon = weapon
        self.aura = aura
        self.inventory = Inventory()

class OhnePixel(Player):
    def __init__(self, name, aura, luck, money, keys):
        super().__init__("OhnePixel", self, name, aura, luck, money, keys)

    def special(self):
        if self.endurance >= 5:
            self.luck += 10
            self.endurance -= 5
            return "OhnePixel schreit: GOLD GOLD GOLD! (+10 Glück)"
        return "Nicht genug Ausdauer."


class Dxno(Player):
    def __init__(self, name, aura, luck, money, keys):
        super().__init__("dxno", self, name, aura, luck, money, keys)

    def special(self):
        self.money += 80
        return "dxno farmt Armory-Pässe (+80$)"


player1 = Player("ohnePixel", 5, 500, 3, [MAC-10 ], 0, [])
player2 = Player("dxno", 5 x 2, 100, 1, [], 0, [])

print(player1.name)
