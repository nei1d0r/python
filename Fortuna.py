print("Welcome young adventurer, to the island of Fortuna! Only the brave should be here, and only the lucky will leave...")

# List of names as index - NameNeil gives good, NameMart gives bad!
NameNeil = ['neildor', 'Neildor', 'Neil', 'neil']
NameMart = ['Martin', 'martin', 'Murphy', 'murphy', 'Squid', 'squid', 'Squiggles', 'squiggles'] 

# finding name
name = input("Please young adventurer, tell me, what is your name? ")
if name in NameNeil:
    print("")
    print("Ahhh",name,", Now that is a REAL adventurers name!")
    print("")
elif name in NameMart:
    print("")
    print(name, "erm, well that's probably the worst name i've ever heard, nothing like the legendary Neildor!")
    print("")
else:
    print("")
    print(name ,", well that's not exactly a usual name for an adventurer, but it's much better than, say, Keith or Martin!") 
    print("")

# Finding age
age = int(input("Tell me, how old are you? "))
if age <30:
    print("")
    print("Really",age,"but you have a face like an old potato? Maybe you just need sleep")
    print("")
elif age >50:
    print("")
    print("Well, hopefully you can finish this before you die... but at ",age," I wouldn't hold your breath!")
    print("")
else:
    print("")
    print("Then you should be in the prime of your life! Good luck Knight")
    print("")

#charachter selection section
# here we will give options for a player class; Warrior, Mage, Ninja
print("There are only a few types of hero in this world ")
print("")
print("Warrior")
print("Mage")
print("Ninja")
print("")

charachter = input("What type of hero are you?")
if charachter == Warrior:
    print("ENTER SOMETHING ABOUT THE WARRIOR")
elif charachter == Mage:
    print("ENTER SOMETHING ABOUT THE MAGE")
elif charachter == Ninja:
    print("ENTER SOMETHING ABOUT THE NINJA")
else:
    print("That is not the a hero! leave here") 


print("Your vision fades to black")
print("")
print("You wake up, There is a gentle trickle running down your neck. It's warm. You hope to god it's not piss. As you touch your neck a throbbing pain spreads throughout your neck, you pull your fingers to your face and see they are covered in blood, you are met with the juxtaposition of joy and fear")
print("")
print("'Where am I?'")

# here we will give options for a player class; Warrior, Mage, Ninja

#Here we can create dictionaries to assign attributes to certain charachter types
# we can implement these in the battle section to alter the values of 'randint'

#here we will set the scene of where we first arrive, and this is where we are given our options to travel
NorthList = ['North','north','N','n']
SouthList = ['South', 'south','S', 's']
EastList = ['East','east','E','e']
WestList = ['West','west','W','w']


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
