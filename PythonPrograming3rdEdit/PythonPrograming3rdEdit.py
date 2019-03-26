#print('\a') # alarm bell
#a='Hello'
#b=' young sir'
#c = (a + b)            # concatinating strings, can be done by 'text' + 'text' or as shown
#print(c)            # Prints a+b
#print(c*10)         # prints a+b 10 times straight after eachother
#for i in range(10): # prints a+b 10 times each on a new line
#    print(c)

#quotation manipulation
# -------------------------------------------------------------------------------------------------
#quote = 'I think there is a world market for maybe 5 computers'
#print(quote)
#print(quote.upper())    # UPPERCASE
#print(quote.lower())    # lower case
#print(quote.title())    # easch word starts with capital
#print(quote.capitalize()) # capitalises first letter
#print(quote.swapcase())   # changes upper to lower and lower to upper
#print(quote.strip())      # removes all spaces, tabs and newlines at BEGINNING AND END
#print(quote.replace('5','millions of')) # temporarily replaces the string, unless variable is assigned
#print(quote)
#quote = quote.replace('5','millions of',10) # variable changed to replaced value ('old','new',max amount of changes
#print(quote)
# -------------------------------------------------------------------------------------------------
# Assignment operators
#x *= 5      # x = x * 5
#x /= 5      # x = x / 5
#x %= 5      # x = x % 5  etc...
#x += 5
#x -= 5
# --------------------------------------------------------------------------------------------------
# how many seconds old are you

#age = int(input('age: '))
#seconds = age * 365 * 24 * 60 *60
#print('you are',seconds,'old')

# -------------------------------------------------------------------------------------------------
# Generating random numbers DICE GAME
# use the randint and randrange functions to complete

#from random import randint, randrange
#dice1 = randint(1,6)
#dice2 = randrange(6+1) # Rand range goe from 0 up to but not including the number called
#total = dice1 + dice2

#print('You rolled a',dice1,'and a',dice2,'for a total of',total)

#password = 'password'
#guess = input('What is the magic word? ')
#alarm = '\a'
#if guess == password:
#    print('Password Accepted')
#else:
#    print('ahh ahh ahhhhh, you didn\'t say the magic word!!')
#    print(alarm)

# ----------MOOD COMPUTER PROGRAM pg60, images as responses to if,elif
#from random import randint
#print('i sense your mood you are')
#for i in range(5):
#    mood = randint(1,3)
#    if mood == 1:
#        print('''
#        --------
#        - -  - -
#        --    --
#        - ---- -
#        --------
#        ''')
#    elif mood == 2:
#        print('''
#        --------
#        - -  - -
#        -      -
#        - ---- -
#        --------
#        ''')
#    elif mood == 3:
#        print('''
#        --------
#        - -  - -
#        - ---- -
#        --    --
#        --------
#        ''')

## ----------3 YEAR OLD SIMULATOR
#answer = '' # This is a sentry variable, initialised before the loop, or the 'answer' in the while loop would not be defined
#while answer != 'Because':  # make sure the sentry variable is not TRUE or the while loop will not run.. eg answer = 'Because'
#    answer = input('Why??')

# ------------THE LOSING BATTLE PROGRAM

#print('Your lone hero is supported by a massive army of trolls')
#print('Their decaying green bodies stretch out. Melting into the horizon')
#print('Your hero unsheaths his sword for the last fight of his life. \n')

#health = 10
#trolls = 0
#damage = 3

#while health > 0:      # asked to find problem was initially 'while health != 0', healthwould never EQUAL 0
#    trolls += 1
#    health -= damage

#    print('your hero swings and defeats an evil troll,'\
#        'but takes',damage,'damage points. \n')

#print('alas, your hero is no more')

# -----------------MAITRE D' Program

#print('Welcome to the chateau D\' food')
#print('it seems we are quite full this evening')
#money = float(input('how many dollars do you slip the matre D\'?'))
#if money:   # basically if the value is not 0 as zero is FALSE, however it can be negative and still pass!!
#    print('Ahh, a table has just opened up sir')
#else:
#    print('No table i am afraid')

# ---------CREATING INTENTIONAL INFINITE LOOPS - INTRODUCING THE FINICKY COUNTER PROGRAM

#count = 0
#while True:
#    count += 1   # count = count + 1 
#    if count > 10000:    # this condition will break the count loop, using BREAK below...
#        break
#    if count == 5: # Skips 5, and continues with the loop
#        continue
#    print(count)
#input('Press the enter key to exit')
## Break and continue may make it difficult to see the flow of a loop, USE SPARINGLY

# USING COMPOUND CONDITIONS - combining simple conditions together
# EXCLUSIVE NETWORK PROGRAM

#members = ['Neil','Nic','Jeff']
#passcode = ['dog','cat','squid']
#name = input('Name: ')
#password = input('Password: ')

#if name in members and password in passcode: # one way off using compound conditions, but any name
#    print('welcome')                         # will work with any password if they are in the list
#else:
#    print('You are not welcome')

## BOOK VERSION OF EXCLUSIVE NETWORK PROGRAM
#print('\tExclusive Network Program')
#print('\tMembers Only!\n')

#security = 0
#username = ''    #defines username for use in the while loop
#while not username:
#    username = input('Username: ')

#password = ''    #defines password for use in the while loop
#while not password:
#    password = input('Password: ')

#if username == 'Neil' and password == 'neildor':
#    print('Hi Lord Dor')
#    security = 10
#elif username == 'Jeff' and password == 'jeff':
#    print('Hey Jeff!')
#    security = 3
#elif username == 'Guest' and password == 'guest':
#    print('Welcome Guest')
#    security = 1
#else:
#    print('Login failed, security on the way')

# CREATING ALGORITHMS WITH PSEUDO CODE - ie BUILD A STUDENT TIMETABLE
# PSEUDO CODE IS BASICALLY A PLAIN ENGLISH STEP BY STEP GUIDE...
# MAKE WINDOW
# MAKE BUTTON
# WHEN BUTTON PRESS OPEN IMPORTANT INFO DOCUMENT...

# Use this method to help break down problems into smaller finite steps

# RETURNING TO THE GUESS MY NUMBER GAME - Pg 83
# Planning the program in pseudocode
# ---------------------------------------------------------------------------
# pick a random number
# while the player hasnt guessed the number
#   let the player guess
#   tell the player if too high or too low
# congratulate the player
# ---------------------------------------------------------------------------

#from random import randint
#print('guess a number between 1 and 100')
#number = randint(1,100)
#tries = 1

#while True:
#    guess = input('Pick a number between 1 and 100: ')
#    if int(guess) > 100 or int(guess) < 1:
#        print('number out of range')
#    elif int(guess) > number:
#        print('your guess was too high')
#    elif int(guess) < number:
#        print('Your guess was too low')
#    else:
#        break
#    tries += 1
 
#print('CONGRATULATIONS, THAT WAS CORRECT, THE ANSWER WAS',number,'you guessed in',tries,'tries!')
#input('press any key to exit')
## sounds daft but i built this without looking at the book!!

# CHALLENGE
# Flip a coin 100 times, get computer to tell you how many of each

#from random import randint
#heads = 0
#tails = 0

#for i in range(100):
#    side = randint(1,2)
#    if side == 1:
#        heads += 1
#    else:
#        tails += 1
#print('There were',heads,'heads, and',tails,'tails')

# -----------------------------------CHALLENGE-------------------------------------------
# you pick a number and the computer has to guess - write pseudocode first

#from random import randint
#think of a number
#computer guesses from 1 to 100
#if too low, computer guesses >guess<100
#if too high, computer guesses <guess >1

#print('is your number ',guess)
#min_value = 1
#max_value = 100
#guess = randint(min_value,max_value)    # by setting randint range to min,max guesses can be factored into 
#while guess:                            # next guess range... SEE IF STATEMENTS
#    guess = randint((min_value+1),(max_value-1))
#    print('is your number ',guess)
#    response = input('')
#    if response == 'l':
#        min_value = guess        
#    if response == 'h':
#        max_value = guess
#    if response == 'correct':
#        break

# LOOPS STRING AND TUPLES - THE WORD JUMBLE GAME    

# takes a word and prints it off in order on a new line
#word = input('pick a word')
#for i in word:
#    print(i)      # i can be anything you like, such as letter, this becomes the iterant variable

## Counting using loops
#print('counting')
#for i in range(10):
#    print(i,end=', ')   # adding end='' makes numbers all on one line

## counting by fives
#print('\ncounting in fives')
#for i in range(10):
#    print(i*5,end=', ') # can be done this way or...

#print('\ncounting in fives')
#for i in range(0,50,5):     # LOWEST,HIGHEST,GAP
#    print(i,end=', ')

## counting in reverse
#print('\ncounting in reverse')
#for i in range(10,0,-1):    # start value, end value, -1 means to reverse count...tells program to go to
#    print(i,end=', ')       # start point and subtract 1 each time

# USING SEQUENCE OPERATORS AND FUNCTIONS WITH STRINGS
# strings are one type ofsequence made up of individiual charachters
# THE MESSAGE ANALYSER PROGRAM

#message = input('Enter a message: ')
#message = message.upper()    # changed it to upper case for no reason :)
#print(message)
#length = len(message)    # gets charachters in mesage
#print('\n the length of your message is',length,'charachters')
#print('\n the most common letter in the English language, \'e\'')
#if 'e' in message:   # you can use 'in' to check if an element is a member of a sequence
#    print(' is in your message')
#else:
#    print('is not in your message')

# RANDOM ACCESS PROGRAM
# uses INDEXING which, can randomly access any part of a string. you specify the element of the strings
# position or 'index' and the program will call it for you

#import random
#word = 'index'
#print('The word is',word)

#high = len(word)
#low = -len(word)

#for i in range(10):
#    position = random.randrange(low,high)
#    print('Word[',position,']\t',word[position]) 
#    # picks a random position from the string and shows it's index
#    # -1 means the LAST element (-0) does not exist
#print(low) # returns -5.. just to see! . just like putting a negative infront of a number in maths

# UNDERSTANDING STRING IMMUTIBILITY

#word = 'game'
#word[0] = 'l'      # strings cannot be change, however the variable can be re-assigned (this is fundamentally different)
#print(word)        # gives error; 'str' object does not support assignment

# THE NO VOWELS PROGRAM - takes user input message and prints it without vowels

#message = input('Enter a message: ') #gets message from user
#new_message = ''                   # creates new empty message
#VOWELS = 'aeiou'                   # Variable names in CAPS are constants, and are not meant to change

#print()
#for letter in message:
#    if letter.lower() not in VOWELS:      # A is not the same as a... so you must standardise the string
#        new_message += letter             # new_message = new_message + letter(in message) per iteration
#        print('a new string has been created',new_message) # can use this to re format arguments (pg104)

#print('\nyour message without vowels is',new_message)

## name == winner
## john == John... would not match due to case difference
## name.lower() == winner.lower()
## john == John... would match as case difference negated

## SLICING STRINGS - PIZZA SLICER PROGRAM

#word = 'pizza'
#print(
#'''
#Slicing 'cheat sheet'
#0   1   2   3   4   5
#+---+---+---+---+---+
#¦ p ¦ i ¦ z ¦ z ¦ a ¦
#+---+---+---+---+---+
#-5  -4  -3  -2  -1
#'''
#)
#print('Enter the beginnind and ending index for your slice of pizza')
#print("Press the enter key at 'start' to exit.")
#start = None # assigns a FALSE placeholder value when treated as a condition. used here to initialize while loop
#while start!= " ":     # if i don't type and press enter the loop will not run (because of 'None' being FALSE)
#    start = (input("\nStart: "))
#    if start:
#        start = int(start)    # pick a starting index number
#        finish = int(input("Finish: "))   # pick an ending index number
#        print("word[", start, ":",finish, "] is",end=" ") # eg word 3:4 is z   ... 
#        print(word[start:finish])
## shortcuts... [1:] 1 to end   [:3] start to 3   [:] all  

# ------------- THE HEROES INVENTORY GAME - CREATING TUPLES

#inventory = () # creates an empty tuple or in this case inventory list

#if not inventory: # Treats tuple as a condition
#    print("You are empty handed.") # basically if your inventory is empty it'll tell you

#input("Press the enter key to continue.")

#create a tuple with some items

#inventory = ("Sword",
#             "Armor",
#             "Shield",
#             "Healing potion")
## print the tuple
#print("\nThe tuple inventory is: ")
#print(inventory)

## Print each element in tuple
#print("\nYour items:")
#for item in inventory: # iterates through each item, executes print on new line wach time
#    print(item)

# HERO'S INVENTORY 2.0
# Inventory counted, indexed and sliced

#inventory = ("Sword",
#             "Armor",
#             "Shield",
#             "healing potion")
#print("\nThe tuple inventory is: ")
#print(inventory)
#print("\nYour items:")
#for item in inventory:
#    print(item)

## Get lenght of inventory list
#print("You have",len(inventory),"items in your inventory")  # in this case will indicate 4

## Using operators with tuples
#if 'healing potion' in inventory:
#    print("You will live to fight another day")
## Indexing tuples - display one item through an index
#index = int(input("\nEnter the index number for an item in your inventory"))
#print("At index",index,"is",inventory[index])

## Display a slice
#start = int(input("\nEnter the index number to begin a slice: "))
#finish = int(input("\nEnter the index number to end the slice: "))
#print("Inventory, [",start,":",finish,"] is",end=" ")
#print(inventory[start:finish])   # 1:3  prints armour and shield

## Understanding Tuple immutability

## if i write inventory[0] = 'Battle Axe'      i get a traceback error, object doesn'tsuppot item assignment
## You CAN create new tuples from existing ones though...

## Concatinate 2 tuples
#chest = ("gold","gems")
#print("You find a chest, it contains: ")
#print(chest)
#print("\nYou add the contents of the chest to your inventory")
#inventory += chest
#print(inventory) # prints everything

# -----------------------------------------------------------------------------------------------

##BACK TO THE WORD JUMBLE GAME pg116.. computer picks a random word then jumbles it
#import random

## create a sequence of words to choose from
#WORDS = ("python","jumble","easy","difficult","answer","xylophone")

## Pick one word randomly from the sequence
#word = random.choice(WORDS) # random.choice is new... it picks a random element

## create a variable to use later to see if the guess is correct
#correct = word

## PSEUDOCODE
## CREATE AN EMPTY JUMBLE WORD
##   EXTRACT A CHOSEN LETTER FROM THE JUMBLE WORD
##   ADD THE RANDOM LETTER TO THE JUMBLE WORD

## Creating an empty jumble word
#jumble = " "

## Setting up the loop
#while word:     # set this up so the loop will continue until word is equal to empty string
#    position = random.randrange(len(word)) # will select a random letter from word
#    jumble += word[position]
#    word = word[:position] + word[(position + 1):] # creates a new version of the word, minus the letter in
#                                                   # the position 'position' :position every letter upto
#                                                   # but not including.. position+1: every letter after
#                                                   # the letter in position 'position'
## Welcome the player
#print("""
#/t/t/tWelcome to Word Jumble!
#/t/tUnscramble the letters to make a word.
#\t(Press the enter key at the prompt to quit.)
#""")
#print("The jumble is",jumble)

## Getting the player to guess
#guess = input("/nWhat is your guess: ")
#while guess != correct and guess != "": # until correct or until enter is pressed without typing
#    print("Sorry, that is not the right answer")
#    guess = input("What is your guess: ")
## at this point the player is correct or has quit the game.. hence the if statement
#if guess == correct:
#    print("Congratulations, that is correct!")

## Ending the game
#print("\nThanks for playing")
#input("\nPress Enter to exit")

# --------------------------------------CHALLENGES-Ch4-------------------------------------------
# 1. write a program that counts for the user, let user choose start, end and increment
# 2. create a program that takes a message from the user and prints it backwards
# 3. imporve word jumble so each word is paired with a hint the player should be able to see the hint if stuck
# 4. add scoring system to reward player for not using hint
# 5. create a game where the computer picks a word and the player has to guess that word. The computer tells 
#    the player how many letters are in the word, the player get 5 chances to ask if the letter is in the 
#    word, the computer can respond y/n

#   1.
#start = int(input("Pick a start number: " ))
#finish = int(input("Pick an end number: "))
#increment = int(input("Choose an increment value: "))
#for i in range(start,finish,increment):
#    print(i) 

#   2.
#message = input("Type something, and i will reversulate it: ")
#message = message[::-1]     # no reverse function, so :: means start to finish, -1 reverse
#print(message)

#   3 & 4.

#import random
#WORDS = ("python","jumble","easy","difficult","answer","xylophone")

#word = random.choice(WORDS) 

#correct = word
#jumble = " "

#while word:
#    position = random.randrange(len(word))
#    jumble += word[position]
#    word = word[:position] + word[(position + 1):]

#score = 0

#print("""
#\t\t\tWelcome to Word Jumble!
#\t\tUnscramble the letters to make a word.
#\t(Press the enter key at the prompt to quit.)
#""")
#print("The jumble is",jumble)

#guess = input("/nWhat is your guess: ")
#guess = guess.lower()
#lst = range(len(jumble))
#hint = " "*len(jumble)

#while True: 
 
#    if guess == correct:
#        print("Congratulations, that is correct!")
#        break
#    elif guess == '?':
#        i = random.choice(lst)
#        print(correct[i],"is the",i+1,"letter")
#        score += 1
#        guess = input("/nWhat is your guess: ")
#    elif guess == "":
#        print("Better luck next time")
#        break
#    else:
#        print("Sorry, that\'s not it... try again.")
#        guess = input("/nWhat is your guess: ")

#print("\nThanks for playing")
#input("\nPress Enter to exit")

#   5.

##computer picks random word
##player guesses word
##computer tells player length of word
##player gets 5 chances to ask if a letter is in word
##computer can respond y/n
#import random
#WORDS = ("python","jumble","easy","difficult","answer","xylophone")
#word = random.choice(WORDS)
#print(word)
#print("The word is",len(word),"letters long")
#guess = 0

#for i in range(5):
#    letter = input("Guess a letter in the word: ")
#    letter = letter.lower()
#    if letter == word:
#        break                                         # NO HELP !!! WOOOP
#    elif letter in word:
#        print("Yes, that is in the word")
#        guess += 1
#    else:
#        print("No, that is not in the word")
#        guess += 1
#if guess == 5:
#    print("\n\nYou ran out of guesses")
#    print("\nThe word was...",word)
#elif guess < 5:
#    print("\nCONGRATULATIONS!!!")
#    print("The number of guesses you took was",guess)

# ------------------------- LISTS, DICTIONARIES AND THE HANGMAN GAME--------------------------------

# Hero's inventory 3.0
# COPY PREVIOUS HERO STUFF TO PLAY

# Inventory counted, indexed and sliced

#inventory = ["Sword",
#             "Armor",
#             "Shield",
#             "healing potion"]
#print("\nThe tuple inventory is: ")
#print(inventory)
#print("\nYour items:")
#for item in inventory:
#    print(item)

## Get lenght of inventory list
#print("You have",len(inventory),"items in your inventory")  # in this case will indicate 4

## Using operators with tuples
#if 'healing potion' in inventory:
#    print("You will live to fight another day")
## display one item through an index
#index = int(input("\nEnter the index number for an item in your inventory"))
#print("At index",index,"is",inventory[index])

### Display a slice
#start = int(input("\nEnter the index number to begin a slice: "))
#finish = int(input("\nEnter the index number to end the slice: "))
#print("Inventory, [",start,":",finish,"] is",end=" ")
#print(inventory[start:finish])   # 1:3  prints armour and shield

## Concatinate 2 tuples
#chest = ["gold","gems"]
#print("You find a chest, it contains: ")
#print(chest)
#print("\nYou add the contents of the chest to your inventory")
#inventory += chest
#print(inventory) # prints everything

## Assigning new elements by index
#print("You trade your sword for a crossbow")
#inventory[0] = "crossbow"
#print("Your inventory is now")
#print(inventory)

## Assigning new list slice
#print("You use your gold and gems to buy an orb of future telling")
#inventory[4:6] = ["orb of future telling"]
#print("Your inventory is now")
#print(inventory)

###Add item using inventory.append()
##print("You use your gold and gems to buy an orb of future telling")
##inventory.append("Chicken")
##print("Your inventory is now")
##print(inventory)

###Add item using inventory.insert() in certain position
##print("You use your gold and gems to buy an orb of future telling")
##inventory.insert(-1,"Banana") # -1 will put it in as the penultimate value
##print("Your inventory is now")
##print(inventory)

### Deleting a list element
##del inventory[3:] # this will delete everything from 3 onwards (healing potion onwards)
##print(inventory)

#print("In the battle your shield was destroyed")
#del inventory[2]
#print("Your inventory is:")
#print(inventory)

### Deleting a slice
#print("Your crossbow and armour are stolen by thieves")
#del inventory[:2] # this will delete everything from 3 onwards (healing potion onwards)
#print(inventory)

# List elements allow you to manipulate them, so you can add, delete based on value, sort the list and 
# even reverse it etc...

# -----------------------------------THE HIGH SCORES PROGRAM--------------------------------------

## setting up the program
#scores = []
#choice = None # None simply signifies 'empty'

## display the menu

#while choice != "0":
#    print("""
#    High Scores
#    0. Exit
#    1. Show scores
#    2. Add a score
#    3. Delete a score
#    4. Sort score
#    """)
#    choice = input("Choice: ")
#    print()
#    if choice == "0":  # ends loop as score != 0 is False
#        print("Goodbye")
#    elif choice == "1":
#        print("High scores")
#        for score in scores: # will iterate through the scores
#            print(score)
            
#    elif choice == "2":
#        score = int(input("What score did you get?")) # converts user value to int 
#        scores.append(score)                          # appends value to list
#    elif choice == "3":
#        score = int(input("What score did you want to remove?"))
#        if score in scores:             # checks if the score is in the list
#            scores.remove(score)        # removes the score from the list
#        else:
#            print(score,"Is not in the list")
#    elif choice == "4":
#        scores.sort(reverse=True)         # or you could put scores.sort() to just sort in normal order
#        for score in scores:
#            print(score)
#    else:
#        print("Sorry", choice, "is not a valid choice")

# -------------List methods

#append(Value)      adds value to end of list
#sort()             sorts list smallest value first
#reverse()          reverses order of list   (BUT NOT BY VALUE, JUST THE ORDER)
#count(Value)       Tells you how many items in list
#index(Value)       returns the first position number of where Value occurs
#insert(i,Value)    inserts value at position 1
#pop([i])           removes and returns the value from position[i], if i not specified, removes last element
#remove(value)      removes value based on value

#---------------- High scores program 2.0

# Creating nested sequences

#nested = [("First"),("Second","Third"),("Fourth","Fifth")] # only has 3 elements
#print(nested)

#scores = [("Moe",1000),("Larry",1500),("Curly",3000)]
#print(scores) # each element is a tuple, each tuple has 2 elements

## AVOID nested sequences in sequences in sequences etc....
## eg, nested = ("deep"("deeper"(""Deepest, "still deepest))) ... makes it confusing!!

## Accessing nested elements

#print(scores[0])        # prints ("Moe",1000)
#print(scores[0][1])     # prints 1000

## Unpacking a sequence - works with any sequence type (ensure you have the same amount of values as elements)

#name, score = ("Shemp", 175)
#print(name)     # prints 'shemp'
#print(score)    # prints 175

# ----------- Setting up the program ---- High score 2.0
# ----------- Using packed variables ----

#scores = []
#choice = None

#while choice != "0":
#    print("""
#    0. Exit
#    1. List Scores
#    2. Add Scores
#    """)
#    choice = input("What is your choice? ")
    
#    if choice == "0":
#        print("Goodbye!")
#    elif choice == "1":
#        print("High Scores")
#        print("NAME\t\tSCORE" )         # sets up a header
#        for entry in scores:             # loops through entries - defined in next step
#            score,name = entry          # unpacks the tuple
#            print(name,"\t\t",score)    # prints unpacked tuple values
#    elif choice == "2":
#        name = input("What is your name? ")
#        score = int(input("What was your score? "))
#        entry = (score,name)        # creates unpacked values for entry
#        scores.append(entry)        # adds the packed values for entry
#        scores.sort(reverse=True)   # sorts in ascending order
#        scores = scores[:5]         # Keeps only the top 5 scores
#    else:
#        print(choice,"is not a valid option")
#        choice = input("What is your choice? ")

## SHARED REFERENCES -------------------------------

#Neil = ["White T-shirt","Black Jeans","Brown Trainers"]   # Defines me
#Neildor = Neil          # Defines Neildor as Neil (A bit like a nickname, same person, different name)
#Huspig = Neil           # Again different name, same person... depending on who references me

## If i change the value of Neil, then regardless of who calls me they get the same version of me
#print(Neildor)
#print(Huspig) 

## if Nic asks me to change my shirt, then everybody else will see that change even though they didn't 
## tell me to change... after all, it's still me!
#Neil[0] = "Black T-shirt"
#print(Neildor)

## BEWARE OF THIS FOR MUTABLE VALUES AS IT WILL CHANGE VALUES FOR ALL, TO AVOID YOU CAN MAKE A COPY
## THROUGH SLICING

#Neil = ["White T-shirt","Black Jeans","Brown Trainers"] 
#Neildor = Neil[:] # creates a copy of the list under the name 'Neildor'
#Neildor[2] = "White Trainers"
#print(Neildor)
#print(Neil)

# --------------- USING DICTINARIES ----------------------

#geek = {"404": "clueless.  From the web error message 404, meaning page not found.",
#        "Googling": "searching the Internet for background information on a person.",
#        "Keyboard Plaque" : "the collection of debris found in computer keyboards.",
#        "Link Rot" : "the process by which web page links become obsolete.",
#        "Percussive Maintenance" : "the act of striking an electronic device to make it work.",
#        "Uninstalled" : "being fired.  Especially popular during the dot-bomb era."}

## creates a dictionary named 'geek' it has 6 pairs, called items. each item consists of a key : Value
## the 'key' is literally the key to getting the value

## --- Accessing dictionary values --- commonly using a key to get its value
#print(geek["404"]) # prints the value for 404
#print(geek["Link Rot"]) # etc...
## if you try to access a key that doesn't exist in the dictionary you get traceback error
##print(geek["Chicken Soup"]) # gives a key error

## TESTING FOR A KEY WITH THE OPERATOR BEFORE RETRIEVING A VALUE
#if "Chicken Soup" in geek:
#    print(geek["Chicken Soup"])
#else:
#    print("That is not a value in the dictionary")

# using the get() method to retrieve a value

#print(geek.get("Chicken Soup","I have no idea. ")) # if the value is not in the dictionary, the function
#                                                # goes to the set default value, in this case "I have no idea"
## To use get() simply type the search term with an OPTIONAL default value
#print(geek.get("Chicken Soup"))
## this prints (None)
#if (geek.get("Chicken Soup")) == None: # JUST PLAYING WITH CONDITIONS
#    print("Poop")

## --------- Setting up the program GEEK DICTIONARY

#choice = None
#while choice != "0":

#    print(
#    """
#    Geek Translator
    
#    0 - Quit
#    1 - Look Up a Geek Term
#    2 - Add a Geek Term
#    3 - Redefine a Geek Term
#    4 - Delete a Geek Term
#    """
#    )
    
#    choice = input("Choice: ")
#    print()

#    if choice == "0":
#        print("Goodbye!")
#    elif choice == "1":         # GETTING A VALUE
#        term = input("What term do you want to transtlate")
#        if term in geek:
#            definition = geek[term]
#            print("\n",term,"means",definition) 
#        else:
#            print("sorry",term, "is not in the dictionary.. Yet")
#    elif choice == "2":         # ADDING A KEY-VALUE PAIR
#        term = input("What term do you want me to add? ")
#        if term not in geek:
#            definition = input("\nWhat\'s the definition?: ")
#            geek[term] = definition
#            print("\n",term,"has been added")
#        else:
#            print("That term is already in the dictionary")
## computer asks for a term, if it doesnt already exist it asks for a definition and pairs it
#    elif choice == "3":   # REPLACING A KEY VALUE PAIR
#        term = input("What term do you want to re-define? ")
#        if term in geek:
#            definition = input("\nWhat\'s the new definition? ")
#            geek[term] = definition
#            print("\n",term,"has been re-defined")
#        else:
#            print("That term is not in the dictionary, try adding it")
#    elif choice == "4":
#        term = input("What term did you want to delete?")
#        if term in geek:       # checks if inputted term exists
#            del geek[term]     # deletes term from dictionary
#            print("\n",term,"has been deleted")
#        else:
#            print("That term was not in the dictionary")
#    else:
#        print("Sorry",choice,"is not a valid choice")

# A dictionary cannot contain 2 items with the same key
# a key HAS TO BE IMMUTABLE, it can be a string, number or tuple though
# Values dont have to be unique and can be MUTABLE or IMMUTABLE

# geek.get(key,[default])        returns the value of key, or default message - if no default, returns none
# geek.keys()                    returns a view of all of the keys in a dictionary
# geek.values()                  returns a viewof all values in dictionary
# geek.items()                   returns all items in dictionary in tuple form


# ------------------ BACK TO THE HANGMAN GAME

## Setting up the game
#import random

##creating constants
## constants
#HANGMAN = (
#"""
# ------
# |    |
# |
# |
# |
# |
# |
# |
# |
#----------
#""",
#"""
# ------
# |    |
# |    O
# |
# |
# |
# |
# |
# |
#----------
#""",
#"""
# ------
# |    |
# |    O
# |   -+-
# | 
# |   
# |   
# |   
# |   
#----------
#""",
#"""
# ------
# |    |
# |    O
# |  /-+-
# |   
# |   
# |   
# |   
# |   
#----------
#""",
#"""
# ------
# |    |
# |    O
# |  /-+-/
# |   
# |   
# |   
# |   
# |   
#----------
#""",
#"""
# ------
# |    |
# |    O
# |  /-+-/
# |    |
# |   
# |   
# |   
# |   
#----------
#""",
#"""
# ------
# |    |
# |    O
# |  /-+-/
# |    |
# |    |
# |   | 
# |   | 
# |   
#----------
#""",
#"""
# ------
# |    |
# |    O
# |  /-+-/
# |    |
# |    |
# |   | |
# |   | |
# |  
#----------
#""")

## creating the max number of wrong guesses
#MAX_WRONG = len(HANGMAN) - 1 # -1... as the gallows are already displayed, player gets 7 goes

## Creating words list
#WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON")

## initialise variables
#word = random.choice(WORDS)

#so_far = "-" * len(word) # prints a dash for each letter depending on the word
#wrong = 0
#used = [] # creates an empty list to store guessed letters

## Creating the main loop pg152
#print("Welcome to hangman, good luck! ")
#while wrong < MAX_WRONG and so_far != word:

#    print(HANGMAN[wrong])
#    print("You\'ve used the following letters:",used)
#    print("\nSo far, the word is:\n",so_far) # this displays the partially guessed word

## Getting the player's guess
#    guess = input("Enter your guess: \n")
#    guess = guess.upper()

#    while guess in used: # checks if letter has alread been guessed
#        print("You\'ve already used that letter")
#        guess = input("Enter your guess: \n")
#        guess = guess.upper()

#    used.append(guess) # adds the guess to the list

## Checking the guess
#    if guess in word:
#        print("\nYES!",guess,"is in the word!")
#    # create a new so_far to include the guess
#        new = ""
#        for i in range(len(word)):
#            if guess == word[i]:
#                new += guess
#            else:
#                new += so_far[i]
#        so_far = new     # see shared references
#    else:
#        print("\nSorry,",guess,"is not in the word.")
#        wrong += 1

## Ending the game
#if wrong == MAX_WRONG:
#    print("You have ran out of guesses")
#else:
#    print("You guessed it!!!")

#print("The answer was",word)

# ------------------------ Challenges ---------------------------

#   1. create program that prints a list of words in a random order, whilst not repeating ay words
#   2. player gets 30 points to distribute between, Strength, Health, Wisdom, Dexterity, can take from pool
#      and put back in to spend elsewhere
#   3. Who's your Daddy, enters a name and brings back name if their father. 
#      User can add, replace, delete son father pairs
#   4. Improve who's your daddy, by adding grandfathers too!!

# ---------Challenge 1.
#import random

#WORDS = ["Neil","Nic","Evelyn","Matilda","Bella","Sirius"]
#random.shuffle(WORDS)     # random.shuffle from random will simply re-order the list of words (Mist be a mutable list)
#print(WORDS)

# ---------Challenge 2.

#attributes = {"strength": int("0"),
#             "health": "0",
#             "wisdom": "0",
#             "dexterity": "0"}

#pool = 30                   # sets max points to 30
#choice = None               # choice = empty
#print("The Making of a Hero !!!")
#print(attributes)
#print("\nYou have", pool, "points to spend.")

#while choice != "0":
#    # list of choices
#    print(
#    """
#    Options: 

#    0 - End
#    1 - Add points to an attribute
#    2 - remove points from an attribute
#    3 - Show attributes
#    """
#    )
#    choice = input("Choose option: ") # gets the player to choose from options list
#    if choice == "0":                 #exits
#        print("\nYour hero stats are:")
#        print(attributes)
#        print("Good-Bye.")
#    elif choice == "1":
#        print("\nADD POINTS TO AN ATTRIBUTE")
#        print("You have", pool, "points to spend.")
#        print(
#        """
#        Choose an attribute:
#           strength
#           health
#           wisdom
#           dexterity
#        """
#        )
#        at_choice = input("Your choice: ") # gets user to choose which skill to add to
#        if at_choice.lower() in attributes: # converts choice into lowercase and checks if it is in attribute list
#            points = int(input("How many points do you want to assign: "))
#            if points <= pool: # if the number of points is less than/equal to pool total then proceed
#                pool -= points # pool = pool - points 
#                result = int(attributes[at_choice]) + points  # attributes get added to key's value
#                attributes[at_choice] = result
#                print("\nPoints have been added.")
#            else:
#                print("\nYou do not have that many points to spend") # if not enough points not proceed
#        else:
#            print("\nThat attribute does not exist.") # if attribute not in list then not proceed
#    elif choice == "2":
#        print("\nREMOVE POINTS FROM AN ATTRIBUTE")
#        print("You have", pool, "points to spend.")
#        print(
#        """
#        Choose an attribute:
#           strength
#           health
#           wisdom
#           dexterity
#        """
#        )
#        at_choice = input("Your choice: ")
#        if at_choice.lower() in attributes:
#            points = int(input("How many points do you want to remove: "))
#            if points <= int(attributes[at_choice]): # if points are <= than the value of the key
#                pool += points # returns points back to pool
#                result = int(attributes[at_choice]) - points # associated point value with key
#                attributes[at_choice] = result 
#                print("\nPoints have been removed.")
#            else:
#                print("\nThere are not that many points in that attribute")
#        else:
#            print("\nThat attribute does not exist.")

#    elif choice == "3":
#        print("\n", attributes)
#        print("Pool: ", pool)
#    else:
#        print(choice, "is not a valid option.")



#input("\n\nPress the enter key to exit.")

 #---------Challenge 3.
#family = {"Neil":("Paul","Keith"),
#          "Paul":("Keith","Joseph"),
#          "John":("Ringo","Liam"),
#          "Michael":("Jackson","Darth Vader")}

#def daddy_list():
#    print("""
#    0. Exit
#    1. View Son/Father
#    2. Replace Son/Father
#    3. Add Son/Father
#    4. Delete Son/Father
#    """)
#    choice = None

#    while choice != 0:

#        choice = int(input("\nWhat is your choice? "))
#        if choice == 1:
#            get_father = input("Who's the son? ")
#            get_father = get_father.title() # changed it to title to capitalise first letter if not correct case
#            if get_father in family:
#                father = family[get_father]
#                print(get_father,"You father is called",father)
#            else:
#                print("You have no father") # view father son pairs
#        elif choice == 2:
#            get_father = input("Who\'s father so you want to replace? ")
#            get_father = get_father.title()
#            if get_father in family:
#                new_father = input("Who\'s your new daddy? ")
#                father = family[get_father]
#                old_father = father
#                family[get_father] = new_father
#                father = new_father
#                print(old_father,"was your daddy, now",father,"is your daddy!") # replace father
#            else:
#                print("That is not a valid choice")   #
#        elif choice == 3:
#            new_child = input("Who is the child you want to add? ")
#            new_father = input("Who is the daddy you want to add? ")
#            family[new_child] = new_father
#            print(family)   # add son/father
#        elif choice == 4:
#            get_father = input("Which father and son do you want to delete? please type son\s name")
#            get_father = get_father.title()
#            if get_father in family:
#                del family[get_father]
#                print(family)   # delete son/father
#    print("Good-Bye! ")
#    input("")

#def grandad_list():
#    print("""
#    0. Exit
#    1. View Grandchild/Grandfather
#    2. Replace Grandchild/Grandfather
#    3. Add Grandchild/Grandfather
#    4. Delete Grandchild/Grandfather
#    """)
#    choice = None

#    while choice != 0:

#        choice = int(input("\nWhat is your choice? "))
#        if choice == 1:
#            get_father = input("Who's the son? ")
#            get_father = get_father.title() # changed it to title to capitalise first letter if not correct case
#            if get_father in family:
#                father = family[get_father]
#                grandfather = father[1]
#                print(get_father,"You grandad is called",grandfather)
#            else:
#                print("You have no father") # view father son pairs
#        elif choice == 2:
#            get_father = input("Who\'s grandfather so you want to replace? ")
#            get_father = get_father.title()
#            if get_father in family:
#                new_father = input("Who\'s your new grandfather? ")
#                father = family[get_father]
#                old_father = father
#                family[get_father] = new_father
#                grandfather = new_father
#                grandfather = grandfather.capitalize()
#                family[get_father] = father,grandfather
#                print(old_father[1],"was your grandad, now",grandfather,"is your grandfather!") # replace father
#            else:
#                print("That is not a valid choice")   #
#        elif choice == 3:
#            new_child = input("Who is the child you want to add? ")
#            new_father = input("Who is the daddy you want to add? ")
#            new_grandfather = input("Who is the Grandfather you want to add? ")
#            family[new_child] = new_father,new_grandfather
#            print(family)   # add son/father
#        elif choice == 4:
#            get_father = input("Which grandfather and grandson do you want to delete? please type grandsonson\'s name")
#            get_father = get_father.title()
#            if get_father in family:
#                del family[get_father]
#                print(family)   # delete grandson/father/grandfather
#    print("Good-Bye! ")
#    input("")

#print("Welcome to the Daddy/Grandfather list. Find out who your daddy is.. or your grandad. Don\'t like it?? Change it!")

#select = input("""\n
#Choose 1. for Daddy list
#Choose 2. for Grandfather list
#\n""")

#if select == "1":
#    daddy_list()
#elif select == "2":
#    grandad_list()
#else:
#    print("That is not a valid choice")
#    input("""\n
#Choose 1. for Daddy list
#Choose 2. for Grandfather list
#\n""")
# ---------Challenge 4. Added into above code... definitely not perfect/tidy, but works

# ------- CHAPTER 6 ------- FUNCTIONS - THE TIC TAC TOE GAME

#def instructions():
#    """Display game instructions."""  
#    print(
#    """
#    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.  
#    This will be a showdown between your human brain and my silicon processor.  

#    You will make your move known by entering a number, 0 - 8.  The number 
#    will correspond to the board position as illustrated:
    
#                    0 | 1 | 2
#                    ---------
#                    3 | 4 | 5
#                    ---------
#                    6 | 7 | 8

#    Prepare yourself, human.  The ultimate battle is about to begin. \n
#    """
#    )
#instructions()

## Using parameters and return values

#def display(message): # will print whatever you type into the function
#    print(message)

#def give_me_five():
#    five = 5          # will return the value of five... in this case 5
#    return five       # the variable 5 only exists inside the function, until it is returned to another variable

#def ask_yes_no(question):
#    """Ask a yes or no question"""
#    response = None
#    while response not in ("y","n"):
#        response = input(question).lower()
#    return response             # make sure return is outside of the while loop!

##Main
#display("Here's a message for you")

#number = give_me_five()   # the variable 'number' will therefore be assigned the output value of the function
#print("Here\'s what i got from give_me_five():",number)

#answer = ask_yes_no("\nPlease enter 'y' or 'n': ") # assigns the output of yes_no as the value of answer
#print("Thanks for entering",answer)

# -------- The birthday wishes program -- demonstrates key word arguements

## Positional arguements
#def birthday1(name,age):   # positional parameters
#    print(name,"I heard you are",age,"years old today")

#birthday1("Neil",31) #   positional arguements, however can be as follows
#birthday1(31,"Neil") #   positional arguements are not specific to required output

## parameters with default values


#def birthday2(name = "Neil",age = 31): # if you assign a default value to one variable you need to assign to all
#    # birthday2(name = 'Neil', 31) will produce error as it should be age = 31
#    print("Happy birthday",name,"You are",age,"Years old today!")

#birthday2()

## I prefer this way, to get user to assign the parameters (based on same function as birthday1)
#name = input("Name: ")
#age = int(input("age: ")) # you could set either of these parameters anywhere in the main program

#birthday1(name,age)

# --- Using global variables and constants ---- THE GLOBAL REACH PROJECT
# --- Demonstrates global variables

#def read_global():
#    print("From inside the local scope of read_global(), value is: ",value)

#def shadow_global(): # it is not good to shadow a global variable inside a function, as it can be confusing
#    value = -10   # try using another name for the variable!!
#    print("From inside the local scope of shadow_global(), value is: ",value)

#def change_global():
#    global value   # useful to know, similar to returning value??
#    value = -10
#    print("From inside the local scope of change_global(), value is",value)

#value = 10   # this is a globalvalue
#read_global()
#print("Back in global scope 'value' is...",value)

#shadow_global()
#print("Back in global scope 'value' is...",value)

#change_global()
#print("Back in global scope 'value' is...",value)

# ---------------------- BACK TO THE TIC TAC TOE GAME -------------------------------

# ----- FOR PSEUDOCODE SEE PG 176
# ----- THE PSEUDOCODE INSPIRES THE FUNCTIONS NEEDED FOR THE PROGRAM

## GLOBAL CONSTANTS
#X = 'x' # represents player a
#O = 'o' # represents player b
#EMPTY = '' # represents an empty square
#TIE = "TIE"
#NUM_SQUARES = 9

## THE DISPLAY_INSTRUCT() FUNCTION

#def display_instruct():
#    """Display Game Instructions."""
#    print("""
#    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
#    This will be a showdown between your human brain and my silicon processor.

#    You will make your move known by entering a number, 0 - 8. The number 
#    will correspond to the board position as illustrated:

#                        0 ¦ 1 ¦ 2
#                        ----------
#                        3 ¦ 4 ¦ 5
#                        ----------
#                        6 ¦ 7 ¦ 8

#    Prepare yourself, human. The ultimate battle is about to begin\n
#    """)

## THE ASK_YES_NO() FUNCTION

#def ask_yes_no(question):
#    """Ask a yes or no question"""
#    response = None
#    while response not in ("y","n"):
#        response = input(question).lower()
#    return response

## THE ASK_NUMBER() FUNCTION

#def ask_number(question,low,high): # asks for a number within range, and returns the number specified
#    response = None
#    while response not in range(low,high):
#        response = int(input(question))
#    return response

## THE PIECES() FUNCTION

#def pieces():
#    """Determines if player of computer goes first"""
#    go_first = input("Do you require the first move?(y/n): ") # basically decides who is X
#    if go_first == "y":
#        print("\nThen take the first move, you will need it!")
#        human = X
#        computer = O
#    else:
#        print("\nYour bravery will be your undoing, I will go first!")
#        computer = X
#        human = O
#    return computer,human # returns the values of computer and human as X or O

## THE NEW BOARD FUNCTION

#def new_board():
#    """Create new game board"""
#    board = [] # creates a board (empty list) and sets all nine elements to EMPTY
#    for square in range(NUM_SQUARES):
#        board.append(EMPTY)
#    return board

## THE DISPLAY_BOARD() FUNCTION

#def display_board(board):
#    """Display board on screen""" # displays the board passed into it
#    print("\n\t ", board[0], "¦" ,board[1], "¦",board[2])
#    print("\t", "---------")
#    print("\t ", board[3], "¦" ,board[4], "¦",board[5])
#    print("\t", "---------")
#    print("\t ", board[6], "¦" ,board[7], "¦",board[8], "\n")
    
## THE LEGAL_MOVES() FUNCTION

#def legal_moves(board):
#    """Create a list of legal moves""" # basically iterates to check if board position is empty
#    moves = []
#    for square in range(NUM_SQUARES):
#        if board[square] == EMPTY:
#            moves.append(square)
#    return moves

## THE WINNER FUNCTION
## Create ways_to_win constant which has all 8 ways to get three in a row

#def winner(board):
#    WAYS_TO_WIN = ((0, 1, 2),
#                   (3, 4, 5),
#                   (6, 7, 8),
#                   (0, 3, 6),
#                   (1, 4, 7),
#                   (2, 5, 8),
#                   (0, 4, 8),
#                   (2, 4, 6))
#    for row in WAYS_TO_WIN: # checks to see if the squares in all question have same valua of empty 
#        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
#            winner = board[row[0]] # assigns one piece to winner and returns winner
#            return winner
#    if EMPTY not in board: # if nobosy has won, and no empty squares then return TIE
#        return TIE
#    return None

## THE HUMAN_MOVE() FUNCTION

#def human_move(board,human):
#    """Get human move."""
#    legal = legal_moves(board)
#    move = None
#    while move not in legal:
#        move = ask_number("Where will you move? (0 - 9)", 0, NUM_SQUARES) # question,low,high parameters
#        if move not in legal:
#            print("\nThat square is already occupied, foolish human. Choose another.\n")
#    print("Fine...")
#    return move

## THE COMPUTER_MOVE() FUNCTION

#def computer_move(board,computer,human):
#    """Make computer move"""
#    # make a copy to work with since function will be changing list
#    board = board[:] # changes as computer searches for best move, hence making a copy
## basic strategy
## 1. if there is a move to allow computer to win - pick it
## 2. if there is a move to allow human to win on next turn - pick it
## 3. otherwise choose the best empty square
    
#    # The best positions to have in order
#    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
#    print("I shall take the square number", end=" ")
    
#    # If computer can win - take that move
#    for move in legal_moves(board):
#        board[move] = computer
#        if winner(board) == computer:
#            print(move)
#            return(move)
#        # done checking this move... undo it
#        board[move] = EMPTY

#    # if human can win - block that move
#    for move in legal_moves(board):
#        board[move] = human
#        if winner(board) == human:
#            print(move)
#            return(move)
#        # done checking this move... undo it
#        board[move] = EMPTY

#    #since nobody can win on the next move, pick best open square
#    for move in BEST_MOVES:
#        if move in legal_moves(board):
#            print(move)
#            return(move)

## THE NEXT_TURN() FUNCTION

#def next_turn(turn):
#    """Switch turn"""
#    if turn == X:
#        return O
#    else:
#        return X

## THE CONGRAT_WINNER() FUNCTION

#def congrat_winner(the_winner,computer,human):
#    """Congratulate the winner"""
#    if the_winner != TIE:
#        print(the_winner,"WON!\n")
#    else:
#        print("It's a tie!\n")

#    if the_winner == computer:
#        print("As I predicted human, I am triumphant once more. \n" \
#            "proof that computers are superior to humans in all regards!")
#    elif the_winner == human:
#        print("No, it cannot be! somehow you tricked me human!\n" \
#            "but never again! I, the computer, swear to it!")
#    else:
#        print("You were most lucky human, and somehow managed to tie me\n" \
#            "Celebrate today, for this is the best you will ever achieve!")

## ----- MAIN_LOOP()

#def main():
#    display_instruct()
#    computer, human = pieces()
#    turn = X
#    board = new_board()
#    display_board(board)

#    while not winner(board):
#        if turn == human:
#            move = human_move(board,human)
#            board[move] = human
#        else:
#            move = computer_move(board,computer,human)
#            board[move] = computer
#        display_board(board)
#        turn = next_turn(turn)

#    the_winner = winner(board)
#    congrat_winner(the_winner,computer,human)

#main()


#-------------------------- CHALLENGES CHAPTER 6 --------------------------------

# --- Challenge 1

#def ask_number(question,low,high,step = 1): # asks for a number within range, and returns the number specified
#    response = None
#    while response not in range(low,high):
#        response = int(input(question))
#    return response

# --- challenge 2 and 3

#def ask_number(question,low,high,step = 1):
#    from random import randint
#    print(question,"between",low,"and", high)
#    number = randint(low,high)
#    tries = 1
#    guess = None
#    while True:
#        guess = input("What's your guess? ")
#        if int(guess) > high or int(guess) < low:
#            print('number out of range')
#            guess = int(input(question))
#        elif int(guess) > number:
#            print('your guess was too high')
#        elif int(guess) < number:
#            print('Your guess was too low')
#        else:
#            break
#        tries += step
 
#    print('CONGRATULATIONS, THAT WAS CORRECT, THE ANSWER WAS',number,'you guessed in',tries,'tries!')
#    input('press any key to exit')

#def main():
#    ask_number("Guess a number between",1,1000)

#main()

# --- Challenge 4 --- DONE, COMPUTER ALREADY UNBEATABLE


# ---------------------- CHAPTER 7 - FILES AND EXCEPTIONS -------------------------

# ---- READ an ASCII text file

#print("Opening and closing file")
#text_file = open("read_it.txt","r")   # can't figure out where shit lives so created file with "wb"
#text_file.close()

#print("\nRead charachters from file")
#text_file = open("read_it.txt","r")
#print(text_file.read(1))
#print(text_file.read(5))
#text_file.close()

#print("\nreading the entire file at once..")
#text_file = open("read_it.txt","r")
#print(text_file.read())
#text_file.close()

#print("\nReading charachters from a line")
#text_file = open("read_it.txt","r")
#print(text_file.readline(1))
#print(text_file.readline(5)) # python picks up where the last statement left off - like a bookmark
#text_file.close()

#print("\nReading one line at a time")
#text_file = open("read_it.txt","r")
#print(text_file.readline())
#print(text_file.readline())
#print(text_file.readline())
#text_file.close()

#print("\nReading entire file into a list")
#text_file = open("read_it.txt","r")
#lines = text_file.readlines()
#print(lines)
#print(len(lines))
#for line in lines:
#    print(line)
#text_file.close()

#print("\nLooping through the file line by line")
#text_file = open("read_it.txt","r")
#for line in text_file:
#    print(line)
#text_file.close()

# ----- WRITE TEXT FILE
#Demonstrates writing text to file

#print("Creating a text file with the write() method")
#text_file = open("write_it.txt","w")
#text_file.write("Line 1\n")
#text_file.write("This is line 2\n")             # does not automatically put a new line, you need to do that
#text_file.write("This is another line, Neildor!\n")
#text_file.close

#text_file = open("write_it.txt","r")    # Just to prove it worked... it did
#print(text_file.read())
#text_file.close()

# --- WRITING LIST OF STRINGS TO A FILE

#print("\nCreating a text file with the writelines() method")
#text_file = open("write_it.txt","w")
#lines = ["Line 1\n",
#         "Line 2\n",
#         "Line 3\n"]
#text_file.writelines(lines)
#text_file.close()

#text_file = open("write_it.txt","r")
#print(text_file.read())
#text_file.close()

## READ WRITE METHODS
## close() - closes the file
## read([size]) - 
## readline([size]) -
## readlines() - converts lines into a list
## write(output) - writes the string 'output' to a file
## writelines(output) - writes strings in the list 'output' to file


# ---- Storing complex data in files
# --- introducing the 'pickle it'program

# demonstrates pickling and shelving data

import pickle, shelve   # pickle means to preserve, shelve allows you to store and randomly access pickled objects

print("Pickling lists.")
variety = ["sweet","hot","dill"]
shape = ["whole","spear","chip"] 
brand = ["Claussen","Heinz","Vlassic"]

f = open("pickles1.dat","wb") # dat is a binary file, CANNOT be stored as txt. wb = write to binary mode

pickle.dump(variety,f) # pickles the list and writes it as one object to filename f
pickle.dump(shape,f)
pickle.dump(brand,f)
f.close() # closes file

# you can pickle a variety of objects including; numbers, strings, tuples, lists, dictionaries

# UNPICKLING AND READING DATA

print("\nUnpickling lists")
f = open("pickles1.dat","rb") # rb - reads binary data file
variety = pickle.load(f) # unpickles the single file back to the list for each...
shape = pickle.load(f)
brand = pickle.load(f)

print(variety)
print(shape)
print(brand)
f.close()

# functions
# dump(object,filename,[bin]) if bin = TRUE, object is written as binary, if FALSE is written more readable, but less efficient
# load(file)

# --- Using a shelf to store pickled data
# --- this shelves the three pickled lists into a single file, it acts like a dictionary..

# first i create a shelf s
print("\nShelving lists")
s = shelve.open("pickles2.dat") # shelve.open works with pickled files not charachters
                                # requires 1 arguement - a file name, additional arguements c,n,r,w can be added, if not defaults to c
# next i add three lists to the shelf       c = open, n = new, r = read, w = write
s["variety"] = ["sweet","hot","dill"]
s["shape"] = ["whole","spear","chip"]       # works like dictionary.. shape = key, whole,spear.. = value
s["brand"] = ["Claussen","Heinz","Vlassic"] 

# last i envoke the shelf sync method
s.sync() # makes sure data is written

# --- Using shelf to retrieve pickled data
print("\nRetrieving lists from shelved file")
print("brand - ",s["brand"])
print("Variety - ",s["variety"])
print("Shape - ",s["shape"])
s.close()

# Pickling and shelving are great ways to store and retrieve structured information. complex information can
# require more power and flexibility. Databases and XML are 2 popular methods for storing and retrieving
# more complex data... Python has modules for both (xml,beautifulSoup, probably more?)

 




