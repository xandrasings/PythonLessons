# CtoF.py
# this program converts celsius temperatures to fahrenheit

def main():
	celsius = eval(input("What temperature is it in C? "))

	fahrenheit = (9 * celsius) / 5 + 32

	print(celsius)
	print(" degrees celsius is ")
	print(fahrenheit)
	print(" degrees fahrenheit.")

main()