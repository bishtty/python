# exercise 6-10
# exercise 6-2 person favourite number


favorite_num = {
	'bishty': [7, 4],
	'auri': [21, 3, 29],
	'maff_ox': [15],
	'franci': [90, 13],
	'mari': [29]
	}
	
for name, number in favorite_num.items():
	if len(number) > 1:
		print(name + "'s favourite numbers are: " + str(number))
	else:
		print(name + "'s favourite number is: " + str(number))
