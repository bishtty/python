# exercise5-6 pg 89

age = int(input('enter your age to know the stage of your life: '))

if age <= 2:
	print('you are a baby')
elif 2 < age < 4:
	print('you are a toddler')
elif 4 <= age < 13:
	print('you are akid')
elif 13 <= age < 20:
	print('you are a tenager')
elif 20 <= age < 65:
	print('you are an adult')
else:
	print('you are an elder')
	
