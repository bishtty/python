
requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']

'''
if 'mushrooms' in requested_toppings:
    print('adding mushrooms')
if 'pepparoni' in requested_toppings:
    print('adding pepparoni')
if 'extra cheese' in requested_toppings:
    print('adding extra cheese')
    
print('\n Finished making your yummy pizza')

'''
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print('sorry, we are out of green peppers right now')
	else:
		print('Adding ' + requested_topping.title() + '.')
print('\nyour yummy pizza is ready')

