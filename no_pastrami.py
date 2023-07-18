# exercise 7-9 pg164/131

sandwich_orders = ['cheese', 'pastrami', 'jam', 
					'pastrami', 'butter', 'onion', 'pastrami']
print("deli has run out of pastrami")
print()
finished_sandwiches = []
for sandwich in sandwich_orders:
	if sandwich == 'pastrami':
		sandwich_orders.remove('pastrami')
while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print("i am making " + current_sandwich.title() + 
		" sandwich for you")
	
	finished_sandwiches.append(current_sandwich)

print("\nthe sandwiches that were made are: ")
for sandwich in finished_sandwiches:
	print(sandwich)
