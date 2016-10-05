# futVal.py
# computes the value of an investment after a given number of years.

def main():
	value = eval(input("Enter the principal loan value ($__): "))
	rate = eval(input("Enter the annual interest rate (__%): "))
	years = eval(input("Enter the number of years of investment: "))

	rate = rate/100 # This converts rate format from __% to .__

	for i in range(years):
		value = value * (1 + rate)

	print("The value after", years, "years is: $", value)
main()