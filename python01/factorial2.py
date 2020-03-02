#factorial.py
#calculates the factorial of an int

def main():
	count = 1
	number = eval(input("What number would you like to factorialize? "))
	factorial = 1


	for count in range(1,number + 1):
		# logic here
		factorial = factorial * count

	print("Here's your factorial you filthy animal: " + str(factorial))

main()