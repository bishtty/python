# exercise 7-8 pg 164/131

sandwich_orders = ['cheese', 'jam', 'butter', 'onion']
finished_sandwiches = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print("i am making " + current_sandwich.title() + 
		" sandwich for you")
	
	finished_sandwiches.append(current_sandwich)
	
print("the sandwiches that were made are: " + str(finished_sandwiches))



