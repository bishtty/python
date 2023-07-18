# start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candance']
confirmed_users = []

# verify eachother until there are no more unconfirmed users.
# move each verified user into list of unverified users
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	
	print("verifying user: " + current_user.title())
	confirmed_users.append(current_user)
	
# display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())


