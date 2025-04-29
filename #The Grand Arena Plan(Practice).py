#The Grand Arena Plan(Practice)
import random
import time

class Warrior:
  
  def greet():
     print("Hail, traveler!")

  def __init__(self, name, strength, health):
    self.name = name
    self.strength = strength
    self.health = health

  def battle_cry(self):
    return f"{self.name} shouts: 'Victory or death!'"
  
  
  def attack (self, enemy):
    damage = random.randint(1, self.strength)
    enemy.take_damage(damage)
    print(f"{self.name} attacks {enemy.name} for {damage} damage!")

  def take_damage(self, amount):
    self.health -= amount
    print(f"{self.name} take {amount} damage! Reamaning health: {self.health}")

  def is_alive(self):
    return self.health > 0

warriors = [
    Warrior("Sir Austen", strength = 20, health = 125),
    Warrior("Dark Lork Codex", strength = 18, health =95),
    Warrior("Lady Byteblade", strength = 15, health=110),
    Warrior("Knight of Ram", strength = 17, health = 105),
]


print("The Grand Arena Opens") 

while len([w for w in warriors if w.is_alive()]) > 1:
    for warrior in warriors:
        if warrior.is_alive():
            opponents = [w for w in warriors if w.is_alive() and w != warrior]
            if opponents:
                target = random.choice(opponents)
                warrior.attack(target)
                time.sleep(1) #dramatic pause

champions = [w for w in warriors if w.is_alive()]

if champions:
    print(f"\n {champions [0].name} is the Champion of the Arena!")
else:
    print("All have fallen. The arena is silent.")