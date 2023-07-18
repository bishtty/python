# using break statement

prompt = "please enter your city name: "
prompt += "\n(Enter 'quit' when finished) "

while True:
	city = input(prompt)
	if city == 'quit':
		print("exiting program....")
		break
	else:
		print("i'd love to go to " + city.title() + "!")
	
