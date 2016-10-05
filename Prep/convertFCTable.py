# convertFCTable.py
# asks the user for 5 temperatures in Fahrenheit,
# then prints a table with each Fahrenheit temp on the left,
# and the associated Celsius temp on the right.

def main():
	print("Enter 5 Fahrenheit temperatures:")
	F1, F2, F3, F4, F5 = eval(input()), eval(input()), eval(input()), eval(input()), eval(input())

	FTemps = [F1, F2, F3, F4, F5]

	print() # print an empty line to separate inputs and outputs
	print("F", "\t", "C") # table header
	print("------------") # line
	for FTemp in FTemps:
		CTemp = (FTemp-32) * 5 / 9
		print(FTemp, "\t", CTemp)

main()