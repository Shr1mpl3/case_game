from __future__ import annotations
import random
from inventory import Inventory

class Player:
    def __init__(self, name: str, gender: str, endurance: int, dmg: int, hp: int, luck: int, money: int, key: int):
        self.name = name
        self.gender = gender
        self.endurance = endurance
        self.dmg = dmg
        self.hp = hp
        self.luck = luck
        self.money = money
        self.key = key
        self.inventory = Inventory()

    def attack(self):
        bonus = random.randint(0, self.luck // 5)
        return self.dmg + bonus

    def is_alive(self):
        return self.hp > 0


class OhnePixel(Player):
    def __init__(self, gender, endurance, dmg, hp, luck, money, key):
        super().__init__("OhnePixel", gender, endurance, dmg, hp, luck, money, key)

    def special(self):
        if self.endurance >= 5:
            self.luck += 10
            self.endurance -= 5
            return "OhnePixel schreit: GOLD GOLD GOLD! (+10 Glück)"
        return "Nicht genug Ausdauer."


class Dxno(Player):
    def __init__(self, gender, endurance, dmg, hp, luck, money, key):
        super().__init__("dxno", gender, endurance, dmg, hp, luck, money, key)

    def special(self):
        self.money += 80
        return "dxno farmt Armory-Pässe (+80$)"
