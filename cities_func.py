# exercize 8-5 pg 175/141

def describe_city(city, country = 'India'):
	print(city + " is in " + country)
	
describe_city("dehradun")
describe_city('sardania', 'italy')
describe_city("napoli", "italy")
	
# exercise 8-6 pg 146/179

def city_country(city, country):
	location = city + ", " + country
	return location.title()

print()	
exact_location = city_country('dehradun', 'India')
print(exact_location)
exact_location = city_country('pune', 'India')
print(exact_location)
exact_location = city_country('sardania', 'Italy') 
print(exact_location)

	



