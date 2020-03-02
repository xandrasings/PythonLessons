#futVal.py
# this is a program to calculate interest
def main ():
	principal= eval(input("define principal: "))
	rate= eval(input("define interest rate (as decimal): "))
	for i in range(10):
		principal= principal*(1+rate)
	print(principal, "This is the value for initial principal over 10 years at said rate.")
main()
	