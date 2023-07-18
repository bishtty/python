# exercise 7-4 pizza toppings

prompt = "enter pizza toppings of your choice"
prompt += "\n(enter 'quit' when u r done adding.) "

active = True
while active:
	message = input(prompt)
	
	if message == 'quit':
		active = False
		# print("your pizza is ready")
	else:
		 print("\nadding " + message.title() + " to your pizza")
		 print()

