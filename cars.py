
cars = ['bmw', 'audi', 'toyata', 'sabru']
cars.sort() # sort() for sorting in alphaB order - sorts list permanently
print(cars)

cars.sort(reverse=True) # sorting in reverse order using "reverse=True"
print(cars)

cars = ['bmw', 'audi', 'toyata', 'sabru']
print('\nhere is original list: \n', cars)
print('here is sorted list: \n', sorted(cars))
print('\nhere is sorted list(reverse): \n', sorted(cars, reverse=True))
print('here is original list again: \n', cars)

cars.reverse()
print('\n',cars) # reverse() simply reverse the order of list not alphaB

