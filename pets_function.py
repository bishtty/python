# function chapter 8
# positional arguements
# keyword arguement

# positional arguements
print("printing through positional argument")
def describe_pet1(pet_type, pet_name):
	print("\ni have a " + pet_type + ".")
	print("My " + pet_type + "'s name is " + pet_name.title() + ".")
	
describe_pet1('hamster', 'jerry')
describe_pet1('cat', 'ninja')

# keyword arguements
print("\nprinting through keyword argument")
def describe_pet2(pet_type, pet_name):
	print("\ni have a " + pet_type + ".")
	print("My " + pet_type + "'s name is " + pet_name.title() + ".")
	
describe_pet2(pet_type = 'hamster', pet_name = 'jerry')
describe_pet2(pet_type = 'cat', pet_name = 'ninja')
