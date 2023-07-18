
pizzas = ['pepperoni', 'paneer', 'onion', 'cheese']
for pizza in pizzas:
    print('i like ' + pizza + ' pizza!')
    
print('i am vegan so i only like veg pizza, althogh when i was not vegan i liked pepperoni pizza')

friend_pizza = pizzas[:]

pizzas.append('farm house')
friend_pizza.append('capsicum')

print('\n my favourite pizzas are: ')
for pizza in pizzas:
	print(pizza.title())
	
print("\n my friend's favourite pizzas are: ")
for pizza in friend_pizza:
	print(pizza.title())
