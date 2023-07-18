squares = []
for value in range(1,10+1):
    # square = value**2 -> more precise code remove this line
    squares.append(value**2)
    
print(squares)

#to find min, max, and sum
min_max_sum = []
for value in range(0,10):
    min_max_sum.append(value)
    
print('\n ', min_max_sum)
print('minimun number: ', min(min_max_sum))
print('maximum number: ', max(min_max_sum))
print('sum of all number: ', sum(min_max_sum))
