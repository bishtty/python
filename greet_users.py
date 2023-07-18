# function

def greet_users(names):
	'''print a simple greeting to each user in the list'''
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)
		
usernames = ['hannah', 'ty','aayu']
greet_users(usernames)



