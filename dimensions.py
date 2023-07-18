# tuple
# in tuple we use (), whereas in list we use []

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions(250) if we try to change values in tuple it will give type error

print('\n print original dimensions: ')
for dimension in dimensions:
	print(dimension)

dimensions = (400,100)
print('\n modified dimensions: ')
for dimension in dimensions:
	print(dimension)

# we cant modify tuple, but we can assign new values to the variable that holds tuple
