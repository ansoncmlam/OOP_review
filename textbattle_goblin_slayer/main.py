from character import Hero, Goblin
from weapon import short_bow, iron_sword


hero = Hero("Hero", 100)

hero.equip(iron_sword)
goblin = Goblin("Goblin", 50, weapon=short_bow)

while True:
    hero.attack(goblin)
    goblin.attack(hero)

    hero.health_bar.draw()
    goblin.health_bar.draw()
    # print(f"Health of {goblin.name}: {goblin.health}")
    if goblin.health == 0:
        print(f"{goblin.name} is dead!")
        print(f"{hero.name} wins! 😂😍😂 ")
        break
    input()