# convertFC.py
# converts Fahrenheit temperatures to Celsius.

def main():
	FTemp = eval(input("What is the temperature in Fahrenheit? "))
	CTemp = (FTemp-32) * 5 / 9

	print(FTemp, "degrees Fahrenheit is", CTemp, "degrees Celsius.")
main()