# input() pg 118/151


prompt = "\n tell me something, and i will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
'''
message = ""
while message != 'quit':
	message = input(prompt)
	print(message)
'''

# using flag pg 124/157

active = True
while active:
	message = input(prompt)
	
	if message == 'quit':
		active = False
	else:
		print(message)
