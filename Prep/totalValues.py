# totalValues.py
# asks for 3 values, stores them in a list, then uses a loop to sum them.

def main():
	print("Input 3 values: ")
	val1, val2, val3 = eval(input()), eval(input()), eval(input())
	valList = [val1, val2, val3]
	total = 0

	for val in valList:
		total = total + val

	print("The sum of", val1, ",", val2, ",", val3, "is", total)
main()