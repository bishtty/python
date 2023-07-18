# self program to ask what topping pizza you want.

available_toppings = ['mushroom', 'olives', 'green peppers',
                       'pepparoni', 'pineapple', 'extra cheese']

requested_toppings = []

print('toppings available at the moment are: ')
print(available_toppings)
n = int(input('\nhow number of toppings you want?'))
for i in range(1, n+1):
	 print('enter the topping no.', i, )
	 item = input()
	 requested_toppings.append(item)
# print(requested_toppings)

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print('adding ' + requested_topping + '.')
	else:
		print('sorry we dont have ' + requested_topping + '.')
		
print('\nyou yummy pizza is ready')


