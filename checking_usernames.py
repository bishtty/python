# exercise 5-11

current_users = ['auri', 'bishty', 'maff_ox', 'franci', 'mari']
new_users = ['ales', 'Maff_ox', 'mari', 'laudia', 'mimichan']


for user in new_users:
	if user.lower() in current_users: #to make it case sensitive
		print("username already assigned, enter new username")
	else:
		print("username is available")
