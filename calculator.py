#Returns the sum of num1 and num2
def add(num1, num2):
	return num1 + num2
#Returns the result of subtracting num1 and num2
def sub(num1, num2):
	return num1 - num2
#Returns the result of Multiplying num1 and num2
def mul(num1, num2):
	return num1 * num2
#Returns the result of Dividing num1 and num2
def div(num1, num2):
	return num1 / num2
#User select, and number input
def main(): # +-*/ Functions
	operation = input("What do you want to do(+,-,*,/")
	if(operation != '+' and operation != '-' and operation != '*' and operation != '/' and operation != 'sqr'):
		# Invalid Operation
		print("You must enter a valid operation")	
	else:
		Var1 = int(input("Enter num1: "))
		Var2 = int(input("Enter num2: "))
		if(operation == '+'):
			print(add(Var1, Var2))
		elif(operation == '-'):
			print(sub(Var1, Var2))
		elif(operation == '*'):
			print(mul(Var1, Var2))
		elif(operation == '/'):
			print(div(Var1, Var2))
		

main()
