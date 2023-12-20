# introducing tuples 
# tuples are imutable lists i.e. its values cannot be changed throughout the life of program
dimensions = (200, 50)
print("these are the original dimensions")
for dimension in dimensions:
    print(dimension)

# you cant change value of tuple but you can redfine the entire value of tuple

dimensions = (400, 40) # new value assigned
print("these are the new dimensions ")
for dimension in dimensions:
    print(dimension)