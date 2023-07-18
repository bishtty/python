# greeting everyone using function and while loop

def get_formatted_name(first_name, last_name):
	full_name = first_name + " " + last_name
	return full_name.title()

# now putting if statements to prevant infinite while loop	
while True:
	print("\n please tell me ur name")
	print("enter 'q' at any time to quit")
	f_name = input("enter your first name: ")
	if f_name == 'q':
		break
	l_name = input("enter your last name: ")
	if l_name == 'q':
		break
	
	formatted_name = get_formatted_name(f_name, l_name)
	print("\n Hello, " + formatted_name + "!")




