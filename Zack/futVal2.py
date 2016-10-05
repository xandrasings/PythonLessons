#futVal.py
# this is a program to calculate interest
def main ():
	principal= eval(input("define principal: "))
	rate= eval(input("define interest rate (as decimal): "))
	years= eval(input("define number of years: "))
	for i in range(years):
		principal= principal*(1+rate)
	print(principal, "This is the value for initial principal over requested years at said rate.")
main()
	