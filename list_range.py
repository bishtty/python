# using range() to store numbers in list
numbers = list(range(1, 11))
for number in numbers:
    print(number)

even_numbers = list(range(2, 11, 2))
for even_number in even_numbers:
    print(even_number)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

# list comprehension for cube
cubes = [value**3 for value in range(1,11)]
print(cubes)