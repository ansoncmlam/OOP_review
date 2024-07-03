from weapon import fists
from colorbar import HealthBar
import random

class Character: # any problem with this class? 
    
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        # self.damage = damage

        self.weapon = fists

    def attack(self, target) -> None:
        self.damage_volatility = random.randint(-2, 2)
        target.health -= self.weapon.damage + self.damage_volatility
        target.health = max(0, target.health)
        target.health_bar.update()
        print(f"{self.name} dealt ⚔️ {self.weapon.damage} damage to {target.name} with {self.weapon.name}")

class Hero(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name=name, health=health)
        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, color='green') ##pass self as entity to HealthBar class

    def equip(self, weapon)-> None:
        self.weapon = weapon ##this weapon will be assigned with Weapon class object
        print(f"{self.name} equipped a(n) {self.weapon.name}!")

    def drop(self) -> None:
        self.weapon = self.default_weapon
        print(f"{self.name} dropped his {self.weapon.name}")

class Goblin(Character):
    def __init__(self, name: str, health: int, weapon,) -> None:
        super().__init__(name=name, health=health)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color='red')
