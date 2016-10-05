# futVal.py
# computes the value of an investment after 10 years.

def main():
	value = eval(input("Enter the principal loan value ($__): "))
	rate = eval(input("Enter the annual interest rate (__%): "))

	rate = rate/100 # This converts rate format from __% to .__

	for i in range(10):
		value = value * (1 + rate)

	print("The value after 10 years is: $", value)
main()