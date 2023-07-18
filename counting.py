'''
sum_mil = []
for counting in range(1,1000001):
    sum_mil.append(counting)
    
print('sum of 1 million: ', sum(sum_mil))
print(min(sum_mil))
print(max(sum_mil))
'''

# practice chapter 7 pg122/155
'''
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1
'''

# using continue statement

current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
		
	print(current_number)
	
