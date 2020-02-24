# fussing with python

def main():
	print("Welcome to the program!")

	mattsMatrix = [[[1,2,3],[1,2,3],[1,2,3]],[[1,2,3],[1,2,3],[1,2,3]],[[1,2,3],[1,2,3],[1,2,3]]]


	for n in mattsMatrix:
		print(n)


	keepGoing = True
	while (keepGoing):
		print("Enter \"STOP\" to end array")
		newVal = input("Enter a new val: ")
		if (newVal == "STOP"):
			keepGoing = False


main()