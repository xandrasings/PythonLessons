#factorial.py
#calculates the factorial of an int

def main():
	count = 1
	number = eval(input("What number would you like to factorialize? "))
	factorial = 1

	while count <= number:
		# logic here
		factorial = factorial * count
		count += 1

	print("Here's your factorial you filthy animal: " + str(factorial))

main()