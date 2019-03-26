#Here we can create dictionaries to assign attributes to certain charachter types
# we can implement these in the battle section to alter the values of 'randint'

'''
# Battle code

from random import randint
# Charbattle is any charachter capable of entering a fight.
class Player1(Warrior):
    health = 0
    strength = 0 
    agility = 0
    defence = 0
    magic = 0
    total = 0
    
    def battle(self):
        self.strength = randint(1,10) 
        self.agility = randint(1,10)
        self.defence = randint(1,10)
        self.magic = randint(1,10)
        self.total = self.strength + self.agility + self.skill + self.magic

class Player1(Mage):
    health = 0
    strength = 0 
    agility = 0
    defence = 0
    magic = 0
    total = 0
    
    def battle(self):
        self.strength = randint(1,10) 
        self.agility = randint(1,10)
        self.defence = randint(1,10)
        self.magic = randint(1,10)
        self.total = self.strength + self.agility + self.skill + self.magic

class Player1(ninja):
    health = 0
    strength = 0 
    agility = 0
    defence = 0
    magic = 0
    total = 0
    
    def battle(self):
        self.strength = randint(1,10) 
        self.agility = randint(1,10)
        self.defence = randint(1,10)
        self.magic = randint(1,10)
        self.total = self.strength + self.agility + self.skill + self.magic


class Enemy(Minator):
    strength = 0 
    agility = 0
    defence = 0
    magic = 0
    total = 0
    
    def battle(self):
        self.strength = randint(1,9) 
        self.agility = randint(1,9)
        self.defence = randint(1,9)
        self.magic = randint(1,9)
        self.total = self.strength + self.agility + self.skill + self.magic

class Enemy(Necromancer):
    strength = 0 
    agility = 0
    defence = 0
    magic = 0
    total = 0
    
    def battle(self):
        self.strength = randint(1,9) 
        self.agility = randint(1,9)
        self.defence = randint(1,9)
        self.magic = randint(1,9)
        self.total = self.strength + self.agility + self.skill + self.magic

class Enemy(Shadow Stalker):
    strength = 0 
    agility = 0
    defence = 0
    magic = 0
    total = 0
    
    def battle(self):
        self.strength = randint(1,9) 
        self.agility = randint(5,9)
        self.defence = randint(1,9)
        self.magic = randint(1,9)
        self.total = self.strength + self.agility + self.skill + self.magic

neildor = Player1()
murphy = Enemy()

neildor.battle()
murphy.battle()

print("Neildor unleashes his fury, with a combined total of: ", (int(neildor.total)))
print("Murphy unleashes his fury, with a combined total of: ", (int(murphy.total)))

if neildor.total > murphy.total:
    print("Neildor annhialated Murphy in one blow!")
elif neildor.total < murphy.total:
    print("Murphy got lucky this time!")
else:
    print("It was a draw this time")
'''
