def main():

	print("Name: {name}\nAge: int{age}\nFavourite Colour: {colour}\nPet name(s): {pet}\nHobbies: {hobby}".format(name = input("What is your name? "),age = int(input("How old are you? ")),colour = input("What is your favourite colour? "),pet = input("What is/are your pet's name(s)? "),hobby = input("What are your hobbies? ")))
'''
	if name == 'Neil':
		print("hello sir, and welcome!")
	else:
		print("Who the fuck is {name}!?")
	if age >= 18:
		print("you are old enough to be here.")
	else:
		print("you need to be 18 or over to enter.")                     #Have to define these individually, cannot associate with .format!
	if colour == orange:
		print("Orange, no way me too!!")
	else:
		print("I don't really relate to people with {colour} as colour choice!")
	if hobby == code:
		print("HelloWorld")
	else:
		print("GoodbyeWorld")
'''		
main()
