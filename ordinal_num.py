# exersice 5-11

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if not num_list:
	print("enter numbers in the list to check for condition")
else:
	print("ordinal numbers are :")
	for num in num_list:
		if num == 1:
			print(str(num) + "st")
		elif num == 2:
			print(str(num) + "nd")
		elif num == 3:
			print(str(num) + "rd")
		else:
			print(str(num) + "th")
			
