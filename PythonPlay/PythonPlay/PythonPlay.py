#class Player(object):
#    """ A player in a shooter game. """

#    def __init__(self,ammo):
#        self.ammo = ammo # choose ammo amount
#        self.lose = False   # sets self.lose to false

#    def blast(self, enemy): #creates the method blast, taking in arguement "enemy"
#        if self.lose: # currently false as per above
#            print("You were unsuccessful and did not kill the alien!\nNow the Earth was destroyed thanks to you.")
#        else:
#            print("The player blasts an enemy.") 
#            if self.ammo > 0: # if the gun is not empty
#                self.ammo -= 1 # take a bullet from the ammo
#                print("Your ammunition count is reduced by 1.")
#                enemy.die() #envokes the enemy method 'die
#            else:
#                if enemy.health == 0: # if you have no ammo, but the alien has no health...
#                    print("They're already dead, yo.")
#                else:
#                    self.lose = True # no ammo, but alien alive... sets self.lose to true, and will die.
#                    print("The alien has more health than you have ammo.")
#                    print("You run out of ammo and die!")

#class Alien(object):
#    """ An alien in a shooter game. """

#    def __init__(self, health):
#        self.health = health # health = argv above

#    def die(self):
#        if self.health > 1:
#            self.health -= 1 # -1 from health
#            print("Is that all you've got??")
#            print("Alien has",self.health,"health left\n")
#        elif self.health == 1: # heath -1 = 0 so alien dies
#            self.health -= 1
#            print("Oh no im gonna die")
#            print("Alien has",self.health,"health left\n")
#        else:
#            print("The alien is already dead.  What you're doing is unneccessary.")
#            print("Alien has",self.health,"health left\n")

## main
#print("\tThe Death of an Alien\n")

##same health and ammo
#print("\n-----You have 6 counts of ammo.-----")
#print("-----The alien has 6 health.-----\n")
#hero = Player(6)
#invader = Alien(6)
#for i in range(6):
#    hero.blast(invader)

##lower health than ammo
#print("\n-----You have 6 counts of ammo.-----")
#print("-----The alien has 5 health.-----\n")
#hero = Player(6)
#invader = Alien(5)
#for i in range(6):
#    hero.blast(invader)

##lower ammo than health
#print("\n-----You have 5 counts of ammo.-----")
#print("-----The alien has 6 health.-----\n")
#hero = Player(5)
#invader = Alien(6)
#for i in range(6):
#    hero.blast(invader)

#input("\n\nPress the enter key to exit.")

## PLAY WITH ABOVE

accList = []

class Account(object):
    def __init__(self, name, balance):
        self.balance = int(balance)
        self.name = name

    def deposit(self,amount):
        self.balance += amount
        print(self.balance)
        return self.balance

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(self.balance)
            return self.balance
        else:
            print("You do not have sufficient funds for this transaction, please contact your local branch manager")

    def transfer(self,amount,account):
        if amount >= self.balance:
            self.balance -= amount
            print(self.balance)
            account.deposit()

    def printBalance(self):
        print(self.name)
        print(self.balance)

class Savings(Account):

    def transfer(self,amount,account):
        if amount >= self.balance:
            self.balance -= amount
            print(self.balance)
            account.deposit()
        else:
            print("Not enough money")

neil = Account("Neil",1000)
neil2 = Savings("Neildor",0)

neil.printBalance()
neil.transfer(500,neil2)
neil.printBalance()
neil2.printBalance()





