# I have to create two lists here, one for the inventory of the player and one for the guard,
# if the guard has the bread then you will not be hassled by him at every door or when you return
PlayerInventory = []
GuardInventory = []

NorthList = ['North','north','N','n']
SouthList = ['South', 'south','S', 's']
EastList = ['East','east','E','e']
WestList = ['West','west','W','w']

doorlocked = "The guard moves infront of the exit","He groans 'I could do this all day, if i wasn't so bloody hungry!'"

def RoomA():
    Print("You look around and can see 4 exits; N,E,S,W. There is a guard watching each door. The cell is pretty empty all except for a piece of almost mouldy bread")
    whattodoa = input("")
    if input in NorthList:
        if 'bread' in GuardInventory:
            RoomC()
        else:
            print(doorlocked)
    elif input in EastList:
        if 'bread' in GuardInventory:
            RoomD()
        else:
            print(doorlocked)
    elif input in SouthList:
        if 'bread' in GuardInventory:
            RoomE()
        else:
            print(doorlocked)
    elif input in WestList:
        if 'bread' in GuardInventory:
            RoomB()
        else:
            print(doorlocked)
#Room B needs editing, but its just to show how the rest are to be done
def RoomB():
    Print("You look around and can see 4 exits; N,E,S,W. There is a guard watching each door. The cell is pretty empty all except for a piece of almost mouldy bread")
    whattodoa = input("")
    if input in NorthList:
        print("You cannot go this way")
    elif input in EastList:
        RoomA()
    elif input in SouthList:
        print("You cannot go this way")
    elif input in WestList:
        print("you cannot go this way")

def RoomC():
    Print("You look around and can see 4 exits; N,E,S,W. There is a guard watching each door. The cell is pretty empty all except for a piece of almost mouldy bread")
    whattodoa = input("")
    if input in NorthList:
        RoomH()
    elif input in EastList:
        print("You cannot go this way")
    elif input in SouthList:
        RoomA()
    elif input in WestList:
        print("you cannot go this way")

def RoomD():
    Print("You look around and can see 4 exits; N,E,S,W. There is a guard watching each door. The cell is pretty empty all except for a piece of almost mouldy bread")
    whattodoa = input("")
    if input in NorthList:
        print("You cannot go this way")
    elif input in EastList:
        RoomA()
    elif input in SouthList:
        print("You cannot go this way")
    elif input in WestList:
        print("you cannot go this way")

def RoomE():
    Print("You look around and can see 4 exits; N,E,S,W. There is a guard watching each door. The cell is pretty empty all except for a piece of almost mouldy bread")
    whattodoa = input("")
    if input in NorthList:
        RoomA()
    elif input in EastList:
        print("You cannot go this way")
    elif input in SouthList:
        Print("You cannot go this way")
    elif input in WestList:
        RoomF()

def RoomF():
    Print("You look around and can see 4 exits; N,E,S,W. There is a guard watching each door. The cell is pretty empty all except for a piece of almost mouldy bread")
    whattodoa = input("")
    if input in NorthList:
        print("You cannot go this way")
    elif input in EastList:
        RoomE()
    elif input in SouthList:
        RoomG()
    elif input in WestList:
        print("you cannot go this way")

def RoomG():
    Print("You look around and can see 4 exits; N,E,S,W. There is a guard watching each door. The cell is pretty empty all except for a piece of almost mouldy bread")
    whattodoa = input("")
    if input in NorthList:
        RoomF()
    elif input in EastList:
        print("You cannot go this way")
    elif input in SouthList:
        print("You cannot go this way")
    elif input in WestList:
        print("you cannot go this way")

def RoomH():
    Print("You look around and can see 4 exits; N,E,S,W. There is a guard watching each door. The cell is pretty empty all except for a piece of almost mouldy bread")
    whattodoa = input("")
    if input in NorthList: # Need to make a key code
        if key in PlayerInventory:
            print("You made it out of the castle")
        else:
            print("You do not have the key for this door")
    elif input in EastList:
        print("You cannot go this way")
    elif input in SouthList:
        RoomC()
    elif input in WestList:
        print("you cannot go this way")
#We still need to make a command to pick the bread up and give the bread away