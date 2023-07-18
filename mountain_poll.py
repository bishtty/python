
responses = {}

# set a flag to indicate that polling is active
polling_active = True

while polling_active:
	# prompt for persons name and response.
	name = input("\nwhat is your name? ")
	response = input("which mountain would you like to climb someday: ")
	
	#store the response in the dictionary
	responses[name] = response
	
	# findout if anyone else is going to take the poll
	repeat = input("would you let another person to respond? (y/n)")
	if repeat == 'n':
		polling_active =False
		
# polling is complete show the result
print("\n--- Poll Result ---")
for name, response in responses.items():
	print(name.title() + " would like to climb " + response.title() + ".")
	

