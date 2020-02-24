# this is a madlibs knock-off starring samuel jackson


def main():
	# collect the words
	adjective_1 = input("Give me an adjective, bitch: ")
	verb_1 = input("Tell me a fucking verb: ")
	pl_noun_1 = input("Plural noun or I blow this shit up: ")

	while pl_noun_1 == "what":
		pl_noun_1 = input("What ain't no country I've ever heard of. > ")


	adjective_2 = input("Give me a second adjective, you " + adjective_1 + " fucking bitch: ")

	# check whether Jon says "no"
	if adjective_2 == "no":
		#admonish Jon
		print("Jon, you " + adjective_1 + " singularitan oaf.")
		#ask again for a value
		adjective_2 = input("I told you to give me a fucking adjective: ")
	
	# thank the kindly user for not saying "no"
	else:
		print("Thank you.")

	article = ""

	if adjective_2.startswith("a"):
		article = "an"
	elif adjective_2.startswith("e"):
		article = "an"
	elif adjective_2.startswith("i"):
		article = "an"
	elif adjective_2.startswith("o"):
		article = "an"
	elif adjective_2.startswith("u"):
		article = "an"
	else:
		article = "a"	

	# print the story
	print("My favorite superhero is the " + adjective_1 + 
		" " + verb_1 + "er. His superpower is moving " + pl_noun_1 +
		" with his mind. He has " + article + " " + adjective_2 + " origin story."
		# TODO write something to determine a vs an
	)

main()