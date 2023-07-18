# exercise 7-5 Movie tickets

prompt = "enter ur age to know ticket price?"
prompt += "\nenter 0 to quit entering: "


active = True

while active:
	age = int(input(prompt))
	print()
	
	if age == 0:
		active = False
	else:
		if age <= 3:
			print("ur ticket is free")
		elif 3 < age <= 12:
			print("ur ticket price is $3")
		else:
			print("ur ticket price is $15")
	print()
