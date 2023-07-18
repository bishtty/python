# exercise 6-5 page 108/141

rivers = {
	'nile': 'egypt',
	'ganga': 'India',
	'thames': 'britain'
		}

# to print key-values		
for key, value in rivers.items():
	print("the " + key.title() + " runs through " + value.title())
print()		
for river in rivers.keys():
	print(river.title())
print()
for country in rivers.values():
	print(country.title())
